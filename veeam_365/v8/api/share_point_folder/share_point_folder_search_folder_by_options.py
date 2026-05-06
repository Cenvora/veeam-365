from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_item_composed import PageOfRESTItemComposed
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.restvesp_search_options import RESTVESPSearchOptions
from ...models.share_point_folder_search_folder_by_options_item_type import SharePointFolderSearchFolderByOptionsItemType
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    body: RESTVESPSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    item_type: SharePointFolderSearchFolderByOptionsItemType | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    json_set_id: str | Unset = UNSET
    if not isinstance(set_id, Unset):
        json_set_id = str(set_id)
    params["setId"] = json_set_id

    json_item_type: str | Unset = UNSET
    if not isinstance(item_type, Unset):
        json_item_type = item_type.value

    params["itemType"] = json_item_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Folders/{folder_id}/search".format(restore_session_id=quote(str(restore_session_id), safe=""),site_id=quote(str(site_id), safe=""),folder_id=quote(str(folder_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTItemComposed | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTItemComposed.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTItemComposed | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTVESPSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    item_type: SharePointFolderSearchFolderByOptionsItemType | Unset = UNSET,

) -> Response[PageOfRESTItemComposed | RESTExceptionInfo]:
    """ Search for SharePoint Documents in SharePoint Folder

     Searches for SharePoint documents in a backed-up SharePoint folder with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        item_type (SharePointFolderSearchFolderByOptionsItemType | Unset):
        body (RESTVESPSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTItemComposed | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
site_id=site_id,
folder_id=folder_id,
body=body,
offset=offset,
limit=limit,
set_id=set_id,
item_type=item_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTVESPSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    item_type: SharePointFolderSearchFolderByOptionsItemType | Unset = UNSET,

) -> PageOfRESTItemComposed | RESTExceptionInfo | None:
    """ Search for SharePoint Documents in SharePoint Folder

     Searches for SharePoint documents in a backed-up SharePoint folder with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        item_type (SharePointFolderSearchFolderByOptionsItemType | Unset):
        body (RESTVESPSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTItemComposed | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
site_id=site_id,
folder_id=folder_id,
client=client,
body=body,
offset=offset,
limit=limit,
set_id=set_id,
item_type=item_type,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTVESPSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    item_type: SharePointFolderSearchFolderByOptionsItemType | Unset = UNSET,

) -> Response[PageOfRESTItemComposed | RESTExceptionInfo]:
    """ Search for SharePoint Documents in SharePoint Folder

     Searches for SharePoint documents in a backed-up SharePoint folder with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        item_type (SharePointFolderSearchFolderByOptionsItemType | Unset):
        body (RESTVESPSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTItemComposed | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
site_id=site_id,
folder_id=folder_id,
body=body,
offset=offset,
limit=limit,
set_id=set_id,
item_type=item_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTVESPSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    item_type: SharePointFolderSearchFolderByOptionsItemType | Unset = UNSET,

) -> PageOfRESTItemComposed | RESTExceptionInfo | None:
    """ Search for SharePoint Documents in SharePoint Folder

     Searches for SharePoint documents in a backed-up SharePoint folder with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        item_type (SharePointFolderSearchFolderByOptionsItemType | Unset):
        body (RESTVESPSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTItemComposed | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
site_id=site_id,
folder_id=folder_id,
client=client,
body=body,
offset=offset,
limit=limit,
set_id=set_id,
item_type=item_type,

    )).parsed
