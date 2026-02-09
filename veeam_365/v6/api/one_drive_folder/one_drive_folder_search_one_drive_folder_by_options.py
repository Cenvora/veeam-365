from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.one_drive_folder_search_one_drive_folder_by_options_item_type import (
    OneDriveFolderSearchOneDriveFolderByOptionsItemType,
)
from ...models.page_of_rest_item_composed import PageOfRESTItemComposed
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.restvesp_search_options import RESTVESPSearchOptions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_session_id: UUID,
    one_drive_id: str,
    folder_id: UUID,
    *,
    body: RESTVESPSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    item_type: OneDriveFolderSearchOneDriveFolderByOptionsItemType | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    json_set_id: str | Unset = UNSET
    if not isinstance(set_id, Unset):
        json_set_id = str(set_id)
    params["setId"] = json_set_id

    json_item_type: str | Unset = UNSET
    if not isinstance(item_type, Unset):
        json_item_type = item_type.value

    params["itemType"] = json_item_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v6/RestoreSessions/{restore_session_id}/Organization/OneDrives/{one_drive_id}/Folders/{folder_id}/search".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            one_drive_id=quote(str(one_drive_id), safe=""),
            folder_id=quote(str(folder_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    one_drive_id: str,
    folder_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTVESPSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    item_type: OneDriveFolderSearchOneDriveFolderByOptionsItemType | Unset = UNSET,
) -> Response[PageOfRESTItemComposed | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        folder_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        item_type (OneDriveFolderSearchOneDriveFolderByOptionsItemType | Unset):
        body (RESTVESPSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTItemComposed | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        folder_id=folder_id,
        body=body,
        offset=offset,
        limit=limit,
        set_id=set_id,
        item_type=item_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    one_drive_id: str,
    folder_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTVESPSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    item_type: OneDriveFolderSearchOneDriveFolderByOptionsItemType | Unset = UNSET,
) -> PageOfRESTItemComposed | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        folder_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        item_type (OneDriveFolderSearchOneDriveFolderByOptionsItemType | Unset):
        body (RESTVESPSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTItemComposed | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        folder_id=folder_id,
        client=client,
        body=body,
        offset=offset,
        limit=limit,
        set_id=set_id,
        item_type=item_type,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    folder_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTVESPSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    item_type: OneDriveFolderSearchOneDriveFolderByOptionsItemType | Unset = UNSET,
) -> Response[PageOfRESTItemComposed | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        folder_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        item_type (OneDriveFolderSearchOneDriveFolderByOptionsItemType | Unset):
        body (RESTVESPSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTItemComposed | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        folder_id=folder_id,
        body=body,
        offset=offset,
        limit=limit,
        set_id=set_id,
        item_type=item_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    one_drive_id: str,
    folder_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTVESPSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
    item_type: OneDriveFolderSearchOneDriveFolderByOptionsItemType | Unset = UNSET,
) -> PageOfRESTItemComposed | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        folder_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        item_type (OneDriveFolderSearchOneDriveFolderByOptionsItemType | Unset):
        body (RESTVESPSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTItemComposed | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            one_drive_id=one_drive_id,
            folder_id=folder_id,
            client=client,
            body=body,
            offset=offset,
            limit=limit,
            set_id=set_id,
            item_type=item_type,
        )
    ).parsed
