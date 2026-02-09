from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_teams_tab import RestTeamsTab
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    tab_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/teams/{team_id}/channels/{channel_id}/tabs/{tab_id}".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            team_id=quote(str(team_id), safe=""),
            channel_id=quote(str(channel_id), safe=""),
            tab_id=quote(str(tab_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RestTeamsTab:
    if response.status_code == 200:
        response_200 = RestTeamsTab.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RestTeamsTab]:
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
    tab_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RestTeamsTab]:
    """Get Tab

     Returns a resource representation of a backed-up Microsoft Teams channel tab with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        tab_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RestTeamsTab]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        channel_id=channel_id,
        tab_id=tab_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    tab_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RestTeamsTab | None:
    """Get Tab

     Returns a resource representation of a backed-up Microsoft Teams channel tab with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        tab_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RestTeamsTab
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        team_id=team_id,
        channel_id=channel_id,
        tab_id=tab_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    tab_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RestTeamsTab]:
    """Get Tab

     Returns a resource representation of a backed-up Microsoft Teams channel tab with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        tab_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RestTeamsTab]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        channel_id=channel_id,
        tab_id=tab_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    tab_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RestTeamsTab | None:
    """Get Tab

     Returns a resource representation of a backed-up Microsoft Teams channel tab with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        tab_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RestTeamsTab
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            team_id=team_id,
            channel_id=channel_id,
            tab_id=tab_id,
            client=client,
        )
    ).parsed
