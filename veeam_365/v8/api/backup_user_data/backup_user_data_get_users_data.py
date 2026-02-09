from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_backup_user_data import PageOfRESTBackupUserData
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repository_id: UUID,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/BackupRepositories/{repository_id}/UserData".format(
            repository_id=quote(str(repository_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTBackupUserData | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTBackupUserData.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTBackupUserData | RESTExceptionInfo]:
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTBackupUserData | RESTExceptionInfo]:
    """Get List of Users by Repository ID

     Returns a collection of backed-up users whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupUserData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTBackupUserData | RESTExceptionInfo | None:
    """Get List of Users by Repository ID

     Returns a collection of backed-up users whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupUserData | RESTExceptionInfo
    """

    return sync_detailed(
        repository_id=repository_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTBackupUserData | RESTExceptionInfo]:
    """Get List of Users by Repository ID

     Returns a collection of backed-up users whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupUserData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTBackupUserData | RESTExceptionInfo | None:
    """Get List of Users by Repository ID

     Returns a collection of backed-up users whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupUserData | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
