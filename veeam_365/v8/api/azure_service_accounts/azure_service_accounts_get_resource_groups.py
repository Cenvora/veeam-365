from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_azure_resource_group import RESTAzureResourceGroup
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    service_account_id: UUID,
    subscription_id: str,
    *,
    location_name: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["locationName"] = location_name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/AzureServiceAccounts/{service_account_id}/Subscriptions/{subscription_id}/ResourceGroups".format(service_account_id=quote(str(service_account_id), safe=""),subscription_id=quote(str(subscription_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | list[RESTAzureResourceGroup]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = RESTAzureResourceGroup.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | list[RESTAzureResourceGroup]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_account_id: UUID,
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
    location_name: str | Unset = UNSET,

) -> Response[RESTExceptionInfo | list[RESTAzureResourceGroup]]:
    """ Get Resource Groups

     Returns a list of resource groups that will be associated with the Azure archiver appliance.

    Args:
        service_account_id (UUID):
        subscription_id (str):
        location_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAzureResourceGroup]]
     """


    kwargs = _get_kwargs(
        service_account_id=service_account_id,
subscription_id=subscription_id,
location_name=location_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    service_account_id: UUID,
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
    location_name: str | Unset = UNSET,

) -> RESTExceptionInfo | list[RESTAzureResourceGroup] | None:
    """ Get Resource Groups

     Returns a list of resource groups that will be associated with the Azure archiver appliance.

    Args:
        service_account_id (UUID):
        subscription_id (str):
        location_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAzureResourceGroup]
     """


    return sync_detailed(
        service_account_id=service_account_id,
subscription_id=subscription_id,
client=client,
location_name=location_name,

    ).parsed

async def asyncio_detailed(
    service_account_id: UUID,
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
    location_name: str | Unset = UNSET,

) -> Response[RESTExceptionInfo | list[RESTAzureResourceGroup]]:
    """ Get Resource Groups

     Returns a list of resource groups that will be associated with the Azure archiver appliance.

    Args:
        service_account_id (UUID):
        subscription_id (str):
        location_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAzureResourceGroup]]
     """


    kwargs = _get_kwargs(
        service_account_id=service_account_id,
subscription_id=subscription_id,
location_name=location_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    service_account_id: UUID,
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
    location_name: str | Unset = UNSET,

) -> RESTExceptionInfo | list[RESTAzureResourceGroup] | None:
    """ Get Resource Groups

     Returns a list of resource groups that will be associated with the Azure archiver appliance.

    Args:
        service_account_id (UUID):
        subscription_id (str):
        location_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAzureResourceGroup]
     """


    return (await asyncio_detailed(
        service_account_id=service_account_id,
subscription_id=subscription_id,
client=client,
location_name=location_name,

    )).parsed
