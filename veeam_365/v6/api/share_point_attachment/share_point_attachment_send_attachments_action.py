from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_send_attachments_as_msg_options import RESTSendAttachmentsAsMsgOptions
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    *,
    body: RESTSendAttachmentsAsMsgOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v6/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Items/{item_id}/Attachments/send".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

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
    site_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSendAttachmentsAsMsgOptions,
) -> Response[Any | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        body (RESTSendAttachmentsAsMsgOptions):

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
    *,
    client: AuthenticatedClient | Client,
    body: RESTSendAttachmentsAsMsgOptions,
) -> Any | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        body (RESTSendAttachmentsAsMsgOptions):

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
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSendAttachmentsAsMsgOptions,
) -> Response[Any | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        body (RESTSendAttachmentsAsMsgOptions):

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
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSendAttachmentsAsMsgOptions,
) -> Any | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        body (RESTSendAttachmentsAsMsgOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            site_id=site_id,
            item_id=item_id,
            client=client,
            body=body,
        )
    ).parsed
