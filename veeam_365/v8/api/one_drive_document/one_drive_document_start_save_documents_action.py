from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_start_export_to_object_storage_response import RESTStartExportToObjectStorageResponse
from ...models.rest_start_save_one_drive_documents_options import RESTStartSaveOneDriveDocumentsOptions
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    body: RESTStartSaveOneDriveDocumentsOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/Organization/OneDrives/{one_drive_id}/Documents/startSave".format(
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
) -> RESTExceptionInfo | RESTStartExportToObjectStorageResponse:
    if response.status_code == 200:
        response_200 = RESTStartExportToObjectStorageResponse.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTStartExportToObjectStorageResponse]:
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
    body: RESTStartSaveOneDriveDocumentsOptions,
) -> Response[RESTExceptionInfo | RESTStartExportToObjectStorageResponse]:
    """Get Save OneDrive Documents Operation ID

     Creates and starts an asynchronous operation to save backed-up OneDrive documents to Azure Blob
    Storage and returns the operation ID.
    OneDrive documents are always saved in a ZIP archive. When you save backed-up OneDrive documents,
    the request command archives the documents and places the ZIP archive in a temporary folder on the
    Veeam Backup for Microsoft 365 server.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTStartSaveOneDriveDocumentsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTStartExportToObjectStorageResponse]
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
    body: RESTStartSaveOneDriveDocumentsOptions,
) -> RESTExceptionInfo | RESTStartExportToObjectStorageResponse | None:
    """Get Save OneDrive Documents Operation ID

     Creates and starts an asynchronous operation to save backed-up OneDrive documents to Azure Blob
    Storage and returns the operation ID.
    OneDrive documents are always saved in a ZIP archive. When you save backed-up OneDrive documents,
    the request command archives the documents and places the ZIP archive in a temporary folder on the
    Veeam Backup for Microsoft 365 server.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTStartSaveOneDriveDocumentsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTStartExportToObjectStorageResponse
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
    body: RESTStartSaveOneDriveDocumentsOptions,
) -> Response[RESTExceptionInfo | RESTStartExportToObjectStorageResponse]:
    """Get Save OneDrive Documents Operation ID

     Creates and starts an asynchronous operation to save backed-up OneDrive documents to Azure Blob
    Storage and returns the operation ID.
    OneDrive documents are always saved in a ZIP archive. When you save backed-up OneDrive documents,
    the request command archives the documents and places the ZIP archive in a temporary folder on the
    Veeam Backup for Microsoft 365 server.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTStartSaveOneDriveDocumentsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTStartExportToObjectStorageResponse]
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
    body: RESTStartSaveOneDriveDocumentsOptions,
) -> RESTExceptionInfo | RESTStartExportToObjectStorageResponse | None:
    """Get Save OneDrive Documents Operation ID

     Creates and starts an asynchronous operation to save backed-up OneDrive documents to Azure Blob
    Storage and returns the operation ID.
    OneDrive documents are always saved in a ZIP archive. When you save backed-up OneDrive documents,
    the request command archives the documents and places the ZIP archive in a temporary folder on the
    Veeam Backup for Microsoft 365 server.

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTStartSaveOneDriveDocumentsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTStartExportToObjectStorageResponse
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            one_drive_id=one_drive_id,
            client=client,
            body=body,
        )
    ).parsed
