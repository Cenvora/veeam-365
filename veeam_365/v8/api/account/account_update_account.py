from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_account_to_send import RESTAccountToSend
from ...models.rest_exception_info import RESTExceptionInfo
from typing import cast
from uuid import UUID



def _get_kwargs(
    account_id: UUID,
    *,
    body: RESTAccountToSend,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v8/Accounts/{account_id}".format(account_id=quote(str(account_id), safe=""),),
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
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTAccountToSend,

) -> Response[Any | RESTExceptionInfo]:
    """ Edit Account

     Modifies cloud credentials with the specified ID.

    Args:
        account_id (UUID):
        body (RESTAccountToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTAccountToSend,

) -> Any | RESTExceptionInfo | None:
    """ Edit Account

     Modifies cloud credentials with the specified ID.

    Args:
        account_id (UUID):
        body (RESTAccountToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return sync_detailed(
        account_id=account_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTAccountToSend,

) -> Response[Any | RESTExceptionInfo]:
    """ Edit Account

     Modifies cloud credentials with the specified ID.

    Args:
        account_id (UUID):
        body (RESTAccountToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTAccountToSend,

) -> Any | RESTExceptionInfo | None:
    """ Edit Account

     Modifies cloud credentials with the specified ID.

    Args:
        account_id (UUID):
        body (RESTAccountToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        account_id=account_id,
client=client,
body=body,

    )).parsed
