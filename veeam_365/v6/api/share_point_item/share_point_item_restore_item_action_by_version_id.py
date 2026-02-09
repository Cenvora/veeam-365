from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_item_restore_statistics import RESTItemRestoreStatistics
from ...models.rest_restore_item_config import RESTRestoreItemConfig
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    version_id: int,
    *,
    body: RESTRestoreItemConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v6/RestoreSessions/{restore_session_id}/Organization/Sites/{site_id}/Items/{item_id}/Versions/{version_id}/restore".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            site_id=quote(str(site_id), safe=""),
            item_id=quote(str(item_id), safe=""),
            version_id=quote(str(version_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTItemRestoreStatistics:
    if response.status_code == 200:
        response_200 = RESTItemRestoreStatistics.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTItemRestoreStatistics]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreItemConfig,
) -> Response[RESTExceptionInfo | RESTItemRestoreStatistics]:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        version_id (int):
        body (RESTRestoreItemConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTItemRestoreStatistics]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        item_id=item_id,
        version_id=version_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreItemConfig,
) -> RESTExceptionInfo | RESTItemRestoreStatistics | None:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        version_id (int):
        body (RESTRestoreItemConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTItemRestoreStatistics
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        site_id=site_id,
        item_id=item_id,
        version_id=version_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreItemConfig,
) -> Response[RESTExceptionInfo | RESTItemRestoreStatistics]:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        version_id (int):
        body (RESTRestoreItemConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTItemRestoreStatistics]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        site_id=site_id,
        item_id=item_id,
        version_id=version_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    site_id: str,
    item_id: str,
    version_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RESTRestoreItemConfig,
) -> RESTExceptionInfo | RESTItemRestoreStatistics | None:
    """
    Args:
        restore_session_id (UUID):
        site_id (str):
        item_id (str):
        version_id (int):
        body (RESTRestoreItemConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTItemRestoreStatistics
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            site_id=site_id,
            item_id=item_id,
            version_id=version_id,
            client=client,
            body=body,
        )
    ).parsed
