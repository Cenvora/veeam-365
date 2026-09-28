from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_explore_options import RESTExploreOptions
from ...models.rest_restore_session import RESTRestoreSession
from ...types import Response


def _get_kwargs(
    job_id: UUID,
    *,
    body: RESTExploreOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/Jobs/{job_id}/explore".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTRestoreSession:
    if response.status_code == 201:
        response_201 = RESTRestoreSession.from_dict(response.json())

        return response_201

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExploreOptions,
) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    """Create Restore Session

     Creates and starts a restore session for a backup job with the specified ID.

    The request command will start a restore session only for backups that were created at the time you
    specified. The `firstBackuptime` and `lastBackuptime` properties of the
    `/Organizations/{organizationId}` resource inform you when the organization data was backed up for
    the first and last times. For more information, see [Get Organization by Organization
    ID](Organization#operation/Organization_GetById).

    Mind the following: <ul> <li>If you specify the point in time which precedes the organization first
    backup time, the restore session will be created with no backup data for explore or restore.</li>
    <li>If you specify the point in time which exceeds the organization last backup time, the restore
    session will be created with backup data as of the latest restore point.</li> </ul>

    Args:
        job_id (UUID):
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSession]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExploreOptions,
) -> RESTExceptionInfo | RESTRestoreSession | None:
    """Create Restore Session

     Creates and starts a restore session for a backup job with the specified ID.

    The request command will start a restore session only for backups that were created at the time you
    specified. The `firstBackuptime` and `lastBackuptime` properties of the
    `/Organizations/{organizationId}` resource inform you when the organization data was backed up for
    the first and last times. For more information, see [Get Organization by Organization
    ID](Organization#operation/Organization_GetById).

    Mind the following: <ul> <li>If you specify the point in time which precedes the organization first
    backup time, the restore session will be created with no backup data for explore or restore.</li>
    <li>If you specify the point in time which exceeds the organization last backup time, the restore
    session will be created with backup data as of the latest restore point.</li> </ul>

    Args:
        job_id (UUID):
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSession
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExploreOptions,
) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    """Create Restore Session

     Creates and starts a restore session for a backup job with the specified ID.

    The request command will start a restore session only for backups that were created at the time you
    specified. The `firstBackuptime` and `lastBackuptime` properties of the
    `/Organizations/{organizationId}` resource inform you when the organization data was backed up for
    the first and last times. For more information, see [Get Organization by Organization
    ID](Organization#operation/Organization_GetById).

    Mind the following: <ul> <li>If you specify the point in time which precedes the organization first
    backup time, the restore session will be created with no backup data for explore or restore.</li>
    <li>If you specify the point in time which exceeds the organization last backup time, the restore
    session will be created with backup data as of the latest restore point.</li> </ul>

    Args:
        job_id (UUID):
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSession]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExploreOptions,
) -> RESTExceptionInfo | RESTRestoreSession | None:
    """Create Restore Session

     Creates and starts a restore session for a backup job with the specified ID.

    The request command will start a restore session only for backups that were created at the time you
    specified. The `firstBackuptime` and `lastBackuptime` properties of the
    `/Organizations/{organizationId}` resource inform you when the organization data was backed up for
    the first and last times. For more information, see [Get Organization by Organization
    ID](Organization#operation/Organization_GetById).

    Mind the following: <ul> <li>If you specify the point in time which precedes the organization first
    backup time, the restore session will be created with no backup data for explore or restore.</li>
    <li>If you specify the point in time which exceeds the organization last backup time, the restore
    session will be created with backup data as of the latest restore point.</li> </ul>

    Args:
        job_id (UUID):
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSession
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed
