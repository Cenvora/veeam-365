from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_restore_point import RESTRestorePoint
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    rbac_item: str | Unset = UNSET,
    is_copy: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["rbacItem"] = rbac_item

    params["isCopy"] = is_copy

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/Organization/LoggedInUser/RestorePoints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTRestorePoint]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTRestorePoint.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTRestorePoint]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    rbac_item: str | Unset = UNSET,
    is_copy: bool | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTRestorePoint]]:
    """Get Restore Points

     Returns a resource representation of restore points created by Veeam Backup for Microsoft 365 for
    organization users currently logged in to Restore Portal.

    Args:
        rbac_item (str | Unset):
        is_copy (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTRestorePoint]]
    """

    kwargs = _get_kwargs(
        rbac_item=rbac_item,
        is_copy=is_copy,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    rbac_item: str | Unset = UNSET,
    is_copy: bool | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTRestorePoint] | None:
    """Get Restore Points

     Returns a resource representation of restore points created by Veeam Backup for Microsoft 365 for
    organization users currently logged in to Restore Portal.

    Args:
        rbac_item (str | Unset):
        is_copy (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTRestorePoint]
    """

    return sync_detailed(
        client=client,
        rbac_item=rbac_item,
        is_copy=is_copy,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    rbac_item: str | Unset = UNSET,
    is_copy: bool | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTRestorePoint]]:
    """Get Restore Points

     Returns a resource representation of restore points created by Veeam Backup for Microsoft 365 for
    organization users currently logged in to Restore Portal.

    Args:
        rbac_item (str | Unset):
        is_copy (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTRestorePoint]]
    """

    kwargs = _get_kwargs(
        rbac_item=rbac_item,
        is_copy=is_copy,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    rbac_item: str | Unset = UNSET,
    is_copy: bool | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTRestorePoint] | None:
    """Get Restore Points

     Returns a resource representation of restore points created by Veeam Backup for Microsoft 365 for
    organization users currently logged in to Restore Portal.

    Args:
        rbac_item (str | Unset):
        is_copy (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTRestorePoint]
    """

    return (
        await asyncio_detailed(
            client=client,
            rbac_item=rbac_item,
            is_copy=is_copy,
        )
    ).parsed
