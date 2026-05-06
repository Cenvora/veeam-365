from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_teams_file import PageOfRESTTeamsFile
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    team_id: UUID,
    *,
    channel_id: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    folders_only: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["channelId"] = channel_id

    params["parentId"] = parent_id

    params["foldersOnly"] = folders_only

    params["offset"] = offset

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/teams/{team_id}/files".format(restore_session_id=quote(str(restore_session_id), safe=""),team_id=quote(str(team_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTTeamsFile | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTTeamsFile.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTTeamsFile | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    channel_id: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    folders_only: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[PageOfRESTTeamsFile | RESTExceptionInfo]:
    """ Get Files

     Returns a collection of backed-up files of a Microsoft Teams team with the specified ID to explore
    and restore.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str | Unset):
        parent_id (str | Unset):
        folders_only (bool | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTTeamsFile | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
parent_id=parent_id,
folders_only=folders_only,
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
    *,
    client: AuthenticatedClient | Client,
    channel_id: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    folders_only: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> PageOfRESTTeamsFile | RESTExceptionInfo | None:
    """ Get Files

     Returns a collection of backed-up files of a Microsoft Teams team with the specified ID to explore
    and restore.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str | Unset):
        parent_id (str | Unset):
        folders_only (bool | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTTeamsFile | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
team_id=team_id,
client=client,
channel_id=channel_id,
parent_id=parent_id,
folders_only=folders_only,
offset=offset,
limit=limit,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    channel_id: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    folders_only: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[PageOfRESTTeamsFile | RESTExceptionInfo]:
    """ Get Files

     Returns a collection of backed-up files of a Microsoft Teams team with the specified ID to explore
    and restore.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str | Unset):
        parent_id (str | Unset):
        folders_only (bool | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTTeamsFile | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
parent_id=parent_id,
folders_only=folders_only,
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
    *,
    client: AuthenticatedClient | Client,
    channel_id: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    folders_only: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> PageOfRESTTeamsFile | RESTExceptionInfo | None:
    """ Get Files

     Returns a collection of backed-up files of a Microsoft Teams team with the specified ID to explore
    and restore.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str | Unset):
        parent_id (str | Unset):
        folders_only (bool | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTTeamsFile | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
team_id=team_id,
client=client,
channel_id=channel_id,
parent_id=parent_id,
folders_only=folders_only,
offset=offset,
limit=limit,

    )).parsed
