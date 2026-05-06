from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_organization_composed import PageOfRestOrganizationComposed
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    extended_view: bool | Unset = False,
    msid: UUID | Unset = UNSET,
    backed_up_organization_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["extendedView"] = extended_view

    json_msid: str | Unset = UNSET
    if not isinstance(msid, Unset):
        json_msid = str(msid)
    params["msid"] = json_msid

    params["backedUpOrganizationId"] = backed_up_organization_id

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/Organizations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRestOrganizationComposed | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRestOrganizationComposed.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRestOrganizationComposed | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool | Unset = False,
    msid: UUID | Unset = UNSET,
    backed_up_organization_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[PageOfRestOrganizationComposed | RESTExceptionInfo]:
    """ Get Organizations

     Returns a collection of Microsoft organizations added to the Veeam Backup for Microsoft 365
    infrastructure.

    Args:
        extended_view (bool | Unset):  Default: False.
        msid (UUID | Unset):
        backed_up_organization_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRestOrganizationComposed | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        extended_view=extended_view,
msid=msid,
backed_up_organization_id=backed_up_organization_id,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool | Unset = False,
    msid: UUID | Unset = UNSET,
    backed_up_organization_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> PageOfRestOrganizationComposed | RESTExceptionInfo | None:
    """ Get Organizations

     Returns a collection of Microsoft organizations added to the Veeam Backup for Microsoft 365
    infrastructure.

    Args:
        extended_view (bool | Unset):  Default: False.
        msid (UUID | Unset):
        backed_up_organization_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRestOrganizationComposed | RESTExceptionInfo
     """


    return sync_detailed(
        client=client,
extended_view=extended_view,
msid=msid,
backed_up_organization_id=backed_up_organization_id,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool | Unset = False,
    msid: UUID | Unset = UNSET,
    backed_up_organization_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[PageOfRestOrganizationComposed | RESTExceptionInfo]:
    """ Get Organizations

     Returns a collection of Microsoft organizations added to the Veeam Backup for Microsoft 365
    infrastructure.

    Args:
        extended_view (bool | Unset):  Default: False.
        msid (UUID | Unset):
        backed_up_organization_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRestOrganizationComposed | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        extended_view=extended_view,
msid=msid,
backed_up_organization_id=backed_up_organization_id,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    extended_view: bool | Unset = False,
    msid: UUID | Unset = UNSET,
    backed_up_organization_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> PageOfRestOrganizationComposed | RESTExceptionInfo | None:
    """ Get Organizations

     Returns a collection of Microsoft organizations added to the Veeam Backup for Microsoft 365
    infrastructure.

    Args:
        extended_view (bool | Unset):  Default: False.
        msid (UUID | Unset):
        backed_up_organization_id (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRestOrganizationComposed | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        client=client,
extended_view=extended_view,
msid=msid,
backed_up_organization_id=backed_up_organization_id,
limit=limit,
offset=offset,

    )).parsed
