from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.azure_storage_endpoint import AzureStorageEndpoint
from ...models.rest_azure_folder_to_receive import RESTAzureFolderToReceive
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    container_name: str,
    *,
    account_id: UUID,
    region_type: AzureStorageEndpoint,
    name: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_account_id = str(account_id)
    params["accountId"] = json_account_id

    json_region_type = region_type.value
    params["RegionType"] = json_region_type

    params["Name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/AzureResources/containers/{container_name}/folders".format(
            container_name=quote(str(container_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTAzureFolderToReceive]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTAzureFolderToReceive.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTAzureFolderToReceive]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    container_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AzureStorageEndpoint,
    name: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTAzureFolderToReceive]]:
    """Get Folders

     Returns a list of Azure storage folders created in the specified container.

    Args:
        container_name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint): Specifies a Microsoft Azure region.
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAzureFolderToReceive]]
    """

    kwargs = _get_kwargs(
        container_name=container_name,
        account_id=account_id,
        region_type=region_type,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    container_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AzureStorageEndpoint,
    name: str | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTAzureFolderToReceive] | None:
    """Get Folders

     Returns a list of Azure storage folders created in the specified container.

    Args:
        container_name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint): Specifies a Microsoft Azure region.
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAzureFolderToReceive]
    """

    return sync_detailed(
        container_name=container_name,
        client=client,
        account_id=account_id,
        region_type=region_type,
        name=name,
    ).parsed


async def asyncio_detailed(
    container_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AzureStorageEndpoint,
    name: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTAzureFolderToReceive]]:
    """Get Folders

     Returns a list of Azure storage folders created in the specified container.

    Args:
        container_name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint): Specifies a Microsoft Azure region.
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAzureFolderToReceive]]
    """

    kwargs = _get_kwargs(
        container_name=container_name,
        account_id=account_id,
        region_type=region_type,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    container_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AzureStorageEndpoint,
    name: str | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTAzureFolderToReceive] | None:
    """Get Folders

     Returns a list of Azure storage folders created in the specified container.

    Args:
        container_name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint): Specifies a Microsoft Azure region.
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAzureFolderToReceive]
    """

    return (
        await asyncio_detailed(
            container_name=container_name,
            client=client,
            account_id=account_id,
            region_type=region_type,
            name=name,
        )
    ).parsed
