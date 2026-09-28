from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_proxy_from_client import RESTProxyFromClient
from ...types import Response


def _get_kwargs(
    proxy_id: UUID,
    *,
    body: RESTProxyFromClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v8/Proxies/{proxy_id}".format(
            proxy_id=quote(str(proxy_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RESTExceptionInfo:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    proxy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTProxyFromClient,
) -> Response[Any | RESTExceptionInfo]:
    """Edit Backup Proxy Server Settings

     Modifies settings of a backup proxy server with the specified ID.

    Args:
        proxy_id (UUID):
        body (RESTProxyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        proxy_id=proxy_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proxy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTProxyFromClient,
) -> Any | RESTExceptionInfo | None:
    """Edit Backup Proxy Server Settings

     Modifies settings of a backup proxy server with the specified ID.

    Args:
        proxy_id (UUID):
        body (RESTProxyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return sync_detailed(
        proxy_id=proxy_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    proxy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTProxyFromClient,
) -> Response[Any | RESTExceptionInfo]:
    """Edit Backup Proxy Server Settings

     Modifies settings of a backup proxy server with the specified ID.

    Args:
        proxy_id (UUID):
        body (RESTProxyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        proxy_id=proxy_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proxy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTProxyFromClient,
) -> Any | RESTExceptionInfo | None:
    """Edit Backup Proxy Server Settings

     Modifies settings of a backup proxy server with the specified ID.

    Args:
        proxy_id (UUID):
        body (RESTProxyFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            proxy_id=proxy_id,
            client=client,
            body=body,
        )
    ).parsed
