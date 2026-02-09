from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_backup_user_data import RESTBackupUserData
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    repository_id: UUID,
    user_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/BackupRepositories/{repository_id}/UserData/{user_id}".format(
            repository_id=quote(str(repository_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTBackupUserData | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTBackupUserData.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTBackupUserData | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTBackupUserData | RESTExceptionInfo]:
    """Get User Data by Repository and User ID

     Returns a backed-up or user with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupUserData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTBackupUserData | RESTExceptionInfo | None:
    """Get User Data by Repository and User ID

     Returns a backed-up or user with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupUserData | RESTExceptionInfo
    """

    return sync_detailed(
        repository_id=repository_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    repository_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTBackupUserData | RESTExceptionInfo]:
    """Get User Data by Repository and User ID

     Returns a backed-up or user with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupUserData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTBackupUserData | RESTExceptionInfo | None:
    """Get User Data by Repository and User ID

     Returns a backed-up or user with the specified ID whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupUserData | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
