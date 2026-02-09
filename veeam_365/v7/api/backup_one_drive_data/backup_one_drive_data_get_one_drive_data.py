from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_backup_one_drive_data import RESTBackupOneDriveData
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    repository_id: UUID,
    one_drive_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/BackupRepositories/{repository_id}/OneDriveData/{one_drive_id}".format(
            repository_id=quote(str(repository_id), safe=""),
            one_drive_id=quote(str(one_drive_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTBackupOneDriveData | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTBackupOneDriveData.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTBackupOneDriveData | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTBackupOneDriveData | RESTExceptionInfo]:
    """Get OneDrive Data by Repository and OneDrive ID

     Returns a backed-up OneDrive with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        one_drive_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupOneDriveData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        one_drive_id=one_drive_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTBackupOneDriveData | RESTExceptionInfo | None:
    """Get OneDrive Data by Repository and OneDrive ID

     Returns a backed-up OneDrive with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        one_drive_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupOneDriveData | RESTExceptionInfo
    """

    return sync_detailed(
        repository_id=repository_id,
        one_drive_id=one_drive_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    repository_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTBackupOneDriveData | RESTExceptionInfo]:
    """Get OneDrive Data by Repository and OneDrive ID

     Returns a backed-up OneDrive with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        one_drive_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupOneDriveData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        one_drive_id=one_drive_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTBackupOneDriveData | RESTExceptionInfo | None:
    """Get OneDrive Data by Repository and OneDrive ID

     Returns a backed-up OneDrive with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        one_drive_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupOneDriveData | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            one_drive_id=one_drive_id,
            client=client,
        )
    ).parsed
