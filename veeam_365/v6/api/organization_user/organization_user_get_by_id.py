from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_user import RESTUser
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    user_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/Organizations/{organization_id}/Users/{user_id}".format(
            organization_id=quote(str(organization_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTUser:
    if response.status_code == 200:
        response_200 = RESTUser.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTUser]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTUser]:
    """
    Args:
        organization_id (UUID):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTUser]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTUser | None:
    """
    Args:
        organization_id (UUID):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTUser
    """

    return sync_detailed(
        organization_id=organization_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTUser]:
    """
    Args:
        organization_id (UUID):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTUser]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTUser | None:
    """
    Args:
        organization_id (UUID):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTUser
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
