from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_bulk_restore_options import RestBulkRestoreOptions
from ...models.rest_bulk_restore_statistics import RESTBulkRestoreStatistics
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    *,
    body: RestBulkRestoreOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v7/RestoreSessions/{restore_session_id}/organization/mailboxes/restore".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTBulkRestoreStatistics | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTBulkRestoreStatistics.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTBulkRestoreStatistics | RESTExceptionInfo]:
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
    body: RestBulkRestoreOptions,
) -> Response[RESTBulkRestoreStatistics | RESTExceptionInfo]:
    """Bulk Restore of Mailbox Data

     Performs a bulk restore of backed-up organization mailbox data.

    Args:
        restore_session_id (UUID):
        body (RestBulkRestoreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBulkRestoreStatistics | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RestBulkRestoreOptions,
) -> RESTBulkRestoreStatistics | RESTExceptionInfo | None:
    """Bulk Restore of Mailbox Data

     Performs a bulk restore of backed-up organization mailbox data.

    Args:
        restore_session_id (UUID):
        body (RestBulkRestoreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBulkRestoreStatistics | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RestBulkRestoreOptions,
) -> Response[RESTBulkRestoreStatistics | RESTExceptionInfo]:
    """Bulk Restore of Mailbox Data

     Performs a bulk restore of backed-up organization mailbox data.

    Args:
        restore_session_id (UUID):
        body (RestBulkRestoreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBulkRestoreStatistics | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RestBulkRestoreOptions,
) -> RESTBulkRestoreStatistics | RESTExceptionInfo | None:
    """Bulk Restore of Mailbox Data

     Performs a bulk restore of backed-up organization mailbox data.

    Args:
        restore_session_id (UUID):
        body (RestBulkRestoreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBulkRestoreStatistics | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            client=client,
            body=body,
        )
    ).parsed
