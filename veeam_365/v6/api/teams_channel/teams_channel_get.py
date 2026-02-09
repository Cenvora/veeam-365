from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_teams_channel import PageOfRESTTeamsChannel
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_session_id: UUID,
    team_id: UUID,
    *,
    display_name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["displayName"] = display_name

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/RestoreSessions/{restore_session_id}/organization/teams/{team_id}/channels".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            team_id=quote(str(team_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTTeamsChannel | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTTeamsChannel.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTTeamsChannel | RESTExceptionInfo]:
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
    display_name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfRESTTeamsChannel | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        team_id (UUID):
        display_name (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTTeamsChannel | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        display_name=display_name,
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
    display_name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfRESTTeamsChannel | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        team_id (UUID):
        display_name (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTTeamsChannel | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        team_id=team_id,
        client=client,
        display_name=display_name,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    display_name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfRESTTeamsChannel | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        team_id (UUID):
        display_name (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTTeamsChannel | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        display_name=display_name,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    team_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    display_name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfRESTTeamsChannel | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        team_id (UUID):
        display_name (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTTeamsChannel | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            team_id=team_id,
            client=client,
            display_name=display_name,
            offset=offset,
            limit=limit,
        )
    ).parsed
