from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response


def _get_kwargs(
    role_id: UUID,
    *,
    ids: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ids"] = ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v7/RbacRoles/{role_id}/selectedItems".format(
            role_id=quote(str(role_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RESTExceptionInfo:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RESTExceptionInfo]:
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
    ids: str,
) -> Response[Any | RESTExceptionInfo]:
    """Remove Objects to Manage

     Removes objects added to a restore operator role with the specified ID as objects to manage from
    this restore operator role.

    Args:
        role_id (UUID):
        ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    ids: str,
) -> Any | RESTExceptionInfo | None:
    """Remove Objects to Manage

     Removes objects added to a restore operator role with the specified ID as objects to manage from
    this restore operator role.

    Args:
        role_id (UUID):
        ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return sync_detailed(
        role_id=role_id,
        client=client,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    ids: str,
) -> Response[Any | RESTExceptionInfo]:
    """Remove Objects to Manage

     Removes objects added to a restore operator role with the specified ID as objects to manage from
    this restore operator role.

    Args:
        role_id (UUID):
        ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    ids: str,
) -> Any | RESTExceptionInfo | None:
    """Remove Objects to Manage

     Removes objects added to a restore operator role with the specified ID as objects to manage from
    this restore operator role.

    Args:
        role_id (UUID):
        ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            client=client,
            ids=ids,
        )
    ).parsed
