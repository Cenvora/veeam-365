from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_channel_entity import PageOfRESTChannelEntity
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_teams_search_options import RESTTeamsSearchOptions
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    body: RESTTeamsSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/teams/{team_id}/channels/{channel_id}/search".format(restore_session_id=quote(str(restore_session_id), safe=""),team_id=quote(str(team_id), safe=""),channel_id=quote(str(channel_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTChannelEntity | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTChannelEntity.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTChannelEntity | RESTExceptionInfo]:
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
    body: RESTTeamsSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[PageOfRESTChannelEntity | RESTExceptionInfo]:
    """ Search for Teams Items in Channel

     Searches for Microsoft Teams items in a backed-up channel with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        offset (int | Unset):
        limit (int | Unset):
        body (RESTTeamsSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTChannelEntity | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
body=body,
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
    body: RESTTeamsSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> PageOfRESTChannelEntity | RESTExceptionInfo | None:
    """ Search for Teams Items in Channel

     Searches for Microsoft Teams items in a backed-up channel with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        offset (int | Unset):
        limit (int | Unset):
        body (RESTTeamsSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTChannelEntity | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
client=client,
body=body,
offset=offset,
limit=limit,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTTeamsSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[PageOfRESTChannelEntity | RESTExceptionInfo]:
    """ Search for Teams Items in Channel

     Searches for Microsoft Teams items in a backed-up channel with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        offset (int | Unset):
        limit (int | Unset):
        body (RESTTeamsSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTChannelEntity | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
body=body,
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
    body: RESTTeamsSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> PageOfRESTChannelEntity | RESTExceptionInfo | None:
    """ Search for Teams Items in Channel

     Searches for Microsoft Teams items in a backed-up channel with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        offset (int | Unset):
        limit (int | Unset):
        body (RESTTeamsSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTChannelEntity | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
client=client,
body=body,
offset=offset,
limit=limit,

    )).parsed
