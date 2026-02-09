from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.o_auth_token_response import OAuthTokenResponse
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.token_data_body import TokenDataBody
from ...models.token_json_body import TokenJsonBody
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: TokenDataBody | TokenJsonBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v6/token",
    }

    if isinstance(body, TokenDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, TokenJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OAuthTokenResponse | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = OAuthTokenResponse.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OAuthTokenResponse | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TokenDataBody | TokenJsonBody | Unset = UNSET,
) -> Response[OAuthTokenResponse | RESTExceptionInfo]:
    """
    Args:
        body (TokenDataBody):
        body (TokenJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuthTokenResponse | RESTExceptionInfo]
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
    body: TokenDataBody | TokenJsonBody | Unset = UNSET,
) -> OAuthTokenResponse | RESTExceptionInfo | None:
    """
    Args:
        body (TokenDataBody):
        body (TokenJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OAuthTokenResponse | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TokenDataBody | TokenJsonBody | Unset = UNSET,
) -> Response[OAuthTokenResponse | RESTExceptionInfo]:
    """
    Args:
        body (TokenDataBody):
        body (TokenJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuthTokenResponse | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TokenDataBody | TokenJsonBody | Unset = UNSET,
) -> OAuthTokenResponse | RESTExceptionInfo | None:
    """
    Args:
        body (TokenDataBody):
        body (TokenJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OAuthTokenResponse | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
