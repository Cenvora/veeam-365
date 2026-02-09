from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_protected_group import RESTProtectedGroup
from ...types import Response


def _get_kwargs(
    protected_group_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/ProtectedGroups/{protected_group_id}".format(
            protected_group_id=quote(str(protected_group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTProtectedGroup:
    if response.status_code == 200:
        response_200 = RESTProtectedGroup.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTProtectedGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    protected_group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTProtectedGroup]:
    """Get Protected Group

     Returns a resource representation of a protected group with the specified ID.

    Args:
        protected_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTProtectedGroup]
    """

    kwargs = _get_kwargs(
        protected_group_id=protected_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    protected_group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTProtectedGroup | None:
    """Get Protected Group

     Returns a resource representation of a protected group with the specified ID.

    Args:
        protected_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTProtectedGroup
    """

    return sync_detailed(
        protected_group_id=protected_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    protected_group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTProtectedGroup]:
    """Get Protected Group

     Returns a resource representation of a protected group with the specified ID.

    Args:
        protected_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTProtectedGroup]
    """

    kwargs = _get_kwargs(
        protected_group_id=protected_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    protected_group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTProtectedGroup | None:
    """Get Protected Group

     Returns a resource representation of a protected group with the specified ID.

    Args:
        protected_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTProtectedGroup
    """

    return (
        await asyncio_detailed(
            protected_group_id=protected_group_id,
            client=client,
        )
    ).parsed
