from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_share_point_library import RESTSharePointLibrary
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    library_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Libraries/{library_id}".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            library_id=quote(str(library_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTSharePointLibrary:
    if response.status_code == 200:
        response_200 = RESTSharePointLibrary.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTSharePointLibrary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    site_id: str,
    library_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTSharePointLibrary]:
    """Get SharePoint Library

     Returns a resource representation of a backed-up SharePoint document library with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        library_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTSharePointLibrary]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        library_id=library_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    site_id: str,
    library_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTSharePointLibrary | None:
    """Get SharePoint Library

     Returns a resource representation of a backed-up SharePoint document library with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        library_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTSharePointLibrary
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        site_id=site_id,
        library_id=library_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    library_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTSharePointLibrary]:
    """Get SharePoint Library

     Returns a resource representation of a backed-up SharePoint document library with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        library_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTSharePointLibrary]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        library_id=library_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    site_id: str,
    library_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTSharePointLibrary | None:
    """Get SharePoint Library

     Returns a resource representation of a backed-up SharePoint document library with the specified ID.

    Args:
        restore_session_id (UUID):
        site_id (str):
        library_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTSharePointLibrary
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            site_id=site_id,
            library_id=library_id,
            client=client,
        )
    ).parsed
