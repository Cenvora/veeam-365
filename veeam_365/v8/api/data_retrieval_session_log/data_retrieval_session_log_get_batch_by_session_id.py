from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_log_item import PageOfRESTLogItem
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: UUID,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["orderAsc"] = order_asc

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/DataRetrievalSessions/{session_id}/LogItems".format(
            session_id=quote(str(session_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTLogItem | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTLogItem.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTLogItem | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
) -> Response[PageOfRESTLogItem | RESTExceptionInfo]:
    """Get Information on Operations by Session ID

     Returns information about the operations performed during a data retrieval session with the
    specified ID.

    Args:
        session_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        order_asc (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTLogItem | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        offset=offset,
        limit=limit,
        order_asc=order_asc,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
) -> PageOfRESTLogItem | RESTExceptionInfo | None:
    """Get Information on Operations by Session ID

     Returns information about the operations performed during a data retrieval session with the
    specified ID.

    Args:
        session_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        order_asc (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTLogItem | RESTExceptionInfo
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
        offset=offset,
        limit=limit,
        order_asc=order_asc,
    ).parsed


async def asyncio_detailed(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
) -> Response[PageOfRESTLogItem | RESTExceptionInfo]:
    """Get Information on Operations by Session ID

     Returns information about the operations performed during a data retrieval session with the
    specified ID.

    Args:
        session_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        order_asc (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTLogItem | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        offset=offset,
        limit=limit,
        order_asc=order_asc,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    order_asc: bool | Unset = UNSET,
) -> PageOfRESTLogItem | RESTExceptionInfo | None:
    """Get Information on Operations by Session ID

     Returns information about the operations performed during a data retrieval session with the
    specified ID.

    Args:
        session_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        order_asc (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTLogItem | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            offset=offset,
            limit=limit,
            order_asc=order_asc,
        )
    ).parsed
