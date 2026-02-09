import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_restore_point import PageOfRESTRestorePoint
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_id: UUID | Unset = UNSET,
    job_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
    is_long_term_copy: bool | Unset = UNSET,
    is_copy: bool | Unset = UNSET,
    is_retrieved: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
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

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["orderAsc"] = order_asc

    params["isLongTermCopy"] = is_long_term_copy

    params["isCopy"] = is_copy

    params["isRetrieved"] = is_retrieved

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/RestorePoints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTRestorePoint | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTRestorePoint.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTRestorePoint | RESTExceptionInfo]:
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
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
    is_long_term_copy: bool | Unset = UNSET,
    is_copy: bool | Unset = UNSET,
    is_retrieved: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTRestorePoint | RESTExceptionInfo]:
    """Get Restore Points

     Returns a collection of restore points created by Veeam Backup for Microsoft 365.

    Args:
        organization_id (UUID | Unset):
        job_id (UUID | Unset):
        repository_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        order_asc (bool | Unset):
        is_long_term_copy (bool | Unset):
        is_copy (bool | Unset):
        is_retrieved (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTRestorePoint | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        job_id=job_id,
        repository_id=repository_id,
        from_=from_,
        to=to,
        order_asc=order_asc,
        is_long_term_copy=is_long_term_copy,
        is_copy=is_copy,
        is_retrieved=is_retrieved,
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
    organization_id: UUID | Unset = UNSET,
    job_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
    is_long_term_copy: bool | Unset = UNSET,
    is_copy: bool | Unset = UNSET,
    is_retrieved: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTRestorePoint | RESTExceptionInfo | None:
    """Get Restore Points

     Returns a collection of restore points created by Veeam Backup for Microsoft 365.

    Args:
        organization_id (UUID | Unset):
        job_id (UUID | Unset):
        repository_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        order_asc (bool | Unset):
        is_long_term_copy (bool | Unset):
        is_copy (bool | Unset):
        is_retrieved (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTRestorePoint | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        organization_id=organization_id,
        job_id=job_id,
        repository_id=repository_id,
        from_=from_,
        to=to,
        order_asc=order_asc,
        is_long_term_copy=is_long_term_copy,
        is_copy=is_copy,
        is_retrieved=is_retrieved,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    job_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
    is_long_term_copy: bool | Unset = UNSET,
    is_copy: bool | Unset = UNSET,
    is_retrieved: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTRestorePoint | RESTExceptionInfo]:
    """Get Restore Points

     Returns a collection of restore points created by Veeam Backup for Microsoft 365.

    Args:
        organization_id (UUID | Unset):
        job_id (UUID | Unset):
        repository_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        order_asc (bool | Unset):
        is_long_term_copy (bool | Unset):
        is_copy (bool | Unset):
        is_retrieved (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTRestorePoint | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        job_id=job_id,
        repository_id=repository_id,
        from_=from_,
        to=to,
        order_asc=order_asc,
        is_long_term_copy=is_long_term_copy,
        is_copy=is_copy,
        is_retrieved=is_retrieved,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    job_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
    is_long_term_copy: bool | Unset = UNSET,
    is_copy: bool | Unset = UNSET,
    is_retrieved: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTRestorePoint | RESTExceptionInfo | None:
    """Get Restore Points

     Returns a collection of restore points created by Veeam Backup for Microsoft 365.

    Args:
        organization_id (UUID | Unset):
        job_id (UUID | Unset):
        repository_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        order_asc (bool | Unset):
        is_long_term_copy (bool | Unset):
        is_copy (bool | Unset):
        is_retrieved (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTRestorePoint | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_id=organization_id,
            job_id=job_id,
            repository_id=repository_id,
            from_=from_,
            to=to,
            order_asc=order_asc,
            is_long_term_copy=is_long_term_copy,
            is_copy=is_copy,
            is_retrieved=is_retrieved,
            limit=limit,
            offset=offset,
        )
    ).parsed
