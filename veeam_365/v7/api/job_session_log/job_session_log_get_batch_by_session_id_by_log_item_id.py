from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_log_item import RESTLogItem
from ...types import Response


def _get_kwargs(
    session_id: UUID,
    log_item_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/JobSessions/{session_id}/LogItems/{log_item_id}".format(
            session_id=quote(str(session_id), safe=""),
            log_item_id=quote(str(log_item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTLogItem:
    if response.status_code == 200:
        response_200 = RESTLogItem.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTLogItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: UUID,
    log_item_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTLogItem]:
    """Get Information on Operation by LogItem ID

     Returns information about a specific operation performed during a backup or backup copy job session
    with the specified ID.

    Args:
        session_id (UUID):
        log_item_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTLogItem]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        log_item_id=log_item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: UUID,
    log_item_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTLogItem | None:
    """Get Information on Operation by LogItem ID

     Returns information about a specific operation performed during a backup or backup copy job session
    with the specified ID.

    Args:
        session_id (UUID):
        log_item_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTLogItem
    """

    return sync_detailed(
        session_id=session_id,
        log_item_id=log_item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    session_id: UUID,
    log_item_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTLogItem]:
    """Get Information on Operation by LogItem ID

     Returns information about a specific operation performed during a backup or backup copy job session
    with the specified ID.

    Args:
        session_id (UUID):
        log_item_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTLogItem]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        log_item_id=log_item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: UUID,
    log_item_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTLogItem | None:
    """Get Information on Operation by LogItem ID

     Returns information about a specific operation performed during a backup or backup copy job session
    with the specified ID.

    Args:
        session_id (UUID):
        log_item_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTLogItem
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            log_item_id=log_item_id,
            client=client,
        )
    ).parsed
