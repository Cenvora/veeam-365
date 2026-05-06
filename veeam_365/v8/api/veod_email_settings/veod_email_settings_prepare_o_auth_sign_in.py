from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_prepare_o_auth_sign_in_request import RESTPrepareOAuthSignInRequest
from ...models.rest_prepare_o_auth_sign_in_response import RESTPrepareOAuthSignInResponse
from typing import cast



def _get_kwargs(
    *,
    body: RESTPrepareOAuthSignInRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/VeodEmailSettings/PrepareOAuthSignIn",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTPrepareOAuthSignInResponse:
    if response.status_code == 200:
        response_200 = RESTPrepareOAuthSignInResponse.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTPrepareOAuthSignInResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTPrepareOAuthSignInRequest,

) -> Response[RESTExceptionInfo | RESTPrepareOAuthSignInResponse]:
    """ Prepare to Authentication Request

     Prepares to create authentication request that allows you to acquire an access token. Veeam Explorer
    for Microsoft OneDrive for Business will send email messages on behalf of either a Microsoft 365
    account or a Google account.

    Args:
        body (RESTPrepareOAuthSignInRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTPrepareOAuthSignInResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RESTPrepareOAuthSignInRequest,

) -> RESTExceptionInfo | RESTPrepareOAuthSignInResponse | None:
    """ Prepare to Authentication Request

     Prepares to create authentication request that allows you to acquire an access token. Veeam Explorer
    for Microsoft OneDrive for Business will send email messages on behalf of either a Microsoft 365
    account or a Google account.

    Args:
        body (RESTPrepareOAuthSignInRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTPrepareOAuthSignInResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTPrepareOAuthSignInRequest,

) -> Response[RESTExceptionInfo | RESTPrepareOAuthSignInResponse]:
    """ Prepare to Authentication Request

     Prepares to create authentication request that allows you to acquire an access token. Veeam Explorer
    for Microsoft OneDrive for Business will send email messages on behalf of either a Microsoft 365
    account or a Google account.

    Args:
        body (RESTPrepareOAuthSignInRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTPrepareOAuthSignInResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RESTPrepareOAuthSignInRequest,

) -> RESTExceptionInfo | RESTPrepareOAuthSignInResponse | None:
    """ Prepare to Authentication Request

     Prepares to create authentication request that allows you to acquire an access token. Veeam Explorer
    for Microsoft OneDrive for Business will send email messages on behalf of either a Microsoft 365
    account or a Google account.

    Args:
        body (RESTPrepareOAuthSignInRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTPrepareOAuthSignInResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
