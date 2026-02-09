from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_license_usage import RESTLicenseUsage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform_id: UUID | Unset = UNSET,
    organization_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_platform_id: str | Unset = UNSET
    if not isinstance(platform_id, Unset):
        json_platform_id = str(platform_id)
    params["platformId"] = json_platform_id

    params["organizationId"] = organization_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/licensing/statistic/usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTLicenseUsage:
    if response.status_code == 200:
        response_200 = RESTLicenseUsage.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTLicenseUsage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform_id: UUID | Unset = UNSET,
    organization_id: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | RESTLicenseUsage]:
    """Get License Usage by Organization ID

     Returns a resource representation of the license usage for a Microsoft organization with the
    specified ID.

    Args:
        platform_id (UUID | Unset):
        organization_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTLicenseUsage]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
        organization_id=organization_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    platform_id: UUID | Unset = UNSET,
    organization_id: str | Unset = UNSET,
) -> RESTExceptionInfo | RESTLicenseUsage | None:
    """Get License Usage by Organization ID

     Returns a resource representation of the license usage for a Microsoft organization with the
    specified ID.

    Args:
        platform_id (UUID | Unset):
        organization_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTLicenseUsage
    """

    return sync_detailed(
        client=client,
        platform_id=platform_id,
        organization_id=organization_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform_id: UUID | Unset = UNSET,
    organization_id: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | RESTLicenseUsage]:
    """Get License Usage by Organization ID

     Returns a resource representation of the license usage for a Microsoft organization with the
    specified ID.

    Args:
        platform_id (UUID | Unset):
        organization_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTLicenseUsage]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
        organization_id=organization_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    platform_id: UUID | Unset = UNSET,
    organization_id: str | Unset = UNSET,
) -> RESTExceptionInfo | RESTLicenseUsage | None:
    """Get License Usage by Organization ID

     Returns a resource representation of the license usage for a Microsoft organization with the
    specified ID.

    Args:
        platform_id (UUID | Unset):
        organization_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTLicenseUsage
    """

    return (
        await asyncio_detailed(
            client=client,
            platform_id=platform_id,
            organization_id=organization_id,
        )
    ).parsed
