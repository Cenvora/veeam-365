from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_application import PageOfRESTApplication
from ...models.rest_application_from_client import RESTApplicationFromClient
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    *,
    body: RESTApplicationFromClient,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/Organizations/{organization_id}/Applications".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTApplication | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTApplication.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTApplication | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTApplicationFromClient,
) -> Response[PageOfRESTApplication | RESTExceptionInfo]:
    """Create Applications in Microsoft Entra

     Creates Microsoft Entra applications in Microsoft Entra ID using the device code.

    Args:
        organization_id (UUID):
        body (RESTApplicationFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTApplication | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTApplicationFromClient,
) -> PageOfRESTApplication | RESTExceptionInfo | None:
    """Create Applications in Microsoft Entra

     Creates Microsoft Entra applications in Microsoft Entra ID using the device code.

    Args:
        organization_id (UUID):
        body (RESTApplicationFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTApplication | RESTExceptionInfo
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTApplicationFromClient,
) -> Response[PageOfRESTApplication | RESTExceptionInfo]:
    """Create Applications in Microsoft Entra

     Creates Microsoft Entra applications in Microsoft Entra ID using the device code.

    Args:
        organization_id (UUID):
        body (RESTApplicationFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTApplication | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTApplicationFromClient,
) -> PageOfRESTApplication | RESTExceptionInfo | None:
    """Create Applications in Microsoft Entra

     Creates Microsoft Entra applications in Microsoft Entra ID using the device code.

    Args:
        organization_id (UUID):
        body (RESTApplicationFromClient):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTApplication | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            body=body,
        )
    ).parsed
