from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.teams_post_export_by_id_response_200 import TeamsPostExportByIdResponse200
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    team_id: UUID,
    post_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/teams/{team_id}/posts/{post_id}/export".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            team_id=quote(str(team_id), safe=""),
            post_id=quote(str(post_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | TeamsPostExportByIdResponse200:
    if response.status_code == 200:
        response_200 = TeamsPostExportByIdResponse200.from_dict(response.content)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | TeamsPostExportByIdResponse200]:
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
) -> Response[RESTExceptionInfo | TeamsPostExportByIdResponse200]:
    r"""Export Post

     Exports a backed-up Microsoft Teams post with the specified ID.\n\nWhen you export a post, the
    request command exports the post to an HTML file and places this file in a temporary folder on the
    Veeam Backup for Microsoft 365 server. After that, the HTML file is transferred as
    application/octet-stream media to the client. To download, read or perform other actions with the
    octet-stream, use features of programming languages.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | TeamsPostExportByIdResponse200]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        post_id=post_id,
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
) -> RESTExceptionInfo | TeamsPostExportByIdResponse200 | None:
    r"""Export Post

     Exports a backed-up Microsoft Teams post with the specified ID.\n\nWhen you export a post, the
    request command exports the post to an HTML file and places this file in a temporary folder on the
    Veeam Backup for Microsoft 365 server. After that, the HTML file is transferred as
    application/octet-stream media to the client. To download, read or perform other actions with the
    octet-stream, use features of programming languages.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | TeamsPostExportByIdResponse200
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        team_id=team_id,
        post_id=post_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    post_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | TeamsPostExportByIdResponse200]:
    r"""Export Post

     Exports a backed-up Microsoft Teams post with the specified ID.\n\nWhen you export a post, the
    request command exports the post to an HTML file and places this file in a temporary folder on the
    Veeam Backup for Microsoft 365 server. After that, the HTML file is transferred as
    application/octet-stream media to the client. To download, read or perform other actions with the
    octet-stream, use features of programming languages.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | TeamsPostExportByIdResponse200]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        team_id=team_id,
        post_id=post_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    team_id: UUID,
    post_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | TeamsPostExportByIdResponse200 | None:
    r"""Export Post

     Exports a backed-up Microsoft Teams post with the specified ID.\n\nWhen you export a post, the
    request command exports the post to an HTML file and places this file in a temporary folder on the
    Veeam Backup for Microsoft 365 server. After that, the HTML file is transferred as
    application/octet-stream media to the client. To download, read or perform other actions with the
    octet-stream, use features of programming languages.

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        post_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | TeamsPostExportByIdResponse200
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            team_id=team_id,
            post_id=post_id,
            client=client,
        )
    ).parsed
