from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_organization_composed import RestOrganizationComposed
from ...types import UNSET, Response


def _get_kwargs(
    *,
    extended_view: bool = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["extendedView"] = extended_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/Organizations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RestOrganizationComposed]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RestOrganizationComposed.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RestOrganizationComposed]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool = True,
) -> Response[RESTExceptionInfo | list[RestOrganizationComposed]]:
    """
    Args:
        extended_view (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RestOrganizationComposed]]
    """

    kwargs = _get_kwargs(
        extended_view=extended_view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool = True,
) -> RESTExceptionInfo | list[RestOrganizationComposed] | None:
    """
    Args:
        extended_view (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RestOrganizationComposed]
    """

    return sync_detailed(
        client=client,
        extended_view=extended_view,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool = True,
) -> Response[RESTExceptionInfo | list[RestOrganizationComposed]]:
    """
    Args:
        extended_view (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RestOrganizationComposed]]
    """

    kwargs = _get_kwargs(
        extended_view=extended_view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool = True,
) -> RESTExceptionInfo | list[RestOrganizationComposed] | None:
    """
    Args:
        extended_view (bool):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RestOrganizationComposed]
    """

    return (
        await asyncio_detailed(
            client=client,
            extended_view=extended_view,
        )
    ).parsed
