from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_proxy import PageOfRESTProxy
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pool_id: UUID,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/ProxyPools/{pool_id}/proxies".format(
            pool_id=quote(str(pool_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTProxy | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTProxy.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTProxy | RESTExceptionInfo]:
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTProxy | RESTExceptionInfo]:
    """Get Backup Proxy Servers by Backup Proxy Pool ID

     Returns a collection of backup proxy servers added to a backup proxy pool with the specified ID.

    Args:
        pool_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTProxy | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        pool_id=pool_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pool_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTProxy | RESTExceptionInfo | None:
    """Get Backup Proxy Servers by Backup Proxy Pool ID

     Returns a collection of backup proxy servers added to a backup proxy pool with the specified ID.

    Args:
        pool_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTProxy | RESTExceptionInfo
    """

    return sync_detailed(
        pool_id=pool_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    pool_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTProxy | RESTExceptionInfo]:
    """Get Backup Proxy Servers by Backup Proxy Pool ID

     Returns a collection of backup proxy servers added to a backup proxy pool with the specified ID.

    Args:
        pool_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTProxy | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        pool_id=pool_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pool_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTProxy | RESTExceptionInfo | None:
    """Get Backup Proxy Servers by Backup Proxy Pool ID

     Returns a collection of backup proxy servers added to a backup proxy pool with the specified ID.

    Args:
        pool_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTProxy | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            pool_id=pool_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
