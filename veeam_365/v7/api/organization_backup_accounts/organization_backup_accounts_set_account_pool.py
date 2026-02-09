from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_account_pool import RESTAccountPool
from ...models.rest_backup_account import RESTBackupAccount
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    *,
    body: list[RESTBackupAccount],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v7/Organizations/{organization_id}/BackupAccounts".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTAccountPool | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTAccountPool.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTAccountPool | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTBackupAccount],
) -> Response[RESTAccountPool | RESTExceptionInfo]:
    """Add Backup Accounts

     Adds Microsoft 365 backup accounts to the backup configuration to minimize throttling when backing
    up Microsoft SharePoint and OneDrive for Business items.

    Args:
        organization_id (UUID):
        body (list[RESTBackupAccount]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAccountPool | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTBackupAccount],
) -> RESTAccountPool | RESTExceptionInfo | None:
    """Add Backup Accounts

     Adds Microsoft 365 backup accounts to the backup configuration to minimize throttling when backing
    up Microsoft SharePoint and OneDrive for Business items.

    Args:
        organization_id (UUID):
        body (list[RESTBackupAccount]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAccountPool | RESTExceptionInfo
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTBackupAccount],
) -> Response[RESTAccountPool | RESTExceptionInfo]:
    """Add Backup Accounts

     Adds Microsoft 365 backup accounts to the backup configuration to minimize throttling when backing
    up Microsoft SharePoint and OneDrive for Business items.

    Args:
        organization_id (UUID):
        body (list[RESTBackupAccount]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAccountPool | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTBackupAccount],
) -> RESTAccountPool | RESTExceptionInfo | None:
    """Add Backup Accounts

     Adds Microsoft 365 backup accounts to the backup configuration to minimize throttling when backing
    up Microsoft SharePoint and OneDrive for Business items.

    Args:
        organization_id (UUID):
        body (list[RESTBackupAccount]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAccountPool | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            body=body,
        )
    ).parsed
