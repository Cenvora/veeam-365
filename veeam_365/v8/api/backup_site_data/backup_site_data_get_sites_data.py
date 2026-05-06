from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_backup_site_data import PageOfRESTBackupSiteData
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    repository_id: UUID,
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
        "url": "/v8/BackupRepositories/{repository_id}/SiteData".format(repository_id=quote(str(repository_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTBackupSiteData | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTBackupSiteData.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTBackupSiteData | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[PageOfRESTBackupSiteData | RESTExceptionInfo]:
    """ Get SharePoint Data by Repository ID

     Returns a collection of backed-up SharePoint sites whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupSiteData | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        repository_id=repository_id,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> PageOfRESTBackupSiteData | RESTExceptionInfo | None:
    """ Get SharePoint Data by Repository ID

     Returns a collection of backed-up SharePoint sites whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupSiteData | RESTExceptionInfo
     """


    return sync_detailed(
        repository_id=repository_id,
client=client,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[PageOfRESTBackupSiteData | RESTExceptionInfo]:
    """ Get SharePoint Data by Repository ID

     Returns a collection of backed-up SharePoint sites whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupSiteData | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        repository_id=repository_id,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> PageOfRESTBackupSiteData | RESTExceptionInfo | None:
    """ Get SharePoint Data by Repository ID

     Returns a collection of backed-up SharePoint sites whose data is stored in a backup repository with
    the specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupSiteData | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        repository_id=repository_id,
client=client,
limit=limit,
offset=offset,

    )).parsed
