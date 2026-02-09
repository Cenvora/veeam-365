from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_azure_subscription import RESTAzureSubscription
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_account_id: UUID,
    *,
    subscription_name: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["subscriptionName"] = subscription_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/AzureServiceAccounts/{service_account_id}/Subscriptions".format(
            service_account_id=quote(str(service_account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTAzureSubscription]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTAzureSubscription.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTAzureSubscription]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    subscription_name: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTAzureSubscription]]:
    """
    Args:
        service_account_id (UUID):
        subscription_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAzureSubscription]]
    """

    kwargs = _get_kwargs(
        service_account_id=service_account_id,
        subscription_name=subscription_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    subscription_name: str | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTAzureSubscription] | None:
    """
    Args:
        service_account_id (UUID):
        subscription_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAzureSubscription]
    """

    return sync_detailed(
        service_account_id=service_account_id,
        client=client,
        subscription_name=subscription_name,
    ).parsed


async def asyncio_detailed(
    service_account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    subscription_name: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTAzureSubscription]]:
    """
    Args:
        service_account_id (UUID):
        subscription_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAzureSubscription]]
    """

    kwargs = _get_kwargs(
        service_account_id=service_account_id,
        subscription_name=subscription_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    subscription_name: str | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTAzureSubscription] | None:
    """
    Args:
        service_account_id (UUID):
        subscription_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAzureSubscription]
    """

    return (
        await asyncio_detailed(
            service_account_id=service_account_id,
            client=client,
            subscription_name=subscription_name,
        )
    ).parsed
