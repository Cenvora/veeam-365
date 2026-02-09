from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_organization_composed import RestOrganizationComposed
from ...types import Response


def _get_kwargs(
    *,
    body: RestOrganizationComposed,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v7/Organizations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RestOrganizationComposed:
    if response.status_code == 200:
        response_200 = RestOrganizationComposed.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RestOrganizationComposed]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestOrganizationComposed,
) -> Response[RESTExceptionInfo | RestOrganizationComposed]:
    """Add Organization

     Adds a Microsoft organization to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        body (RestOrganizationComposed):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RestOrganizationComposed]
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
    body: RestOrganizationComposed,
) -> RESTExceptionInfo | RestOrganizationComposed | None:
    """Add Organization

     Adds a Microsoft organization to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        body (RestOrganizationComposed):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RestOrganizationComposed
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestOrganizationComposed,
) -> Response[RESTExceptionInfo | RestOrganizationComposed]:
    """Add Organization

     Adds a Microsoft organization to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        body (RestOrganizationComposed):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RestOrganizationComposed]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestOrganizationComposed,
) -> RESTExceptionInfo | RestOrganizationComposed | None:
    """Add Organization

     Adds a Microsoft organization to the Veeam Backup for Microsoft 365 infrastructure.

    Args:
        body (RestOrganizationComposed):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RestOrganizationComposed
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
