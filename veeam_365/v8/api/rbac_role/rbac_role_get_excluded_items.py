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

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/RbacRoles/{role_id}/excludedItems".format(role_id=quote(str(role_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | list[RESTRbacItemComposed]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = RESTRbacItemComposed.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | list[RESTRbacItemComposed]]:
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

) -> Response[RESTExceptionInfo | list[RESTRbacItemComposed]]:
    """ Get Excluded Objects

     Returns a resource representation of objects excluded from the scope of a restore operator role with
    the specified ID. Restore operators are not allowed to explore and restore data from backups created
    by Veeam Backup for Microsoft 365 for these objects.

    Args:
        role_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTRbacItemComposed]]
     """


    kwargs = _get_kwargs(
        role_id=role_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | list[RESTRbacItemComposed] | None:
    """ Get Excluded Objects

     Returns a resource representation of objects excluded from the scope of a restore operator role with
    the specified ID. Restore operators are not allowed to explore and restore data from backups created
    by Veeam Backup for Microsoft 365 for these objects.

    Args:
        role_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTRbacItemComposed]
     """


    return sync_detailed(
        role_id=role_id,
client=client,

    ).parsed

async def asyncio_detailed(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | list[RESTRbacItemComposed]]:
    """ Get Excluded Objects

     Returns a resource representation of objects excluded from the scope of a restore operator role with
    the specified ID. Restore operators are not allowed to explore and restore data from backups created
    by Veeam Backup for Microsoft 365 for these objects.

    Args:
        role_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTRbacItemComposed]]
     """


    kwargs = _get_kwargs(
        role_id=role_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    role_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | list[RESTRbacItemComposed] | None:
    """ Get Excluded Objects

     Returns a resource representation of objects excluded from the scope of a restore operator role with
    the specified ID. Restore operators are not allowed to explore and restore data from backups created
    by Veeam Backup for Microsoft 365 for these objects.

    Args:
        role_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTRbacItemComposed]
     """


    return (await asyncio_detailed(
        role_id=role_id,
client=client,

    )).parsed
