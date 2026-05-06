from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_data_retrieval_web import PageOfRESTDataRetrievalWeb
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



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
        "url": "/v8/DataRetrievals/{data_retrieval_id}/webs".format(data_retrieval_id=quote(str(data_retrieval_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTDataRetrievalWeb | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTDataRetrievalWeb.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTDataRetrievalWeb | RESTExceptionInfo]:
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

) -> Response[PageOfRESTDataRetrievalWeb | RESTExceptionInfo]:
    """ Get Sites

     Returns a collection of sites whose backed-up data was retrieved from object storage repository by a
    retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTDataRetrievalWeb | RESTExceptionInfo]
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

) -> PageOfRESTDataRetrievalWeb | RESTExceptionInfo | None:
    """ Get Sites

     Returns a collection of sites whose backed-up data was retrieved from object storage repository by a
    retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTDataRetrievalWeb | RESTExceptionInfo
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

) -> Response[PageOfRESTDataRetrievalWeb | RESTExceptionInfo]:
    """ Get Sites

     Returns a collection of sites whose backed-up data was retrieved from object storage repository by a
    retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTDataRetrievalWeb | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        data_retrieval_id=data_retrieval_id,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    data_retrieval_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> PageOfRESTDataRetrievalWeb | RESTExceptionInfo | None:
    """ Get Sites

     Returns a collection of sites whose backed-up data was retrieved from object storage repository by a
    retrieval job with the specified ID.

    Args:
        data_retrieval_id (UUID):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTDataRetrievalWeb | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        data_retrieval_id=data_retrieval_id,
client=client,
limit=limit,
offset=offset,

    )).parsed
