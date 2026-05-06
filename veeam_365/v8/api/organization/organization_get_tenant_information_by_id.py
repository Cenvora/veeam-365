from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_tenant_information import RESTTenantInformation
from typing import cast
from uuid import UUID



def _get_kwargs(
    organization_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/Organizations/{organization_id}/tenantInformation".format(organization_id=quote(str(organization_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTTenantInformation:
    if response.status_code == 200:
        response_200 = RESTTenantInformation.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTTenantInformation]:
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

) -> Response[RESTExceptionInfo | RESTTenantInformation]:
    """ Get Multi-Geo Tenants by Organization ID

     Returns a resource representation of Multi-Geo tenants for an organization with the specified ID.

    Args:
        organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTTenantInformation]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTTenantInformation | None:
    """ Get Multi-Geo Tenants by Organization ID

     Returns a resource representation of Multi-Geo tenants for an organization with the specified ID.

    Args:
        organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTTenantInformation
     """


    return sync_detailed(
        organization_id=organization_id,
client=client,

    ).parsed

async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | RESTTenantInformation]:
    """ Get Multi-Geo Tenants by Organization ID

     Returns a resource representation of Multi-Geo tenants for an organization with the specified ID.

    Args:
        organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTTenantInformation]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTTenantInformation | None:
    """ Get Multi-Geo Tenants by Organization ID

     Returns a resource representation of Multi-Geo tenants for an organization with the specified ID.

    Args:
        organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTTenantInformation
     """


    return (await asyncio_detailed(
        organization_id=organization_id,
client=client,

    )).parsed
