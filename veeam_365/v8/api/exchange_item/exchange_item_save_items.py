from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exchange_item_save_items_response_200 import ExchangeItemSaveItemsResponse200
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_save_to_msg_options import RESTSaveToMsgOptions
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    body: RESTSaveToMsgOptions,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/mailboxes/{mailbox_id}/items/Save".format(restore_session_id=quote(str(restore_session_id), safe=""),mailbox_id=quote(str(mailbox_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExchangeItemSaveItemsResponse200 | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = ExchangeItemSaveItemsResponse200.from_dict(response.content)



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExchangeItemSaveItemsResponse200 | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveToMsgOptions,

) -> Response[ExchangeItemSaveItemsResponse200 | RESTExceptionInfo]:
    """ Save Mailbox Items

     Saves backed-up items to MSG files (Outlook Message Files).

    When you save backed-up items, the request command saves the items to MSG files and transfers them
    to application/octet-stream media.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download files from the temporary folder.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTSaveToMsgOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeItemSaveItemsResponse200 | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveToMsgOptions,

) -> ExchangeItemSaveItemsResponse200 | RESTExceptionInfo | None:
    """ Save Mailbox Items

     Saves backed-up items to MSG files (Outlook Message Files).

    When you save backed-up items, the request command saves the items to MSG files and transfers them
    to application/octet-stream media.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download files from the temporary folder.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTSaveToMsgOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeItemSaveItemsResponse200 | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveToMsgOptions,

) -> Response[ExchangeItemSaveItemsResponse200 | RESTExceptionInfo]:
    """ Save Mailbox Items

     Saves backed-up items to MSG files (Outlook Message Files).

    When you save backed-up items, the request command saves the items to MSG files and transfers them
    to application/octet-stream media.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download files from the temporary folder.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTSaveToMsgOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeItemSaveItemsResponse200 | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSaveToMsgOptions,

) -> ExchangeItemSaveItemsResponse200 | RESTExceptionInfo | None:
    """ Save Mailbox Items

     Saves backed-up items to MSG files (Outlook Message Files).

    When you save backed-up items, the request command saves the items to MSG files and transfers them
    to application/octet-stream media.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download files from the temporary folder.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        body (RESTSaveToMsgOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeItemSaveItemsResponse200 | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
mailbox_id=mailbox_id,
client=client,
body=body,

    )).parsed
