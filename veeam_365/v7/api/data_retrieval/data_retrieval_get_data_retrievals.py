from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_data_retrieval_composed import RESTDataRetrievalComposed
from ...models.rest_data_retrieval_data_state import RESTDataRetrievalDataState
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    data_state: RESTDataRetrievalDataState | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organizationId"] = json_organization_id

    json_repository_id: str | Unset = UNSET
    if not isinstance(repository_id, Unset):
        json_repository_id = str(repository_id)
    params["repositoryId"] = json_repository_id

    json_data_state: str | Unset = UNSET
    if not isinstance(data_state, Unset):
        json_data_state = data_state.value

    params["dataState"] = json_data_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v7/DataRetrievals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTDataRetrievalComposed]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTDataRetrievalComposed.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTDataRetrievalComposed]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    data_state: RESTDataRetrievalDataState | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTDataRetrievalComposed]]:
    """Get Retrieval Jobs

     Returns a list of configured retrieval jobs.

    Args:
        organization_id (UUID | Unset):
        repository_id (UUID | Unset):
        data_state (RESTDataRetrievalDataState | Unset): Status of the backed-up data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTDataRetrievalComposed]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        repository_id=repository_id,
        data_state=data_state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    data_state: RESTDataRetrievalDataState | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTDataRetrievalComposed] | None:
    """Get Retrieval Jobs

     Returns a list of configured retrieval jobs.

    Args:
        organization_id (UUID | Unset):
        repository_id (UUID | Unset):
        data_state (RESTDataRetrievalDataState | Unset): Status of the backed-up data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTDataRetrievalComposed]
    """

    return sync_detailed(
        client=client,
        organization_id=organization_id,
        repository_id=repository_id,
        data_state=data_state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    data_state: RESTDataRetrievalDataState | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTDataRetrievalComposed]]:
    """Get Retrieval Jobs

     Returns a list of configured retrieval jobs.

    Args:
        organization_id (UUID | Unset):
        repository_id (UUID | Unset):
        data_state (RESTDataRetrievalDataState | Unset): Status of the backed-up data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTDataRetrievalComposed]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        repository_id=repository_id,
        data_state=data_state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    data_state: RESTDataRetrievalDataState | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTDataRetrievalComposed] | None:
    """Get Retrieval Jobs

     Returns a list of configured retrieval jobs.

    Args:
        organization_id (UUID | Unset):
        repository_id (UUID | Unset):
        data_state (RESTDataRetrievalDataState | Unset): Status of the backed-up data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTDataRetrievalComposed]
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_id=organization_id,
            repository_id=repository_id,
            data_state=data_state,
        )
    ).parsed
