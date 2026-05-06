from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exchange_item_export_item_to_pst_action_response_200 import ExchangeItemExportItemToPstActionResponse200
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_export_to_pst_options import RESTExportToPstOptions
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    mailbox_id: UUID,
    item_id: str,
    *,
    body: RESTExportToPstOptions,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/mailboxes/{mailbox_id}/items/{item_id}/exportToPst".format(restore_session_id=quote(str(restore_session_id), safe=""),mailbox_id=quote(str(mailbox_id), safe=""),item_id=quote(str(item_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExchangeItemExportItemToPstActionResponse200 | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = ExchangeItemExportItemToPstActionResponse200.from_dict(response.content)



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExchangeItemExportItemToPstActionResponse200 | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    mailbox_id: UUID,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExportToPstOptions,

) -> Response[ExchangeItemExportItemToPstActionResponse200 | RESTExceptionInfo]:
    r""" Export Mailbox Item

     Exports a backed-up item with the specified ID to a PST file. <div
    class=\"important\"><strong>IMPORTANT</strong> </br> To export data to PST (Personal Storage Table)
    files, you must have a 64-bit version of Microsoft Outlook 2016, Microsoft Outlook 2013 or Microsoft
    Outlook 2010 installed on a computer running restore sessions. </div>
    The request command will export a backed-up item to a PST file and place it in a temporary folder on
    the Veeam Backup for Microsoft 365 server. After that, the PST file will be transferred as
    application/octet-stream media to the client. To download, read, convert to PST or perform other
    actions with the octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        item_id (str):
        body (RESTExportToPstOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeItemExportItemToPstActionResponse200 | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
item_id=item_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    mailbox_id: UUID,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExportToPstOptions,

) -> ExchangeItemExportItemToPstActionResponse200 | RESTExceptionInfo | None:
    r""" Export Mailbox Item

     Exports a backed-up item with the specified ID to a PST file. <div
    class=\"important\"><strong>IMPORTANT</strong> </br> To export data to PST (Personal Storage Table)
    files, you must have a 64-bit version of Microsoft Outlook 2016, Microsoft Outlook 2013 or Microsoft
    Outlook 2010 installed on a computer running restore sessions. </div>
    The request command will export a backed-up item to a PST file and place it in a temporary folder on
    the Veeam Backup for Microsoft 365 server. After that, the PST file will be transferred as
    application/octet-stream media to the client. To download, read, convert to PST or perform other
    actions with the octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        item_id (str):
        body (RESTExportToPstOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeItemExportItemToPstActionResponse200 | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
item_id=item_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    mailbox_id: UUID,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExportToPstOptions,

) -> Response[ExchangeItemExportItemToPstActionResponse200 | RESTExceptionInfo]:
    r""" Export Mailbox Item

     Exports a backed-up item with the specified ID to a PST file. <div
    class=\"important\"><strong>IMPORTANT</strong> </br> To export data to PST (Personal Storage Table)
    files, you must have a 64-bit version of Microsoft Outlook 2016, Microsoft Outlook 2013 or Microsoft
    Outlook 2010 installed on a computer running restore sessions. </div>
    The request command will export a backed-up item to a PST file and place it in a temporary folder on
    the Veeam Backup for Microsoft 365 server. After that, the PST file will be transferred as
    application/octet-stream media to the client. To download, read, convert to PST or perform other
    actions with the octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        item_id (str):
        body (RESTExportToPstOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeItemExportItemToPstActionResponse200 | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
item_id=item_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    mailbox_id: UUID,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExportToPstOptions,

) -> ExchangeItemExportItemToPstActionResponse200 | RESTExceptionInfo | None:
    r""" Export Mailbox Item

     Exports a backed-up item with the specified ID to a PST file. <div
    class=\"important\"><strong>IMPORTANT</strong> </br> To export data to PST (Personal Storage Table)
    files, you must have a 64-bit version of Microsoft Outlook 2016, Microsoft Outlook 2013 or Microsoft
    Outlook 2010 installed on a computer running restore sessions. </div>
    The request command will export a backed-up item to a PST file and place it in a temporary folder on
    the Veeam Backup for Microsoft 365 server. After that, the PST file will be transferred as
    application/octet-stream media to the client. To download, read, convert to PST or perform other
    actions with the octet-stream, use features of programming languages.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        item_id (str):
        body (RESTExportToPstOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeItemExportItemToPstActionResponse200 | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
item_id=item_id,
client=client,
body=body,

    )).parsed
