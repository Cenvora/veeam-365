from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_restore_session import PageOfRESTRestoreSession
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    start_time_from: str | Unset = UNSET,
    start_time_to: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["startTimeFrom"] = start_time_from

    params["startTimeTo"] = start_time_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/RestoreSessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTRestoreSession | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTRestoreSession.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTRestoreSession | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    start_time_from: str | Unset = UNSET,
    start_time_to: str | Unset = UNSET,
) -> Response[PageOfRESTRestoreSession | RESTExceptionInfo]:
    """Get Restore Sessions

     Returns a collection of restore sessions.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        start_time_from (str | Unset):
        start_time_to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTRestoreSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        start_time_from=start_time_from,
        start_time_to=start_time_to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    start_time_from: str | Unset = UNSET,
    start_time_to: str | Unset = UNSET,
) -> PageOfRESTRestoreSession | RESTExceptionInfo | None:
    """Get Restore Sessions

     Returns a collection of restore sessions.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        start_time_from (str | Unset):
        start_time_to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTRestoreSession | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        start_time_from=start_time_from,
        start_time_to=start_time_to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    start_time_from: str | Unset = UNSET,
    start_time_to: str | Unset = UNSET,
) -> Response[PageOfRESTRestoreSession | RESTExceptionInfo]:
    """Get Restore Sessions

     Returns a collection of restore sessions.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        start_time_from (str | Unset):
        start_time_to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTRestoreSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        start_time_from=start_time_from,
        start_time_to=start_time_to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    start_time_from: str | Unset = UNSET,
    start_time_to: str | Unset = UNSET,
) -> PageOfRESTRestoreSession | RESTExceptionInfo | None:
    """Get Restore Sessions

     Returns a collection of restore sessions.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        start_time_from (str | Unset):
        start_time_to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTRestoreSession | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            start_time_from=start_time_from,
            start_time_to=start_time_to,
        )
    ).parsed
