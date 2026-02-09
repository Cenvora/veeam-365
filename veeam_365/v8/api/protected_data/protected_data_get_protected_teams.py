from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.page_of_rest_protected_team import PageOfRESTProtectedTeam
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_id: UUID | Unset = UNSET,
    backed_up_organization_id: str | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    restore_point_id: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organizationId"] = json_organization_id

    params["backedUpOrganizationId"] = backed_up_organization_id

    json_repository_id: str | Unset = UNSET
    if not isinstance(repository_id, Unset):
        json_repository_id = str(repository_id)
    params["repositoryId"] = json_repository_id

    params["restorePointId"] = restore_point_id

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/ProtectedTeams",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageOfRESTProtectedTeam | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTProtectedTeam.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageOfRESTProtectedTeam | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    backed_up_organization_id: str | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    restore_point_id: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfRESTProtectedTeam | RESTExceptionInfo]:
    """Get Protected Teams

     Returns a collection of protected teams.

    Args:
        organization_id (UUID | Unset):
        backed_up_organization_id (str | Unset):
        repository_id (UUID | Unset):
        restore_point_id (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTProtectedTeam | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        backed_up_organization_id=backed_up_organization_id,
        repository_id=repository_id,
        restore_point_id=restore_point_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    backed_up_organization_id: str | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    restore_point_id: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfRESTProtectedTeam | RESTExceptionInfo | None:
    """Get Protected Teams

     Returns a collection of protected teams.

    Args:
        organization_id (UUID | Unset):
        backed_up_organization_id (str | Unset):
        repository_id (UUID | Unset):
        restore_point_id (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTProtectedTeam | RESTExceptionInfo
    """

    return sync_detailed(
        client=client,
        organization_id=organization_id,
        backed_up_organization_id=backed_up_organization_id,
        repository_id=repository_id,
        restore_point_id=restore_point_id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    backed_up_organization_id: str | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    restore_point_id: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[PageOfRESTProtectedTeam | RESTExceptionInfo]:
    """Get Protected Teams

     Returns a collection of protected teams.

    Args:
        organization_id (UUID | Unset):
        backed_up_organization_id (str | Unset):
        repository_id (UUID | Unset):
        restore_point_id (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTProtectedTeam | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        backed_up_organization_id=backed_up_organization_id,
        repository_id=repository_id,
        restore_point_id=restore_point_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    organization_id: UUID | Unset = UNSET,
    backed_up_organization_id: str | Unset = UNSET,
    repository_id: UUID | Unset = UNSET,
    restore_point_id: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> PageOfRESTProtectedTeam | RESTExceptionInfo | None:
    """Get Protected Teams

     Returns a collection of protected teams.

    Args:
        organization_id (UUID | Unset):
        backed_up_organization_id (str | Unset):
        repository_id (UUID | Unset):
        restore_point_id (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTProtectedTeam | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_id=organization_id,
            backed_up_organization_id=backed_up_organization_id,
            repository_id=repository_id,
            restore_point_id=restore_point_id,
            offset=offset,
            limit=limit,
        )
    ).parsed
