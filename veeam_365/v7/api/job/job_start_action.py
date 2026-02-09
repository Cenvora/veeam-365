from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_start_job_options import RESTStartJobOptions
from ...types import Response


def _get_kwargs(
    job_id: UUID,
    *,
    body: RESTStartJobOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v7/Jobs/{job_id}/start".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RESTExceptionInfo:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RESTExceptionInfo]:
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
    body: RESTStartJobOptions,
) -> Response[Any | RESTExceptionInfo]:
    """Start Backup Job

     Starts a backup job with the specified ID.

    Args:
        job_id (UUID):
        body (RESTStartJobOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
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
    body: RESTStartJobOptions,
) -> Any | RESTExceptionInfo | None:
    """Start Backup Job

     Starts a backup job with the specified ID.

    Args:
        job_id (UUID):
        body (RESTStartJobOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
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
    body: RESTStartJobOptions,
) -> Response[Any | RESTExceptionInfo]:
    """Start Backup Job

     Starts a backup job with the specified ID.

    Args:
        job_id (UUID):
        body (RESTStartJobOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
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
    body: RESTStartJobOptions,
) -> Any | RESTExceptionInfo | None:
    """Start Backup Job

     Starts a backup job with the specified ID.

    Args:
        job_id (UUID):
        body (RESTStartJobOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed
