from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_share_point_document import PageOfRESTSharePointDocument
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    document_id: str,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Documents/{document_id}/Versions".format(restore_session_id=quote(str(restore_session_id), safe=""),site_id=quote(str(site_id), safe=""),document_id=quote(str(document_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTSharePointDocument | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTSharePointDocument.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTSharePointDocument | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    site_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[PageOfRESTSharePointDocument | RESTExceptionInfo]:
    """ Get Previous Versions of SharePoint Document

     Returns a collection of versions of a backed-up SharePoint document with the specified ID.

    When you get SharePoint document versions, the server returns information about previous versions of
    the document. To get the latest version, use either [Get SharePoint
    Document](#/SharePointDocument/SharePointDocument_GetById) or [Get Specific Version of SharePoint
    Document](#/SharePointDocument/SharePointDocument_GetByIdByVersionId).

    Args:
        restore_session_id (UUID):
        site_id (str):
        document_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTSharePointDocument | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
site_id=site_id,
document_id=document_id,
offset=offset,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    site_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> PageOfRESTSharePointDocument | RESTExceptionInfo | None:
    """ Get Previous Versions of SharePoint Document

     Returns a collection of versions of a backed-up SharePoint document with the specified ID.

    When you get SharePoint document versions, the server returns information about previous versions of
    the document. To get the latest version, use either [Get SharePoint
    Document](#/SharePointDocument/SharePointDocument_GetById) or [Get Specific Version of SharePoint
    Document](#/SharePointDocument/SharePointDocument_GetByIdByVersionId).

    Args:
        restore_session_id (UUID):
        site_id (str):
        document_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTSharePointDocument | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
site_id=site_id,
document_id=document_id,
client=client,
offset=offset,
limit=limit,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[PageOfRESTSharePointDocument | RESTExceptionInfo]:
    """ Get Previous Versions of SharePoint Document

     Returns a collection of versions of a backed-up SharePoint document with the specified ID.

    When you get SharePoint document versions, the server returns information about previous versions of
    the document. To get the latest version, use either [Get SharePoint
    Document](#/SharePointDocument/SharePointDocument_GetById) or [Get Specific Version of SharePoint
    Document](#/SharePointDocument/SharePointDocument_GetByIdByVersionId).

    Args:
        restore_session_id (UUID):
        site_id (str):
        document_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTSharePointDocument | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
site_id=site_id,
document_id=document_id,
offset=offset,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    site_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> PageOfRESTSharePointDocument | RESTExceptionInfo | None:
    """ Get Previous Versions of SharePoint Document

     Returns a collection of versions of a backed-up SharePoint document with the specified ID.

    When you get SharePoint document versions, the server returns information about previous versions of
    the document. To get the latest version, use either [Get SharePoint
    Document](#/SharePointDocument/SharePointDocument_GetById) or [Get Specific Version of SharePoint
    Document](#/SharePointDocument/SharePointDocument_GetByIdByVersionId).

    Args:
        restore_session_id (UUID):
        site_id (str):
        document_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTSharePointDocument | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
site_id=site_id,
document_id=document_id,
client=client,
offset=offset,
limit=limit,

    )).parsed
