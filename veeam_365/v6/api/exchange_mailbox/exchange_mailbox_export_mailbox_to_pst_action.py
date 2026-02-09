from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.exchange_mailbox_export_mailbox_to_pst_action_response_200 import (
    ExchangeMailboxExportMailboxToPstActionResponse200,
)
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_export_folder_to_pst import RESTExportFolderToPst
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    body: RESTExportFolderToPst,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v6/RestoreSessions/{restore_session_id}/organization/mailboxes/{mailbox_id}/exportToPst".format(
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
) -> ExchangeMailboxExportMailboxToPstActionResponse200 | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = ExchangeMailboxExportMailboxToPstActionResponse200.from_dict(response.content)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExchangeMailboxExportMailboxToPstActionResponse200 | RESTExceptionInfo]:
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
    body: RESTExportFolderToPst,
) -> Response[ExchangeMailboxExportMailboxToPstActionResponse200 | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTExportFolderToPst):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeMailboxExportMailboxToPstActionResponse200 | RESTExceptionInfo]
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
    body: RESTExportFolderToPst,
) -> ExchangeMailboxExportMailboxToPstActionResponse200 | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTExportFolderToPst):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeMailboxExportMailboxToPstActionResponse200 | RESTExceptionInfo
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
    body: RESTExportFolderToPst,
) -> Response[ExchangeMailboxExportMailboxToPstActionResponse200 | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTExportFolderToPst):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeMailboxExportMailboxToPstActionResponse200 | RESTExceptionInfo]
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
    body: RESTExportFolderToPst,
) -> ExchangeMailboxExportMailboxToPstActionResponse200 | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTExportFolderToPst):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeMailboxExportMailboxToPstActionResponse200 | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            mailbox_id=mailbox_id,
            client=client,
            body=body,
        )
    ).parsed
