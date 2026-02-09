from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.job_session_changes_get_response import JobSessionChangesGetResponse
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_job_session_type import RESTJobSessionType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    job_type: RESTJobSessionType | Unset = UNSET,
    limit: int | Unset = UNSET,
    from_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_job_type: str | Unset = UNSET
    if not isinstance(job_type, Unset):
        json_job_type = job_type.value

    params["jobType"] = json_job_type

    params["limit"] = limit

    params["from"] = from_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/JobSessions/Changes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JobSessionChangesGetResponse | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = JobSessionChangesGetResponse.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JobSessionChangesGetResponse | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    job_type: RESTJobSessionType | Unset = UNSET,
    limit: int | Unset = UNSET,
    from_: str | Unset = UNSET,
) -> Response[JobSessionChangesGetResponse | RESTExceptionInfo]:
    """Get Changes

     Returns a collection of changes that appeared during job sessions starting from the initial
    backup/backup copy or from a specified change token.

    Args:
        job_type (RESTJobSessionType | Unset):
        limit (int | Unset):
        from_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobSessionChangesGetResponse | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
        limit=limit,
        from_=from_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    job_type: RESTJobSessionType | Unset = UNSET,
    limit: int | Unset = UNSET,
    from_: str | Unset = UNSET,
) -> JobSessionChangesGetResponse | RESTExceptionInfo | None:
    """Get Changes

     Returns a collection of changes that appeared during job sessions starting from the initial
    backup/backup copy or from a specified change token.

    Args:
        job_type (RESTJobSessionType | Unset):
        limit (int | Unset):
        from_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobSessionChangesGetResponse | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        job_type=job_type,
        limit=limit,
        from_=from_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    job_type: RESTJobSessionType | Unset = UNSET,
    limit: int | Unset = UNSET,
    from_: str | Unset = UNSET,
) -> Response[JobSessionChangesGetResponse | RESTExceptionInfo]:
    """Get Changes

     Returns a collection of changes that appeared during job sessions starting from the initial
    backup/backup copy or from a specified change token.

    Args:
        job_type (RESTJobSessionType | Unset):
        limit (int | Unset):
        from_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobSessionChangesGetResponse | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
        limit=limit,
        from_=from_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    job_type: RESTJobSessionType | Unset = UNSET,
    limit: int | Unset = UNSET,
    from_: str | Unset = UNSET,
) -> JobSessionChangesGetResponse | RESTExceptionInfo | None:
    """Get Changes

     Returns a collection of changes that appeared during job sessions starting from the initial
    backup/backup copy or from a specified change token.

    Args:
        job_type (RESTJobSessionType | Unset):
        limit (int | Unset):
        from_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobSessionChangesGetResponse | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            job_type=job_type,
            limit=limit,
            from_=from_,
        )
    ).parsed
