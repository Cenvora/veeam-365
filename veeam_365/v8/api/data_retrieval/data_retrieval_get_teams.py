from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_data_retrieval_team import PageOfRESTDataRetrievalTeam
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    data_retrieval_id: UUID,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/DataRetrievals/{data_retrieval_id}/teams".format(
            data_retrieval_id=quote(str(data_retrieval_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTDataRetrievalTeam | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTDataRetrievalTeam.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTDataRetrievalTeam | RESTExceptionInfo]:
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTDataRetrievalTeam | RESTExceptionInfo]:
    """Get Teams

     Returns a collection of teams whose backed-up data was retrieved from object storage repository by a
    retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTDataRetrievalTeam | RESTExceptionInfo]
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
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTDataRetrievalTeam | RESTExceptionInfo | None:
    """Get Teams

     Returns a collection of teams whose backed-up data was retrieved from object storage repository by a
    retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTDataRetrievalTeam | RESTExceptionInfo
    """

    return sync_detailed(
        data_retrieval_id=data_retrieval_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTDataRetrievalTeam | RESTExceptionInfo]:
    """Get Teams

     Returns a collection of teams whose backed-up data was retrieved from object storage repository by a
    retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTDataRetrievalTeam | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        data_retrieval_id=data_retrieval_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTDataRetrievalTeam | RESTExceptionInfo | None:
    """Get Teams

     Returns a collection of teams whose backed-up data was retrieved from object storage repository by a
    retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTDataRetrievalTeam | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            data_retrieval_id=data_retrieval_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
