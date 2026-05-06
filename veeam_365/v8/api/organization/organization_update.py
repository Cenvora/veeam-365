from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_organization_composed import RestOrganizationComposed
from typing import cast
from uuid import UUID



def _get_kwargs(
    organization_id: UUID,
    *,
    body: RestOrganizationComposed,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v8/Organizations/{organization_id}".format(organization_id=quote(str(organization_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RESTExceptionInfo:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RestOrganizationComposed,

) -> Response[Any | RESTExceptionInfo]:
    """ Edit Organization

     Modifies settings of an organization with the specified ID.

    Args:
        organization_id (UUID):
        body (RestOrganizationComposed):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RestOrganizationComposed,

) -> Any | RESTExceptionInfo | None:
    """ Edit Organization

     Modifies settings of an organization with the specified ID.

    Args:
        organization_id (UUID):
        body (RestOrganizationComposed):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return sync_detailed(
        organization_id=organization_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RestOrganizationComposed,

) -> Response[Any | RESTExceptionInfo]:
    """ Edit Organization

     Modifies settings of an organization with the specified ID.

    Args:
        organization_id (UUID):
        body (RestOrganizationComposed):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RestOrganizationComposed,

) -> Any | RESTExceptionInfo | None:
    """ Edit Organization

     Modifies settings of an organization with the specified ID.

    Args:
        organization_id (UUID):
        body (RestOrganizationComposed):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        organization_id=organization_id,
client=client,
body=body,

    )).parsed
