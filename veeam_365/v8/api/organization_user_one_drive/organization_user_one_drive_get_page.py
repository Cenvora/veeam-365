from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_one_drive import PageOfRESTOneDrive
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    organization_id: UUID,
    user_id: str,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_set_id: str | Unset = UNSET
    if not isinstance(set_id, Unset):
        json_set_id = str(set_id)
    params["setId"] = json_set_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/Organizations/{organization_id}/Users/{user_id}/OneDrives".format(organization_id=quote(str(organization_id), safe=""),user_id=quote(str(user_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTOneDrive | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTOneDrive.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTOneDrive | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,

) -> Response[PageOfRESTOneDrive | RESTExceptionInfo]:
    r""" Get OneDrives of Organization User

     Returns a collection of an organization user OneDrives. <div class=\"note\"><strong>NOTE</strong>
    </br> A user can have two OneDrives if it is a member of a hybrid Microsoft 365 organization. </div>

    Args:
        organization_id (UUID):
        user_id (str):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTOneDrive | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
user_id=user_id,
limit=limit,
offset=offset,
set_id=set_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    organization_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,

) -> PageOfRESTOneDrive | RESTExceptionInfo | None:
    r""" Get OneDrives of Organization User

     Returns a collection of an organization user OneDrives. <div class=\"note\"><strong>NOTE</strong>
    </br> A user can have two OneDrives if it is a member of a hybrid Microsoft 365 organization. </div>

    Args:
        organization_id (UUID):
        user_id (str):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTOneDrive | RESTExceptionInfo
     """


    return sync_detailed(
        organization_id=organization_id,
user_id=user_id,
client=client,
limit=limit,
offset=offset,
set_id=set_id,

    ).parsed

async def asyncio_detailed(
    organization_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,

) -> Response[PageOfRESTOneDrive | RESTExceptionInfo]:
    r""" Get OneDrives of Organization User

     Returns a collection of an organization user OneDrives. <div class=\"note\"><strong>NOTE</strong>
    </br> A user can have two OneDrives if it is a member of a hybrid Microsoft 365 organization. </div>

    Args:
        organization_id (UUID):
        user_id (str):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTOneDrive | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
user_id=user_id,
limit=limit,
offset=offset,
set_id=set_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    organization_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,

) -> PageOfRESTOneDrive | RESTExceptionInfo | None:
    r""" Get OneDrives of Organization User

     Returns a collection of an organization user OneDrives. <div class=\"note\"><strong>NOTE</strong>
    </br> A user can have two OneDrives if it is a member of a hybrid Microsoft 365 organization. </div>

    Args:
        organization_id (UUID):
        user_id (str):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTOneDrive | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        organization_id=organization_id,
user_id=user_id,
client=client,
limit=limit,
offset=offset,
set_id=set_id,

    )).parsed
