from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_encryption_key import RESTEncryptionKey
from ...models.rest_exception_info import RESTExceptionInfo
from typing import cast
from uuid import UUID



def _get_kwargs(
    key_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/EncryptionKeys/{key_id}".format(key_id=quote(str(key_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTEncryptionKey | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTEncryptionKey.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTEncryptionKey | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTEncryptionKey | RESTExceptionInfo]:
    """ Get Encryption Password Properties

     Returns properties of an encryption password with the specified ID.

    Args:
        key_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTEncryptionKey | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        key_id=key_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    key_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTEncryptionKey | RESTExceptionInfo | None:
    """ Get Encryption Password Properties

     Returns properties of an encryption password with the specified ID.

    Args:
        key_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTEncryptionKey | RESTExceptionInfo
     """


    return sync_detailed(
        key_id=key_id,
client=client,

    ).parsed

async def asyncio_detailed(
    key_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTEncryptionKey | RESTExceptionInfo]:
    """ Get Encryption Password Properties

     Returns properties of an encryption password with the specified ID.

    Args:
        key_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTEncryptionKey | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        key_id=key_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    key_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTEncryptionKey | RESTExceptionInfo | None:
    """ Get Encryption Password Properties

     Returns properties of an encryption password with the specified ID.

    Args:
        key_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTEncryptionKey | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        key_id=key_id,
client=client,

    )).parsed
