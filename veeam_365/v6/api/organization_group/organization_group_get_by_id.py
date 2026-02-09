from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_group import RESTGroup
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    group_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/Organizations/{organization_id}/Groups/{group_id}".format(
            organization_id=quote(str(organization_id), safe=""),
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTGroup:
    if response.status_code == 200:
        response_200 = RESTGroup.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTGroup]:
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
) -> Response[RESTExceptionInfo | RESTGroup]:
    """
    Args:
        organization_id (UUID):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTGroup]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        group_id=group_id,
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
) -> RESTExceptionInfo | RESTGroup | None:
    """
    Args:
        organization_id (UUID):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTGroup
    """

    return sync_detailed(
        organization_id=organization_id,
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTGroup]:
    """
    Args:
        organization_id (UUID):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTGroup]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTGroup | None:
    """
    Args:
        organization_id (UUID):
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTGroup
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            group_id=group_id,
            client=client,
        )
    ).parsed
