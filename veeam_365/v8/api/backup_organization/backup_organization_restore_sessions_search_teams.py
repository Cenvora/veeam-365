from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_team_entity import PageOfRESTTeamEntity
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_teams_search_options import RESTTeamsSearchOptions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_session_id: UUID,
    *,
    body: RESTTeamsSearchOptions,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/searchTeams".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTTeamEntity | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTTeamEntity.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTTeamEntity | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTTeamsSearchOptions,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTTeamEntity | RESTExceptionInfo]:
    """Search for Teams Items in Organization Backups

     Searches for Microsoft Teams items in backups of a Microsoft 365 organization.

    Args:
        restore_session_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        body (RESTTeamsSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTTeamEntity | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        body=body,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTTeamsSearchOptions,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTTeamEntity | RESTExceptionInfo | None:
    """Search for Teams Items in Organization Backups

     Searches for Microsoft Teams items in backups of a Microsoft 365 organization.

    Args:
        restore_session_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        body (RESTTeamsSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTTeamEntity | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        client=client,
        body=body,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTTeamsSearchOptions,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTTeamEntity | RESTExceptionInfo]:
    """Search for Teams Items in Organization Backups

     Searches for Microsoft Teams items in backups of a Microsoft 365 organization.

    Args:
        restore_session_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        body (RESTTeamsSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTTeamEntity | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        body=body,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTTeamsSearchOptions,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTTeamEntity | RESTExceptionInfo | None:
    """Search for Teams Items in Organization Backups

     Searches for Microsoft Teams items in backups of a Microsoft 365 organization.

    Args:
        restore_session_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        body (RESTTeamsSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTTeamEntity | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            client=client,
            body=body,
            limit=limit,
            offset=offset,
        )
    ).parsed
