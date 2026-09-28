from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_async_restore_response import RESTAsyncRestoreResponse
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_restore_file_options import RESTRestoreFileOptions
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    file_id: UUID,
    *,
    body: RESTRestoreFileOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/teams/{team_id}/channels/{channel_id}/files/{file_id}/restore".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            team_id=quote(str(team_id), safe=""),
            channel_id=quote(str(channel_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTAsyncRestoreResponse | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTAsyncRestoreResponse.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTAsyncRestoreResponse | RESTExceptionInfo]:
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
    file_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreFileOptions,
) -> Response[RESTAsyncRestoreResponse | RESTExceptionInfo]:
    """Restore File

     Restores a backed-up Microsoft Teams file with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        file_id (UUID):
        body (RESTRestoreFileOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAsyncRestoreResponse | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        channel_id=channel_id,
        file_id=file_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreFileOptions,
) -> RESTAsyncRestoreResponse | RESTExceptionInfo | None:
    """Restore File

     Restores a backed-up Microsoft Teams file with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        file_id (UUID):
        body (RESTRestoreFileOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAsyncRestoreResponse | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        team_id=team_id,
        channel_id=channel_id,
        file_id=file_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreFileOptions,
) -> Response[RESTAsyncRestoreResponse | RESTExceptionInfo]:
    """Restore File

     Restores a backed-up Microsoft Teams file with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        file_id (UUID):
        body (RESTRestoreFileOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAsyncRestoreResponse | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        channel_id=channel_id,
        file_id=file_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreFileOptions,
) -> RESTAsyncRestoreResponse | RESTExceptionInfo | None:
    """Restore File

     Restores a backed-up Microsoft Teams file with the specified ID.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        file_id (UUID):
        body (RESTRestoreFileOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAsyncRestoreResponse | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            team_id=team_id,
            channel_id=channel_id,
            file_id=file_id,
            client=client,
            body=body,
        )
    ).parsed
