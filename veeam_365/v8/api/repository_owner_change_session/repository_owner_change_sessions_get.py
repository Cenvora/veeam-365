from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_backup_repository_owner_change_session import PageOfRESTBackupRepositoryOwnerChangeSession
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
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
        "url": "/v8/RepositoryOwnerChangeSessions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTBackupRepositoryOwnerChangeSession.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[PageOfRESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]:
    """ Get Change Owner Sessions

     Returns a collection of change owner sessions when Veeam Backup for Microsoft 365 changes an owner
    for backup repositories from one to another.

    Args:
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> PageOfRESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo | None:
    """ Get Change Owner Sessions

     Returns a collection of change owner sessions when Veeam Backup for Microsoft 365 changes an owner
    for backup repositories from one to another.

    Args:
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo
     """


    return sync_detailed(
        client=client,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[PageOfRESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]:
    """ Get Change Owner Sessions

     Returns a collection of change owner sessions when Veeam Backup for Microsoft 365 changes an owner
    for backup repositories from one to another.

    Args:
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> PageOfRESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo | None:
    """ Get Change Owner Sessions

     Returns a collection of change owner sessions when Veeam Backup for Microsoft 365 changes an owner
    for backup repositories from one to another.

    Args:
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
offset=offset,

    )).parsed
