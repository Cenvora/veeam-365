from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_item_composed import PageOfRESTItemComposed
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    include_folders: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["parentId"] = parent_id

    params["includeFolders"] = include_folders

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Documents".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            site_id=quote(str(site_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTItemComposed | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTItemComposed.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTItemComposed | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    include_folders: bool | Unset = UNSET,
) -> Response[PageOfRESTItemComposed | RESTExceptionInfo]:
    """Get SharePoint Documents

     Returns a collection of backed-up SharePoint documents to explore and restore.

    Args:
        restore_session_id (UUID):
        site_id (str):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):
        include_folders (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTItemComposed | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        offset=offset,
        limit=limit,
        parent_id=parent_id,
        include_folders=include_folders,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    include_folders: bool | Unset = UNSET,
) -> PageOfRESTItemComposed | RESTExceptionInfo | None:
    """Get SharePoint Documents

     Returns a collection of backed-up SharePoint documents to explore and restore.

    Args:
        restore_session_id (UUID):
        site_id (str):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):
        include_folders (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTItemComposed | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        site_id=site_id,
        client=client,
        offset=offset,
        limit=limit,
        parent_id=parent_id,
        include_folders=include_folders,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    include_folders: bool | Unset = UNSET,
) -> Response[PageOfRESTItemComposed | RESTExceptionInfo]:
    """Get SharePoint Documents

     Returns a collection of backed-up SharePoint documents to explore and restore.

    Args:
        restore_session_id (UUID):
        site_id (str):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):
        include_folders (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTItemComposed | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        offset=offset,
        limit=limit,
        parent_id=parent_id,
        include_folders=include_folders,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    site_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    include_folders: bool | Unset = UNSET,
) -> PageOfRESTItemComposed | RESTExceptionInfo | None:
    """Get SharePoint Documents

     Returns a collection of backed-up SharePoint documents to explore and restore.

    Args:
        restore_session_id (UUID):
        site_id (str):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):
        include_folders (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTItemComposed | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            site_id=site_id,
            client=client,
            offset=offset,
            limit=limit,
            parent_id=parent_id,
            include_folders=include_folders,
        )
    ).parsed
