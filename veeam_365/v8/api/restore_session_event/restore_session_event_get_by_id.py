from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_restore_session_event import RESTRestoreSessionEvent
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    event_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RestoreSessions/{restore_session_id}/Events/{event_id}".format(restore_session_id=quote(str(restore_session_id), safe=""),event_id=quote(str(event_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTRestoreSessionEvent:
    if response.status_code == 200:
        response_200 = RESTRestoreSessionEvent.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTRestoreSessionEvent]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | RESTRestoreSessionEvent]:
    """ Get Restore Session Event

     Returns a resource representation of properties for the specified event of a restore session with
    the specified ID.

    Args:
        restore_session_id (UUID):
        event_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSessionEvent]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
event_id=event_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTRestoreSessionEvent | None:
    """ Get Restore Session Event

     Returns a resource representation of properties for the specified event of a restore session with
    the specified ID.

    Args:
        restore_session_id (UUID):
        event_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSessionEvent
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
event_id=event_id,
client=client,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | RESTRestoreSessionEvent]:
    """ Get Restore Session Event

     Returns a resource representation of properties for the specified event of a restore session with
    the specified ID.

    Args:
        restore_session_id (UUID):
        event_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSessionEvent]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
event_id=event_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTRestoreSessionEvent | None:
    """ Get Restore Session Event

     Returns a resource representation of properties for the specified event of a restore session with
    the specified ID.

    Args:
        restore_session_id (UUID):
        event_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSessionEvent
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
event_id=event_id,
client=client,

    )).parsed
