from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_proxy import RESTProxy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    proxy_id: UUID,
    *,
    extended_view: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["extendedView"] = extended_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/Proxies/{proxy_id}".format(
            proxy_id=quote(str(proxy_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTProxy:
    if response.status_code == 200:
        response_200 = RESTProxy.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTProxy]:
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
    extended_view: bool | Unset = False,
) -> Response[RESTExceptionInfo | RESTProxy]:
    """Get Backup Proxy Server

     Returns a resource representation of a backup proxy server with the specified ID.

    Args:
        proxy_id (UUID):
        extended_view (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTProxy]
    """

    kwargs = _get_kwargs(
        proxy_id=proxy_id,
        extended_view=extended_view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proxy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool | Unset = False,
) -> RESTExceptionInfo | RESTProxy | None:
    """Get Backup Proxy Server

     Returns a resource representation of a backup proxy server with the specified ID.

    Args:
        proxy_id (UUID):
        extended_view (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTProxy
    """

    return sync_detailed(
        proxy_id=proxy_id,
        client=client,
        extended_view=extended_view,
    ).parsed


async def asyncio_detailed(
    proxy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool | Unset = False,
) -> Response[RESTExceptionInfo | RESTProxy]:
    """Get Backup Proxy Server

     Returns a resource representation of a backup proxy server with the specified ID.

    Args:
        proxy_id (UUID):
        extended_view (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTProxy]
    """

    kwargs = _get_kwargs(
        proxy_id=proxy_id,
        extended_view=extended_view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proxy_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool | Unset = False,
) -> RESTExceptionInfo | RESTProxy | None:
    """Get Backup Proxy Server

     Returns a resource representation of a backup proxy server with the specified ID.

    Args:
        proxy_id (UUID):
        extended_view (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTProxy
    """

    return (
        await asyncio_detailed(
            proxy_id=proxy_id,
            client=client,
            extended_view=extended_view,
        )
    ).parsed
