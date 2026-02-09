from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_azure_virtual_machine_size import RESTAzureVirtualMachineSize
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    service_account_id: UUID,
    subscription_id: str,
    location_name: str,
    vm_size_name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/AzureServiceAccounts/{service_account_id}/Subscriptions/{subscription_id}/Locations/{location_name}/VirtualMachineSizes/{vm_size_name}".format(
            service_account_id=quote(str(service_account_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
            location_name=quote(str(location_name), safe=""),
            vm_size_name=quote(str(vm_size_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTAzureVirtualMachineSize | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTAzureVirtualMachineSize.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTAzureVirtualMachineSize | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_account_id: UUID,
    subscription_id: str,
    location_name: str,
    vm_size_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTAzureVirtualMachineSize | RESTExceptionInfo]:
    """Get Virtual Machine Size by Name

     Returns information about the Azure archiver appliance - an auxiliary virtual machine with the
    specified name.

    Args:
        service_account_id (UUID):
        subscription_id (str):
        location_name (str):
        vm_size_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAzureVirtualMachineSize | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        service_account_id=service_account_id,
        subscription_id=subscription_id,
        location_name=location_name,
        vm_size_name=vm_size_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_account_id: UUID,
    subscription_id: str,
    location_name: str,
    vm_size_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTAzureVirtualMachineSize | RESTExceptionInfo | None:
    """Get Virtual Machine Size by Name

     Returns information about the Azure archiver appliance - an auxiliary virtual machine with the
    specified name.

    Args:
        service_account_id (UUID):
        subscription_id (str):
        location_name (str):
        vm_size_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAzureVirtualMachineSize | RESTExceptionInfo
    """

    return sync_detailed(
        service_account_id=service_account_id,
        subscription_id=subscription_id,
        location_name=location_name,
        vm_size_name=vm_size_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_account_id: UUID,
    subscription_id: str,
    location_name: str,
    vm_size_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTAzureVirtualMachineSize | RESTExceptionInfo]:
    """Get Virtual Machine Size by Name

     Returns information about the Azure archiver appliance - an auxiliary virtual machine with the
    specified name.

    Args:
        service_account_id (UUID):
        subscription_id (str):
        location_name (str):
        vm_size_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAzureVirtualMachineSize | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        service_account_id=service_account_id,
        subscription_id=subscription_id,
        location_name=location_name,
        vm_size_name=vm_size_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_account_id: UUID,
    subscription_id: str,
    location_name: str,
    vm_size_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTAzureVirtualMachineSize | RESTExceptionInfo | None:
    """Get Virtual Machine Size by Name

     Returns information about the Azure archiver appliance - an auxiliary virtual machine with the
    specified name.

    Args:
        service_account_id (UUID):
        subscription_id (str):
        location_name (str):
        vm_size_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAzureVirtualMachineSize | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            service_account_id=service_account_id,
            subscription_id=subscription_id,
            location_name=location_name,
            vm_size_name=vm_size_name,
            client=client,
        )
    ).parsed
