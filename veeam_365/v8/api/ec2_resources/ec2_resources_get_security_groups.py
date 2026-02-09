from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_amazon_security_group import RESTAmazonSecurityGroup
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    account_id: UUID,
    region_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_account_id = str(account_id)
    params["accountId"] = json_account_id

    params["regionId"] = region_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/EC2Resources/VirtualPrivateCloud/{id}/SecurityGroup".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTAmazonSecurityGroup]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTAmazonSecurityGroup.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTAmazonSecurityGroup]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_id: str,
) -> Response[RESTExceptionInfo | list[RESTAmazonSecurityGroup]]:
    """Get Security Groups

     Returns a list of security groups that will be associated with the Amazon archiver appliance.

    Args:
        id (str):
        account_id (UUID):
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAmazonSecurityGroup]]
    """

    kwargs = _get_kwargs(
        id=id,
        account_id=account_id,
        region_id=region_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_id: str,
) -> RESTExceptionInfo | list[RESTAmazonSecurityGroup] | None:
    """Get Security Groups

     Returns a list of security groups that will be associated with the Amazon archiver appliance.

    Args:
        id (str):
        account_id (UUID):
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAmazonSecurityGroup]
    """

    return sync_detailed(
        id=id,
        client=client,
        account_id=account_id,
        region_id=region_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_id: str,
) -> Response[RESTExceptionInfo | list[RESTAmazonSecurityGroup]]:
    """Get Security Groups

     Returns a list of security groups that will be associated with the Amazon archiver appliance.

    Args:
        id (str):
        account_id (UUID):
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAmazonSecurityGroup]]
    """

    kwargs = _get_kwargs(
        id=id,
        account_id=account_id,
        region_id=region_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_id: str,
) -> RESTExceptionInfo | list[RESTAmazonSecurityGroup] | None:
    """Get Security Groups

     Returns a list of security groups that will be associated with the Amazon archiver appliance.

    Args:
        id (str):
        account_id (UUID):
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAmazonSecurityGroup]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            account_id=account_id,
            region_id=region_id,
        )
    ).parsed
