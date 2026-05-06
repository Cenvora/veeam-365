from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.azure_storage_endpoint import AzureStorageEndpoint
from ...models.rest_azure_folder_to_receive import RESTAzureFolderToReceive
from ...models.rest_azure_folder_to_send import RESTAzureFolderToSend
from ...models.rest_exception_info import RESTExceptionInfo
from typing import cast
from uuid import UUID



def _get_kwargs(
    container_name: str,
    *,
    body: RESTAzureFolderToSend,
    account_id: UUID,
    region_type: AzureStorageEndpoint,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_account_id = str(account_id)
    params["accountId"] = json_account_id

    json_region_type = region_type.value
    params["RegionType"] = json_region_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/AzureResources/containers/{container_name}/folders".format(container_name=quote(str(container_name), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTAzureFolderToReceive | RESTExceptionInfo:
    if response.status_code == 201:
        response_201 = RESTAzureFolderToReceive.from_dict(response.json())



        return response_201

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTAzureFolderToReceive | RESTExceptionInfo]:
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
    body: RESTAzureFolderToSend,
    account_id: UUID,
    region_type: AzureStorageEndpoint,

) -> Response[RESTAzureFolderToReceive | RESTExceptionInfo]:
    """ Create Folders

     Creates a new folder in the specified Azure container.

    Args:
        container_name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint): Specifies a Microsoft Entra region.
        body (RESTAzureFolderToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAzureFolderToReceive | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        container_name=container_name,
body=body,
account_id=account_id,
region_type=region_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    container_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTAzureFolderToSend,
    account_id: UUID,
    region_type: AzureStorageEndpoint,

) -> RESTAzureFolderToReceive | RESTExceptionInfo | None:
    """ Create Folders

     Creates a new folder in the specified Azure container.

    Args:
        container_name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint): Specifies a Microsoft Entra region.
        body (RESTAzureFolderToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAzureFolderToReceive | RESTExceptionInfo
     """


    return sync_detailed(
        container_name=container_name,
client=client,
body=body,
account_id=account_id,
region_type=region_type,

    ).parsed

async def asyncio_detailed(
    container_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTAzureFolderToSend,
    account_id: UUID,
    region_type: AzureStorageEndpoint,

) -> Response[RESTAzureFolderToReceive | RESTExceptionInfo]:
    """ Create Folders

     Creates a new folder in the specified Azure container.

    Args:
        container_name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint): Specifies a Microsoft Entra region.
        body (RESTAzureFolderToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAzureFolderToReceive | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        container_name=container_name,
body=body,
account_id=account_id,
region_type=region_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    container_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTAzureFolderToSend,
    account_id: UUID,
    region_type: AzureStorageEndpoint,

) -> RESTAzureFolderToReceive | RESTExceptionInfo | None:
    """ Create Folders

     Creates a new folder in the specified Azure container.

    Args:
        container_name (str):
        account_id (UUID):
        region_type (AzureStorageEndpoint): Specifies a Microsoft Entra region.
        body (RESTAzureFolderToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAzureFolderToReceive | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        container_name=container_name,
client=client,
body=body,
account_id=account_id,
region_type=region_type,

    )).parsed
