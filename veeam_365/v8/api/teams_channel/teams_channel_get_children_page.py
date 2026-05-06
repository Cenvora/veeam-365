from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_teams_node import PageOfRESTTeamsNode
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/teams/{team_id}/channels/{channel_id}/children".format(restore_session_id=quote(str(restore_session_id), safe=""),team_id=quote(str(team_id), safe=""),channel_id=quote(str(channel_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTTeamsNode | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTTeamsNode.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTTeamsNode | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[PageOfRESTTeamsNode | RESTExceptionInfo]:
    """ Get Teams Items of Channel

     Returns a collection of tabs, posts and files contained in a channel with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTTeamsNode | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
offset=offset,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> PageOfRESTTeamsNode | RESTExceptionInfo | None:
    """ Get Teams Items of Channel

     Returns a collection of tabs, posts and files contained in a channel with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTTeamsNode | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
client=client,
offset=offset,
limit=limit,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[PageOfRESTTeamsNode | RESTExceptionInfo]:
    """ Get Teams Items of Channel

     Returns a collection of tabs, posts and files contained in a channel with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTTeamsNode | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
offset=offset,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> PageOfRESTTeamsNode | RESTExceptionInfo | None:
    """ Get Teams Items of Channel

     Returns a collection of tabs, posts and files contained in a channel with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTTeamsNode | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
client=client,
offset=offset,
limit=limit,

    )).parsed
