from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_copy_job import RESTCopyJob
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    repository_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_repository_id: str | Unset = UNSET
    if not isinstance(repository_id, Unset):
        json_repository_id = str(repository_id)
    params["repositoryId"] = json_repository_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/CopyJobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTCopyJob]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTCopyJob.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTCopyJob]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    repository_id: UUID | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTCopyJob]]:
    """Get Backup Copy Jobs

     Returns a list of configured backup copy jobs.

    Args:
        repository_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTCopyJob]]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    repository_id: UUID | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTCopyJob] | None:
    """Get Backup Copy Jobs

     Returns a list of configured backup copy jobs.

    Args:
        repository_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTCopyJob]
    """

    return sync_detailed(
        client=client,
        repository_id=repository_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    repository_id: UUID | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTCopyJob]]:
    """Get Backup Copy Jobs

     Returns a list of configured backup copy jobs.

    Args:
        repository_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTCopyJob]]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    repository_id: UUID | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTCopyJob] | None:
    """Get Backup Copy Jobs

     Returns a list of configured backup copy jobs.

    Args:
        repository_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTCopyJob]
    """

    return (
        await asyncio_detailed(
            client=client,
            repository_id=repository_id,
        )
    ).parsed
