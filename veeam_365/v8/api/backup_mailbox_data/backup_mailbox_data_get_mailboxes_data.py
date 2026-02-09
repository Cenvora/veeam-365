import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_backup_mailbox_data import PageOfRESTBackupMailboxData
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repository_id: UUID,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    point_in_time: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["filter"] = filter_

    params["organizationId"] = organization_id

    json_point_in_time: str | Unset = UNSET
    if not isinstance(point_in_time, Unset):
        json_point_in_time = point_in_time.isoformat()
    params["pointInTime"] = json_point_in_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/BackupRepositories/{repository_id}/MailboxData".format(
            repository_id=quote(str(repository_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTBackupMailboxData | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTBackupMailboxData.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTBackupMailboxData | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    point_in_time: datetime.datetime | Unset = UNSET,
) -> Response[PageOfRESTBackupMailboxData | RESTExceptionInfo]:
    """Get Mailbox Data by Repository ID

     Returns a collection of backed-up mailboxes whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        filter_ (str | Unset):
        organization_id (str | Unset):
        point_in_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupMailboxData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        limit=limit,
        offset=offset,
        filter_=filter_,
        organization_id=organization_id,
        point_in_time=point_in_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    point_in_time: datetime.datetime | Unset = UNSET,
) -> PageOfRESTBackupMailboxData | RESTExceptionInfo | None:
    """Get Mailbox Data by Repository ID

     Returns a collection of backed-up mailboxes whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        filter_ (str | Unset):
        organization_id (str | Unset):
        point_in_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupMailboxData | RESTExceptionInfo
    """

    return sync_detailed(
        repository_id=repository_id,
        client=client,
        limit=limit,
        offset=offset,
        filter_=filter_,
        organization_id=organization_id,
        point_in_time=point_in_time,
    ).parsed


async def asyncio_detailed(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    point_in_time: datetime.datetime | Unset = UNSET,
) -> Response[PageOfRESTBackupMailboxData | RESTExceptionInfo]:
    """Get Mailbox Data by Repository ID

     Returns a collection of backed-up mailboxes whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        filter_ (str | Unset):
        organization_id (str | Unset):
        point_in_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTBackupMailboxData | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        limit=limit,
        offset=offset,
        filter_=filter_,
        organization_id=organization_id,
        point_in_time=point_in_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    point_in_time: datetime.datetime | Unset = UNSET,
) -> PageOfRESTBackupMailboxData | RESTExceptionInfo | None:
    """Get Mailbox Data by Repository ID

     Returns a collection of backed-up mailboxes whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        filter_ (str | Unset):
        organization_id (str | Unset):
        point_in_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTBackupMailboxData | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            client=client,
            limit=limit,
            offset=offset,
            filter_=filter_,
            organization_id=organization_id,
            point_in_time=point_in_time,
        )
    ).parsed
