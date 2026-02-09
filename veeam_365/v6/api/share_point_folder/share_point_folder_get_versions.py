from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_share_point_folder import PageOfRESTSharePointFolder
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Folders/{folder_id}/Versions".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            folder_id=quote(str(folder_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTSharePointFolder | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTSharePointFolder.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTSharePointFolder | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfRESTSharePointFolder | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTSharePointFolder | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        folder_id=folder_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfRESTSharePointFolder | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTSharePointFolder | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        site_id=site_id,
        folder_id=folder_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfRESTSharePointFolder | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTSharePointFolder | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        folder_id=folder_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfRESTSharePointFolder | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTSharePointFolder | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            site_id=site_id,
            folder_id=folder_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
