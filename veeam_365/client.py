import asyncio
import builtins
import importlib
import re
import ssl
from collections.abc import Mapping
from datetime import datetime, timedelta, timezone
from json import JSONDecodeError
from typing import Any

import attrs
import httpx

from .exceptions import VeeamAuthenticationError, VeeamSessionError

# Errors that mean "the server could not be reached or did not answer in time". They are
# never turned into authentication errors: a caller has to be able to tell a server that
# is down from a password that is wrong. asyncio.TimeoutError is only an alias of
# TimeoutError from Python 3.11.
_TRANSPORT_ERRORS = (httpx.HTTPError, OSError, TimeoutError, asyncio.TimeoutError)

# Statuses on the token endpoint that say "try again later" rather than "wrong password".
_RETRYABLE_LOGIN_STATUSES = (429,)


# ----------------------------
# helpers
# ----------------------------


def _camel_to_snake(name: str) -> str:
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def _import_with_unset_patch(module_path: str, package: str):
    """
    Import a module with Unset patching to work around generated code issue.

    The generated OpenAPI code uses Unset in type annotations but doesn't import it.
    This helper temporarily injects Unset into builtins during import.
    """
    types_mod = importlib.import_module(f"{package}.types")
    builtins.Unset = types_mod.Unset

    try:
        return importlib.import_module(module_path)
    finally:
        if hasattr(builtins, "Unset"):
            delattr(builtins, "Unset")


def _is_token(candidate: Any) -> bool:
    """Whether a token-endpoint result is actually a token.

    The token operation returns an OAuthTokenResponse on success but a RESTExceptionInfo
    for any other status, and it does not raise. Reading .access_token off the error
    model raises AttributeError far from the real cause.
    """
    fields = ("access_token", "refresh_token", "expires_in")
    return all(hasattr(candidate, field) for field in fields)


def _present(value: Any) -> Any:
    """The value, or None when it is missing or the generated Unset sentinel."""
    if value is None or type(value).__name__ == "Unset":
        return None
    return value


def _describe_login_failure(result: Any, status_code: int | None = None) -> str:
    """Explain a token-endpoint result that is not a token."""
    status = f"HTTP {status_code}" if status_code is not None else None

    if result is None:
        detail = "the server returned no token and a response that could not be read"
        return f"{detail} ({status})" if status else detail

    if isinstance(result, Mapping):
        # Raw JSON that did not fit the generated error model.
        message = result.get("message")
        error_code = result.get("errorCode")
        extra = result
    else:
        message = _present(getattr(result, "message", None))
        error_code = _present(getattr(result, "error_code", None))
        extra = getattr(result, "additional_properties", None) or {}
    # The token endpoint may answer in OAuth style ({"error": ..., "error_description": ...}),
    # which the generated RESTExceptionInfo keeps in additional_properties.
    if not message:
        message = extra.get("error_description") or extra.get("error")

    if message or error_code or status:
        code = getattr(error_code, "value", error_code)
        details = ", ".join(str(part) for part in (code, status) if part)
        text = f"the server rejected the login: {message or 'no message'}"
        return f"{text} ({details})" if details else text

    return f"the server returned {type(result).__name__} instead of a token"


async def _aclose_generated_client(client: Any) -> None:
    """Close the httpx.AsyncClient a generated Client created, if it created one."""
    if client is None:
        return
    async_client = getattr(client, "_async_client", None)
    if async_client is not None:
        await async_client.aclose()


# ----------------------------
# API namespace proxy
# ----------------------------


class ApiNamespace:
    """
    Lazy namespace for openapi-python-client operation modules.

    Example:
        vc.api("repositories").get_all_repositories
        → veeam_365.vX.api.repositories.get_all_repositories.asyncio
    """

    def __init__(self, client: "VeeamClient", base_module: str):
        self._client = client
        self._base = base_module

    def __getattr__(self, name: str):
        mod = _import_with_unset_patch(f"{self._base}.{name}", self._client.package)
        return mod.asyncio


# ----------------------------
# main client
# ----------------------------


