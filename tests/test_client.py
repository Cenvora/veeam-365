"""Tests for VeeamClient authentication, refresh and session handling.

The generated SDK runs for real against an httpx.MockTransport, so request encoding and
response parsing are exercised rather than mocked out.
"""

import asyncio
import json
from datetime import datetime, timedelta, timezone
from urllib.parse import parse_qs

import httpx
import pytest

from veeam_365.client import VeeamClient, _camel_to_snake
from veeam_365.exceptions import (
    VeeamAuthenticationError,
    VeeamError,
    VeeamSessionError,
)
from veeam_365.versions import VERSION_TO_PACKAGE

HOST = "https://vb365.example.com:4443"
USERNAME = "administrator"
PASSWORD = "SuperSecretPassword"


def token_json(n):
    now = datetime.now(timezone.utc)
    return {
        "access_token": f"access-{n}",
        "refresh_token": f"refresh-{n}",
        "token_type": "bearer",
        "expires_in": 3600,
        "userName": USERNAME,
        ".issued": now.isoformat(),
        ".expires": (now + timedelta(hours=1)).isoformat(),
    }


class FakeServer:
    """A VB365 REST API stand-in.

    ``password_result`` / ``refresh_result`` are "ok" to issue a token, or an
    httpx.Response to answer with, or an exception to raise.
    """

    def __init__(self, password_result="ok", refresh_result="ok", api_result="ok"):
        self.password_result = password_result
        self.refresh_result = refresh_result
        self.api_result = api_result
        self.grants = []
        self.api_auth = []
        self.issued = 0
        self.token_delay = 0.0

    async def handler(self, request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/token"):
            form = {k: v[0] for k, v in parse_qs(request.content.decode()).items()}
            grant = form["grant_type"]
            self.grants.append(grant)
            if self.token_delay:
                await asyncio.sleep(self.token_delay)
            result = (
                self.password_result if grant == "password" else self.refresh_result
            )
            if grant == "password":
                assert form["username"] == USERNAME
                assert form["password"] == PASSWORD
            else:
                assert form["refresh_token"] == f"refresh-{self.issued}"
            if "authorization" in request.headers:
                raise AssertionError("token requests must not carry a bearer token")
            return self._answer(result, lambda: self._issue())

        self.api_auth.append(request.headers.get("authorization"))
        return self._answer(
            self.api_result,
            lambda: httpx.Response(
                200,
                json={
                    "version": "8.0",
                    "installationId": "12345678-1234-5678-1234-567812345678",
                },
            ),
        )

    def _issue(self):
        self.issued += 1
        return httpx.Response(200, json=token_json(self.issued))

    @staticmethod
    def _answer(result, ok):
        if isinstance(result, BaseException):
            raise result
        if isinstance(result, httpx.Response):
            # A fresh copy: a Response is single-use once a transport hands it out.
            return httpx.Response(
                result.status_code, content=result.content, headers=result.headers
            )
        return ok()


def make_client(server=None, api_version="v8", **kwargs):
    vc = VeeamClient(
        host=HOST,
        username=USERNAME,
        password=PASSWORD,
        api_version=api_version,
        **kwargs,
    )
    if server is not None:
        vc._httpx_args = {"transport": httpx.MockTransport(server.handler)}
    return vc


def service_instance(vc):
    return vc.api("service_instance").service_instance_get


def expire(vc):
    vc._expires_at = datetime.now(timezone.utc) - timedelta(seconds=1)


# ---------------------------------------------------------------------------
# construction and routing
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("version,package", sorted(VERSION_TO_PACKAGE.items()))
def test_routes_to_version_package(version, package):
    assert make_client(api_version=version).package == package


def test_rejects_unsupported_version():
    with pytest.raises(ValueError, match="Unsupported API version"):
        make_client(api_version="v5")


def test_starts_unauthenticated():
    vc = make_client()
    assert vc._client is None
    assert vc._access_token is None
    assert vc._expires_at is None


def test_constructs_outside_a_running_loop():
    # HA constructs clients in executor threads; nothing here may need a loop.
    vc = make_client()
    assert vc._auth_lock is not None


def test_dotted_path_resolves_operation():
    vc = make_client()
    assert vc.api("service_instance.service_instance_get") is service_instance(vc)


@pytest.mark.parametrize(
    "camel,snake",
    [
        ("getAllRepositories", "get_all_repositories"),
        ("BackupObjects", "backup_objects"),
        ("already_snake", "already_snake"),
    ],
)
def test_camel_to_snake(camel, snake):
    assert _camel_to_snake(camel) == snake


def test_exception_hierarchy():
    assert issubclass(VeeamAuthenticationError, VeeamError)
    assert issubclass(VeeamAuthenticationError, PermissionError)
    assert issubclass(VeeamSessionError, VeeamError)
    assert issubclass(VeeamSessionError, PermissionError)
    assert not issubclass(VeeamSessionError, VeeamAuthenticationError)


# ---------------------------------------------------------------------------
# timeout
# ---------------------------------------------------------------------------


def test_timeout_defaults_to_30_seconds():
    assert make_client().timeout == httpx.Timeout(30.0)


def test_timeout_float_and_none():
    assert make_client(timeout=5).timeout == httpx.Timeout(5)
    assert make_client(timeout=None).timeout is None
    custom = httpx.Timeout(10.0, connect=2.0)
    assert make_client(timeout=custom).timeout is custom


@pytest.mark.asyncio
async def test_timeout_and_verify_applied_to_generated_clients():
    server = FakeServer()
    vc = make_client(server, timeout=7.5, verify_ssl=False)
    await vc.connect()
    try:
        assert vc._client._timeout == httpx.Timeout(7.5)
        assert vc._client._verify_ssl is False
        assert vc._client.get_async_httpx_client().timeout == httpx.Timeout(7.5)
    finally:
        await vc.close()


@pytest.mark.asyncio
async def test_no_timeout_opt_out_reaches_httpx():
    server = FakeServer()
    vc = make_client(server, timeout=None)
    await vc.connect()
    try:
        assert vc._client.get_async_httpx_client().timeout == httpx.Timeout(None)
    finally:
        await vc.close()


# ---------------------------------------------------------------------------
# login
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
@pytest.mark.parametrize("api_version", sorted(VERSION_TO_PACKAGE))
async def test_login_success(api_version):
    server = FakeServer()
    async with make_client(server, api_version=api_version) as vc:
        await vc.connect()
        assert server.grants == ["password"]
        assert vc._access_token == "access-1"
        assert vc._expires_at.tzinfo is not None
        # 3600s lifetime minus the 30s safety margin
        remaining = vc._expires_at - datetime.now(timezone.utc)
        assert timedelta(seconds=3560) < remaining <= timedelta(seconds=3570)

        result = await vc.call(service_instance(vc))
        assert result.version == "8.0"
        assert server.api_auth == ["Bearer access-1"]


@pytest.mark.asyncio
async def test_call_connects_on_first_use():
    server = FakeServer()
    async with make_client(server) as vc:
        await vc.call(service_instance(vc))
        assert server.grants == ["password"]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "response",
    [
        httpx.Response(
            401, json={"message": "Access denied", "errorCode": "ResourceAccessDenied"}
        ),
        httpx.Response(401, json={"message": "Denied", "errorCode": "NotInTheEnum"}),
        httpx.Response(
            400, json={"error": "invalid_grant", "error_description": "bad password"}
        ),
        httpx.Response(401),
    ],
    ids=["rest-exception-info", "unknown-error-code", "oauth-error", "empty-body"],
)
async def test_login_rejected_raises_authentication_error(response):
    server = FakeServer(password_result=response)
    vc = make_client(server)

    with pytest.raises(VeeamAuthenticationError, match="Veeam login failed") as info:
        await vc.connect()

    assert str(response.status_code) in str(info.value)
    assert vc._access_token is None, "a refused login must not look authenticated"
    assert vc._expires_at is None


