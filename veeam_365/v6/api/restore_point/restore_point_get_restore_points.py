import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_restore_point import RESTRestorePoint
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_id: UUID | Unset = UNSET,
    job_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    backup_time: datetime.datetime | Unset = UNSET,
    is_long_term_copy: bool | Unset = UNSET,
    is_retrieved: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organizationId"] = json_organization_id

    json_job_id: str | Unset = UNSET
    if not isinstance(job_id, Unset):
        json_job_id = str(job_id)
    params["jobId"] = json_job_id

    json_repository_id: str | Unset = UNSET
    if not isinstance(repository_id, Unset):
        json_repository_id = str(repository_id)
    params["repositoryId"] = json_repository_id

    json_backup_time: str | Unset = UNSET
    if not isinstance(backup_time, Unset):
        json_backup_time = backup_time.isoformat()
    params["backupTime"] = json_backup_time

    params["isLongTermCopy"] = is_long_term_copy

    params["isRetrieved"] = is_retrieved

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/RestorePoints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTRestorePoint]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTRestorePoint.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTRestorePoint]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    job_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    backup_time: datetime.datetime | Unset = UNSET,
    is_long_term_copy: bool | Unset = UNSET,
    is_retrieved: bool | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTRestorePoint]]:
    """
    Args:
        organization_id (UUID | Unset):
        job_id (UUID | Unset):
        repository_id (UUID | Unset):
        backup_time (datetime.datetime | Unset):
        is_long_term_copy (bool | Unset):
        is_retrieved (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTRestorePoint]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        job_id=job_id,
        repository_id=repository_id,
        backup_time=backup_time,
        is_long_term_copy=is_long_term_copy,
        is_retrieved=is_retrieved,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    job_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    backup_time: datetime.datetime | Unset = UNSET,
    is_long_term_copy: bool | Unset = UNSET,
    is_retrieved: bool | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTRestorePoint] | None:
    """
    Args:
        organization_id (UUID | Unset):
        job_id (UUID | Unset):
        repository_id (UUID | Unset):
        backup_time (datetime.datetime | Unset):
        is_long_term_copy (bool | Unset):
        is_retrieved (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTRestorePoint]
    """

    return sync_detailed(
        client=client,
        organization_id=organization_id,
        job_id=job_id,
        repository_id=repository_id,
        backup_time=backup_time,
        is_long_term_copy=is_long_term_copy,
        is_retrieved=is_retrieved,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    job_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    backup_time: datetime.datetime | Unset = UNSET,
    is_long_term_copy: bool | Unset = UNSET,
    is_retrieved: bool | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTRestorePoint]]:
    """
    Args:
        organization_id (UUID | Unset):
        job_id (UUID | Unset):
        repository_id (UUID | Unset):
        backup_time (datetime.datetime | Unset):
        is_long_term_copy (bool | Unset):
        is_retrieved (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTRestorePoint]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        job_id=job_id,
        repository_id=repository_id,
        backup_time=backup_time,
        is_long_term_copy=is_long_term_copy,
        is_retrieved=is_retrieved,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    job_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    backup_time: datetime.datetime | Unset = UNSET,
    is_long_term_copy: bool | Unset = UNSET,
    is_retrieved: bool | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTRestorePoint] | None:
    """
    Args:
        organization_id (UUID | Unset):
        job_id (UUID | Unset):
        repository_id (UUID | Unset):
        backup_time (datetime.datetime | Unset):
        is_long_term_copy (bool | Unset):
        is_retrieved (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTRestorePoint]
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_id=organization_id,
            job_id=job_id,
            repository_id=repository_id,
            backup_time=backup_time,
            is_long_term_copy=is_long_term_copy,
            is_retrieved=is_retrieved,
        )
    ).parsed
