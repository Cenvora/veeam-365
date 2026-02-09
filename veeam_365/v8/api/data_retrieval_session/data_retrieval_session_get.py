from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_data_retrieval_session import PageOfRESTDataRetrievalSession
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    data_retrieval_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_data_retrieval_id: str | Unset = UNSET
    if not isinstance(data_retrieval_id, Unset):
        json_data_retrieval_id = str(data_retrieval_id)
    params["dataRetrievalId"] = json_data_retrieval_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/DataRetrievalSessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTDataRetrievalSession | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTDataRetrievalSession.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTDataRetrievalSession | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_retrieval_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTDataRetrievalSession | RESTExceptionInfo]:
    """Get Data Retrieval Sessions

     Returns a collection of all sessions created for retrieval jobs.

    Args:
        data_retrieval_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTDataRetrievalSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        data_retrieval_id=data_retrieval_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    data_retrieval_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTDataRetrievalSession | RESTExceptionInfo | None:
    """Get Data Retrieval Sessions

     Returns a collection of all sessions created for retrieval jobs.

    Args:
        data_retrieval_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTDataRetrievalSession | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        data_retrieval_id=data_retrieval_id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_retrieval_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTDataRetrievalSession | RESTExceptionInfo]:
    """Get Data Retrieval Sessions

     Returns a collection of all sessions created for retrieval jobs.

    Args:
        data_retrieval_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTDataRetrievalSession | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        data_retrieval_id=data_retrieval_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    data_retrieval_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTDataRetrievalSession | RESTExceptionInfo | None:
    """Get Data Retrieval Sessions

     Returns a collection of all sessions created for retrieval jobs.

    Args:
        data_retrieval_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTDataRetrievalSession | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            data_retrieval_id=data_retrieval_id,
            limit=limit,
            offset=offset,
        )
    ).parsed
