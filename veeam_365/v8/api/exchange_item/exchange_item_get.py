from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_exchange_items_composed import PageOfRESTExchangeItemsComposed
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["parentId"] = parent_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/mailboxes/{mailbox_id}/items".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            mailbox_id=quote(str(mailbox_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTExchangeItemsComposed | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTExchangeItemsComposed.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTExchangeItemsComposed | RESTExceptionInfo]:
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
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
) -> Response[PageOfRESTExchangeItemsComposed | RESTExceptionInfo]:
    """Get Mailbox Items

     Returns a collection of organization mailbox items to explore and restore.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTExchangeItemsComposed | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        mailbox_id=mailbox_id,
        offset=offset,
        limit=limit,
        parent_id=parent_id,
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
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
) -> PageOfRESTExchangeItemsComposed | RESTExceptionInfo | None:
    """Get Mailbox Items

     Returns a collection of organization mailbox items to explore and restore.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTExchangeItemsComposed | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        mailbox_id=mailbox_id,
        client=client,
        offset=offset,
        limit=limit,
        parent_id=parent_id,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
) -> Response[PageOfRESTExchangeItemsComposed | RESTExceptionInfo]:
    """Get Mailbox Items

     Returns a collection of organization mailbox items to explore and restore.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTExchangeItemsComposed | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        mailbox_id=mailbox_id,
        offset=offset,
        limit=limit,
        parent_id=parent_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    mailbox_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
) -> PageOfRESTExchangeItemsComposed | RESTExceptionInfo | None:
    """Get Mailbox Items

     Returns a collection of organization mailbox items to explore and restore.

    Args:
        restore_session_id (UUID):
        mailbox_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTExchangeItemsComposed | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            mailbox_id=mailbox_id,
            client=client,
            offset=offset,
            limit=limit,
            parent_id=parent_id,
        )
    ).parsed
