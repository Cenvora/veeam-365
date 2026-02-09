from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_object_storage_repository_composed import RESTObjectStorageRepositoryComposed
from ...types import Response


def _get_kwargs(
    repository_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/objectstoragerepositories/{repository_id}".format(
            repository_id=quote(str(repository_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTObjectStorageRepositoryComposed:
    if response.status_code == 200:
        response_200 = RESTObjectStorageRepositoryComposed.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTObjectStorageRepositoryComposed]:
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
) -> Response[RESTExceptionInfo | RESTObjectStorageRepositoryComposed]:
    """Get Object Storage

     Returns a resource representation of an object storage with the specified ID.

    Args:
        repository_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTObjectStorageRepositoryComposed]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTObjectStorageRepositoryComposed | None:
    """Get Object Storage

     Returns a resource representation of an object storage with the specified ID.

    Args:
        repository_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTObjectStorageRepositoryComposed
    """

    return sync_detailed(
        repository_id=repository_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTObjectStorageRepositoryComposed]:
    """Get Object Storage

     Returns a resource representation of an object storage with the specified ID.

    Args:
        repository_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTObjectStorageRepositoryComposed]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTObjectStorageRepositoryComposed | None:
    """Get Object Storage

     Returns a resource representation of an object storage with the specified ID.

    Args:
        repository_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTObjectStorageRepositoryComposed
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            client=client,
        )
    ).parsed
