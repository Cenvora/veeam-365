from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_teams_post import RESTTeamsPost
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_session_id: UUID,
    team_id: UUID,
    post_id: int,
    *,
    channel_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["channelId"] = channel_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/RestoreSessions/{restore_session_id}/organization/teams/{team_id}/posts/{post_id}".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            team_id=quote(str(team_id), safe=""),
            post_id=quote(str(post_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTTeamsPost:
    if response.status_code == 200:
        response_200 = RESTTeamsPost.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTTeamsPost]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    post_id: int,
    *,
    client: AuthenticatedClient | Client,
    channel_id: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | RESTTeamsPost]:
    """
    Args:
        restore_session_id (UUID):
        team_id (UUID):
        post_id (int):
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTTeamsPost]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        post_id=post_id,
        channel_id=channel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    team_id: UUID,
    post_id: int,
    *,
    client: AuthenticatedClient | Client,
    channel_id: str | Unset = UNSET,
) -> RESTExceptionInfo | RESTTeamsPost | None:
    """
    Args:
        restore_session_id (UUID):
        team_id (UUID):
        post_id (int):
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTTeamsPost
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        team_id=team_id,
        post_id=post_id,
        client=client,
        channel_id=channel_id,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    post_id: int,
    *,
    client: AuthenticatedClient | Client,
    channel_id: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | RESTTeamsPost]:
    """
    Args:
        restore_session_id (UUID):
        team_id (UUID):
        post_id (int):
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTTeamsPost]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        post_id=post_id,
        channel_id=channel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    team_id: UUID,
    post_id: int,
    *,
    client: AuthenticatedClient | Client,
    channel_id: str | Unset = UNSET,
) -> RESTExceptionInfo | RESTTeamsPost | None:
    """
    Args:
        restore_session_id (UUID):
        team_id (UUID):
        post_id (int):
        channel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTTeamsPost
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            team_id=team_id,
            post_id=post_id,
            client=client,
            channel_id=channel_id,
        )
    ).parsed
