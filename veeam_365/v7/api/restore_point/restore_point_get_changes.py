from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.restore_point_get_changes_response import RestorePointGetChangesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: str,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["from"] = from_

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/RestorePoints/Changes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RestorePointGetChangesResponse:
    if response.status_code == 200:
        response_200 = RestorePointGetChangesResponse.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RestorePointGetChangesResponse]:
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
) -> Response[RESTExceptionInfo | RestorePointGetChangesResponse]:
    """Get Changes

     Returns a collection of changes that appeared in restore points starting from the initial
    backup/backup copy or from a specified change token.

    Args:
        from_ (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RestorePointGetChangesResponse]
    """

    kwargs = _get_kwargs(
        from_=from_,
        limit=limit,
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
) -> RESTExceptionInfo | RestorePointGetChangesResponse | None:
    """Get Changes

     Returns a collection of changes that appeared in restore points starting from the initial
    backup/backup copy or from a specified change token.

    Args:
        from_ (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RestorePointGetChangesResponse
    """

    return sync_detailed(
        client=client,
        from_=from_,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str,
    limit: int | Unset = UNSET,
) -> Response[RESTExceptionInfo | RestorePointGetChangesResponse]:
    """Get Changes

     Returns a collection of changes that appeared in restore points starting from the initial
    backup/backup copy or from a specified change token.

    Args:
        from_ (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RestorePointGetChangesResponse]
    """

    kwargs = _get_kwargs(
        from_=from_,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: str,
    limit: int | Unset = UNSET,
) -> RESTExceptionInfo | RestorePointGetChangesResponse | None:
    """Get Changes

     Returns a collection of changes that appeared in restore points starting from the initial
    backup/backup copy or from a specified change token.

    Args:
        from_ (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RestorePointGetChangesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            limit=limit,
        )
    ).parsed
