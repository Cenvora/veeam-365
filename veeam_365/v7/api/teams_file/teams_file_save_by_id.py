from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_file_save_options import RESTFileSaveOptions
from ...models.teams_file_save_by_id_response_200 import TeamsFileSaveByIdResponse200
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    team_id: UUID,
    file_id: UUID,
    *,
    body: RESTFileSaveOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v7/RestoreSessions/{restore_session_id}/organization/teams/{team_id}/files/{file_id}/save".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            team_id=quote(str(team_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | TeamsFileSaveByIdResponse200:
    if response.status_code == 200:
        response_200 = TeamsFileSaveByIdResponse200.from_dict(response.content)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | TeamsFileSaveByIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    file_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTFileSaveOptions,
) -> Response[RESTExceptionInfo | TeamsFileSaveByIdResponse200]:
    """Save File

     Saves a backed-up Microsoft Teams file with the specified ID.

    When you save a file, the request command places the file to a temporary folder on the Veeam Backup
    for Microsoft 365 server. After that, the file is transferred as application/octet-stream media to
    the client. To download, read or perform other actions with the octet-stream, use features of
    programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        file_id (UUID):
        body (RESTFileSaveOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | TeamsFileSaveByIdResponse200]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
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
    file_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTFileSaveOptions,
) -> RESTExceptionInfo | TeamsFileSaveByIdResponse200 | None:
    """Save File

     Saves a backed-up Microsoft Teams file with the specified ID.

    When you save a file, the request command places the file to a temporary folder on the Veeam Backup
    for Microsoft 365 server. After that, the file is transferred as application/octet-stream media to
    the client. To download, read or perform other actions with the octet-stream, use features of
    programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        file_id (UUID):
        body (RESTFileSaveOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | TeamsFileSaveByIdResponse200
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        team_id=team_id,
        file_id=file_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    file_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTFileSaveOptions,
) -> Response[RESTExceptionInfo | TeamsFileSaveByIdResponse200]:
    """Save File

     Saves a backed-up Microsoft Teams file with the specified ID.

    When you save a file, the request command places the file to a temporary folder on the Veeam Backup
    for Microsoft 365 server. After that, the file is transferred as application/octet-stream media to
    the client. To download, read or perform other actions with the octet-stream, use features of
    programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        file_id (UUID):
        body (RESTFileSaveOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | TeamsFileSaveByIdResponse200]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        file_id=file_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    team_id: UUID,
    file_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTFileSaveOptions,
) -> RESTExceptionInfo | TeamsFileSaveByIdResponse200 | None:
    """Save File

     Saves a backed-up Microsoft Teams file with the specified ID.

    When you save a file, the request command places the file to a temporary folder on the Veeam Backup
    for Microsoft 365 server. After that, the file is transferred as application/octet-stream media to
    the client. To download, read or perform other actions with the octet-stream, use features of
    programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        file_id (UUID):
        body (RESTFileSaveOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | TeamsFileSaveByIdResponse200
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            team_id=team_id,
            file_id=file_id,
            client=client,
            body=body,
        )
    ).parsed
