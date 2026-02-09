from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_organization_composed import RestOrganizationComposed
from ...types import UNSET, Response


def _get_kwargs(
    organization_id: UUID,
    *,
    extended_view: bool = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["extendedView"] = extended_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/Organizations/{organization_id}".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
        "params": params,
    }

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
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool = True,
) -> Response[RESTExceptionInfo | RestOrganizationComposed]:
    """
    Args:
        organization_id (UUID):
        extended_view (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RestOrganizationComposed]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        extended_view=extended_view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool = True,
) -> RESTExceptionInfo | RestOrganizationComposed | None:
    """
    Args:
        organization_id (UUID):
        extended_view (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RestOrganizationComposed
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        extended_view=extended_view,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool = True,
) -> Response[RESTExceptionInfo | RestOrganizationComposed]:
    """
    Args:
        organization_id (UUID):
        extended_view (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RestOrganizationComposed]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        extended_view=extended_view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool = True,
) -> RESTExceptionInfo | RestOrganizationComposed | None:
    """
    Args:
        organization_id (UUID):
        extended_view (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RestOrganizationComposed
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            extended_view=extended_view,
        )
    ).parsed
