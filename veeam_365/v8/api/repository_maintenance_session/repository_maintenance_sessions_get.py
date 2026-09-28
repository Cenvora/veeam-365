from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_backup_repository_maintenance_session import PageOfRESTBackupRepositoryMaintenanceSession
from ...models.rest_backup_repository_maintenance_session_status import RESTBackupRepositoryMaintenanceSessionStatus
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: RESTBackupRepositoryMaintenanceSessionStatus | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_repository_id: str | Unset = UNSET
    if not isinstance(repository_id, Unset):
        json_repository_id = str(repository_id)
    params["repositoryId"] = json_repository_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/backupRepositories/maintenanceSessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTBackupRepositoryMaintenanceSession | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTBackupRepositoryMaintenanceSession.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTBackupRepositoryMaintenanceSession | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: RESTBackupRepositoryMaintenanceSessionStatus | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTBackupRepositoryMaintenanceSession | RESTExceptionInfo]:
    """Get Maintenance Sessions

     Returns a collection of maintenance sessions.

    Args:
        status (RESTBackupRepositoryMaintenanceSessionStatus | Unset): Status of the maintenance
            session.
        repository_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupRepositoryMaintenanceSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        status=status,
        repository_id=repository_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: RESTBackupRepositoryMaintenanceSessionStatus | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTBackupRepositoryMaintenanceSession | RESTExceptionInfo | None:
    """Get Maintenance Sessions

     Returns a collection of maintenance sessions.

    Args:
        status (RESTBackupRepositoryMaintenanceSessionStatus | Unset): Status of the maintenance
            session.
        repository_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupRepositoryMaintenanceSession | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        status=status,
        repository_id=repository_id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: RESTBackupRepositoryMaintenanceSessionStatus | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTBackupRepositoryMaintenanceSession | RESTExceptionInfo]:
    """Get Maintenance Sessions

     Returns a collection of maintenance sessions.

    Args:
        status (RESTBackupRepositoryMaintenanceSessionStatus | Unset): Status of the maintenance
            session.
        repository_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupRepositoryMaintenanceSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        status=status,
        repository_id=repository_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: RESTBackupRepositoryMaintenanceSessionStatus | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTBackupRepositoryMaintenanceSession | RESTExceptionInfo | None:
    """Get Maintenance Sessions

     Returns a collection of maintenance sessions.

    Args:
        status (RESTBackupRepositoryMaintenanceSessionStatus | Unset): Status of the maintenance
            session.
        repository_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupRepositoryMaintenanceSession | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            repository_id=repository_id,
            limit=limit,
            offset=offset,
        )
    ).parsed
