from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_one_drive_document import PageOfRESTOneDriveDocument
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_session_id: UUID,
    one_drive_id: str,
    document_id: UUID,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/RestoreSessions/{restore_session_id}/Organization/OneDrives/{one_drive_id}/Documents/{document_id}/Versions".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            one_drive_id=quote(str(one_drive_id), safe=""),
            document_id=quote(str(document_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTOneDriveDocument | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTOneDriveDocument.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTOneDriveDocument | RESTExceptionInfo]:
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
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfRESTOneDriveDocument | RESTExceptionInfo]:
    """Get All Versions of OneDrive Document

     Returns a collection of versions of a backed-up OneDrive document with the specified ID.

    When you get OneDrive document versions, the server returns information about previous versions of
    the document. To get the latest version, use either [Get OneDrive
    Document](#tag/OneDriveDocument/operation/OneDriveDocument_GetById) or [Get Specific Version of
    OneDrive Document](#tag/OneDriveDocument/operation/OneDriveDocument_GetByIdByVersionId).

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTOneDriveDocument | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        document_id=document_id,
        offset=offset,
        limit=limit,
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
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfRESTOneDriveDocument | RESTExceptionInfo | None:
    """Get All Versions of OneDrive Document

     Returns a collection of versions of a backed-up OneDrive document with the specified ID.

    When you get OneDrive document versions, the server returns information about previous versions of
    the document. To get the latest version, use either [Get OneDrive
    Document](#tag/OneDriveDocument/operation/OneDriveDocument_GetById) or [Get Specific Version of
    OneDrive Document](#tag/OneDriveDocument/operation/OneDriveDocument_GetByIdByVersionId).

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTOneDriveDocument | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        document_id=document_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    document_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfRESTOneDriveDocument | RESTExceptionInfo]:
    """Get All Versions of OneDrive Document

     Returns a collection of versions of a backed-up OneDrive document with the specified ID.

    When you get OneDrive document versions, the server returns information about previous versions of
    the document. To get the latest version, use either [Get OneDrive
    Document](#tag/OneDriveDocument/operation/OneDriveDocument_GetById) or [Get Specific Version of
    OneDrive Document](#tag/OneDriveDocument/operation/OneDriveDocument_GetByIdByVersionId).

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTOneDriveDocument | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        document_id=document_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    one_drive_id: str,
    document_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfRESTOneDriveDocument | RESTExceptionInfo | None:
    """Get All Versions of OneDrive Document

     Returns a collection of versions of a backed-up OneDrive document with the specified ID.

    When you get OneDrive document versions, the server returns information about previous versions of
    the document. To get the latest version, use either [Get OneDrive
    Document](#tag/OneDriveDocument/operation/OneDriveDocument_GetById) or [Get Specific Version of
    OneDrive Document](#tag/OneDriveDocument/operation/OneDriveDocument_GetByIdByVersionId).

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        document_id (UUID):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTOneDriveDocument | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            one_drive_id=one_drive_id,
            document_id=document_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
