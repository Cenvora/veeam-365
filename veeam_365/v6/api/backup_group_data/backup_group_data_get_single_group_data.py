from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_backup_group_data import RESTBackupGroupData
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    repository_id: UUID,
    group_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/BackupRepositories/{repository_id}/GroupData/{group_id}".format(
            repository_id=quote(str(repository_id), safe=""),
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTBackupGroupData | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTBackupGroupData.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTBackupGroupData | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: UUID,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTBackupGroupData | RESTExceptionInfo]:
    """
    Args:
        repository_id (UUID):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupGroupData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: UUID,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTBackupGroupData | RESTExceptionInfo | None:
    """
    Args:
        repository_id (UUID):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupGroupData | RESTExceptionInfo
    """

    return sync_detailed(
        repository_id=repository_id,
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    repository_id: UUID,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTBackupGroupData | RESTExceptionInfo]:
    """
    Args:
        repository_id (UUID):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupGroupData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: UUID,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTBackupGroupData | RESTExceptionInfo | None:
    """
    Args:
        repository_id (UUID):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupGroupData | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            group_id=group_id,
            client=client,
        )
    ).parsed
