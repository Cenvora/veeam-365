from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_protected_user import RESTProtectedUser
from typing import cast



def _get_kwargs(
    protected_user_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/ProtectedUsers/{protected_user_id}".format(protected_user_id=quote(str(protected_user_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTProtectedUser:
    if response.status_code == 200:
        response_200 = RESTProtectedUser.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTProtectedUser]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    protected_user_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | RESTProtectedUser]:
    """ Get Protected User

     Returns a resource representation of a protected user with the specified ID.

    Args:
        protected_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTProtectedUser]
     """


    kwargs = _get_kwargs(
        protected_user_id=protected_user_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    protected_user_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTProtectedUser | None:
    """ Get Protected User

     Returns a resource representation of a protected user with the specified ID.

    Args:
        protected_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTProtectedUser
     """


    return sync_detailed(
        protected_user_id=protected_user_id,
client=client,

    ).parsed

async def asyncio_detailed(
    protected_user_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | RESTProtectedUser]:
    """ Get Protected User

     Returns a resource representation of a protected user with the specified ID.

    Args:
        protected_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTProtectedUser]
     """


    kwargs = _get_kwargs(
        protected_user_id=protected_user_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    protected_user_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTProtectedUser | None:
    """ Get Protected User

     Returns a resource representation of a protected user with the specified ID.

    Args:
        protected_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTProtectedUser
     """


    return (await asyncio_detailed(
        protected_user_id=protected_user_id,
client=client,

    )).parsed
