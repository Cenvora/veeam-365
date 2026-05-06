from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from typing import cast



def _get_kwargs(
    licensed_user_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v8/LicensedUsers/{licensed_user_id}".format(licensed_user_id=quote(str(licensed_user_id), safe=""),),
    }


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
    licensed_user_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | RESTExceptionInfo]:
    r""" Revoke License from Users

     Removes information about a licensed user from Veeam Backup for Microsoft 365.

    When you remove information about a licensed user, Veeam Backup for Microsoft 365 revokes the
    license from this user. You can use a unit in the license to back up data of other user in your
    Microsoft 365 organization. <div class=\"note\"><strong>NOTE</strong> </br> You cannot revoke a
    license from a user if a backup repository contains data of this user. </div>

    Args:
        licensed_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        licensed_user_id=licensed_user_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    licensed_user_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | RESTExceptionInfo | None:
    r""" Revoke License from Users

     Removes information about a licensed user from Veeam Backup for Microsoft 365.

    When you remove information about a licensed user, Veeam Backup for Microsoft 365 revokes the
    license from this user. You can use a unit in the license to back up data of other user in your
    Microsoft 365 organization. <div class=\"note\"><strong>NOTE</strong> </br> You cannot revoke a
    license from a user if a backup repository contains data of this user. </div>

    Args:
        licensed_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return sync_detailed(
        licensed_user_id=licensed_user_id,
client=client,

    ).parsed

async def asyncio_detailed(
    licensed_user_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | RESTExceptionInfo]:
    r""" Revoke License from Users

     Removes information about a licensed user from Veeam Backup for Microsoft 365.

    When you remove information about a licensed user, Veeam Backup for Microsoft 365 revokes the
    license from this user. You can use a unit in the license to back up data of other user in your
    Microsoft 365 organization. <div class=\"note\"><strong>NOTE</strong> </br> You cannot revoke a
    license from a user if a backup repository contains data of this user. </div>

    Args:
        licensed_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        licensed_user_id=licensed_user_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    licensed_user_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | RESTExceptionInfo | None:
    r""" Revoke License from Users

     Removes information about a licensed user from Veeam Backup for Microsoft 365.

    When you remove information about a licensed user, Veeam Backup for Microsoft 365 revokes the
    license from this user. You can use a unit in the license to back up data of other user in your
    Microsoft 365 organization. <div class=\"note\"><strong>NOTE</strong> </br> You cannot revoke a
    license from a user if a backup repository contains data of this user. </div>

    Args:
        licensed_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        licensed_user_id=licensed_user_id,
client=client,

    )).parsed
