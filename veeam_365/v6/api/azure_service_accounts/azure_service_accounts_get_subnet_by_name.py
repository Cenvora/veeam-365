from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_azure_subnet import RESTAzureSubnet
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    service_account_id: UUID,
    subscription_id: str,
    resource_group_name: str,
    virtual_network_name: str,
    subnet_name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/AzureServiceAccounts/{service_account_id}/Subscriptions/{subscription_id}/ResourceGroups/{resource_group_name}/VirtualNetworks/{virtual_network_name}/Subnets/{subnet_name}".format(
            service_account_id=quote(str(service_account_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
            resource_group_name=quote(str(resource_group_name), safe=""),
            virtual_network_name=quote(str(virtual_network_name), safe=""),
            subnet_name=quote(str(subnet_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTAzureSubnet | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTAzureSubnet.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTAzureSubnet | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_account_id: UUID,
    subscription_id: str,
    resource_group_name: str,
    virtual_network_name: str,
    subnet_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTAzureSubnet | RESTExceptionInfo]:
    """
    Args:
        service_account_id (UUID):
        subscription_id (str):
        resource_group_name (str):
        virtual_network_name (str):
        subnet_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAzureSubnet | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        service_account_id=service_account_id,
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
        virtual_network_name=virtual_network_name,
        subnet_name=subnet_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_account_id: UUID,
    subscription_id: str,
    resource_group_name: str,
    virtual_network_name: str,
    subnet_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTAzureSubnet | RESTExceptionInfo | None:
    """
    Args:
        service_account_id (UUID):
        subscription_id (str):
        resource_group_name (str):
        virtual_network_name (str):
        subnet_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAzureSubnet | RESTExceptionInfo
    """

    return sync_detailed(
        service_account_id=service_account_id,
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
        virtual_network_name=virtual_network_name,
        subnet_name=subnet_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_account_id: UUID,
    subscription_id: str,
    resource_group_name: str,
    virtual_network_name: str,
    subnet_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTAzureSubnet | RESTExceptionInfo]:
    """
    Args:
        service_account_id (UUID):
        subscription_id (str):
        resource_group_name (str):
        virtual_network_name (str):
        subnet_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAzureSubnet | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        service_account_id=service_account_id,
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
        virtual_network_name=virtual_network_name,
        subnet_name=subnet_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_account_id: UUID,
    subscription_id: str,
    resource_group_name: str,
    virtual_network_name: str,
    subnet_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTAzureSubnet | RESTExceptionInfo | None:
    """
    Args:
        service_account_id (UUID):
        subscription_id (str):
        resource_group_name (str):
        virtual_network_name (str):
        subnet_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAzureSubnet | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            service_account_id=service_account_id,
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            virtual_network_name=virtual_network_name,
            subnet_name=subnet_name,
            client=client,
        )
    ).parsed
