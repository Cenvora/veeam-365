from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.one_drive_document_save_document_action_by_version_id_response_200 import (
    OneDriveDocumentSaveDocumentActionByVersionIdResponse200,
)
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_save_one_drive_document_options import RESTSaveOneDriveDocumentOptions
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    one_drive_id: str,
    document_id: UUID,
    version_id: int,
    *,
    body: RESTSaveOneDriveDocumentOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v6/RestoreSessions/{restore_session_id}/Organization/OneDrives/{one_drive_id}/Documents/{document_id}/Versions/{version_id}/save".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            one_drive_id=quote(str(one_drive_id), safe=""),
            document_id=quote(str(document_id), safe=""),
            version_id=quote(str(version_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OneDriveDocumentSaveDocumentActionByVersionIdResponse200 | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = OneDriveDocumentSaveDocumentActionByVersionIdResponse200.from_dict(response.content)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OneDriveDocumentSaveDocumentActionByVersionIdResponse200 | RESTExceptionInfo]:
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
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveOneDriveDocumentOptions,
) -> Response[OneDriveDocumentSaveDocumentActionByVersionIdResponse200 | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        version_id (int):
        body (RESTSaveOneDriveDocumentOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OneDriveDocumentSaveDocumentActionByVersionIdResponse200 | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        document_id=document_id,
        version_id=version_id,
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
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveOneDriveDocumentOptions,
) -> OneDriveDocumentSaveDocumentActionByVersionIdResponse200 | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        version_id (int):
        body (RESTSaveOneDriveDocumentOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OneDriveDocumentSaveDocumentActionByVersionIdResponse200 | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        document_id=document_id,
        version_id=version_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    document_id: UUID,
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveOneDriveDocumentOptions,
) -> Response[OneDriveDocumentSaveDocumentActionByVersionIdResponse200 | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        version_id (int):
        body (RESTSaveOneDriveDocumentOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OneDriveDocumentSaveDocumentActionByVersionIdResponse200 | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        document_id=document_id,
        version_id=version_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    one_drive_id: str,
    document_id: UUID,
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveOneDriveDocumentOptions,
) -> OneDriveDocumentSaveDocumentActionByVersionIdResponse200 | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        version_id (int):
        body (RESTSaveOneDriveDocumentOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OneDriveDocumentSaveDocumentActionByVersionIdResponse200 | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            one_drive_id=one_drive_id,
            document_id=document_id,
            version_id=version_id,
            client=client,
            body=body,
        )
    ).parsed
