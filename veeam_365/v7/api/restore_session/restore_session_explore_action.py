from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_explore_options import RESTExploreOptions
from ...models.rest_restore_session import RESTRestoreSession
from ...types import Response


def _get_kwargs(
    *,
    body: RESTExploreOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v7/Organization/Explore",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTRestoreSession:
    if response.status_code == 200:
        response_200 = RESTRestoreSession.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTExploreOptions,
) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    """Create Restore Session for Tenant Organization

     Creates and starts a restore session to explore and restore data of a tenant Microsoft organization.

    To use this resource, make sure to obtain a token using the same credentials that were used to add
    the organization instead of credentials of an administrative account. For organizations with modern
    app-only authentication, obtain a token using an assertion obtained from Microsoft Azure. For more
    information, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization for
    Tenants](https://helpcenter.veeam.com/docs/vbo365/rest/authorization_tenants_section.html?ver=70).

    Args:
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSession]
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
    body: RESTExploreOptions,
) -> RESTExceptionInfo | RESTRestoreSession | None:
    """Create Restore Session for Tenant Organization

     Creates and starts a restore session to explore and restore data of a tenant Microsoft organization.

    To use this resource, make sure to obtain a token using the same credentials that were used to add
    the organization instead of credentials of an administrative account. For organizations with modern
    app-only authentication, obtain a token using an assertion obtained from Microsoft Azure. For more
    information, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization for
    Tenants](https://helpcenter.veeam.com/docs/vbo365/rest/authorization_tenants_section.html?ver=70).

    Args:
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSession
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTExploreOptions,
) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    """Create Restore Session for Tenant Organization

     Creates and starts a restore session to explore and restore data of a tenant Microsoft organization.

    To use this resource, make sure to obtain a token using the same credentials that were used to add
    the organization instead of credentials of an administrative account. For organizations with modern
    app-only authentication, obtain a token using an assertion obtained from Microsoft Azure. For more
    information, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization for
    Tenants](https://helpcenter.veeam.com/docs/vbo365/rest/authorization_tenants_section.html?ver=70).

    Args:
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSession]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RESTExploreOptions,
) -> RESTExceptionInfo | RESTRestoreSession | None:
    """Create Restore Session for Tenant Organization

     Creates and starts a restore session to explore and restore data of a tenant Microsoft organization.

    To use this resource, make sure to obtain a token using the same credentials that were used to add
    the organization instead of credentials of an administrative account. For organizations with modern
    app-only authentication, obtain a token using an assertion obtained from Microsoft Azure. For more
    information, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization for
    Tenants](https://helpcenter.veeam.com/docs/vbo365/rest/authorization_tenants_section.html?ver=70).

    Args:
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSession
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
