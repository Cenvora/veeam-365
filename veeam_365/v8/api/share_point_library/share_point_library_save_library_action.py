from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.share_point_library_save_library_action_response_200 import SharePointLibrarySaveLibraryActionResponse200
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    library_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Libraries/{library_id}/save".format(restore_session_id=quote(str(restore_session_id), safe=""),site_id=quote(str(site_id), safe=""),library_id=quote(str(library_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | SharePointLibrarySaveLibraryActionResponse200:
    if response.status_code == 200:
        response_200 = SharePointLibrarySaveLibraryActionResponse200.from_dict(response.content)



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | SharePointLibrarySaveLibraryActionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    site_id: str,
    library_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | SharePointLibrarySaveLibraryActionResponse200]:
    """ Save SharePoint Library

     Saves a backed-up SharePoint document library with the specified ID.

    SharePoint document libraries are always saved in a ZIP archive. When you save a SharePoint document
    library, the request command archives the document library and places the ZIP archive in a temporary
    folder on the Veeam Backup for Microsoft 365 server. After that, the archive is transferred as
    application/octet-stream media to the client. To download, read or perform other actions with the
    octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        site_id (str):
        library_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | SharePointLibrarySaveLibraryActionResponse200]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
site_id=site_id,
library_id=library_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    site_id: str,
    library_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | SharePointLibrarySaveLibraryActionResponse200 | None:
    """ Save SharePoint Library

     Saves a backed-up SharePoint document library with the specified ID.

    SharePoint document libraries are always saved in a ZIP archive. When you save a SharePoint document
    library, the request command archives the document library and places the ZIP archive in a temporary
    folder on the Veeam Backup for Microsoft 365 server. After that, the archive is transferred as
    application/octet-stream media to the client. To download, read or perform other actions with the
    octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        site_id (str):
        library_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | SharePointLibrarySaveLibraryActionResponse200
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
site_id=site_id,
library_id=library_id,
client=client,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    library_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | SharePointLibrarySaveLibraryActionResponse200]:
    """ Save SharePoint Library

     Saves a backed-up SharePoint document library with the specified ID.

    SharePoint document libraries are always saved in a ZIP archive. When you save a SharePoint document
    library, the request command archives the document library and places the ZIP archive in a temporary
    folder on the Veeam Backup for Microsoft 365 server. After that, the archive is transferred as
    application/octet-stream media to the client. To download, read or perform other actions with the
    octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        site_id (str):
        library_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | SharePointLibrarySaveLibraryActionResponse200]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
site_id=site_id,
library_id=library_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    site_id: str,
    library_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | SharePointLibrarySaveLibraryActionResponse200 | None:
    """ Save SharePoint Library

     Saves a backed-up SharePoint document library with the specified ID.

    SharePoint document libraries are always saved in a ZIP archive. When you save a SharePoint document
    library, the request command archives the document library and places the ZIP archive in a temporary
    folder on the Veeam Backup for Microsoft 365 server. After that, the archive is transferred as
    application/octet-stream media to the client. To download, read or perform other actions with the
    octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        site_id (str):
        library_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | SharePointLibrarySaveLibraryActionResponse200
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
site_id=site_id,
library_id=library_id,
client=client,

    )).parsed
