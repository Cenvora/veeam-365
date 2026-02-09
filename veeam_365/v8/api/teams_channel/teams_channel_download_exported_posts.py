from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.teams_channel_download_exported_posts_response_200 import TeamsChannelDownloadExportedPostsResponse200
from ...types import UNSET, Response


def _get_kwargs(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    request_export_id: UUID,
    *,
    auth_code: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["authCode"] = auth_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/teams/{team_id}/channels/{channel_id}/operatorExport/{request_export_id}".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            team_id=quote(str(team_id), safe=""),
            channel_id=quote(str(channel_id), safe=""),
            request_export_id=quote(str(request_export_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | TeamsChannelDownloadExportedPostsResponse200:
    if response.status_code == 200:
        response_200 = TeamsChannelDownloadExportedPostsResponse200.from_dict(response.content)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | TeamsChannelDownloadExportedPostsResponse200]:
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
    request_export_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    auth_code: str,
) -> Response[RESTExceptionInfo | TeamsChannelDownloadExportedPostsResponse200]:
    """Get Exported Posts by Restore Operator

     Returns a file in the HTML format which contains exported posts of a backed-up channel with the
    specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        request_export_id (UUID):
        auth_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | TeamsChannelDownloadExportedPostsResponse200]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        channel_id=channel_id,
        request_export_id=request_export_id,
        auth_code=auth_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    request_export_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    auth_code: str,
) -> RESTExceptionInfo | TeamsChannelDownloadExportedPostsResponse200 | None:
    """Get Exported Posts by Restore Operator

     Returns a file in the HTML format which contains exported posts of a backed-up channel with the
    specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        request_export_id (UUID):
        auth_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | TeamsChannelDownloadExportedPostsResponse200
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        team_id=team_id,
        channel_id=channel_id,
        request_export_id=request_export_id,
        client=client,
        auth_code=auth_code,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    request_export_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    auth_code: str,
) -> Response[RESTExceptionInfo | TeamsChannelDownloadExportedPostsResponse200]:
    """Get Exported Posts by Restore Operator

     Returns a file in the HTML format which contains exported posts of a backed-up channel with the
    specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        request_export_id (UUID):
        auth_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | TeamsChannelDownloadExportedPostsResponse200]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        channel_id=channel_id,
        request_export_id=request_export_id,
        auth_code=auth_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    request_export_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    auth_code: str,
) -> RESTExceptionInfo | TeamsChannelDownloadExportedPostsResponse200 | None:
    """Get Exported Posts by Restore Operator

     Returns a file in the HTML format which contains exported posts of a backed-up channel with the
    specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        request_export_id (UUID):
        auth_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | TeamsChannelDownloadExportedPostsResponse200
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            team_id=team_id,
            channel_id=channel_id,
            request_export_id=request_export_id,
            client=client,
            auth_code=auth_code,
        )
    ).parsed
