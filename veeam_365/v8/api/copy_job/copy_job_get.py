from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_copy_job import PageOfRESTCopyJob
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    organization_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

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

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/CopyJobs",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTCopyJob | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTCopyJob.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTCopyJob | RESTExceptionInfo]:
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[PageOfRESTCopyJob | RESTExceptionInfo]:
    """ Get Backup Copy Jobs

     Returns a collection of configured backup copy jobs.

    Args:
        organization_id (UUID | Unset):
        repository_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTCopyJob | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
repository_id=repository_id,
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
    organization_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> PageOfRESTCopyJob | RESTExceptionInfo | None:
    """ Get Backup Copy Jobs

     Returns a collection of configured backup copy jobs.

    Args:
        organization_id (UUID | Unset):
        repository_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTCopyJob | RESTExceptionInfo
     """


    return sync_detailed(
        client=client,
organization_id=organization_id,
repository_id=repository_id,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[PageOfRESTCopyJob | RESTExceptionInfo]:
    """ Get Backup Copy Jobs

     Returns a collection of configured backup copy jobs.

    Args:
        organization_id (UUID | Unset):
        repository_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTCopyJob | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
repository_id=repository_id,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> PageOfRESTCopyJob | RESTExceptionInfo | None:
    """ Get Backup Copy Jobs

     Returns a collection of configured backup copy jobs.

    Args:
        organization_id (UUID | Unset):
        repository_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTCopyJob | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        client=client,
organization_id=organization_id,
repository_id=repository_id,
limit=limit,
offset=offset,

    )).parsed
