from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.account_get_accounts_account_type import AccountGetAccountsAccountType
from ...models.rest_account import RESTAccount
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    account_type: AccountGetAccountsAccountType | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    json_account_type: str | Unset = UNSET
    if not isinstance(account_type, Unset):
        json_account_type = account_type.value

    params["accountType"] = json_account_type

    json_organization_id: str | Unset = UNSET
    if not isinstance(organization_id, Unset):
        json_organization_id = str(organization_id)
    params["organizationId"] = json_organization_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/Accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTAccount]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTAccount.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTAccount]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    account_type: AccountGetAccountsAccountType | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTAccount]]:
    """Get Accounts

     Returns a list of existing cloud credentials.

    Args:
        name (str | Unset):
        account_type (AccountGetAccountsAccountType | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAccount]]
    """

    kwargs = _get_kwargs(
        name=name,
        account_type=account_type,
        organization_id=organization_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    account_type: AccountGetAccountsAccountType | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTAccount] | None:
    """Get Accounts

     Returns a list of existing cloud credentials.

    Args:
        name (str | Unset):
        account_type (AccountGetAccountsAccountType | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAccount]
    """

    return sync_detailed(
        client=client,
        name=name,
        account_type=account_type,
        organization_id=organization_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    account_type: AccountGetAccountsAccountType | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTAccount]]:
    """Get Accounts

     Returns a list of existing cloud credentials.

    Args:
        name (str | Unset):
        account_type (AccountGetAccountsAccountType | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAccount]]
    """

    kwargs = _get_kwargs(
        name=name,
        account_type=account_type,
        organization_id=organization_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    account_type: AccountGetAccountsAccountType | Unset = UNSET,
    organization_id: UUID | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTAccount] | None:
    """Get Accounts

     Returns a list of existing cloud credentials.

    Args:
        name (str | Unset):
        account_type (AccountGetAccountsAccountType | Unset):
        organization_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAccount]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            account_type=account_type,
            organization_id=organization_id,
        )
    ).parsed
