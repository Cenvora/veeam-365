from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_data_retrieval_update_from_client import RESTDataRetrievalUpdateFromClient
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    data_retrieval_id: UUID,
    *,
    body: RESTDataRetrievalUpdateFromClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v7/DataRetrievals/{data_retrieval_id}".format(
            data_retrieval_id=quote(str(data_retrieval_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

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
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTDataRetrievalUpdateFromClient,
) -> Response[Any | RESTExceptionInfo]:
    """Edit Data Retrieval Job Settings

     Modifies settings of a retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        body (RESTDataRetrievalUpdateFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        data_retrieval_id=data_retrieval_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTDataRetrievalUpdateFromClient,
) -> Any | RESTExceptionInfo | None:
    """Edit Data Retrieval Job Settings

     Modifies settings of a retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        body (RESTDataRetrievalUpdateFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return sync_detailed(
        data_retrieval_id=data_retrieval_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTDataRetrievalUpdateFromClient,
) -> Response[Any | RESTExceptionInfo]:
    """Edit Data Retrieval Job Settings

     Modifies settings of a retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        body (RESTDataRetrievalUpdateFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        data_retrieval_id=data_retrieval_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTDataRetrievalUpdateFromClient,
) -> Any | RESTExceptionInfo | None:
    """Edit Data Retrieval Job Settings

     Modifies settings of a retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        body (RESTDataRetrievalUpdateFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            data_retrieval_id=data_retrieval_id,
            client=client,
            body=body,
        )
    ).parsed
