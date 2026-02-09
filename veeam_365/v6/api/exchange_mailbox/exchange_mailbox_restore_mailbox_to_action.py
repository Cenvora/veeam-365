from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_folders_restore_statistics import RESTFoldersRestoreStatistics
from ...models.rest_restore_to_different_location import RESTRestoreToDifferentLocation
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    body: RESTRestoreToDifferentLocation,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v6/RestoreSessions/{restore_session_id}/organization/mailboxes/{mailbox_id}/restoreTo".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            mailbox_id=quote(str(mailbox_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTFoldersRestoreStatistics:
    if response.status_code == 200:
        response_200 = RESTFoldersRestoreStatistics.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTFoldersRestoreStatistics]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToDifferentLocation,
) -> Response[RESTExceptionInfo | RESTFoldersRestoreStatistics]:
    """
    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTRestoreToDifferentLocation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTFoldersRestoreStatistics]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        mailbox_id=mailbox_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToDifferentLocation,
) -> RESTExceptionInfo | RESTFoldersRestoreStatistics | None:
    """
    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTRestoreToDifferentLocation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTFoldersRestoreStatistics
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        mailbox_id=mailbox_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToDifferentLocation,
) -> Response[RESTExceptionInfo | RESTFoldersRestoreStatistics]:
    """
    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTRestoreToDifferentLocation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTFoldersRestoreStatistics]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        mailbox_id=mailbox_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreToDifferentLocation,
) -> RESTExceptionInfo | RESTFoldersRestoreStatistics | None:
    """
    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTRestoreToDifferentLocation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTFoldersRestoreStatistics
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            mailbox_id=mailbox_id,
            client=client,
            body=body,
        )
    ).parsed
