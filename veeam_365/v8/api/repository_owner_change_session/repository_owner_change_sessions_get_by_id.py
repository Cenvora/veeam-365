from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_backup_repository_owner_change_session import RESTBackupRepositoryOwnerChangeSession
from ...models.rest_exception_info import RESTExceptionInfo
from typing import cast
from uuid import UUID



def _get_kwargs(
    session_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RepositoryOwnerChangeSessions/{session_id}".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTBackupRepositoryOwnerChangeSession.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]:
    """ Get Change Owner Session

     Returns a resource representation of a change owner session with the specified ID when Veeam Backup
    for Microsoft 365 changes an owner for backup repositories from one to another.

    Args:
        session_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        session_id=session_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo | None:
    """ Get Change Owner Session

     Returns a resource representation of a change owner session with the specified ID when Veeam Backup
    for Microsoft 365 changes an owner for backup repositories from one to another.

    Args:
        session_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]:
    """ Get Change Owner Session

     Returns a resource representation of a change owner session with the specified ID when Veeam Backup
    for Microsoft 365 changes an owner for backup repositories from one to another.

    Args:
        session_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        session_id=session_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo | None:
    """ Get Change Owner Session

     Returns a resource representation of a change owner session with the specified ID when Veeam Backup
    for Microsoft 365 changes an owner for backup repositories from one to another.

    Args:
        session_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
