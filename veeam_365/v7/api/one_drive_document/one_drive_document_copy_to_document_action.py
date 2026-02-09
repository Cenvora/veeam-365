from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_copy_to_document import RESTCopyToDocument
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_item_restore_statistics import RESTItemRestoreStatistics
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    one_drive_id: str,
    document_id: UUID,
    *,
    body: RESTCopyToDocument,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v7/RestoreSessions/{restore_session_id}/Organization/OneDrives/{one_drive_id}/Documents/{document_id}/copyTo".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            one_drive_id=quote(str(one_drive_id), safe=""),
            document_id=quote(str(document_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTItemRestoreStatistics:
    if response.status_code == 200:
        response_200 = RESTItemRestoreStatistics.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTItemRestoreStatistics]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    document_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTCopyToDocument,
) -> Response[RESTExceptionInfo | RESTItemRestoreStatistics]:
    """Copy OneDrive Document

     Copies a backed-up OneDrive document with the specified ID to another location in Microsoft
    OneDrive.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        body (RESTCopyToDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTItemRestoreStatistics]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        document_id=document_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    one_drive_id: str,
    document_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTCopyToDocument,
) -> RESTExceptionInfo | RESTItemRestoreStatistics | None:
    """Copy OneDrive Document

     Copies a backed-up OneDrive document with the specified ID to another location in Microsoft
    OneDrive.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        body (RESTCopyToDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTItemRestoreStatistics
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        document_id=document_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    document_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTCopyToDocument,
) -> Response[RESTExceptionInfo | RESTItemRestoreStatistics]:
    """Copy OneDrive Document

     Copies a backed-up OneDrive document with the specified ID to another location in Microsoft
    OneDrive.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        body (RESTCopyToDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTItemRestoreStatistics]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        document_id=document_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    one_drive_id: str,
    document_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTCopyToDocument,
) -> RESTExceptionInfo | RESTItemRestoreStatistics | None:
    """Copy OneDrive Document

     Copies a backed-up OneDrive document with the specified ID to another location in Microsoft
    OneDrive.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        body (RESTCopyToDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTItemRestoreStatistics
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            one_drive_id=one_drive_id,
            document_id=document_id,
            client=client,
            body=body,
        )
    ).parsed
