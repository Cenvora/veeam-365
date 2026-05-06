from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_create_backup_job import RESTCreateBackupJob
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_job import RESTJob
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: RESTCreateBackupJob,
    skip_item_update: bool | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["skipItemUpdate"] = skip_item_update


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/Jobs",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTJob:
    if response.status_code == 201:
        response_201 = RESTJob.from_dict(response.json())



        return response_201

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTJob]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTCreateBackupJob,
    skip_item_update: bool | Unset = UNSET,

) -> Response[RESTExceptionInfo | RESTJob]:
    """ Create Backup Job

     Creates a backup job for an organization with the specified ID.

    Args:
        skip_item_update (bool | Unset):
        body (RESTCreateBackupJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTJob]
     """


    kwargs = _get_kwargs(
        body=body,
skip_item_update=skip_item_update,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RESTCreateBackupJob,
    skip_item_update: bool | Unset = UNSET,

) -> RESTExceptionInfo | RESTJob | None:
    """ Create Backup Job

     Creates a backup job for an organization with the specified ID.

    Args:
        skip_item_update (bool | Unset):
        body (RESTCreateBackupJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTJob
     """


    return sync_detailed(
        client=client,
body=body,
skip_item_update=skip_item_update,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTCreateBackupJob,
    skip_item_update: bool | Unset = UNSET,

) -> Response[RESTExceptionInfo | RESTJob]:
    """ Create Backup Job

     Creates a backup job for an organization with the specified ID.

    Args:
        skip_item_update (bool | Unset):
        body (RESTCreateBackupJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTJob]
     """


    kwargs = _get_kwargs(
        body=body,
skip_item_update=skip_item_update,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RESTCreateBackupJob,
    skip_item_update: bool | Unset = UNSET,

) -> RESTExceptionInfo | RESTJob | None:
    """ Create Backup Job

     Creates a backup job for an organization with the specified ID.

    Args:
        skip_item_update (bool | Unset):
        body (RESTCreateBackupJob):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTJob
     """


    return (await asyncio_detailed(
        client=client,
body=body,
skip_item_update=skip_item_update,

    )).parsed
