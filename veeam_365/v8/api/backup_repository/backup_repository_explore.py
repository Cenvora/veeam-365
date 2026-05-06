from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_explore_options import RESTExploreOptions
from ...models.rest_restore_session import RESTRestoreSession
from typing import cast
from uuid import UUID



def _get_kwargs(
    repository_id: UUID,
    *,
    body: RESTExploreOptions,
    organization_id: UUID,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_organization_id = str(organization_id)
    params["organizationId"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/BackupRepositories/{repository_id}/explore".format(repository_id=quote(str(repository_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTRestoreSession:
    if response.status_code == 201:
        response_201 = RESTRestoreSession.from_dict(response.json())



        return response_201

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExploreOptions,
    organization_id: UUID,

) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    """ Create Restore Session for Backup Repository by Repository ID

     Creates and starts a restore session to explore and restore data from backup copies for a backup
    repository with the specified ID.

    Use this resource for Azure Blob Storage, Amazon S3 Standard, Amazon S3 Standard-Infrequent Access,
    Amazon S3 One Zone-Infrequent Access and Amazon S3 Glacier Instant Retrieval storage classes or S3
    Compatible object storage repositories.

    Args:
        repository_id (UUID):
        organization_id (UUID):
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSession]
     """


    kwargs = _get_kwargs(
        repository_id=repository_id,
body=body,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExploreOptions,
    organization_id: UUID,

) -> RESTExceptionInfo | RESTRestoreSession | None:
    """ Create Restore Session for Backup Repository by Repository ID

     Creates and starts a restore session to explore and restore data from backup copies for a backup
    repository with the specified ID.

    Use this resource for Azure Blob Storage, Amazon S3 Standard, Amazon S3 Standard-Infrequent Access,
    Amazon S3 One Zone-Infrequent Access and Amazon S3 Glacier Instant Retrieval storage classes or S3
    Compatible object storage repositories.

    Args:
        repository_id (UUID):
        organization_id (UUID):
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSession
     """


    return sync_detailed(
        repository_id=repository_id,
client=client,
body=body,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExploreOptions,
    organization_id: UUID,

) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    """ Create Restore Session for Backup Repository by Repository ID

     Creates and starts a restore session to explore and restore data from backup copies for a backup
    repository with the specified ID.

    Use this resource for Azure Blob Storage, Amazon S3 Standard, Amazon S3 Standard-Infrequent Access,
    Amazon S3 One Zone-Infrequent Access and Amazon S3 Glacier Instant Retrieval storage classes or S3
    Compatible object storage repositories.

    Args:
        repository_id (UUID):
        organization_id (UUID):
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSession]
     """


    kwargs = _get_kwargs(
        repository_id=repository_id,
body=body,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    repository_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExploreOptions,
    organization_id: UUID,

) -> RESTExceptionInfo | RESTRestoreSession | None:
    """ Create Restore Session for Backup Repository by Repository ID

     Creates and starts a restore session to explore and restore data from backup copies for a backup
    repository with the specified ID.

    Use this resource for Azure Blob Storage, Amazon S3 Standard, Amazon S3 Standard-Infrequent Access,
    Amazon S3 One Zone-Infrequent Access and Amazon S3 Glacier Instant Retrieval storage classes or S3
    Compatible object storage repositories.

    Args:
        repository_id (UUID):
        organization_id (UUID):
        body (RESTExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSession
     """


    return (await asyncio_detailed(
        repository_id=repository_id,
client=client,
body=body,
organization_id=organization_id,

    )).parsed