@pytest.mark.asyncio
async def test_login_error_message_is_reported():
    server = FakeServer(
        password_result=httpx.Response(
            401,
            json={
                "message": "Invalid user name or password",
                "errorCode": "Unauthorized",
            },
        )
    )
    vc = make_client(server)
    with pytest.raises(VeeamAuthenticationError, match="Invalid user name or password"):
        await vc.connect()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "error",
    [httpx.ConnectError("connection refused"), httpx.ReadTimeout("timed out")],
    ids=["connect-error", "timeout"],
)
async def test_connect_to_down_server_propagates_transport_error(error):
    server = FakeServer(password_result=error)
    vc = make_client(server)

    with pytest.raises(type(error)) as info:
        await vc.connect()

    assert not isinstance(info.value, VeeamError)


@pytest.mark.asyncio
async def test_login_server_error_is_not_an_authentication_error():
    server = FakeServer(password_result=httpx.Response(503, text="Service Unavailable"))
    vc = make_client(server)

    with pytest.raises(httpx.HTTPStatusError) as info:
        await vc.connect()

    assert not isinstance(info.value, VeeamError)


# ---------------------------------------------------------------------------
# refresh
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_expired_token_is_refreshed():
    server = FakeServer()
    async with make_client(server) as vc:
        await vc.connect()
        expire(vc)

        await vc.call(service_instance(vc))

        assert server.grants == ["password", "refresh_token"]
        assert server.api_auth == ["Bearer access-2"]


@pytest.mark.asyncio
async def test_refresh_error_falls_back_to_password():
    """A revoked refresh token comes back as a RESTExceptionInfo, not an exception."""
    server = FakeServer()
    async with make_client(server) as vc:
        await vc.connect()
        expire(vc)
        server.refresh_result = httpx.Response(
            400,
            json={"message": "Refresh token is invalid", "errorCode": "Unauthorized"},
        )

        await vc.call(service_instance(vc))

        assert server.grants == ["password", "refresh_token", "password"]
        assert vc._access_token == "access-2"
        assert server.api_auth == ["Bearer access-2"]


