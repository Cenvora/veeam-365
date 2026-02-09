from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.azure_storage_endpoint import AzureStorageEndpoint
from ...models.rest_azure_container import RESTAzureContainer
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response


def _get_kwargs(
    name: str,
    *,
    account_id: UUID,
    region_type: AzureStorageEndpoint,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_account_id = str(account_id)
    params["accountId"] = json_account_id

    json_region_type = region_type.value
    params["RegionType"] = json_region_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/AzureResources/containers/{name}".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTAzureContainer | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTAzureContainer.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTAzureContainer | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AzureStorageEndpoint,
) -> Response[RESTAzureContainer | RESTExceptionInfo]:
    """
    Args:
        name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAzureContainer | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        name=name,
        account_id=account_id,
        region_type=region_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AzureStorageEndpoint,
) -> RESTAzureContainer | RESTExceptionInfo | None:
    """
    Args:
        name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAzureContainer | RESTExceptionInfo
    """

    return sync_detailed(
        name=name,
        client=client,
        account_id=account_id,
        region_type=region_type,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AzureStorageEndpoint,
) -> Response[RESTAzureContainer | RESTExceptionInfo]:
    """
    Args:
        name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAzureContainer | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        name=name,
        account_id=account_id,
        region_type=region_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AzureStorageEndpoint,
) -> RESTAzureContainer | RESTExceptionInfo | None:
    """
    Args:
        name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAzureContainer | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            account_id=account_id,
            region_type=region_type,
        )
    ).parsed
