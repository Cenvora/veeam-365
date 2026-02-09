from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_encryption_key import RESTEncryptionKey
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    description: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["description"] = description

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/EncryptionKeys",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTEncryptionKey]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTEncryptionKey.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTEncryptionKey]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTEncryptionKey]]:
    """
    Args:
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTEncryptionKey]]
    """

    kwargs = _get_kwargs(
        description=description,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTEncryptionKey] | None:
    """
    Args:
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTEncryptionKey]
    """

    return sync_detailed(
        client=client,
        description=description,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTEncryptionKey]]:
    """
    Args:
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTEncryptionKey]]
    """

    kwargs = _get_kwargs(
        description=description,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    description: str | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTEncryptionKey] | None:
    """
    Args:
        description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTEncryptionKey]
    """

    return (
        await asyncio_detailed(
            client=client,
            description=description,
        )
    ).parsed
