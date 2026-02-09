from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_smtp_settings_from_client import RestSmtpSettingsFromClient
from ...types import Response


def _get_kwargs(
    *,
    body: RestSmtpSettingsFromClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v7/VexEmailSettings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestSmtpSettingsFromClient,
) -> Response[Any | RESTExceptionInfo]:
    """Edit Email Notification Settings

     Modifies email notification settings for Veeam Explorer for Microsoft Exchange.

    Args:
        body (RestSmtpSettingsFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
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
    body: RestSmtpSettingsFromClient,
) -> Any | RESTExceptionInfo | None:
    """Edit Email Notification Settings

     Modifies email notification settings for Veeam Explorer for Microsoft Exchange.

    Args:
        body (RestSmtpSettingsFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestSmtpSettingsFromClient,
) -> Response[Any | RESTExceptionInfo]:
    """Edit Email Notification Settings

     Modifies email notification settings for Veeam Explorer for Microsoft Exchange.

    Args:
        body (RestSmtpSettingsFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestSmtpSettingsFromClient,
) -> Any | RESTExceptionInfo | None:
    """Edit Email Notification Settings

     Modifies email notification settings for Veeam Explorer for Microsoft Exchange.

    Args:
        body (RestSmtpSettingsFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
