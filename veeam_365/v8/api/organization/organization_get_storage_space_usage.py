from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_organization_storage_space_usage import PageOfRESTOrganizationStorageSpaceUsage
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    organization_id: UUID,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/Organizations/{organization_id}/usedRepositories".format(organization_id=quote(str(organization_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTOrganizationStorageSpaceUsage | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTOrganizationStorageSpaceUsage.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTOrganizationStorageSpaceUsage | RESTExceptionInfo]:
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

) -> Response[PageOfRESTOrganizationStorageSpaceUsage | RESTExceptionInfo]:
    """ Get Organization Repositories

     Returns a collection of used backup repositories for an organization with the specified ID.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTOrganizationStorageSpaceUsage | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
limit=limit,
offset=offset,

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

) -> PageOfRESTOrganizationStorageSpaceUsage | RESTExceptionInfo | None:
    """ Get Organization Repositories

     Returns a collection of used backup repositories for an organization with the specified ID.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTOrganizationStorageSpaceUsage | RESTExceptionInfo
     """


    return sync_detailed(
        organization_id=organization_id,
client=client,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[PageOfRESTOrganizationStorageSpaceUsage | RESTExceptionInfo]:
    """ Get Organization Repositories

     Returns a collection of used backup repositories for an organization with the specified ID.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTOrganizationStorageSpaceUsage | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
limit=limit,
offset=offset,

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

) -> PageOfRESTOrganizationStorageSpaceUsage | RESTExceptionInfo | None:
    """ Get Organization Repositories

     Returns a collection of used backup repositories for an organization with the specified ID.

    Args:
        organization_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTOrganizationStorageSpaceUsage | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        organization_id=organization_id,
client=client,
limit=limit,
offset=offset,

    )).parsed
