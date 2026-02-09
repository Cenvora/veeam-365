from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.one_drive_document_save_documents_action_response_200 import (
    OneDriveDocumentSaveDocumentsActionResponse200,
)
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_save_documents_options import RESTSaveDocumentsOptions
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    body: RESTSaveDocumentsOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/Organization/OneDrives/{one_drive_id}/Documents/save".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            one_drive_id=quote(str(one_drive_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OneDriveDocumentSaveDocumentsActionResponse200 | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = OneDriveDocumentSaveDocumentsActionResponse200.from_dict(response.content)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OneDriveDocumentSaveDocumentsActionResponse200 | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveDocumentsOptions,
) -> Response[OneDriveDocumentSaveDocumentsActionResponse200 | RESTExceptionInfo]:
    """Save OneDrive Documents

     Saves backed-up OneDrive documents.

    OneDrive documents are always saved in a ZIP archive. When you save backed-up OneDrive documents,
    the request command archives the documents and places the ZIP archive a temporary folder on the
    Veeam Backup for Microsoft 365 server. After that, the archive is transferred as application/octet-
    stream media to the client. To download, read or perform other actions with the octet-stream, use
    features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTSaveDocumentsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OneDriveDocumentSaveDocumentsActionResponse200 | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveDocumentsOptions,
) -> OneDriveDocumentSaveDocumentsActionResponse200 | RESTExceptionInfo | None:
    """Save OneDrive Documents

     Saves backed-up OneDrive documents.

    OneDrive documents are always saved in a ZIP archive. When you save backed-up OneDrive documents,
    the request command archives the documents and places the ZIP archive a temporary folder on the
    Veeam Backup for Microsoft 365 server. After that, the archive is transferred as application/octet-
    stream media to the client. To download, read or perform other actions with the octet-stream, use
    features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTSaveDocumentsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OneDriveDocumentSaveDocumentsActionResponse200 | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveDocumentsOptions,
) -> Response[OneDriveDocumentSaveDocumentsActionResponse200 | RESTExceptionInfo]:
    """Save OneDrive Documents

     Saves backed-up OneDrive documents.

    OneDrive documents are always saved in a ZIP archive. When you save backed-up OneDrive documents,
    the request command archives the documents and places the ZIP archive a temporary folder on the
    Veeam Backup for Microsoft 365 server. After that, the archive is transferred as application/octet-
    stream media to the client. To download, read or perform other actions with the octet-stream, use
    features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTSaveDocumentsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OneDriveDocumentSaveDocumentsActionResponse200 | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveDocumentsOptions,
) -> OneDriveDocumentSaveDocumentsActionResponse200 | RESTExceptionInfo | None:
    """Save OneDrive Documents

     Saves backed-up OneDrive documents.

    OneDrive documents are always saved in a ZIP archive. When you save backed-up OneDrive documents,
    the request command archives the documents and places the ZIP archive a temporary folder on the
    Veeam Backup for Microsoft 365 server. After that, the archive is transferred as application/octet-
    stream media to the client. To download, read or perform other actions with the octet-stream, use
    features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTSaveDocumentsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OneDriveDocumentSaveDocumentsActionResponse200 | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            one_drive_id=one_drive_id,
            client=client,
            body=body,
        )
    ).parsed
