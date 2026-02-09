from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_logged_in_organization import RESTLoggedInOrganization
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/Organization",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTLoggedInOrganization:
    if response.status_code == 200:
        response_200 = RESTLoggedInOrganization.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTLoggedInOrganization]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTLoggedInOrganization]:
    """Get Tenant Organization

     Returns information about Microsoft 365 and on-premises Microsoft organizations that were added as
    tenants by service providers.

    To use this resource, make sure to obtain a token using the same credentials that were used to add
    the organization instead of credentials of an administrative account. For more information on how to
    obtain a token, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization
    for Organizations with Modern Authentication and Legacy Protocols or Basic Authentication](https://h
    elpcenter.veeam.com/docs/vbo365/rest/authorization_basic_legacy.html?ver=70).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTLoggedInOrganization]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTLoggedInOrganization | None:
    """Get Tenant Organization

     Returns information about Microsoft 365 and on-premises Microsoft organizations that were added as
    tenants by service providers.

    To use this resource, make sure to obtain a token using the same credentials that were used to add
    the organization instead of credentials of an administrative account. For more information on how to
    obtain a token, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization
    for Organizations with Modern Authentication and Legacy Protocols or Basic Authentication](https://h
    elpcenter.veeam.com/docs/vbo365/rest/authorization_basic_legacy.html?ver=70).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTLoggedInOrganization
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTLoggedInOrganization]:
    """Get Tenant Organization

     Returns information about Microsoft 365 and on-premises Microsoft organizations that were added as
    tenants by service providers.

    To use this resource, make sure to obtain a token using the same credentials that were used to add
    the organization instead of credentials of an administrative account. For more information on how to
    obtain a token, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization
    for Organizations with Modern Authentication and Legacy Protocols or Basic Authentication](https://h
    elpcenter.veeam.com/docs/vbo365/rest/authorization_basic_legacy.html?ver=70).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTLoggedInOrganization]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTLoggedInOrganization | None:
    """Get Tenant Organization

     Returns information about Microsoft 365 and on-premises Microsoft organizations that were added as
    tenants by service providers.

    To use this resource, make sure to obtain a token using the same credentials that were used to add
    the organization instead of credentials of an administrative account. For more information on how to
    obtain a token, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization
    for Organizations with Modern Authentication and Legacy Protocols or Basic Authentication](https://h
    elpcenter.veeam.com/docs/vbo365/rest/authorization_basic_legacy.html?ver=70).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTLoggedInOrganization
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
