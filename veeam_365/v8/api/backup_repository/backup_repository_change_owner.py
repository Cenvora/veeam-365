from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_backup_repository_owner_change_session import RESTBackupRepositoryOwnerChangeSession
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repository_id: UUID,
    *,
    proxy_id: UUID | Unset = UNSET,
    pool_id: UUID | Unset = UNSET,
    include_all_related_repositories: bool | Unset = False,
    wait_for_sessions_timeout: int | Unset = 60,
    force_stop_sessions: bool | Unset = False,
    force_stop_sessions_timeout: int | Unset = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_proxy_id: str | Unset = UNSET
    if not isinstance(proxy_id, Unset):
        json_proxy_id = str(proxy_id)
    params["proxyId"] = json_proxy_id

    json_pool_id: str | Unset = UNSET
    if not isinstance(pool_id, Unset):
        json_pool_id = str(pool_id)
    params["poolId"] = json_pool_id

    params["includeAllRelatedRepositories"] = include_all_related_repositories

    params["waitForSessionsTimeout"] = wait_for_sessions_timeout

    params["forceStopSessions"] = force_stop_sessions

    params["forceStopSessionsTimeout"] = force_stop_sessions_timeout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/BackupRepositories/{repository_id}/changeOwner".format(
            repository_id=quote(str(repository_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTBackupRepositoryOwnerChangeSession.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    proxy_id: UUID | Unset = UNSET,
    pool_id: UUID | Unset = UNSET,
    include_all_related_repositories: bool | Unset = False,
    wait_for_sessions_timeout: int | Unset = 60,
    force_stop_sessions: bool | Unset = False,
    force_stop_sessions_timeout: int | Unset = 10,
) -> Response[RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]:
    """Change Owner for Backup Repository by Repository ID

     Creates and starts a change owner session to change an owner for a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        proxy_id (UUID | Unset):
        pool_id (UUID | Unset):
        include_all_related_repositories (bool | Unset):  Default: False.
        wait_for_sessions_timeout (int | Unset):  Default: 60.
        force_stop_sessions (bool | Unset):  Default: False.
        force_stop_sessions_timeout (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        proxy_id=proxy_id,
        pool_id=pool_id,
        include_all_related_repositories=include_all_related_repositories,
        wait_for_sessions_timeout=wait_for_sessions_timeout,
        force_stop_sessions=force_stop_sessions,
        force_stop_sessions_timeout=force_stop_sessions_timeout,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    proxy_id: UUID | Unset = UNSET,
    pool_id: UUID | Unset = UNSET,
    include_all_related_repositories: bool | Unset = False,
    wait_for_sessions_timeout: int | Unset = 60,
    force_stop_sessions: bool | Unset = False,
    force_stop_sessions_timeout: int | Unset = 10,
) -> RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo | None:
    """Change Owner for Backup Repository by Repository ID

     Creates and starts a change owner session to change an owner for a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        proxy_id (UUID | Unset):
        pool_id (UUID | Unset):
        include_all_related_repositories (bool | Unset):  Default: False.
        wait_for_sessions_timeout (int | Unset):  Default: 60.
        force_stop_sessions (bool | Unset):  Default: False.
        force_stop_sessions_timeout (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo
    """

    return sync_detailed(
        repository_id=repository_id,
        client=client,
        proxy_id=proxy_id,
        pool_id=pool_id,
        include_all_related_repositories=include_all_related_repositories,
        wait_for_sessions_timeout=wait_for_sessions_timeout,
        force_stop_sessions=force_stop_sessions,
        force_stop_sessions_timeout=force_stop_sessions_timeout,
    ).parsed


async def asyncio_detailed(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    proxy_id: UUID | Unset = UNSET,
    pool_id: UUID | Unset = UNSET,
    include_all_related_repositories: bool | Unset = False,
    wait_for_sessions_timeout: int | Unset = 60,
    force_stop_sessions: bool | Unset = False,
    force_stop_sessions_timeout: int | Unset = 10,
) -> Response[RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]:
    """Change Owner for Backup Repository by Repository ID

     Creates and starts a change owner session to change an owner for a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        proxy_id (UUID | Unset):
        pool_id (UUID | Unset):
        include_all_related_repositories (bool | Unset):  Default: False.
        wait_for_sessions_timeout (int | Unset):  Default: 60.
        force_stop_sessions (bool | Unset):  Default: False.
        force_stop_sessions_timeout (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        proxy_id=proxy_id,
        pool_id=pool_id,
        include_all_related_repositories=include_all_related_repositories,
        wait_for_sessions_timeout=wait_for_sessions_timeout,
        force_stop_sessions=force_stop_sessions,
        force_stop_sessions_timeout=force_stop_sessions_timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    proxy_id: UUID | Unset = UNSET,
    pool_id: UUID | Unset = UNSET,
    include_all_related_repositories: bool | Unset = False,
    wait_for_sessions_timeout: int | Unset = 60,
    force_stop_sessions: bool | Unset = False,
    force_stop_sessions_timeout: int | Unset = 10,
) -> RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo | None:
    """Change Owner for Backup Repository by Repository ID

     Creates and starts a change owner session to change an owner for a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        proxy_id (UUID | Unset):
        pool_id (UUID | Unset):
        include_all_related_repositories (bool | Unset):  Default: False.
        wait_for_sessions_timeout (int | Unset):  Default: 60.
        force_stop_sessions (bool | Unset):  Default: False.
        force_stop_sessions_timeout (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupRepositoryOwnerChangeSession | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            client=client,
            proxy_id=proxy_id,
            pool_id=pool_id,
            include_all_related_repositories=include_all_related_repositories,
            wait_for_sessions_timeout=wait_for_sessions_timeout,
            force_stop_sessions=force_stop_sessions,
            force_stop_sessions_timeout=force_stop_sessions_timeout,
        )
    ).parsed
