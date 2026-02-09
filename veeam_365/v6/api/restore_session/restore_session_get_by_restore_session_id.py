from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_restore_session import RESTRestoreSession
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/RestoreSessions/{restore_session_id}".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTRestoreSession:
    if response.status_code == 200:
        response_200 = RESTRestoreSession.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    """
    Args:
        restore_session_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSession]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTRestoreSession | None:
    """
    Args:
        restore_session_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSession
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    """
    Args:
        restore_session_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSession]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTRestoreSession | None:
    """
    Args:
        restore_session_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSession
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            client=client,
        )
    ).parsed
