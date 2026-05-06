from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_device_code_request_options import RESTDeviceCodeRequestOptions
from ...models.rest_device_code_response import RESTDeviceCodeResponse
from ...models.rest_exception_info import RESTExceptionInfo
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    *,
    body: RESTDeviceCodeRequestOptions,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/restoreDeviceCode".format(restore_session_id=quote(str(restore_session_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTDeviceCodeResponse | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTDeviceCodeResponse.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTDeviceCodeResponse | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTDeviceCodeRequestOptions,

) -> Response[RESTDeviceCodeResponse | RESTExceptionInfo]:
    """ Get Device Code

     Allows you to obtain a device code from Microsoft Identity platform to restore data of Microsoft 365
    organizations added using modern app-only authentication.

    Args:
        restore_session_id (UUID):
        body (RESTDeviceCodeRequestOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTDeviceCodeResponse | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTDeviceCodeRequestOptions,

) -> RESTDeviceCodeResponse | RESTExceptionInfo | None:
    """ Get Device Code

     Allows you to obtain a device code from Microsoft Identity platform to restore data of Microsoft 365
    organizations added using modern app-only authentication.

    Args:
        restore_session_id (UUID):
        body (RESTDeviceCodeRequestOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTDeviceCodeResponse | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTDeviceCodeRequestOptions,

) -> Response[RESTDeviceCodeResponse | RESTExceptionInfo]:
    """ Get Device Code

     Allows you to obtain a device code from Microsoft Identity platform to restore data of Microsoft 365
    organizations added using modern app-only authentication.

    Args:
        restore_session_id (UUID):
        body (RESTDeviceCodeRequestOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTDeviceCodeResponse | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTDeviceCodeRequestOptions,

) -> RESTDeviceCodeResponse | RESTExceptionInfo | None:
    """ Get Device Code

     Allows you to obtain a device code from Microsoft Identity platform to restore data of Microsoft 365
    organizations added using modern app-only authentication.

    Args:
        restore_session_id (UUID):
        body (RESTDeviceCodeRequestOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTDeviceCodeResponse | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
client=client,
body=body,

    )).parsed
