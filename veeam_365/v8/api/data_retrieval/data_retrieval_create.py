from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_data_retrieval_composed import RESTDataRetrievalComposed
from ...models.rest_data_retrieval_from_client import RESTDataRetrievalFromClient
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RESTDataRetrievalFromClient,
    force: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/DataRetrievals",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTDataRetrievalComposed | RESTExceptionInfo:
    if response.status_code == 201:
        response_201 = RESTDataRetrievalComposed.from_dict(response.json())

        return response_201

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTDataRetrievalComposed | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTDataRetrievalFromClient,
    force: bool | Unset = False,
) -> Response[RESTDataRetrievalComposed | RESTExceptionInfo]:
    r"""Create Data Retrieval Job

     Creates a retrieval job. <div class=\"note\"><strong>NOTE</strong> </br> You must create individual
    retrieval jobs for different types of objects whose backed-up data you want to retrieve. </div>

    Args:
        force (bool | Unset):  Default: False.
        body (RESTDataRetrievalFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTDataRetrievalComposed | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        body=body,
        force=force,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RESTDataRetrievalFromClient,
    force: bool | Unset = False,
) -> RESTDataRetrievalComposed | RESTExceptionInfo | None:
    r"""Create Data Retrieval Job

     Creates a retrieval job. <div class=\"note\"><strong>NOTE</strong> </br> You must create individual
    retrieval jobs for different types of objects whose backed-up data you want to retrieve. </div>

    Args:
        force (bool | Unset):  Default: False.
        body (RESTDataRetrievalFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTDataRetrievalComposed | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        body=body,
        force=force,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTDataRetrievalFromClient,
    force: bool | Unset = False,
) -> Response[RESTDataRetrievalComposed | RESTExceptionInfo]:
    r"""Create Data Retrieval Job

     Creates a retrieval job. <div class=\"note\"><strong>NOTE</strong> </br> You must create individual
    retrieval jobs for different types of objects whose backed-up data you want to retrieve. </div>

    Args:
        force (bool | Unset):  Default: False.
        body (RESTDataRetrievalFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTDataRetrievalComposed | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        body=body,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RESTDataRetrievalFromClient,
    force: bool | Unset = False,
) -> RESTDataRetrievalComposed | RESTExceptionInfo | None:
    r"""Create Data Retrieval Job

     Creates a retrieval job. <div class=\"note\"><strong>NOTE</strong> </br> You must create individual
    retrieval jobs for different types of objects whose backed-up data you want to retrieve. </div>

    Args:
        force (bool | Unset):  Default: False.
        body (RESTDataRetrievalFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTDataRetrievalComposed | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            force=force,
        )
    ).parsed
