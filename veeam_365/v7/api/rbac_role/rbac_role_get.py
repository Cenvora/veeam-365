from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_rbac_role import RESTRbacRole
from ...types import Response


def _get_kwargs(
    role_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/RbacRoles/{role_id}".format(
            role_id=quote(str(role_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTRbacRole:
    if response.status_code == 200:
        response_200 = RESTRbacRole.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTRbacRole]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTRbacRole]:
    """Get Restore Operator Role

     Returns a resource representation of a restore operator role with the specified ID.

    Args:
        role_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRbacRole]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTRbacRole | None:
    """Get Restore Operator Role

     Returns a resource representation of a restore operator role with the specified ID.

    Args:
        role_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRbacRole
    """

    return sync_detailed(
        role_id=role_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTRbacRole]:
    """Get Restore Operator Role

     Returns a resource representation of a restore operator role with the specified ID.

    Args:
        role_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRbacRole]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTRbacRole | None:
    """Get Restore Operator Role

     Returns a resource representation of a restore operator role with the specified ID.

    Args:
        role_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRbacRole
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            client=client,
        )
    ).parsed
