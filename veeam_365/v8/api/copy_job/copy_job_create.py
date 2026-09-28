from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_copy_job import RESTCopyJob
from ...models.rest_create_copy_job import RESTCreateCopyJob
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    *,
    body: RESTCreateCopyJob,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/CopyJobs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTCopyJob | RESTExceptionInfo:
    if response.status_code == 201:
        response_201 = RESTCopyJob.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient | Client,
    body: RESTCreateCopyJob,
) -> Response[RESTCopyJob | RESTExceptionInfo]:
    """Create Backup Copy Job

     Creates a backup copy job.

    Args:
        body (RESTCreateCopyJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTCopyJob | RESTExceptionInfo]
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
    body: RESTCreateCopyJob,
) -> RESTCopyJob | RESTExceptionInfo | None:
    """Create Backup Copy Job

     Creates a backup copy job.

    Args:
        body (RESTCreateCopyJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTCopyJob | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTCreateCopyJob,
) -> Response[RESTCopyJob | RESTExceptionInfo]:
    """Create Backup Copy Job

     Creates a backup copy job.

    Args:
        body (RESTCreateCopyJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTCopyJob | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RESTCreateCopyJob,
) -> RESTCopyJob | RESTExceptionInfo | None:
    """Create Backup Copy Job

     Creates a backup copy job.

    Args:
        body (RESTCreateCopyJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTCopyJob | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
