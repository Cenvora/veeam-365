from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_backup_repository_maintenance_session import RESTBackupRepositoryMaintenanceSession
from ...models.rest_backup_repository_maintenance_session_start_request import (
    RESTBackupRepositoryMaintenanceSessionStartRequest,
)
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    *,
    body: RESTBackupRepositoryMaintenanceSessionStartRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/backupRepositories/maintenanceSessions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTBackupRepositoryMaintenanceSession | RESTExceptionInfo:
    if response.status_code == 201:
        response_201 = RESTBackupRepositoryMaintenanceSession.from_dict(response.json())

        return response_201

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTBackupRepositoryMaintenanceSession | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTBackupRepositoryMaintenanceSessionStartRequest,
) -> Response[RESTBackupRepositoryMaintenanceSession | RESTExceptionInfo]:
    """Create Maintenance Session

     Creates and starts a maintenance session during which Veeam Backup for Microsoft 365 suspends
    operations on the specified backup repositories.

    Args:
        body (RESTBackupRepositoryMaintenanceSessionStartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupRepositoryMaintenanceSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RESTBackupRepositoryMaintenanceSessionStartRequest,
) -> RESTBackupRepositoryMaintenanceSession | RESTExceptionInfo | None:
    """Create Maintenance Session

     Creates and starts a maintenance session during which Veeam Backup for Microsoft 365 suspends
    operations on the specified backup repositories.

    Args:
        body (RESTBackupRepositoryMaintenanceSessionStartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupRepositoryMaintenanceSession | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTBackupRepositoryMaintenanceSessionStartRequest,
) -> Response[RESTBackupRepositoryMaintenanceSession | RESTExceptionInfo]:
    """Create Maintenance Session

     Creates and starts a maintenance session during which Veeam Backup for Microsoft 365 suspends
    operations on the specified backup repositories.

    Args:
        body (RESTBackupRepositoryMaintenanceSessionStartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupRepositoryMaintenanceSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RESTBackupRepositoryMaintenanceSessionStartRequest,
) -> RESTBackupRepositoryMaintenanceSession | RESTExceptionInfo | None:
    """Create Maintenance Session

     Creates and starts a maintenance session during which Veeam Backup for Microsoft 365 suspends
    operations on the specified backup repositories.

    Args:
        body (RESTBackupRepositoryMaintenanceSessionStartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupRepositoryMaintenanceSession | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
