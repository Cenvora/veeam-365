from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_azure_subscription import RESTAzureSubscription
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    service_account_id: UUID,
    subscription_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/AzureServiceAccounts/{service_account_id}/Subscriptions/{subscription_id}".format(
            service_account_id=quote(str(service_account_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTAzureSubscription | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTAzureSubscription.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTAzureSubscription | RESTExceptionInfo]:
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
) -> Response[RESTAzureSubscription | RESTExceptionInfo]:
    """
    Args:
        service_account_id (UUID):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAzureSubscription | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        service_account_id=service_account_id,
        subscription_id=subscription_id,
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
) -> RESTAzureSubscription | RESTExceptionInfo | None:
    """
    Args:
        service_account_id (UUID):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAzureSubscription | RESTExceptionInfo
    """

    return sync_detailed(
        service_account_id=service_account_id,
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_account_id: UUID,
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTAzureSubscription | RESTExceptionInfo]:
    """
    Args:
        service_account_id (UUID):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAzureSubscription | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        service_account_id=service_account_id,
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_account_id: UUID,
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTAzureSubscription | RESTExceptionInfo | None:
    """
    Args:
        service_account_id (UUID):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAzureSubscription | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            service_account_id=service_account_id,
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
