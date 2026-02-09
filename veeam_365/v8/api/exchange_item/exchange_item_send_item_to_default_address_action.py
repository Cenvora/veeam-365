from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    mailbox_id: UUID,
    item_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/mailboxes/{mailbox_id}/items/{item_id}/sendToDefaultAddress".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            mailbox_id=quote(str(mailbox_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RESTExceptionInfo:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RESTExceptionInfo]:
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
) -> Response[Any | RESTExceptionInfo]:
    r"""Send Mailbox Item to Original Mailbox

     Sends a backed-up item with the specified ID as an attachment in an email message to the original
    mailbox. <div class=\"note\"><strong>NOTE</strong> </br> To send items as attachments, you must
    specify the Veeam Explorer for Microsoft Exchange email settings. For more information, see [Edit
    Email Settings](VexEmailSettings#operation/VexEmailSettings_Update). </div>

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        mailbox_id=mailbox_id,
        item_id=item_id,
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
) -> Any | RESTExceptionInfo | None:
    r"""Send Mailbox Item to Original Mailbox

     Sends a backed-up item with the specified ID as an attachment in an email message to the original
    mailbox. <div class=\"note\"><strong>NOTE</strong> </br> To send items as attachments, you must
    specify the Veeam Explorer for Microsoft Exchange email settings. For more information, see [Edit
    Email Settings](VexEmailSettings#operation/VexEmailSettings_Update). </div>

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        mailbox_id=mailbox_id,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    mailbox_id: UUID,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RESTExceptionInfo]:
    r"""Send Mailbox Item to Original Mailbox

     Sends a backed-up item with the specified ID as an attachment in an email message to the original
    mailbox. <div class=\"note\"><strong>NOTE</strong> </br> To send items as attachments, you must
    specify the Veeam Explorer for Microsoft Exchange email settings. For more information, see [Edit
    Email Settings](VexEmailSettings#operation/VexEmailSettings_Update). </div>

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        mailbox_id=mailbox_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    mailbox_id: UUID,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RESTExceptionInfo | None:
    r"""Send Mailbox Item to Original Mailbox

     Sends a backed-up item with the specified ID as an attachment in an email message to the original
    mailbox. <div class=\"note\"><strong>NOTE</strong> </br> To send items as attachments, you must
    specify the Veeam Explorer for Microsoft Exchange email settings. For more information, see [Edit
    Email Settings](VexEmailSettings#operation/VexEmailSettings_Update). </div>

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            mailbox_id=mailbox_id,
            item_id=item_id,
            client=client,
        )
    ).parsed
