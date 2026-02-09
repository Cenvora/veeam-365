import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.job_session_get_status import JobSessionGetStatus
from ...models.page_of_rest_job_session import PageOfRESTJobSession
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_job_session_type import RESTJobSessionType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    job_id: UUID | Unset = UNSET,
    job_type: RESTJobSessionType | Unset = UNSET,
    end_time_lower_bound: datetime.datetime | Unset = UNSET,
    end_time_upper_bound: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    status: JobSessionGetStatus | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_job_id: str | Unset = UNSET
    if not isinstance(job_id, Unset):
        json_job_id = str(job_id)
    params["jobId"] = json_job_id

    json_job_type: str | Unset = UNSET
    if not isinstance(job_type, Unset):
        json_job_type = job_type.value

    params["jobType"] = json_job_type

    json_end_time_lower_bound: str | Unset = UNSET
    if not isinstance(end_time_lower_bound, Unset):
        json_end_time_lower_bound = end_time_lower_bound.isoformat()
    params["endTimeLowerBound"] = json_end_time_lower_bound

    json_end_time_upper_bound: str | Unset = UNSET
    if not isinstance(end_time_upper_bound, Unset):
        json_end_time_upper_bound = end_time_upper_bound.isoformat()
    params["endTimeUpperBound"] = json_end_time_upper_bound

    params["limit"] = limit

    params["offset"] = offset

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/JobSessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTJobSession | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTJobSession.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTJobSession | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    job_id: UUID | Unset = UNSET,
    job_type: RESTJobSessionType | Unset = UNSET,
    end_time_lower_bound: datetime.datetime | Unset = UNSET,
    end_time_upper_bound: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    status: JobSessionGetStatus | Unset = UNSET,
) -> Response[PageOfRESTJobSession | RESTExceptionInfo]:
    """Get Job Sessions

     Returns a collection of all job sessions created for backup and backup copy jobs or a backup job
    with the specified ID.

    Args:
        job_id (UUID | Unset):
        job_type (RESTJobSessionType | Unset): Type of the job session.
        end_time_lower_bound (datetime.datetime | Unset):
        end_time_upper_bound (datetime.datetime | Unset):
        limit (int | Unset):
        offset (int | Unset):
        status (JobSessionGetStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTJobSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        job_type=job_type,
        end_time_lower_bound=end_time_lower_bound,
        end_time_upper_bound=end_time_upper_bound,
        limit=limit,
        offset=offset,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    job_id: UUID | Unset = UNSET,
    job_type: RESTJobSessionType | Unset = UNSET,
    end_time_lower_bound: datetime.datetime | Unset = UNSET,
    end_time_upper_bound: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    status: JobSessionGetStatus | Unset = UNSET,
) -> PageOfRESTJobSession | RESTExceptionInfo | None:
    """Get Job Sessions

     Returns a collection of all job sessions created for backup and backup copy jobs or a backup job
    with the specified ID.

    Args:
        job_id (UUID | Unset):
        job_type (RESTJobSessionType | Unset): Type of the job session.
        end_time_lower_bound (datetime.datetime | Unset):
        end_time_upper_bound (datetime.datetime | Unset):
        limit (int | Unset):
        offset (int | Unset):
        status (JobSessionGetStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTJobSession | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        job_id=job_id,
        job_type=job_type,
        end_time_lower_bound=end_time_lower_bound,
        end_time_upper_bound=end_time_upper_bound,
        limit=limit,
        offset=offset,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    job_id: UUID | Unset = UNSET,
    job_type: RESTJobSessionType | Unset = UNSET,
    end_time_lower_bound: datetime.datetime | Unset = UNSET,
    end_time_upper_bound: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    status: JobSessionGetStatus | Unset = UNSET,
) -> Response[PageOfRESTJobSession | RESTExceptionInfo]:
    """Get Job Sessions

     Returns a collection of all job sessions created for backup and backup copy jobs or a backup job
    with the specified ID.

    Args:
        job_id (UUID | Unset):
        job_type (RESTJobSessionType | Unset): Type of the job session.
        end_time_lower_bound (datetime.datetime | Unset):
        end_time_upper_bound (datetime.datetime | Unset):
        limit (int | Unset):
        offset (int | Unset):
        status (JobSessionGetStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTJobSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        job_type=job_type,
        end_time_lower_bound=end_time_lower_bound,
        end_time_upper_bound=end_time_upper_bound,
        limit=limit,
        offset=offset,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    job_id: UUID | Unset = UNSET,
    job_type: RESTJobSessionType | Unset = UNSET,
    end_time_lower_bound: datetime.datetime | Unset = UNSET,
    end_time_upper_bound: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    status: JobSessionGetStatus | Unset = UNSET,
) -> PageOfRESTJobSession | RESTExceptionInfo | None:
    """Get Job Sessions

     Returns a collection of all job sessions created for backup and backup copy jobs or a backup job
    with the specified ID.

    Args:
        job_id (UUID | Unset):
        job_type (RESTJobSessionType | Unset): Type of the job session.
        end_time_lower_bound (datetime.datetime | Unset):
        end_time_upper_bound (datetime.datetime | Unset):
        limit (int | Unset):
        offset (int | Unset):
        status (JobSessionGetStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTJobSession | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            job_id=job_id,
            job_type=job_type,
            end_time_lower_bound=end_time_lower_bound,
            end_time_upper_bound=end_time_upper_bound,
            limit=limit,
            offset=offset,
            status=status,
        )
    ).parsed
