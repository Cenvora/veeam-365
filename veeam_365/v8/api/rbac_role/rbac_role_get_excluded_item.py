from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_rbac_item_composed import RESTRbacItemComposed
from ...types import Response


def _get_kwargs(
    role_id: UUID,
    item_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RbacRoles/{role_id}/excludedItems/{item_id}".format(
            role_id=quote(str(role_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTRbacItemComposed:
    if response.status_code == 200:
        response_200 = RESTRbacItemComposed.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTRbacItemComposed]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role_id: UUID,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTRbacItemComposed]:
    """Get Excluded Object

     Returns a resource representation of an object with the specified ID excluded from the scope of a
    restore operator role with the specified ID. Restore operators are not allowed to explore and
    restore data from backups created by Veeam Backup for Microsoft 365 for this object.

    Args:
        role_id (UUID):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRbacItemComposed]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role_id: UUID,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTRbacItemComposed | None:
    """Get Excluded Object

     Returns a resource representation of an object with the specified ID excluded from the scope of a
    restore operator role with the specified ID. Restore operators are not allowed to explore and
    restore data from backups created by Veeam Backup for Microsoft 365 for this object.

    Args:
        role_id (UUID):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRbacItemComposed
    """

    return sync_detailed(
        role_id=role_id,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    role_id: UUID,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTRbacItemComposed]:
    """Get Excluded Object

     Returns a resource representation of an object with the specified ID excluded from the scope of a
    restore operator role with the specified ID. Restore operators are not allowed to explore and
    restore data from backups created by Veeam Backup for Microsoft 365 for this object.

    Args:
        role_id (UUID):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRbacItemComposed]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role_id: UUID,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTRbacItemComposed | None:
    """Get Excluded Object

     Returns a resource representation of an object with the specified ID excluded from the scope of a
    restore operator role with the specified ID. Restore operators are not allowed to explore and
    restore data from backups created by Veeam Backup for Microsoft 365 for this object.

    Args:
        role_id (UUID):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRbacItemComposed
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            item_id=item_id,
            client=client,
        )
    ).parsed
