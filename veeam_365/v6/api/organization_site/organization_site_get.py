from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.organization_site_get_location_filter import OrganizationSiteGetLocationFilter
from ...models.page_of_rest_site import PageOfRESTSite
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: UUID,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    include_personal_sites: bool | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    location_filter: OrganizationSiteGetLocationFilter | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_set_id: str | Unset = UNSET
    if not isinstance(set_id, Unset):
        json_set_id = str(set_id)
    params["setId"] = json_set_id

    params["includePersonalSites"] = include_personal_sites

    params["parentId"] = parent_id

    json_location_filter: str | Unset = UNSET
    if not isinstance(location_filter, Unset):
        json_location_filter = location_filter.value

    params["locationFilter"] = json_location_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/Organizations/{organization_id}/Sites".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTSite | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTSite.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTSite | RESTExceptionInfo]:
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    include_personal_sites: bool | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    location_filter: OrganizationSiteGetLocationFilter | Unset = UNSET,
) -> Response[PageOfRESTSite | RESTExceptionInfo]:
    """
    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        include_personal_sites (bool | Unset):
        parent_id (str | Unset):
        location_filter (OrganizationSiteGetLocationFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTSite | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        limit=limit,
        offset=offset,
        set_id=set_id,
        include_personal_sites=include_personal_sites,
        parent_id=parent_id,
        location_filter=location_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    include_personal_sites: bool | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    location_filter: OrganizationSiteGetLocationFilter | Unset = UNSET,
) -> PageOfRESTSite | RESTExceptionInfo | None:
    """
    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        include_personal_sites (bool | Unset):
        parent_id (str | Unset):
        location_filter (OrganizationSiteGetLocationFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTSite | RESTExceptionInfo
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        limit=limit,
        offset=offset,
        set_id=set_id,
        include_personal_sites=include_personal_sites,
        parent_id=parent_id,
        location_filter=location_filter,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    include_personal_sites: bool | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    location_filter: OrganizationSiteGetLocationFilter | Unset = UNSET,
) -> Response[PageOfRESTSite | RESTExceptionInfo]:
    """
    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        include_personal_sites (bool | Unset):
        parent_id (str | Unset):
        location_filter (OrganizationSiteGetLocationFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTSite | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        limit=limit,
        offset=offset,
        set_id=set_id,
        include_personal_sites=include_personal_sites,
        parent_id=parent_id,
        location_filter=location_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    include_personal_sites: bool | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    location_filter: OrganizationSiteGetLocationFilter | Unset = UNSET,
) -> PageOfRESTSite | RESTExceptionInfo | None:
    """
    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        include_personal_sites (bool | Unset):
        parent_id (str | Unset):
        location_filter (OrganizationSiteGetLocationFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTSite | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            limit=limit,
            offset=offset,
            set_id=set_id,
            include_personal_sites=include_personal_sites,
            parent_id=parent_id,
            location_filter=location_filter,
        )
    ).parsed