@pytest.mark.asyncio
async def test_refresh_empty_body_falls_back_to_password():
    server = FakeServer()
    async with make_client(server) as vc:
        await vc.connect()
        expire(vc)
        server.refresh_result = httpx.Response(401)

        await vc.call(service_instance(vc))

        assert server.grants == ["password", "refresh_token", "password"]


@pytest.mark.asyncio
async def test_refresh_error_and_password_rejected_raises_authentication_error():
    server = FakeServer()
    async with make_client(server) as vc:
        await vc.connect()
        expire(vc)
        server.refresh_result = httpx.Response(
            400, json={"message": "Refresh token is invalid"}
        )
        server.password_result = httpx.Response(
            401, json={"message": "Password changed"}
        )

        with pytest.raises(VeeamAuthenticationError, match="Password changed"):
            await vc.call(service_instance(vc))

        assert vc._refresh_token is None, "the dead refresh token must not be retried"

        # Next call goes straight to the password grant rather than the dead refresh.
        server.password_result = "ok"
        await vc.call(service_instance(vc))
        assert server.grants == ["password", "refresh_token", "password", "password"]


@pytest.mark.asyncio
async def test_refresh_transport_error_propagates_without_password_fallback():
    server = FakeServer()
    async with make_client(server) as vc:
        await vc.connect()
        expire(vc)
        server.refresh_result = httpx.ConnectError("connection refused")

        with pytest.raises(httpx.ConnectError):
            await vc.call(service_instance(vc))

        assert server.grants == ["password", "refresh_token"]


@pytest.mark.asyncio
async def test_concurrent_calls_share_one_refresh():
    server = FakeServer()
    server.token_delay = 0.05
    async with make_client(server) as vc:
        await vc.connect()
        expire(vc)

        await asyncio.gather(*(vc.call(service_instance(vc)) for _ in range(10)))

        assert server.grants == ["password", "refresh_token"]
        assert server.api_auth == ["Bearer access-2"] * 10


@pytest.mark.asyncio
async def test_concurrent_first_calls_share_one_login():
    server = FakeServer()
    server.token_delay = 0.05
    async with make_client(server) as vc:
        await asyncio.gather(*(vc.call(service_instance(vc)) for _ in range(5)))
        assert server.grants == ["password"]


# ---------------------------------------------------------------------------
# rejected session
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_undecodable_response_raises_session_error_and_reauthenticates():
    server = FakeServer()
    async with make_client(server) as vc:
        await vc.connect()
        server.api_result = httpx.Response(401)  # empty body

        with pytest.raises(VeeamSessionError, match="undecodable response") as info:
            await vc.call(service_instance(vc))

        assert isinstance(info.value.__cause__, json.JSONDecodeError)
        assert not isinstance(info.value, VeeamAuthenticationError)
        assert vc._access_token is None
        assert vc._refresh_token is None
        assert vc._expires_at is None

        server.api_result = "ok"
        await vc.call(service_instance(vc))

        assert server.grants == ["password", "password"]
        assert server.api_auth[-1] == "Bearer access-2"


@pytest.mark.asyncio
async def test_undecodable_response_is_not_retried():
    """Retrying could repeat a non-idempotent operation such as starting a restore."""
    server = FakeServer(api_result=httpx.Response(401))
    async with make_client(server) as vc:
        with pytest.raises(VeeamSessionError):
            await vc.call(service_instance(vc))
        assert len(server.api_auth) == 1


@pytest.mark.asyncio
async def test_documented_error_result_is_returned():
    server = FakeServer(
        api_result=httpx.Response(
            404, json={"message": "Not found", "errorCode": "ResourceNotFound"}
        )
    )
    async with make_client(server) as vc:
        result = await vc.call(service_instance(vc))
        assert type(result).__name__ == "RESTExceptionInfo"
        assert result.message == "Not found"


# ---------------------------------------------------------------------------
# closing
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_replaced_clients_are_closed():
    server = FakeServer()
    vc = make_client(server)
    await vc.connect()
    await vc.call(service_instance(vc))
    first = vc._client.get_async_httpx_client()

    expire(vc)
    await vc.call(service_instance(vc))
    second = vc._client.get_async_httpx_client()

    assert first is not second
    assert first.is_closed
    assert not second.is_closed

    await vc.close()
    assert second.is_closed
    assert vc._client is None
    assert vc._access_token is None


@pytest.mark.asyncio
async def test_token_request_clients_are_closed(monkeypatch):
    server = FakeServer()
    created = []
    real = httpx.AsyncClient.__init__

    def tracking_init(self, *args, **kwargs):
        created.append(self)
        real(self, *args, **kwargs)

    monkeypatch.setattr(httpx.AsyncClient, "__init__", tracking_init)

    async with make_client(server) as vc:
        await vc.connect()
        expire(vc)
        await vc.call(service_instance(vc))
        live = vc._client.get_async_httpx_client()

    assert all(c.is_closed for c in created), "every httpx client must be closed"
    assert live in created


@pytest.mark.asyncio
async def test_close_without_connect_is_safe():
    vc = make_client()
    await vc.close()
    async with make_client():
        pass
