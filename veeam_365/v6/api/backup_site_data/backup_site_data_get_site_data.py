from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_backup_site_data import RESTBackupSiteData
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    repository_id: UUID,
    site_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/BackupRepositories/{repository_id}/SiteData/{site_id}".format(
            repository_id=quote(str(repository_id), safe=""),
            site_id=quote(str(site_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTBackupSiteData | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTBackupSiteData.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTBackupSiteData | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: UUID,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTBackupSiteData | RESTExceptionInfo]:
    """
    Args:
        repository_id (UUID):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupSiteData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        site_id=site_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: UUID,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTBackupSiteData | RESTExceptionInfo | None:
    """
    Args:
        repository_id (UUID):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupSiteData | RESTExceptionInfo
    """

    return sync_detailed(
        repository_id=repository_id,
        site_id=site_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    repository_id: UUID,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTBackupSiteData | RESTExceptionInfo]:
    """
    Args:
        repository_id (UUID):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupSiteData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        site_id=site_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: UUID,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTBackupSiteData | RESTExceptionInfo | None:
    """
    Args:
        repository_id (UUID):
        site_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupSiteData | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            site_id=site_id,
            client=client,
        )
    ).parsed
