import importlib
import re
from datetime import datetime, timedelta
from typing import Any

# ----------------------------
# helpers
# ----------------------------


def _camel_to_snake(name: str) -> str:
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


# ----------------------------
# API namespace proxy
# ----------------------------


class ApiNamespace:
    """
    Lazy namespace for openapi-python-client operation modules.

    Example:
        vc.api("repositories").get_all_repositories
        → veeam_br.vX.api.repositories.get_all_repositories.asyncio
    """

    def __init__(self, client: "VeeamClient", base_module: str):
        self._client = client
        self._base = base_module

    def __getattr__(self, name: str):
        mod = importlib.import_module(f"{self._base}.{name}")
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
    - token refresh
    - API namespace routing
    """

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        api_version: str,
        verify_ssl: bool = True,
    ):
        self.host = host.rstrip("/")
        self.username = username
        self.password = password
        self.api_version = api_version
        self.verify_ssl = verify_ssl

        from .versions import VERSION_TO_PACKAGE

        if api_version not in VERSION_TO_PACKAGE:
            raise ValueError(f"Unsupported API version: {api_version}")

        self.package = VERSION_TO_PACKAGE[api_version]

        self._client = None
        self._access_token = None
        self._refresh_token = None
        self._expires_at: datetime | None = None

    async def _request_token(
        self,
        *,
        client,
        grant_type: str,
        username: str | None = None,
        password: str | None = None,
        refresh_token: str | None = None,
    ):
        TokenJsonBody = getattr(
            importlib.import_module(f"{self.package}.models.token_json_body"),
            "TokenJsonBody",
        )
        RESTExceptionInfo = getattr(
            importlib.import_module(f"{self.package}.models.rest_exception_info"),
            "RESTExceptionInfo",
        )
        # Import the token module and get its 'asyncio' function
        # This is the async version of the token endpoint from the generated API
        token_module = importlib.import_module(f"{self.package}.api.auth.token")
        request_token = token_module.asyncio

        body = TokenJsonBody(
            grant_type=grant_type,
            username=username,
            password=password,
            refresh_token=refresh_token,
        )

        result = await request_token(client=client, body=body)

        if isinstance(result, RESTExceptionInfo):
            error_code = getattr(result, 'code', 'N/A')
            error_message = getattr(result, 'message', str(result))
            raise RuntimeError(
                f"Token request failed: code={error_code}, message={error_message}"
            )

        return result

    # ----------------------------
    # connection + auth
    # ----------------------------

    async def connect(self):
        Client = getattr(importlib.import_module(f"{self.package}.client"), "Client")
        AuthenticatedClient = getattr(
            importlib.import_module(f"{self.package}.client"), "AuthenticatedClient"
        )

        TokenJsonBodyGrantType = getattr(
            importlib.import_module(
                f"{self.package}.models.token_json_body_grant_type"
            ),
            "TokenJsonBodyGrantType",
        )

        # unauthenticated client
        self._client = Client(
            base_url=self.host,
            verify_ssl=self.verify_ssl,
        )

        token = await self._request_token(
            client=self._client,
            grant_type=TokenJsonBodyGrantType.PASSWORD,
            username=self.username,
            password=self.password,
        )

        self._store_token(token, AuthenticatedClient)

    async def close(self):
        # openapi-python-client has no shared session to close
        pass

    # ----------------------------
    # token handling
    # ----------------------------

    def _store_token(self, token, AuthenticatedClient):
        self._access_token = token.access_token
        self._refresh_token = token.refresh_token
        self._expires_at = datetime.utcnow() + timedelta(seconds=token.expires_in - 30)

        self._client = AuthenticatedClient(
            base_url=self.host,
            token=self._access_token,
            verify_ssl=self.verify_ssl,
        )

    async def _refresh_token_if_needed(self):
        if self._expires_at and datetime.utcnow() < self._expires_at:
            return

        TokenJsonBodyGrantType = getattr(
            importlib.import_module(
                f"{self.package}.models.token_json_body_grant_type"
            ),
            "TokenJsonBodyGrantType",
        )

        Client = getattr(importlib.import_module(f"{self.package}.client"), "Client")
        AuthenticatedClient = getattr(
            importlib.import_module(f"{self.package}.client"), "AuthenticatedClient"
        )

        # try refresh first
        try:
            token = await self._request_token(
                client=self._client,
                grant_type=TokenJsonBodyGrantType.REFRESH_TOKEN,
                refresh_token=self._refresh_token,
            )
        except Exception:
            # fallback to password
            tmp = Client(
                base_url=self.host,
                verify_ssl=self.verify_ssl,
            )
            token = await self._request_token(
                client=tmp,
                grant_type=TokenJsonBodyGrantType.PASSWORD,
                username=self.username,
                password=self.password,
            )

        self._store_token(token, AuthenticatedClient)

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
            mod = importlib.import_module(f"{self.package}.api.{name}")
            return mod.asyncio

        # namespace
        return ApiNamespace(self, f"{self.package}.api.{name}")

    async def call(self, fn, *args, **kwargs):
        """
        Wrap any API call with:
        - automatic token refresh
        """
        await self._refresh_token_if_needed()

        return await fn(client=self._client, *args, **kwargs)
