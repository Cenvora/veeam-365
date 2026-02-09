from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_backup_mailbox_data import RESTBackupMailboxData
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    repository_id: UUID,
    mailbox_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/BackupRepositories/{repository_id}/MailboxData/{mailbox_id}".format(
            repository_id=quote(str(repository_id), safe=""),
            mailbox_id=quote(str(mailbox_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTBackupMailboxData | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTBackupMailboxData.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTBackupMailboxData | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTBackupMailboxData | RESTExceptionInfo]:
    """Get Mailbox Data by Repository and Mailbox ID

     Returns a backed-up mailbox with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        mailbox_id (UUID):  Example: 00000000-0000-0000-0000-000000000000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupMailboxData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        mailbox_id=mailbox_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTBackupMailboxData | RESTExceptionInfo | None:
    """Get Mailbox Data by Repository and Mailbox ID

     Returns a backed-up mailbox with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        mailbox_id (UUID):  Example: 00000000-0000-0000-0000-000000000000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupMailboxData | RESTExceptionInfo
    """

    return sync_detailed(
        repository_id=repository_id,
        mailbox_id=mailbox_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    repository_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTBackupMailboxData | RESTExceptionInfo]:
    """Get Mailbox Data by Repository and Mailbox ID

     Returns a backed-up mailbox with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        mailbox_id (UUID):  Example: 00000000-0000-0000-0000-000000000000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupMailboxData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        mailbox_id=mailbox_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTBackupMailboxData | RESTExceptionInfo | None:
    """Get Mailbox Data by Repository and Mailbox ID

     Returns a backed-up mailbox with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        mailbox_id (UUID):  Example: 00000000-0000-0000-0000-000000000000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupMailboxData | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            mailbox_id=mailbox_id,
            client=client,
        )
    ).parsed
