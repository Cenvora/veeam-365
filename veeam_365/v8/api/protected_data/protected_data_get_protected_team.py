from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_protected_team import RESTProtectedTeam
from typing import cast



def _get_kwargs(
    protected_team_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/ProtectedTeams/{protected_team_id}".format(protected_team_id=quote(str(protected_team_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTProtectedTeam:
    if response.status_code == 200:
        response_200 = RESTProtectedTeam.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTProtectedTeam]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    protected_team_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | RESTProtectedTeam]:
    """ Get Protected Team

     Returns a resource representation of a protected team with the specified ID.

    Args:
        protected_team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTProtectedTeam]
     """


    kwargs = _get_kwargs(
        protected_team_id=protected_team_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    protected_team_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTProtectedTeam | None:
    """ Get Protected Team

     Returns a resource representation of a protected team with the specified ID.

    Args:
        protected_team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTProtectedTeam
     """


    return sync_detailed(
        protected_team_id=protected_team_id,
client=client,

    ).parsed

async def asyncio_detailed(
    protected_team_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | RESTProtectedTeam]:
    """ Get Protected Team

     Returns a resource representation of a protected team with the specified ID.

    Args:
        protected_team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTProtectedTeam]
     """


    kwargs = _get_kwargs(
        protected_team_id=protected_team_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    protected_team_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTProtectedTeam | None:
    """ Get Protected Team

     Returns a resource representation of a protected team with the specified ID.

    Args:
        protected_team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTProtectedTeam
     """


    return (await asyncio_detailed(
        protected_team_id=protected_team_id,
client=client,

    )).parsed
