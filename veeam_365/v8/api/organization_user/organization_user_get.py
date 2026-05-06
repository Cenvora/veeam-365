from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.organization_user_get_data_source import OrganizationUserGetDataSource
from ...models.organization_user_get_detected_sku_type import OrganizationUserGetDetectedSkuType
from ...models.organization_user_get_location_filter import OrganizationUserGetLocationFilter
from ...models.page_of_rest_user import PageOfRESTUser
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
    user_name: str | Unset = UNSET,
    display_name: str | Unset = UNSET,
    location_filter: OrganizationUserGetLocationFilter | Unset = UNSET,
    data_source: OrganizationUserGetDataSource | Unset = UNSET,
    detected_sku_type: OrganizationUserGetDetectedSkuType | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_set_id: str | Unset = UNSET
    if not isinstance(set_id, Unset):
        json_set_id = str(set_id)
    params["setId"] = json_set_id

    params["userName"] = user_name

    params["displayName"] = display_name

    json_location_filter: str | Unset = UNSET
    if not isinstance(location_filter, Unset):
        json_location_filter = location_filter.value

    params["locationFilter"] = json_location_filter

    json_data_source: str | Unset = UNSET
    if not isinstance(data_source, Unset):
        json_data_source = data_source.value

    params["dataSource"] = json_data_source

    json_detected_sku_type: str | Unset = UNSET
    if not isinstance(detected_sku_type, Unset):
        json_detected_sku_type = detected_sku_type.value

    params["detectedSkuType"] = json_detected_sku_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/Organizations/{organization_id}/Users".format(organization_id=quote(str(organization_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTUser | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTUser.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTUser | RESTExceptionInfo]:
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
    user_name: str | Unset = UNSET,
    display_name: str | Unset = UNSET,
    location_filter: OrganizationUserGetLocationFilter | Unset = UNSET,
    data_source: OrganizationUserGetDataSource | Unset = UNSET,
    detected_sku_type: OrganizationUserGetDetectedSkuType | Unset = UNSET,

) -> Response[PageOfRESTUser | RESTExceptionInfo]:
    """ Get Organization Users

     Returns a collection of organization users.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        user_name (str | Unset):
        display_name (str | Unset):
        location_filter (OrganizationUserGetLocationFilter | Unset):
        data_source (OrganizationUserGetDataSource | Unset):
        detected_sku_type (OrganizationUserGetDetectedSkuType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTUser | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
limit=limit,
offset=offset,
set_id=set_id,
user_name=user_name,
display_name=display_name,
location_filter=location_filter,
data_source=data_source,
detected_sku_type=detected_sku_type,

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
    user_name: str | Unset = UNSET,
    display_name: str | Unset = UNSET,
    location_filter: OrganizationUserGetLocationFilter | Unset = UNSET,
    data_source: OrganizationUserGetDataSource | Unset = UNSET,
    detected_sku_type: OrganizationUserGetDetectedSkuType | Unset = UNSET,

) -> PageOfRESTUser | RESTExceptionInfo | None:
    """ Get Organization Users

     Returns a collection of organization users.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        user_name (str | Unset):
        display_name (str | Unset):
        location_filter (OrganizationUserGetLocationFilter | Unset):
        data_source (OrganizationUserGetDataSource | Unset):
        detected_sku_type (OrganizationUserGetDetectedSkuType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTUser | RESTExceptionInfo
     """


    return sync_detailed(
        organization_id=organization_id,
client=client,
limit=limit,
offset=offset,
set_id=set_id,
user_name=user_name,
display_name=display_name,
location_filter=location_filter,
data_source=data_source,
detected_sku_type=detected_sku_type,

    ).parsed

async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    user_name: str | Unset = UNSET,
    display_name: str | Unset = UNSET,
    location_filter: OrganizationUserGetLocationFilter | Unset = UNSET,
    data_source: OrganizationUserGetDataSource | Unset = UNSET,
    detected_sku_type: OrganizationUserGetDetectedSkuType | Unset = UNSET,

) -> Response[PageOfRESTUser | RESTExceptionInfo]:
    """ Get Organization Users

     Returns a collection of organization users.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        user_name (str | Unset):
        display_name (str | Unset):
        location_filter (OrganizationUserGetLocationFilter | Unset):
        data_source (OrganizationUserGetDataSource | Unset):
        detected_sku_type (OrganizationUserGetDetectedSkuType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTUser | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
limit=limit,
offset=offset,
set_id=set_id,
user_name=user_name,
display_name=display_name,
location_filter=location_filter,
data_source=data_source,
detected_sku_type=detected_sku_type,

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
    user_name: str | Unset = UNSET,
    display_name: str | Unset = UNSET,
    location_filter: OrganizationUserGetLocationFilter | Unset = UNSET,
    data_source: OrganizationUserGetDataSource | Unset = UNSET,
    detected_sku_type: OrganizationUserGetDetectedSkuType | Unset = UNSET,

) -> PageOfRESTUser | RESTExceptionInfo | None:
    """ Get Organization Users

     Returns a collection of organization users.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):
        user_name (str | Unset):
        display_name (str | Unset):
        location_filter (OrganizationUserGetLocationFilter | Unset):
        data_source (OrganizationUserGetDataSource | Unset):
        detected_sku_type (OrganizationUserGetDetectedSkuType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTUser | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        organization_id=organization_id,
client=client,
limit=limit,
offset=offset,
set_id=set_id,
user_name=user_name,
display_name=display_name,
location_filter=location_filter,
data_source=data_source,
detected_sku_type=detected_sku_type,

    )).parsed
