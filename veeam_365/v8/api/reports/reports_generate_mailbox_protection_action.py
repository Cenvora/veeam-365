from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.reports_generate_mailbox_protection_action_response_200 import (
    ReportsGenerateMailboxProtectionActionResponse200,
)
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_mailbox_protection_options import RESTMailboxProtectionOptions
from ...types import Response


def _get_kwargs(
    *,
    body: RESTMailboxProtectionOptions,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/Reports/GenerateMailboxProtection",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | ReportsGenerateMailboxProtectionActionResponse200:
    if response.status_code == 200:
        response_200 = ReportsGenerateMailboxProtectionActionResponse200.from_dict(response.content)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | ReportsGenerateMailboxProtectionActionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTMailboxProtectionOptions,
) -> Response[RESTExceptionInfo | ReportsGenerateMailboxProtectionActionResponse200]:
    """Generate Mailbox Protection Report

     Generates mailbox protection report on the user mailboxes protected by the Veeam Backup for
    Microsoft 365 server.

    Args:
        body (RESTMailboxProtectionOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | ReportsGenerateMailboxProtectionActionResponse200]
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
    body: RESTMailboxProtectionOptions,
) -> RESTExceptionInfo | ReportsGenerateMailboxProtectionActionResponse200 | None:
    """Generate Mailbox Protection Report

     Generates mailbox protection report on the user mailboxes protected by the Veeam Backup for
    Microsoft 365 server.

    Args:
        body (RESTMailboxProtectionOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | ReportsGenerateMailboxProtectionActionResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTMailboxProtectionOptions,
) -> Response[RESTExceptionInfo | ReportsGenerateMailboxProtectionActionResponse200]:
    """Generate Mailbox Protection Report

     Generates mailbox protection report on the user mailboxes protected by the Veeam Backup for
    Microsoft 365 server.

    Args:
        body (RESTMailboxProtectionOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | ReportsGenerateMailboxProtectionActionResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RESTMailboxProtectionOptions,
) -> RESTExceptionInfo | ReportsGenerateMailboxProtectionActionResponse200 | None:
    """Generate Mailbox Protection Report

     Generates mailbox protection report on the user mailboxes protected by the Veeam Backup for
    Microsoft 365 server.

    Args:
        body (RESTMailboxProtectionOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | ReportsGenerateMailboxProtectionActionResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
