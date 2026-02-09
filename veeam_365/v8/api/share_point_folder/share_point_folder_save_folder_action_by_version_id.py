from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.share_point_folder_save_folder_action_by_version_id_response_200 import (
    SharePointFolderSaveFolderActionByVersionIdResponse200,
)
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    version_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Folders/{folder_id}/Versions/{version_id}/save".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            folder_id=quote(str(folder_id), safe=""),
            version_id=quote(str(version_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | SharePointFolderSaveFolderActionByVersionIdResponse200:
    if response.status_code == 200:
        response_200 = SharePointFolderSaveFolderActionByVersionIdResponse200.from_dict(response.content)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | SharePointFolderSaveFolderActionByVersionIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | SharePointFolderSaveFolderActionByVersionIdResponse200]:
    """Save Version of SharePoint Folder

     Saves a specific version of a backed-up SharePoint library folder with the specified ID.

    SharePoint library folders are always saved in a ZIP archive. When you save a backed-up SharePoint
    library folder, the request command archives the library folder and places the ZIP archive in a
    temporary folder on the Veeam Backup for Microsoft 365 server. After that, the archive is
    transferred as application/octet-stream media to the client. To download, read or perform other
    actions with the octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        version_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | SharePointFolderSaveFolderActionByVersionIdResponse200]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        folder_id=folder_id,
        version_id=version_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | SharePointFolderSaveFolderActionByVersionIdResponse200 | None:
    """Save Version of SharePoint Folder

     Saves a specific version of a backed-up SharePoint library folder with the specified ID.

    SharePoint library folders are always saved in a ZIP archive. When you save a backed-up SharePoint
    library folder, the request command archives the library folder and places the ZIP archive in a
    temporary folder on the Veeam Backup for Microsoft 365 server. After that, the archive is
    transferred as application/octet-stream media to the client. To download, read or perform other
    actions with the octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        version_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | SharePointFolderSaveFolderActionByVersionIdResponse200
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        site_id=site_id,
        folder_id=folder_id,
        version_id=version_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | SharePointFolderSaveFolderActionByVersionIdResponse200]:
    """Save Version of SharePoint Folder

     Saves a specific version of a backed-up SharePoint library folder with the specified ID.

    SharePoint library folders are always saved in a ZIP archive. When you save a backed-up SharePoint
    library folder, the request command archives the library folder and places the ZIP archive in a
    temporary folder on the Veeam Backup for Microsoft 365 server. After that, the archive is
    transferred as application/octet-stream media to the client. To download, read or perform other
    actions with the octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        version_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | SharePointFolderSaveFolderActionByVersionIdResponse200]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        folder_id=folder_id,
        version_id=version_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | SharePointFolderSaveFolderActionByVersionIdResponse200 | None:
    """Save Version of SharePoint Folder

     Saves a specific version of a backed-up SharePoint library folder with the specified ID.

    SharePoint library folders are always saved in a ZIP archive. When you save a backed-up SharePoint
    library folder, the request command archives the library folder and places the ZIP archive in a
    temporary folder on the Veeam Backup for Microsoft 365 server. After that, the archive is
    transferred as application/octet-stream media to the client. To download, read or perform other
    actions with the octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        version_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | SharePointFolderSaveFolderActionByVersionIdResponse200
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            site_id=site_id,
            folder_id=folder_id,
            version_id=version_id,
            client=client,
        )
    ).parsed
