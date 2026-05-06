from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from typing import cast
from uuid import UUID



def _get_kwargs(
    pool_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v8/ProxyPools/{pool_id}".format(pool_id=quote(str(pool_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RESTExceptionInfo:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | RESTExceptionInfo]:
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

) -> Response[Any | RESTExceptionInfo]:
    """ Remove Backup Proxy Pool

     Removes a backup proxy pool with the specified ID from the Veeam Backup for Microsoft 365
    infrastructure.

    Args:
        pool_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
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

) -> Any | RESTExceptionInfo | None:
    """ Remove Backup Proxy Pool

     Removes a backup proxy pool with the specified ID from the Veeam Backup for Microsoft 365
    infrastructure.

    Args:
        pool_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return sync_detailed(
        pool_id=pool_id,
client=client,

    ).parsed

async def asyncio_detailed(
    pool_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | RESTExceptionInfo]:
    """ Remove Backup Proxy Pool

     Removes a backup proxy pool with the specified ID from the Veeam Backup for Microsoft 365
    infrastructure.

    Args:
        pool_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        pool_id=pool_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    pool_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Any | RESTExceptionInfo | None:
    """ Remove Backup Proxy Pool

     Removes a backup proxy pool with the specified ID from the Veeam Backup for Microsoft 365
    infrastructure.

    Args:
        pool_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        pool_id=pool_id,
client=client,

    )).parsed
