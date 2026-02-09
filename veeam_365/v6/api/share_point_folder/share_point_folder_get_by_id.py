from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_share_point_folder import RESTSharePointFolder
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Folders/{folder_id}".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            folder_id=quote(str(folder_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTSharePointFolder:
    if response.status_code == 200:
        response_200 = RESTSharePointFolder.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTSharePointFolder]:
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
) -> Response[RESTExceptionInfo | RESTSharePointFolder]:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTSharePointFolder]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        folder_id=folder_id,
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
) -> RESTExceptionInfo | RESTSharePointFolder | None:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTSharePointFolder
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        site_id=site_id,
        folder_id=folder_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTSharePointFolder]:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTSharePointFolder]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        folder_id=folder_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    site_id: str,
    folder_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTSharePointFolder | None:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        folder_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTSharePointFolder
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            site_id=site_id,
            folder_id=folder_id,
            client=client,
        )
    ).parsed
