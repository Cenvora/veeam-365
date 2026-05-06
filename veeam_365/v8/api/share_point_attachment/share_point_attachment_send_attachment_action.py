from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_send_as_msg_options import RESTSendAsMsgOptions
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    attachment_id: str,
    *,
    body: RESTSendAsMsgOptions,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Items/{item_id}/Attachments/{attachment_id}/send".format(restore_session_id=quote(str(restore_session_id), safe=""),site_id=quote(str(site_id), safe=""),item_id=quote(str(item_id), safe=""),attachment_id=quote(str(attachment_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RESTExceptionInfo:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | RESTExceptionInfo]:
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
    body: RESTSendAsMsgOptions,

) -> Response[Any | RESTExceptionInfo]:
    r""" Send SharePoint Attachment

     Sends a backed-up SharePoint item attachment with the specified ID as an attachment in an email
    message. <div class=\"note\"><strong>NOTE</strong> </br> To send items as attachments, you must
    specify the Veeam Explorer for Microsoft SharePoint email settings. For more information, see [Edit
    Email Settings](#/VespEmailSettings/VespEmailSettings_Update). </div>

    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        attachment_id (str):
        body (RESTSendAsMsgOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
site_id=site_id,
item_id=item_id,
attachment_id=attachment_id,
body=body,

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
    body: RESTSendAsMsgOptions,

) -> Any | RESTExceptionInfo | None:
    r""" Send SharePoint Attachment

     Sends a backed-up SharePoint item attachment with the specified ID as an attachment in an email
    message. <div class=\"note\"><strong>NOTE</strong> </br> To send items as attachments, you must
    specify the Veeam Explorer for Microsoft SharePoint email settings. For more information, see [Edit
    Email Settings](#/VespEmailSettings/VespEmailSettings_Update). </div>

    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        attachment_id (str):
        body (RESTSendAsMsgOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
site_id=site_id,
item_id=item_id,
attachment_id=attachment_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSendAsMsgOptions,

) -> Response[Any | RESTExceptionInfo]:
    r""" Send SharePoint Attachment

     Sends a backed-up SharePoint item attachment with the specified ID as an attachment in an email
    message. <div class=\"note\"><strong>NOTE</strong> </br> To send items as attachments, you must
    specify the Veeam Explorer for Microsoft SharePoint email settings. For more information, see [Edit
    Email Settings](#/VespEmailSettings/VespEmailSettings_Update). </div>

    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        attachment_id (str):
        body (RESTSendAsMsgOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
site_id=site_id,
item_id=item_id,
attachment_id=attachment_id,
body=body,

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
    body: RESTSendAsMsgOptions,

) -> Any | RESTExceptionInfo | None:
    r""" Send SharePoint Attachment

     Sends a backed-up SharePoint item attachment with the specified ID as an attachment in an email
    message. <div class=\"note\"><strong>NOTE</strong> </br> To send items as attachments, you must
    specify the Veeam Explorer for Microsoft SharePoint email settings. For more information, see [Edit
    Email Settings](#/VespEmailSettings/VespEmailSettings_Update). </div>

    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        attachment_id (str):
        body (RESTSendAsMsgOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
site_id=site_id,
item_id=item_id,
attachment_id=attachment_id,
client=client,
body=body,

    )).parsed
