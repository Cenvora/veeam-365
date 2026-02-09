from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_object_storage_repository_composed import RESTObjectStorageRepositoryComposed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    long_term: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["longTerm"] = long_term

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/objectstoragerepositories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTObjectStorageRepositoryComposed]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTObjectStorageRepositoryComposed.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTObjectStorageRepositoryComposed]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    long_term: bool | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTObjectStorageRepositoryComposed]]:
    """Get Object Storage

     Returns a list of all object storage added to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        long_term (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTObjectStorageRepositoryComposed]]
    """

    kwargs = _get_kwargs(
        long_term=long_term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    long_term: bool | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTObjectStorageRepositoryComposed] | None:
    """Get Object Storage

     Returns a list of all object storage added to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        long_term (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTObjectStorageRepositoryComposed]
    """

    return sync_detailed(
        client=client,
        long_term=long_term,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    long_term: bool | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTObjectStorageRepositoryComposed]]:
    """Get Object Storage

     Returns a list of all object storage added to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        long_term (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTObjectStorageRepositoryComposed]]
    """

    kwargs = _get_kwargs(
        long_term=long_term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    long_term: bool | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTObjectStorageRepositoryComposed] | None:
    """Get Object Storage

     Returns a list of all object storage added to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        long_term (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTObjectStorageRepositoryComposed]
    """

    return (
        await asyncio_detailed(
            client=client,
            long_term=long_term,
        )
    ).parsed
