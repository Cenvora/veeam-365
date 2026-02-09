from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_amazon_vpc import RESTAmazonVpc
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response


def _get_kwargs(
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
        "url": "/v8/EC2Resources/VirtualPrivateCloud",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTAmazonVpc]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTAmazonVpc.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTAmazonVpc]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_id: str,
) -> Response[RESTExceptionInfo | list[RESTAmazonVpc]]:
    """Get Virtual Private Clouds

     Returns a list of available Amazon Virtual Private Clouds (Amazon VPC) dedicated to the specified
    cloud account.

    Args:
        account_id (UUID):
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAmazonVpc]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        region_id=region_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_id: str,
) -> RESTExceptionInfo | list[RESTAmazonVpc] | None:
    """Get Virtual Private Clouds

     Returns a list of available Amazon Virtual Private Clouds (Amazon VPC) dedicated to the specified
    cloud account.

    Args:
        account_id (UUID):
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAmazonVpc]
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        region_id=region_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_id: str,
) -> Response[RESTExceptionInfo | list[RESTAmazonVpc]]:
    """Get Virtual Private Clouds

     Returns a list of available Amazon Virtual Private Clouds (Amazon VPC) dedicated to the specified
    cloud account.

    Args:
        account_id (UUID):
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAmazonVpc]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        region_id=region_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_id: str,
) -> RESTExceptionInfo | list[RESTAmazonVpc] | None:
    """Get Virtual Private Clouds

     Returns a list of available Amazon Virtual Private Clouds (Amazon VPC) dedicated to the specified
    cloud account.

    Args:
        account_id (UUID):
        region_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAmazonVpc]
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            region_id=region_id,
        )
    ).parsed