class VeeamClient:
    """
    Shared async client for versioned openapi-python-client SDKs.

    Responsibilities:
    - version routing
    - authentication
    - token refresh (serialised, falling back to the password grant)
    - API namespace routing

    Errors:
    - VeeamAuthenticationError: the password login was refused.
    - VeeamSessionError: the session was rejected mid-use; the next call re-authenticates.
    - httpx.HTTPError / OSError / TimeoutError: the server could not be reached. These
      propagate unchanged.

    Use ``async with VeeamClient(...) as vc:`` or call ``close()`` when done.
    """

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        api_version: str,
        verify_ssl: bool | ssl.SSLContext | str = True,
        disable_antiforgery_token: bool = True,
        timeout: float | httpx.Timeout | None = 30.0,
    ):
        self.host = host
        self.username = username
        self.password = password
        self.api_version = api_version
        self.verify_ssl = verify_ssl
        self.disable_antiforgery_token = disable_antiforgery_token
        # None is an explicit opt-out: no timeout at all.
        if timeout is None or isinstance(timeout, httpx.Timeout):
            self.timeout: httpx.Timeout | None = timeout
        else:
            self.timeout = httpx.Timeout(timeout)

        from .versions import VERSION_TO_PACKAGE

        if api_version not in VERSION_TO_PACKAGE:
            raise ValueError(f"Unsupported API version: {api_version}")

        self.package = VERSION_TO_PACKAGE[api_version]

        self._client = None
        self._access_token = None
        self._refresh_token = None
        self._expires_at: datetime | None = None
        # Serialises authentication so concurrent calls share one refresh. From Python
        # 3.10 an asyncio.Lock binds to a loop on first use, not on construction.
        self._auth_lock = asyncio.Lock()
        # Extra keyword arguments for the underlying httpx.AsyncClient (tests inject a
        # transport here).
        self._httpx_args: dict[str, Any] = {}

    async def __aenter__(self) -> "VeeamClient":
        return self

    async def __aexit__(self, *exc_info: Any) -> None:
        await self.close()

    # ----------------------------
    # generated-code plumbing
    # ----------------------------

    def _client_classes(self):
        client_mod = importlib.import_module(f"{self.package}.client")
        return client_mod.Client, client_mod.AuthenticatedClient

    def _client_kwargs(self) -> dict[str, Any]:
        return {
            "base_url": self.host,
            "verify_ssl": self.verify_ssl,
            "timeout": self.timeout,
            "httpx_args": dict(self._httpx_args),
        }

    def _token_body(self, grant: str, **fields: Any):
        TokenDataBody = importlib.import_module(f"{self.package}.models.token_data_body").TokenDataBody
        TokenDataBodyGrantType = importlib.import_module(
            f"{self.package}.models.token_data_body_grant_type"
        ).TokenDataBodyGrantType

        # The v6 model predates the disable_antiforgery_token field.
        if "disable_antiforgery_token" in attrs.fields_dict(TokenDataBody):
            fields["disable_antiforgery_token"] = self.disable_antiforgery_token

        return TokenDataBody(grant_type=getattr(TokenDataBodyGrantType, grant), **fields)

    async def _request_token(self, body) -> tuple[int, Any, httpx.Response]:
        """POST to the token endpoint; return (status code, parsed result, response).

        The parsed result is an OAuthTokenResponse, a RESTExceptionInfo, the raw JSON
        when it does not fit either model, or None when the body could not be decoded
        (a rejected request can come back empty).
        Transport errors propagate.

        The request goes through a short-lived unauthenticated client: an expired
        bearer token has no business on a token request.
        """
        token_mod = _import_with_unset_patch(f"{self.package}.api.auth.token", self.package)
        Client, _ = self._client_classes()

        token_client = Client(**self._client_kwargs())
        try:
            response = await token_client.get_async_httpx_client().request(**token_mod._get_kwargs(body=body))
        finally:
            await _aclose_generated_client(token_client)

        try:
            parsed = token_mod._parse_response(client=token_client, response=response)
        except (ValueError, KeyError, TypeError, AttributeError):
            # JSONDecodeError is a ValueError; an unknown error code or a missing
            # field in the model surfaces as one of the others. Keep the raw JSON, if
            # there is any, so the failure can still be described.
            try:
                parsed = response.json()
            except ValueError:
                parsed = None

        return response.status_code, parsed, response

    # ----------------------------
    # connection + auth
    # ----------------------------

    async def connect(self):
        """Authenticate with the password grant.

        Raises VeeamAuthenticationError when the server refuses the credentials.
        Transport errors propagate unchanged.
        """
        async with self._auth_lock:
            await self._connect()

    async def _connect(self):
        body = self._token_body("PASSWORD", username=self.username, password=self.password)
        status_code, token, response = await self._request_token(body)

        if not _is_token(token):
            if status_code >= 500 or status_code in _RETRYABLE_LOGIN_STATUSES:
                # A server error is not a verdict on the credentials; report it as
                # the HTTP failure it is so the caller retries rather than re-auths.
                response.raise_for_status()
            raise VeeamAuthenticationError(f"Veeam login failed: {_describe_login_failure(token, status_code)}")

        await self._store_token(token)

    async def close(self):
        """Drop the session and close the underlying HTTP connections."""
        old = self._client
        self._client = None
        self._invalidate_session()
        await _aclose_generated_client(old)

    # ----------------------------
    # token handling
    # ----------------------------

    async def _store_token(self, token):
        if not _is_token(token):
            raise VeeamAuthenticationError(f"Veeam login failed: {_describe_login_failure(token)}")

        _, AuthenticatedClient = self._client_classes()

        self._access_token = token.access_token
        self._refresh_token = token.refresh_token
        self._expires_at = datetime.now(timezone.utc) + timedelta(seconds=token.expires_in - 30)

        old = self._client
        self._client = AuthenticatedClient(
            token=self._access_token,
            **self._client_kwargs(),
        )
        await _aclose_generated_client(old)

    def _session_is_valid(self) -> bool:
        return (
            self._client is not None
            and self._access_token is not None
            and self._expires_at is not None
            and datetime.now(timezone.utc) < self._expires_at
        )

    async def _refresh_token_if_needed(self):
        if self._session_is_valid():
            return

        async with self._auth_lock:
            # Another call may have refreshed while this one waited for the lock.
            if self._session_is_valid():
                return

            if not self._refresh_token:
                # Nothing to refresh with: first use, or a session invalidated below.
                await self._connect()
                return

            # Try the refresh grant first, then fall back to the password grant. A
            # refresh token expires or is revoked server-side, and the server reports
            # that by *returning* a RESTExceptionInfo rather than raising, so a
            # non-token result has to fall back or every later call retries the same
            # dead refresh token.
            #
            # Transport errors propagate: the server is unreachable, and falling back to
            # the password grant would only hit it again.
            try:
                body = self._token_body("REFRESH_TOKEN", refresh_token=self._refresh_token)
                _, token, _ = await self._request_token(body)
            except _TRANSPORT_ERRORS:
                raise
            except Exception:
                token = None

            if not _is_token(token):
                self._invalidate_session()
                await self._connect()
                return

            await self._store_token(token)

    def _invalidate_session(self):
        """Forget the current token so the next call authenticates from scratch."""
        self._access_token = None
        self._refresh_token = None
        self._expires_at = None

    # ----------------------------
    # API access
    # ----------------------------

    def api(self, name: str) -> Any:
        """
        Smart API accessor.

        Examples:
            vc.api("repositories").get_all_repositories
            vc.api("repositories.get_all_repositories")
        """

        # direct operation
        if "." in name:
            mod = _import_with_unset_patch(f"{self.package}.api.{name}", self.package)
            return mod.asyncio

        # namespace
        return ApiNamespace(self, f"{self.package}.api.{name}")

    async def call(self, fn, *args, **kwargs):
        """
        Wrap any API call with automatic authentication and token refresh.

        Raises VeeamSessionError when the response cannot be decoded (how the server
        answers a rejected token); the session is dropped so the next call
        re-authenticates. The operation itself is never retried.
        """
        await self._refresh_token_if_needed()

        client = self._client
        try:
            return await fn(client=client, *args, **kwargs)
        except JSONDecodeError as err:
            # VB365 answers a rejected token with an empty body, which the generated
            # parser reports as "Expecting value: line 1 column 1 (char 0)" — the same
            # error from every endpoint until the process restarts. Drop the session so
            # the next call authenticates again, unless a concurrent call already
            # replaced it.
            #
            # The call is deliberately not retried: the operation may not be idempotent
            # (starting a restore, for instance), and a body that failed to decode is no
            # proof the server did not act on it.
            if self._client is client:
                self._invalidate_session()
            raise VeeamSessionError(
                "Veeam returned an undecodable response, which usually means the session "
                f"was rejected; re-authenticating on the next call ({err})"
            ) from err
