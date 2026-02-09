from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_job_item_composed import RESTJobItemComposed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: UUID,
    *,
    body: list[RESTJobItemComposed],
    skip_item_update: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["skipItemUpdate"] = skip_item_update

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/Jobs/{job_id}/SelectedItems".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RESTExceptionInfo:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTJobItemComposed],
    skip_item_update: bool | Unset = UNSET,
) -> Response[Any | RESTExceptionInfo]:
    """Add Items to Backup Job

     Adds items to the processing list of a backup job with the specified ID.

    Args:
        job_id (UUID):
        skip_item_update (bool | Unset):
        body (list[RESTJobItemComposed]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
        skip_item_update=skip_item_update,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTJobItemComposed],
    skip_item_update: bool | Unset = UNSET,
) -> Any | RESTExceptionInfo | None:
    """Add Items to Backup Job

     Adds items to the processing list of a backup job with the specified ID.

    Args:
        job_id (UUID):
        skip_item_update (bool | Unset):
        body (list[RESTJobItemComposed]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        body=body,
        skip_item_update=skip_item_update,
    ).parsed


async def asyncio_detailed(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTJobItemComposed],
    skip_item_update: bool | Unset = UNSET,
) -> Response[Any | RESTExceptionInfo]:
    """Add Items to Backup Job

     Adds items to the processing list of a backup job with the specified ID.

    Args:
        job_id (UUID):
        skip_item_update (bool | Unset):
        body (list[RESTJobItemComposed]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
        skip_item_update=skip_item_update,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTJobItemComposed],
    skip_item_update: bool | Unset = UNSET,
) -> Any | RESTExceptionInfo | None:
    """Add Items to Backup Job

     Adds items to the processing list of a backup job with the specified ID.

    Args:
        job_id (UUID):
        skip_item_update (bool | Unset):
        body (list[RESTJobItemComposed]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
            skip_item_update=skip_item_update,
        )
    ).parsed
