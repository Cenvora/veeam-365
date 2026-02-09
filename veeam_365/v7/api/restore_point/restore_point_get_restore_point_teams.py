from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_restore_point_team import PageOfRESTRestorePointTeam
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_point_id: str,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/RestorePoints/{restore_point_id}/protectedTeams".format(
            restore_point_id=quote(str(restore_point_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTRestorePointTeam | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTRestorePointTeam.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTRestorePointTeam | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_point_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTRestorePointTeam | RESTExceptionInfo]:
    """Get Teams

     Returns a collection of teams contained in a restore point with the specified ID.

    Args:
        restore_point_id (str):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTRestorePointTeam | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_point_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTRestorePointTeam | RESTExceptionInfo | None:
    """Get Teams

     Returns a collection of teams contained in a restore point with the specified ID.

    Args:
        restore_point_id (str):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTRestorePointTeam | RESTExceptionInfo
    """

    return sync_detailed(
        restore_point_id=restore_point_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    restore_point_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTRestorePointTeam | RESTExceptionInfo]:
    """Get Teams

     Returns a collection of teams contained in a restore point with the specified ID.

    Args:
        restore_point_id (str):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTRestorePointTeam | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_point_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTRestorePointTeam | RESTExceptionInfo | None:
    """Get Teams

     Returns a collection of teams contained in a restore point with the specified ID.

    Args:
        restore_point_id (str):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTRestorePointTeam | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_point_id=restore_point_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
