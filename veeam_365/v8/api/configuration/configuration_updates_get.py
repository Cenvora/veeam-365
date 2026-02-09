from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_update_product_config import RESTUpdateProductConfig
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/Configuration/Updates",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTUpdateProductConfig:
    if response.status_code == 200:
        response_200 = RESTUpdateProductConfig.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTUpdateProductConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTUpdateProductConfig]:
    """Get Update Settings

     Returns a resource representation of the Veeam Backup for Microsoft 365 settings for automatic
    updates and notifications on new versions and automatic updates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTUpdateProductConfig]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTUpdateProductConfig | None:
    """Get Update Settings

     Returns a resource representation of the Veeam Backup for Microsoft 365 settings for automatic
    updates and notifications on new versions and automatic updates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTUpdateProductConfig
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTUpdateProductConfig]:
    """Get Update Settings

     Returns a resource representation of the Veeam Backup for Microsoft 365 settings for automatic
    updates and notifications on new versions and automatic updates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTUpdateProductConfig]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTUpdateProductConfig | None:
    """Get Update Settings

     Returns a resource representation of the Veeam Backup for Microsoft 365 settings for automatic
    updates and notifications on new versions and automatic updates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTUpdateProductConfig
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
