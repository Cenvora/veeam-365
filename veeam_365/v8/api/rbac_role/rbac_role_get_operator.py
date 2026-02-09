from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_rbac_operator import RESTRbacOperator
from ...types import Response


def _get_kwargs(
    role_id: UUID,
    operator_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RbacRoles/{role_id}/operators/{operator_id}".format(
            role_id=quote(str(role_id), safe=""),
            operator_id=quote(str(operator_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTRbacOperator:
    if response.status_code == 200:
        response_200 = RESTRbacOperator.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTRbacOperator]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role_id: UUID,
    operator_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTRbacOperator]:
    """Get Restore Operator

     Returns a resource representation of a restore operator with the specified ID.

    Args:
        role_id (UUID):
        operator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRbacOperator]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        operator_id=operator_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role_id: UUID,
    operator_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTRbacOperator | None:
    """Get Restore Operator

     Returns a resource representation of a restore operator with the specified ID.

    Args:
        role_id (UUID):
        operator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRbacOperator
    """

    return sync_detailed(
        role_id=role_id,
        operator_id=operator_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    role_id: UUID,
    operator_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | RESTRbacOperator]:
    """Get Restore Operator

     Returns a resource representation of a restore operator with the specified ID.

    Args:
        role_id (UUID):
        operator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRbacOperator]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        operator_id=operator_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role_id: UUID,
    operator_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | RESTRbacOperator | None:
    """Get Restore Operator

     Returns a resource representation of a restore operator with the specified ID.

    Args:
        role_id (UUID):
        operator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRbacOperator
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            operator_id=operator_id,
            client=client,
        )
    ).parsed
