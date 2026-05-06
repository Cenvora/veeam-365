from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.organization_group_get_data_source import OrganizationGroupGetDataSource
from ...models.organization_group_get_location_filter import OrganizationGroupGetLocationFilter
from ...models.page_of_rest_group import PageOfRESTGroup
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    organization_id: UUID,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    display_name: str | Unset = UNSET,
    group_name: str | Unset = UNSET,
    location_filter: OrganizationGroupGetLocationFilter | Unset = UNSET,
    data_source: OrganizationGroupGetDataSource | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_set_id: str | Unset = UNSET
    if not isinstance(set_id, Unset):
        json_set_id = str(set_id)
    params["setId"] = json_set_id

    params["displayName"] = display_name

    params["groupName"] = group_name

    json_location_filter: str | Unset = UNSET
    if not isinstance(location_filter, Unset):
        json_location_filter = location_filter.value

    params["locationFilter"] = json_location_filter

    json_data_source: str | Unset = UNSET
    if not isinstance(data_source, Unset):
        json_data_source = data_source.value

    params["dataSource"] = json_data_source


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/Organizations/{organization_id}/Groups".format(organization_id=quote(str(organization_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTGroup | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTGroup.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTGroup | RESTExceptionInfo]:
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
    display_name: str | Unset = UNSET,
    group_name: str | Unset = UNSET,
    location_filter: OrganizationGroupGetLocationFilter | Unset = UNSET,
    data_source: OrganizationGroupGetDataSource | Unset = UNSET,

) -> Response[PageOfRESTGroup | RESTExceptionInfo]:
    """ Get Organization Groups

     Returns a collection of organization groups.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        display_name (str | Unset):
        group_name (str | Unset):
        location_filter (OrganizationGroupGetLocationFilter | Unset):
        data_source (OrganizationGroupGetDataSource | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTGroup | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
limit=limit,
offset=offset,
set_id=set_id,
display_name=display_name,
group_name=group_name,
location_filter=location_filter,
data_source=data_source,

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
    display_name: str | Unset = UNSET,
    group_name: str | Unset = UNSET,
    location_filter: OrganizationGroupGetLocationFilter | Unset = UNSET,
    data_source: OrganizationGroupGetDataSource | Unset = UNSET,

) -> PageOfRESTGroup | RESTExceptionInfo | None:
    """ Get Organization Groups

     Returns a collection of organization groups.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        display_name (str | Unset):
        group_name (str | Unset):
        location_filter (OrganizationGroupGetLocationFilter | Unset):
        data_source (OrganizationGroupGetDataSource | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTGroup | RESTExceptionInfo
     """


    return sync_detailed(
        organization_id=organization_id,
client=client,
limit=limit,
offset=offset,
set_id=set_id,
display_name=display_name,
group_name=group_name,
location_filter=location_filter,
data_source=data_source,

    ).parsed

async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    display_name: str | Unset = UNSET,
    group_name: str | Unset = UNSET,
    location_filter: OrganizationGroupGetLocationFilter | Unset = UNSET,
    data_source: OrganizationGroupGetDataSource | Unset = UNSET,

) -> Response[PageOfRESTGroup | RESTExceptionInfo]:
    """ Get Organization Groups

     Returns a collection of organization groups.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        display_name (str | Unset):
        group_name (str | Unset):
        location_filter (OrganizationGroupGetLocationFilter | Unset):
        data_source (OrganizationGroupGetDataSource | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTGroup | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
limit=limit,
offset=offset,
set_id=set_id,
display_name=display_name,
group_name=group_name,
location_filter=location_filter,
data_source=data_source,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    display_name: str | Unset = UNSET,
    group_name: str | Unset = UNSET,
    location_filter: OrganizationGroupGetLocationFilter | Unset = UNSET,
    data_source: OrganizationGroupGetDataSource | Unset = UNSET,

) -> PageOfRESTGroup | RESTExceptionInfo | None:
    """ Get Organization Groups

     Returns a collection of organization groups.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        display_name (str | Unset):
        group_name (str | Unset):
        location_filter (OrganizationGroupGetLocationFilter | Unset):
        data_source (OrganizationGroupGetDataSource | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTGroup | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        organization_id=organization_id,
client=client,
limit=limit,
offset=offset,
set_id=set_id,
display_name=display_name,
group_name=group_name,
location_filter=location_filter,
data_source=data_source,

    )).parsed
