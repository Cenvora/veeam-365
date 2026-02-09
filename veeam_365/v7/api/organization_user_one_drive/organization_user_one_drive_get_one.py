from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_one_drive import RESTOneDrive
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    user_id: str,
    onedrive_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/Organizations/{organization_id}/Users/{user_id}/OneDrives/{onedrive_id}".format(
            organization_id=quote(str(organization_id), safe=""),
            user_id=quote(str(user_id), safe=""),
            onedrive_id=quote(str(onedrive_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTOneDrive:
    if response.status_code == 200:
        response_200 = RESTOneDrive.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTOneDrive]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    user_id: str,
    onedrive_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTOneDrive]:
    """Get OneDrive of Organization User

     Returns a resource representation of OneDrive with the specified ID that belongs to an organization
    user with the specified ID.

    Args:
        organization_id (UUID):
        user_id (str):
        onedrive_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTOneDrive]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        user_id=user_id,
        onedrive_id=onedrive_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    user_id: str,
    onedrive_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTOneDrive | None:
    """Get OneDrive of Organization User

     Returns a resource representation of OneDrive with the specified ID that belongs to an organization
    user with the specified ID.

    Args:
        organization_id (UUID):
        user_id (str):
        onedrive_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTOneDrive
    """

    return sync_detailed(
        organization_id=organization_id,
        user_id=user_id,
        onedrive_id=onedrive_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    user_id: str,
    onedrive_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTOneDrive]:
    """Get OneDrive of Organization User

     Returns a resource representation of OneDrive with the specified ID that belongs to an organization
    user with the specified ID.

    Args:
        organization_id (UUID):
        user_id (str):
        onedrive_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTOneDrive]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        user_id=user_id,
        onedrive_id=onedrive_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    user_id: str,
    onedrive_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTOneDrive | None:
    """Get OneDrive of Organization User

     Returns a resource representation of OneDrive with the specified ID that belongs to an organization
    user with the specified ID.

    Args:
        organization_id (UUID):
        user_id (str):
        onedrive_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTOneDrive
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            user_id=user_id,
            onedrive_id=onedrive_id,
            client=client,
        )
    ).parsed
