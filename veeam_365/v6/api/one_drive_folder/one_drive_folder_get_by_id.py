from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_one_drive_folder import RESTOneDriveFolder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_session_id: UUID,
    one_drive_id: str,
    folder_id: UUID,
    *,
    version_id: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["versionId"] = version_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/RestoreSessions/{restore_session_id}/Organization/OneDrives/{one_drive_id}/Folders/{folder_id}".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            one_drive_id=quote(str(one_drive_id), safe=""),
            folder_id=quote(str(folder_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTOneDriveFolder:
    if response.status_code == 200:
        response_200 = RESTOneDriveFolder.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTOneDriveFolder]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    folder_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    version_id: int | Unset = UNSET,
) -> Response[RESTExceptionInfo | RESTOneDriveFolder]:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        folder_id (UUID):
        version_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTOneDriveFolder]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        folder_id=folder_id,
        version_id=version_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    one_drive_id: str,
    folder_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    version_id: int | Unset = UNSET,
) -> RESTExceptionInfo | RESTOneDriveFolder | None:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        folder_id (UUID):
        version_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTOneDriveFolder
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        folder_id=folder_id,
        client=client,
        version_id=version_id,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    folder_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    version_id: int | Unset = UNSET,
) -> Response[RESTExceptionInfo | RESTOneDriveFolder]:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        folder_id (UUID):
        version_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTOneDriveFolder]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        folder_id=folder_id,
        version_id=version_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    one_drive_id: str,
    folder_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    version_id: int | Unset = UNSET,
) -> RESTExceptionInfo | RESTOneDriveFolder | None:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        folder_id (UUID):
        version_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTOneDriveFolder
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            one_drive_id=one_drive_id,
            folder_id=folder_id,
            client=client,
            version_id=version_id,
        )
    ).parsed
