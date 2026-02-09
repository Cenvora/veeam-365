from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_proxy_pool import RESTProxyPool
from ...types import Response


def _get_kwargs(
    pool_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/ProxyPools/{pool_id}".format(
            pool_id=quote(str(pool_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTProxyPool:
    if response.status_code == 200:
        response_200 = RESTProxyPool.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTProxyPool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pool_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTProxyPool]:
    """Get Backup Proxy Pool

     Returns a resource representation of a backup proxy pool with the specified ID.

    Args:
        pool_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTProxyPool]
    """

    kwargs = _get_kwargs(
        pool_id=pool_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pool_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTProxyPool | None:
    """Get Backup Proxy Pool

     Returns a resource representation of a backup proxy pool with the specified ID.

    Args:
        pool_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTProxyPool
    """

    return sync_detailed(
        pool_id=pool_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    pool_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTProxyPool]:
    """Get Backup Proxy Pool

     Returns a resource representation of a backup proxy pool with the specified ID.

    Args:
        pool_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTProxyPool]
    """

    kwargs = _get_kwargs(
        pool_id=pool_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pool_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTProxyPool | None:
    """Get Backup Proxy Pool

     Returns a resource representation of a backup proxy pool with the specified ID.

    Args:
        pool_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTProxyPool
    """

    return (
        await asyncio_detailed(
            pool_id=pool_id,
            client=client,
        )
    ).parsed
