from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_device_code_info import RESTDeviceCodeInfo
from ...models.rest_device_code_info_request import RESTDeviceCodeInfoRequest
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    *,
    body: RESTDeviceCodeInfoRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/AzureServiceAccounts/DeviceCode",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTDeviceCodeInfo | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTDeviceCodeInfo.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTDeviceCodeInfo | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTDeviceCodeInfoRequest,
) -> Response[RESTDeviceCodeInfo | RESTExceptionInfo]:
    """Get Device Code

     Allows you to obtain a device code to sign in to Microsoft Identity platform.

    Args:
        body (RESTDeviceCodeInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTDeviceCodeInfo | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RESTDeviceCodeInfoRequest,
) -> RESTDeviceCodeInfo | RESTExceptionInfo | None:
    """Get Device Code

     Allows you to obtain a device code to sign in to Microsoft Identity platform.

    Args:
        body (RESTDeviceCodeInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTDeviceCodeInfo | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTDeviceCodeInfoRequest,
) -> Response[RESTDeviceCodeInfo | RESTExceptionInfo]:
    """Get Device Code

     Allows you to obtain a device code to sign in to Microsoft Identity platform.

    Args:
        body (RESTDeviceCodeInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTDeviceCodeInfo | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RESTDeviceCodeInfoRequest,
) -> RESTDeviceCodeInfo | RESTExceptionInfo | None:
    """Get Device Code

     Allows you to obtain a device code to sign in to Microsoft Identity platform.

    Args:
        body (RESTDeviceCodeInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTDeviceCodeInfo | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
