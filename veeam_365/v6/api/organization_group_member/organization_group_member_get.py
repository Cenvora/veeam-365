from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_group_member import PageOfRESTGroupMember
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: UUID,
    group_id: str,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_set_id: str | Unset = UNSET
    if not isinstance(set_id, Unset):
        json_set_id = str(set_id)
    params["setId"] = json_set_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/Organizations/{organization_id}/Groups/{group_id}/Members".format(
            organization_id=quote(str(organization_id), safe=""),
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTGroupMember | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTGroupMember.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTGroupMember | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
) -> Response[PageOfRESTGroupMember | RESTExceptionInfo]:
    """
    Args:
        organization_id (UUID):
        group_id (str):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTGroupMember | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        group_id=group_id,
        limit=limit,
        offset=offset,
        set_id=set_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
) -> PageOfRESTGroupMember | RESTExceptionInfo | None:
    """
    Args:
        organization_id (UUID):
        group_id (str):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTGroupMember | RESTExceptionInfo
    """

    return sync_detailed(
        organization_id=organization_id,
        group_id=group_id,
        client=client,
        limit=limit,
        offset=offset,
        set_id=set_id,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
) -> Response[PageOfRESTGroupMember | RESTExceptionInfo]:
    """
    Args:
        organization_id (UUID):
        group_id (str):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTGroupMember | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        group_id=group_id,
        limit=limit,
        offset=offset,
        set_id=set_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,
) -> PageOfRESTGroupMember | RESTExceptionInfo | None:
    """
    Args:
        organization_id (UUID):
        group_id (str):
        limit (int | Unset):
        offset (int | Unset):
        set_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTGroupMember | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            group_id=group_id,
            client=client,
            limit=limit,
            offset=offset,
            set_id=set_id,
        )
    ).parsed
