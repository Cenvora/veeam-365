from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.events_get_response import EventsGetResponse
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: str,
    limit: int | Unset = UNSET,
    timeout_seconds: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["from"] = from_

    params["limit"] = limit

    params["timeoutSeconds"] = timeout_seconds

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/Events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EventsGetResponse | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = EventsGetResponse.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EventsGetResponse | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str,
    limit: int | Unset = UNSET,
    timeout_seconds: int | Unset = UNSET,
) -> Response[EventsGetResponse | RESTExceptionInfo]:
    """Get Events

     Returns a resource representation of events occurred in Veeam Backup for Microsoft 365.

    Args:
        from_ (str): Specifies a change token. To get events from the latest change token, specify
            the parameter value as *latest*.
        limit (int | Unset): Limits the maximum number of items that the server will return on a
            page. The maximum supported number of items per page is *10,000*. The default value is
            *30*.
        timeout_seconds (int | Unset): Specifies a timeout for the server to wait until new events
            appear.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventsGetResponse | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        from_=from_,
        limit=limit,
        timeout_seconds=timeout_seconds,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: str,
    limit: int | Unset = UNSET,
    timeout_seconds: int | Unset = UNSET,
) -> EventsGetResponse | RESTExceptionInfo | None:
    """Get Events

     Returns a resource representation of events occurred in Veeam Backup for Microsoft 365.

    Args:
        from_ (str): Specifies a change token. To get events from the latest change token, specify
            the parameter value as *latest*.
        limit (int | Unset): Limits the maximum number of items that the server will return on a
            page. The maximum supported number of items per page is *10,000*. The default value is
            *30*.
        timeout_seconds (int | Unset): Specifies a timeout for the server to wait until new events
            appear.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventsGetResponse | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        from_=from_,
        limit=limit,
        timeout_seconds=timeout_seconds,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str,
    limit: int | Unset = UNSET,
    timeout_seconds: int | Unset = UNSET,
) -> Response[EventsGetResponse | RESTExceptionInfo]:
    """Get Events

     Returns a resource representation of events occurred in Veeam Backup for Microsoft 365.

    Args:
        from_ (str): Specifies a change token. To get events from the latest change token, specify
            the parameter value as *latest*.
        limit (int | Unset): Limits the maximum number of items that the server will return on a
            page. The maximum supported number of items per page is *10,000*. The default value is
            *30*.
        timeout_seconds (int | Unset): Specifies a timeout for the server to wait until new events
            appear.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventsGetResponse | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        from_=from_,
        limit=limit,
        timeout_seconds=timeout_seconds,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: str,
    limit: int | Unset = UNSET,
    timeout_seconds: int | Unset = UNSET,
) -> EventsGetResponse | RESTExceptionInfo | None:
    """Get Events

     Returns a resource representation of events occurred in Veeam Backup for Microsoft 365.

    Args:
        from_ (str): Specifies a change token. To get events from the latest change token, specify
            the parameter value as *latest*.
        limit (int | Unset): Limits the maximum number of items that the server will return on a
            page. The maximum supported number of items per page is *10,000*. The default value is
            *30*.
        timeout_seconds (int | Unset): Specifies a timeout for the server to wait until new events
            appear.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventsGetResponse | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            limit=limit,
            timeout_seconds=timeout_seconds,
        )
    ).parsed
