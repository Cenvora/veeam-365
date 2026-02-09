from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_backup_repository import PageOfRESTBackupRepository
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    proxy_id: UUID | Unset = UNSET,
    proxy_pool_id: UUID | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
    long_term: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_proxy_id: str | Unset = UNSET
    if not isinstance(proxy_id, Unset):
        json_proxy_id = str(proxy_id)
    params["proxyId"] = json_proxy_id

    json_proxy_pool_id: str | Unset = UNSET
    if not isinstance(proxy_pool_id, Unset):
        json_proxy_pool_id = str(proxy_pool_id)
    params["proxyPoolId"] = json_proxy_pool_id

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organizationId"] = json_organization_id

    params["longTerm"] = long_term

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/BackupRepositories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTBackupRepository | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTBackupRepository.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTBackupRepository | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    proxy_id: UUID | Unset = UNSET,
    proxy_pool_id: UUID | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
    long_term: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTBackupRepository | RESTExceptionInfo]:
    """Get Backup Repositories

     Returns a collection of backup repositories.

    Args:
        proxy_id (UUID | Unset):
        proxy_pool_id (UUID | Unset):
        organization_id (UUID | Unset):
        long_term (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupRepository | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        proxy_id=proxy_id,
        proxy_pool_id=proxy_pool_id,
        organization_id=organization_id,
        long_term=long_term,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    proxy_id: UUID | Unset = UNSET,
    proxy_pool_id: UUID | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
    long_term: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTBackupRepository | RESTExceptionInfo | None:
    """Get Backup Repositories

     Returns a collection of backup repositories.

    Args:
        proxy_id (UUID | Unset):
        proxy_pool_id (UUID | Unset):
        organization_id (UUID | Unset):
        long_term (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupRepository | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        proxy_id=proxy_id,
        proxy_pool_id=proxy_pool_id,
        organization_id=organization_id,
        long_term=long_term,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    proxy_id: UUID | Unset = UNSET,
    proxy_pool_id: UUID | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
    long_term: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTBackupRepository | RESTExceptionInfo]:
    """Get Backup Repositories

     Returns a collection of backup repositories.

    Args:
        proxy_id (UUID | Unset):
        proxy_pool_id (UUID | Unset):
        organization_id (UUID | Unset):
        long_term (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupRepository | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        proxy_id=proxy_id,
        proxy_pool_id=proxy_pool_id,
        organization_id=organization_id,
        long_term=long_term,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    proxy_id: UUID | Unset = UNSET,
    proxy_pool_id: UUID | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
    long_term: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTBackupRepository | RESTExceptionInfo | None:
    """Get Backup Repositories

     Returns a collection of backup repositories.

    Args:
        proxy_id (UUID | Unset):
        proxy_pool_id (UUID | Unset):
        organization_id (UUID | Unset):
        long_term (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupRepository | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            proxy_id=proxy_id,
            proxy_pool_id=proxy_pool_id,
            organization_id=organization_id,
            long_term=long_term,
            limit=limit,
            offset=offset,
        )
    ).parsed
