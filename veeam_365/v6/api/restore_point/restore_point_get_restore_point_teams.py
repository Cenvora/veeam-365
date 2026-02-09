from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_restore_point_team import RESTRestorePointTeam
from ...types import Response


def _get_kwargs(
    restore_point_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/RestorePoints/{restore_point_id}/teams".format(
            restore_point_id=quote(str(restore_point_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTRestorePointTeam]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTRestorePointTeam.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTRestorePointTeam]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_point_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | list[RESTRestorePointTeam]]:
    """
    Args:
        restore_point_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTRestorePointTeam]]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_point_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | list[RESTRestorePointTeam] | None:
    """
    Args:
        restore_point_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTRestorePointTeam]
    """

    return sync_detailed(
        restore_point_id=restore_point_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    restore_point_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | list[RESTRestorePointTeam]]:
    """
    Args:
        restore_point_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTRestorePointTeam]]
    """

    kwargs = _get_kwargs(
        restore_point_id=restore_point_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_point_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | list[RESTRestorePointTeam] | None:
    """
    Args:
        restore_point_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTRestorePointTeam]
    """

    return (
        await asyncio_detailed(
            restore_point_id=restore_point_id,
            client=client,
        )
    ).parsed
