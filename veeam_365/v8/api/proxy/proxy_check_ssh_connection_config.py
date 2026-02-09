from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_ssh_connection_config_validation_result import RESTSshConnectionConfigValidationResult
from ...models.rest_ssh_settings_from_client import RESTSshSettingsFromClient
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: RESTSshSettingsFromClient,
    host: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["host"] = host

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/Proxies/CheckSshConnectionConfig",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTSshConnectionConfigValidationResult:
    if response.status_code == 200:
        response_200 = RESTSshConnectionConfigValidationResult.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTSshConnectionConfigValidationResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTSshSettingsFromClient,
    host: str,
) -> Response[RESTExceptionInfo | RESTSshConnectionConfigValidationResult]:
    """Check SSH Connection

     Allows you to check the SSH connection to a Linux machine.

    Args:
        host (str):
        body (RESTSshSettingsFromClient): Specifies credentials to access the Linux-based backup
            proxy server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTSshConnectionConfigValidationResult]
    """

    kwargs = _get_kwargs(
        body=body,
        host=host,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RESTSshSettingsFromClient,
    host: str,
) -> RESTExceptionInfo | RESTSshConnectionConfigValidationResult | None:
    """Check SSH Connection

     Allows you to check the SSH connection to a Linux machine.

    Args:
        host (str):
        body (RESTSshSettingsFromClient): Specifies credentials to access the Linux-based backup
            proxy server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTSshConnectionConfigValidationResult
    """

    return sync_detailed(
        client=client,
        body=body,
        host=host,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTSshSettingsFromClient,
    host: str,
) -> Response[RESTExceptionInfo | RESTSshConnectionConfigValidationResult]:
    """Check SSH Connection

     Allows you to check the SSH connection to a Linux machine.

    Args:
        host (str):
        body (RESTSshSettingsFromClient): Specifies credentials to access the Linux-based backup
            proxy server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTSshConnectionConfigValidationResult]
    """

    kwargs = _get_kwargs(
        body=body,
        host=host,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RESTSshSettingsFromClient,
    host: str,
) -> RESTExceptionInfo | RESTSshConnectionConfigValidationResult | None:
    """Check SSH Connection

     Allows you to check the SSH connection to a Linux machine.

    Args:
        host (str):
        body (RESTSshSettingsFromClient): Specifies credentials to access the Linux-based backup
            proxy server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTSshConnectionConfigValidationResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            host=host,
        )
    ).parsed
