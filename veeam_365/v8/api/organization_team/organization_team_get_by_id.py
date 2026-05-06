from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.organization_team_get_by_id_data_source import OrganizationTeamGetByIdDataSource
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_team import RESTTeam
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    organization_id: UUID,
    team_id: str,
    *,
    data_source: OrganizationTeamGetByIdDataSource | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_data_source: str | Unset = UNSET
    if not isinstance(data_source, Unset):
        json_data_source = data_source.value

    params["dataSource"] = json_data_source


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/Organizations/{organization_id}/Teams/{team_id}".format(organization_id=quote(str(organization_id), safe=""),team_id=quote(str(team_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTTeam:
    if response.status_code == 200:
        response_200 = RESTTeam.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTTeam]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    data_source: OrganizationTeamGetByIdDataSource | Unset = UNSET,

) -> Response[RESTExceptionInfo | RESTTeam]:
    """ Get Team

     Returns a resource representation of an organization team with the specified ID.

    Args:
        organization_id (UUID):
        team_id (str):
        data_source (OrganizationTeamGetByIdDataSource | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTTeam]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
team_id=team_id,
data_source=data_source,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    organization_id: UUID,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    data_source: OrganizationTeamGetByIdDataSource | Unset = UNSET,

) -> RESTExceptionInfo | RESTTeam | None:
    """ Get Team

     Returns a resource representation of an organization team with the specified ID.

    Args:
        organization_id (UUID):
        team_id (str):
        data_source (OrganizationTeamGetByIdDataSource | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTTeam
     """


    return sync_detailed(
        organization_id=organization_id,
team_id=team_id,
client=client,
data_source=data_source,

    ).parsed

async def asyncio_detailed(
    organization_id: UUID,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    data_source: OrganizationTeamGetByIdDataSource | Unset = UNSET,

) -> Response[RESTExceptionInfo | RESTTeam]:
    """ Get Team

     Returns a resource representation of an organization team with the specified ID.

    Args:
        organization_id (UUID):
        team_id (str):
        data_source (OrganizationTeamGetByIdDataSource | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTTeam]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
team_id=team_id,
data_source=data_source,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    organization_id: UUID,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    data_source: OrganizationTeamGetByIdDataSource | Unset = UNSET,

) -> RESTExceptionInfo | RESTTeam | None:
    """ Get Team

     Returns a resource representation of an organization team with the specified ID.

    Args:
        organization_id (UUID):
        team_id (str):
        data_source (OrganizationTeamGetByIdDataSource | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTTeam
     """


    return (await asyncio_detailed(
        organization_id=organization_id,
team_id=team_id,
client=client,
data_source=data_source,

    )).parsed
