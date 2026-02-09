from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_one_drive_document import PageOfRESTOneDriveDocument
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["parentId"] = parent_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/RestoreSessions/{restore_session_id}/Organization/OneDrives/{one_drive_id}/Documents".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            one_drive_id=quote(str(one_drive_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTOneDriveDocument | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTOneDriveDocument.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTOneDriveDocument | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
) -> Response[PageOfRESTOneDriveDocument | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTOneDriveDocument | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        offset=offset,
        limit=limit,
        parent_id=parent_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
) -> PageOfRESTOneDriveDocument | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTOneDriveDocument | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        client=client,
        offset=offset,
        limit=limit,
        parent_id=parent_id,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
) -> Response[PageOfRESTOneDriveDocument | RESTExceptionInfo]:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTOneDriveDocument | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        offset=offset,
        limit=limit,
        parent_id=parent_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    parent_id: str | Unset = UNSET,
) -> PageOfRESTOneDriveDocument | RESTExceptionInfo | None:
    """
    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        offset (int | Unset):
        limit (int | Unset):
        parent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTOneDriveDocument | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            one_drive_id=one_drive_id,
            client=client,
            offset=offset,
            limit=limit,
            parent_id=parent_id,
        )
    ).parsed
