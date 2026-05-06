from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_rbac_item_composed import RESTRbacItemComposed
from typing import cast
from uuid import UUID



def _get_kwargs(
    role_id: UUID,
    *,
    body: list[RESTRbacItemComposed],

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RbacRoles/{role_id}/excludedItems".format(role_id=quote(str(role_id), safe=""),),
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



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTRbacItemComposed],

) -> Response[Any | RESTExceptionInfo]:
    """ Add Excluded Objects

     Excludes objects from the scope of a restore operator role with the specified ID. Restore operators
    will not be able to explore and restore data from backups created by Veeam Backup for Microsoft 365
    for these objects.

    Args:
        role_id (UUID):
        body (list[RESTRbacItemComposed]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        role_id=role_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTRbacItemComposed],

) -> Any | RESTExceptionInfo | None:
    """ Add Excluded Objects

     Excludes objects from the scope of a restore operator role with the specified ID. Restore operators
    will not be able to explore and restore data from backups created by Veeam Backup for Microsoft 365
    for these objects.

    Args:
        role_id (UUID):
        body (list[RESTRbacItemComposed]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return sync_detailed(
        role_id=role_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTRbacItemComposed],

) -> Response[Any | RESTExceptionInfo]:
    """ Add Excluded Objects

     Excludes objects from the scope of a restore operator role with the specified ID. Restore operators
    will not be able to explore and restore data from backups created by Veeam Backup for Microsoft 365
    for these objects.

    Args:
        role_id (UUID):
        body (list[RESTRbacItemComposed]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        role_id=role_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[RESTRbacItemComposed],

) -> Any | RESTExceptionInfo | None:
    """ Add Excluded Objects

     Excludes objects from the scope of a restore operator role with the specified ID. Restore operators
    will not be able to explore and restore data from backups created by Veeam Backup for Microsoft 365
    for these objects.

    Args:
        role_id (UUID):
        body (list[RESTRbacItemComposed]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        role_id=role_id,
client=client,
body=body,

    )).parsed
