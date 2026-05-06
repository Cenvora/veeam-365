from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_share_point_attachment import RESTSharePointAttachment
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    attachment_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Items/{item_id}/Attachments/{attachment_id}".format(restore_session_id=quote(str(restore_session_id), safe=""),site_id=quote(str(site_id), safe=""),item_id=quote(str(item_id), safe=""),attachment_id=quote(str(attachment_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTSharePointAttachment:
    if response.status_code == 200:
        response_200 = RESTSharePointAttachment.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTSharePointAttachment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | RESTSharePointAttachment]:
    """ Get SharePoint Attachment

     Returns a resource representation of a backed-up SharePoint item attachment with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTSharePointAttachment]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
site_id=site_id,
item_id=item_id,
attachment_id=attachment_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTSharePointAttachment | None:
    """ Get SharePoint Attachment

     Returns a resource representation of a backed-up SharePoint item attachment with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTSharePointAttachment
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
site_id=site_id,
item_id=item_id,
attachment_id=attachment_id,
client=client,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | RESTSharePointAttachment]:
    """ Get SharePoint Attachment

     Returns a resource representation of a backed-up SharePoint item attachment with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTSharePointAttachment]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
site_id=site_id,
item_id=item_id,
attachment_id=attachment_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTSharePointAttachment | None:
    """ Get SharePoint Attachment

     Returns a resource representation of a backed-up SharePoint item attachment with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTSharePointAttachment
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
site_id=site_id,
item_id=item_id,
attachment_id=attachment_id,
client=client,

    )).parsed
