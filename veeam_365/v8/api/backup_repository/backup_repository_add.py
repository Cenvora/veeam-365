from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_backup_repository import RESTBackupRepository
from ...models.rest_backup_repository_from_client import RESTBackupRepositoryFromClient
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    *,
    body: RESTBackupRepositoryFromClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/BackupRepositories",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTBackupRepository | RESTExceptionInfo:
    if response.status_code == 201:
        response_201 = RESTBackupRepository.from_dict(response.json())

        return response_201

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTBackupRepository | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTBackupRepositoryFromClient,
) -> Response[RESTBackupRepository | RESTExceptionInfo]:
    """Add Backup Repository

     Adds a backup repository to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        body (RESTBackupRepositoryFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupRepository | RESTExceptionInfo]
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
    body: RESTBackupRepositoryFromClient,
) -> RESTBackupRepository | RESTExceptionInfo | None:
    """Add Backup Repository

     Adds a backup repository to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        body (RESTBackupRepositoryFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupRepository | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTBackupRepositoryFromClient,
) -> Response[RESTBackupRepository | RESTExceptionInfo]:
    """Add Backup Repository

     Adds a backup repository to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        body (RESTBackupRepositoryFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupRepository | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RESTBackupRepositoryFromClient,
) -> RESTBackupRepository | RESTExceptionInfo | None:
    """Add Backup Repository

     Adds a backup repository to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        body (RESTBackupRepositoryFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupRepository | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
