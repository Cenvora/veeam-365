from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_copy_job import RESTCopyJob
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    job_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/Jobs/{job_id}/CopyJob".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTCopyJob | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTCopyJob.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTCopyJob | RESTExceptionInfo]:
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
) -> Response[RESTCopyJob | RESTExceptionInfo]:
    """Get Backup Copy Job

     Returns a resource representation of a backup copy job created for the backup job with the specified
    ID.

    Args:
        job_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTCopyJob | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTCopyJob | RESTExceptionInfo | None:
    """Get Backup Copy Job

     Returns a resource representation of a backup copy job created for the backup job with the specified
    ID.

    Args:
        job_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTCopyJob | RESTExceptionInfo
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTCopyJob | RESTExceptionInfo]:
    """Get Backup Copy Job

     Returns a resource representation of a backup copy job created for the backup job with the specified
    ID.

    Args:
        job_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTCopyJob | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTCopyJob | RESTExceptionInfo | None:
    """Get Backup Copy Job

     Returns a resource representation of a backup copy job created for the backup job with the specified
    ID.

    Args:
        job_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTCopyJob | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
