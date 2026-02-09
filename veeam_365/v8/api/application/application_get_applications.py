from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_application import PageOfRESTApplication
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: UUID,
    *,
    display_name: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["displayName"] = display_name

    params["tag"] = tag

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/Organizations/{organization_id}/Applications".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
        "params": params,
    }

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
    display_name: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTApplication | RESTExceptionInfo]:
    """Get Applications from Microsoft Entra

     Returns a collection of existing applications for the specified Microsoft 365 organization from
    Microsoft Entra ID.

    Args:
        organization_id (UUID):
        display_name (str | Unset):
        tag (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTApplication | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        display_name=display_name,
        tag=tag,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    display_name: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTApplication | RESTExceptionInfo | None:
    """Get Applications from Microsoft Entra

     Returns a collection of existing applications for the specified Microsoft 365 organization from
    Microsoft Entra ID.

    Args:
        organization_id (UUID):
        display_name (str | Unset):
        tag (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTApplication | RESTExceptionInfo
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        display_name=display_name,
        tag=tag,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    display_name: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[PageOfRESTApplication | RESTExceptionInfo]:
    """Get Applications from Microsoft Entra

     Returns a collection of existing applications for the specified Microsoft 365 organization from
    Microsoft Entra ID.

    Args:
        organization_id (UUID):
        display_name (str | Unset):
        tag (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTApplication | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        display_name=display_name,
        tag=tag,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    display_name: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> PageOfRESTApplication | RESTExceptionInfo | None:
    """Get Applications from Microsoft Entra

     Returns a collection of existing applications for the specified Microsoft 365 organization from
    Microsoft Entra ID.

    Args:
        organization_id (UUID):
        display_name (str | Unset):
        tag (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

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
            display_name=display_name,
            tag=tag,
            limit=limit,
            offset=offset,
        )
    ).parsed
