from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_async_restore_response import RESTAsyncRestoreResponse
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_restore_to_original import RESTRestoreToOriginal
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    body: RESTRestoreToOriginal,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/Organization/OneDrives/{one_drive_id}/restore".format(restore_session_id=quote(str(restore_session_id), safe=""),one_drive_id=quote(str(one_drive_id), safe=""),),
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
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToOriginal,

) -> Response[RESTAsyncRestoreResponse | RESTExceptionInfo]:
    """ Restore OneDrive Data

     Restores backed-up data of OneDrive with the specified ID to its original location.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTRestoreToOriginal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAsyncRestoreResponse | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
one_drive_id=one_drive_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToOriginal,

) -> RESTAsyncRestoreResponse | RESTExceptionInfo | None:
    """ Restore OneDrive Data

     Restores backed-up data of OneDrive with the specified ID to its original location.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTRestoreToOriginal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAsyncRestoreResponse | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
one_drive_id=one_drive_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToOriginal,

) -> Response[RESTAsyncRestoreResponse | RESTExceptionInfo]:
    """ Restore OneDrive Data

     Restores backed-up data of OneDrive with the specified ID to its original location.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTRestoreToOriginal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAsyncRestoreResponse | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
one_drive_id=one_drive_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToOriginal,

) -> RESTAsyncRestoreResponse | RESTExceptionInfo | None:
    """ Restore OneDrive Data

     Restores backed-up data of OneDrive with the specified ID to its original location.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTRestoreToOriginal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAsyncRestoreResponse | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
one_drive_id=one_drive_id,
client=client,
body=body,

    )).parsed
