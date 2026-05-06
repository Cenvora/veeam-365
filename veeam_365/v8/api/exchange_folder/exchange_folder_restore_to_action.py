from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_async_restore_response import RESTAsyncRestoreResponse
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_restore_to_different_location import RESTRestoreToDifferentLocation
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    mailbox_id: UUID,
    folder_id: str,
    *,
    body: RESTRestoreToDifferentLocation,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/mailboxes/{mailbox_id}/folders/{folder_id}/restoreTo".format(restore_session_id=quote(str(restore_session_id), safe=""),mailbox_id=quote(str(mailbox_id), safe=""),folder_id=quote(str(folder_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTAsyncRestoreResponse | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTAsyncRestoreResponse.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTAsyncRestoreResponse | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    mailbox_id: UUID,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToDifferentLocation,

) -> Response[RESTAsyncRestoreResponse | RESTExceptionInfo]:
    """ Restore Data from Folders to Another Mailbox

     Restores backed-up data from an organization mailbox folder with the specified ID to another
    mailbox.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        folder_id (str):
        body (RESTRestoreToDifferentLocation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAsyncRestoreResponse | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
folder_id=folder_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    mailbox_id: UUID,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToDifferentLocation,

) -> RESTAsyncRestoreResponse | RESTExceptionInfo | None:
    """ Restore Data from Folders to Another Mailbox

     Restores backed-up data from an organization mailbox folder with the specified ID to another
    mailbox.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        folder_id (str):
        body (RESTRestoreToDifferentLocation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAsyncRestoreResponse | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
folder_id=folder_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    mailbox_id: UUID,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToDifferentLocation,

) -> Response[RESTAsyncRestoreResponse | RESTExceptionInfo]:
    """ Restore Data from Folders to Another Mailbox

     Restores backed-up data from an organization mailbox folder with the specified ID to another
    mailbox.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        folder_id (str):
        body (RESTRestoreToDifferentLocation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAsyncRestoreResponse | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
folder_id=folder_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    mailbox_id: UUID,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToDifferentLocation,

) -> RESTAsyncRestoreResponse | RESTExceptionInfo | None:
    """ Restore Data from Folders to Another Mailbox

     Restores backed-up data from an organization mailbox folder with the specified ID to another
    mailbox.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        folder_id (str):
        body (RESTRestoreToDifferentLocation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAsyncRestoreResponse | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
folder_id=folder_id,
client=client,
body=body,

    )).parsed
