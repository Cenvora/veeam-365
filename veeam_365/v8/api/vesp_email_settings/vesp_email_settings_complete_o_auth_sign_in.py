from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_complete_o_auth_sign_in_request import RESTCompleteOAuthSignInRequest
from ...models.rest_complete_o_auth_sign_in_response import RESTCompleteOAuthSignInResponse
from ...models.rest_exception_info import RESTExceptionInfo
from typing import cast



def _get_kwargs(
    *,
    body: RESTCompleteOAuthSignInRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/VespEmailSettings/CompleteOAuthSignIn",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTCompleteOAuthSignInResponse | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTCompleteOAuthSignInResponse.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTCompleteOAuthSignInResponse | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTCompleteOAuthSignInRequest,

) -> Response[RESTCompleteOAuthSignInResponse | RESTExceptionInfo]:
    """ Complete Authentication

     Completes authentication to Google or Microsoft Identity platform that allows Veeam Explorer for
    Microsoft SharePoint to send email messages on behalf of either a Microsoft 365 account or a Google
    account.

    Args:
        body (RESTCompleteOAuthSignInRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTCompleteOAuthSignInResponse | RESTExceptionInfo]
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
    body: RESTCompleteOAuthSignInRequest,

) -> RESTCompleteOAuthSignInResponse | RESTExceptionInfo | None:
    """ Complete Authentication

     Completes authentication to Google or Microsoft Identity platform that allows Veeam Explorer for
    Microsoft SharePoint to send email messages on behalf of either a Microsoft 365 account or a Google
    account.

    Args:
        body (RESTCompleteOAuthSignInRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTCompleteOAuthSignInResponse | RESTExceptionInfo
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTCompleteOAuthSignInRequest,

) -> Response[RESTCompleteOAuthSignInResponse | RESTExceptionInfo]:
    """ Complete Authentication

     Completes authentication to Google or Microsoft Identity platform that allows Veeam Explorer for
    Microsoft SharePoint to send email messages on behalf of either a Microsoft 365 account or a Google
    account.

    Args:
        body (RESTCompleteOAuthSignInRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTCompleteOAuthSignInResponse | RESTExceptionInfo]
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
    body: RESTCompleteOAuthSignInRequest,

) -> RESTCompleteOAuthSignInResponse | RESTExceptionInfo | None:
    """ Complete Authentication

     Completes authentication to Google or Microsoft Identity platform that allows Veeam Explorer for
    Microsoft SharePoint to send email messages on behalf of either a Microsoft 365 account or a Google
    account.

    Args:
        body (RESTCompleteOAuthSignInRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTCompleteOAuthSignInResponse | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
