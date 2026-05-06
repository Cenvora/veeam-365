from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_backup_team_data import RESTBackupTeamData
from ...models.rest_exception_info import RESTExceptionInfo
from typing import cast
from uuid import UUID



def _get_kwargs(
    repository_id: UUID,
    team_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/BackupRepositories/{repository_id}/TeamData/{team_id}".format(repository_id=quote(str(repository_id), safe=""),team_id=quote(str(team_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTBackupTeamData | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTBackupTeamData.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTBackupTeamData | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: UUID,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTBackupTeamData | RESTExceptionInfo]:
    """ Get Teams Data by Repository and Team ID

     Returns a backed-up team with the specified ID whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupTeamData | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        repository_id=repository_id,
team_id=team_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    repository_id: UUID,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> RESTBackupTeamData | RESTExceptionInfo | None:
    """ Get Teams Data by Repository and Team ID

     Returns a backed-up team with the specified ID whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupTeamData | RESTExceptionInfo
     """


    return sync_detailed(
        repository_id=repository_id,
team_id=team_id,
client=client,

    ).parsed

async def asyncio_detailed(
    repository_id: UUID,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTBackupTeamData | RESTExceptionInfo]:
    """ Get Teams Data by Repository and Team ID

     Returns a backed-up team with the specified ID whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTBackupTeamData | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        repository_id=repository_id,
team_id=team_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    repository_id: UUID,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> RESTBackupTeamData | RESTExceptionInfo | None:
    """ Get Teams Data by Repository and Team ID

     Returns a backed-up team with the specified ID whose data is stored in a backup repository with the
    specified ID.

    Args:
        repository_id (UUID):
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTBackupTeamData | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        repository_id=repository_id,
team_id=team_id,
client=client,

    )).parsed
