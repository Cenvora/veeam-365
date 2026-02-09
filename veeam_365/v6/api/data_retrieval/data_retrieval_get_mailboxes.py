from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_data_retrieval_mailbox import RESTDataRetrievalMailbox
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    data_retrieval_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v6/DataRetrievals/{data_retrieval_id}/mailboxes".format(
            data_retrieval_id=quote(str(data_retrieval_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTDataRetrievalMailbox]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTDataRetrievalMailbox.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTDataRetrievalMailbox]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | list[RESTDataRetrievalMailbox]]:
    """
    Args:
        data_retrieval_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTDataRetrievalMailbox]]
    """

    kwargs = _get_kwargs(
        data_retrieval_id=data_retrieval_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | list[RESTDataRetrievalMailbox] | None:
    """
    Args:
        data_retrieval_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTDataRetrievalMailbox]
    """

    return sync_detailed(
        data_retrieval_id=data_retrieval_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RESTExceptionInfo | list[RESTDataRetrievalMailbox]]:
    """
    Args:
        data_retrieval_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTDataRetrievalMailbox]]
    """

    kwargs = _get_kwargs(
        data_retrieval_id=data_retrieval_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> RESTExceptionInfo | list[RESTDataRetrievalMailbox] | None:
    """
    Args:
        data_retrieval_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTDataRetrievalMailbox]
    """

    return (
        await asyncio_detailed(
            data_retrieval_id=data_retrieval_id,
            client=client,
        )
    ).parsed
