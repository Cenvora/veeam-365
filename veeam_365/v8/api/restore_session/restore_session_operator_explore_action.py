from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_operator_explore_options import RESTOperatorExploreOptions
from ...models.rest_restore_session import RESTRestoreSession
from typing import cast



def _get_kwargs(
    *,
    body: RESTOperatorExploreOptions,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/Organization/OperatorExplore",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTRestoreSession:
    if response.status_code == 201:
        response_201 = RESTRestoreSession.from_dict(response.json())



        return response_201

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTOperatorExploreOptions,

) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    """ Create Restore Session for Restore Operator

     Creates and starts a restore session to explore and restore data using Restore Portal.

    To use this resource, make sure to obtain a token using an assertion obtained from Microsoft
    Identity platform and log in to Veeam Backup for Microsoft 365 REST API as a restore operator. For
    more information, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization
    for Restore Operators](https://helpcenter.veeam.com/references/vbo365/8/rest/tag/SectionOverview#sec
    tion/Authorization-and-Security/Authorization-for-Restore-Operators).

    Args:
        body (RESTOperatorExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSession]
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
    body: RESTOperatorExploreOptions,

) -> RESTExceptionInfo | RESTRestoreSession | None:
    """ Create Restore Session for Restore Operator

     Creates and starts a restore session to explore and restore data using Restore Portal.

    To use this resource, make sure to obtain a token using an assertion obtained from Microsoft
    Identity platform and log in to Veeam Backup for Microsoft 365 REST API as a restore operator. For
    more information, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization
    for Restore Operators](https://helpcenter.veeam.com/references/vbo365/8/rest/tag/SectionOverview#sec
    tion/Authorization-and-Security/Authorization-for-Restore-Operators).

    Args:
        body (RESTOperatorExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSession
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTOperatorExploreOptions,

) -> Response[RESTExceptionInfo | RESTRestoreSession]:
    """ Create Restore Session for Restore Operator

     Creates and starts a restore session to explore and restore data using Restore Portal.

    To use this resource, make sure to obtain a token using an assertion obtained from Microsoft
    Identity platform and log in to Veeam Backup for Microsoft 365 REST API as a restore operator. For
    more information, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization
    for Restore Operators](https://helpcenter.veeam.com/references/vbo365/8/rest/tag/SectionOverview#sec
    tion/Authorization-and-Security/Authorization-for-Restore-Operators).

    Args:
        body (RESTOperatorExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTRestoreSession]
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
    body: RESTOperatorExploreOptions,

) -> RESTExceptionInfo | RESTRestoreSession | None:
    """ Create Restore Session for Restore Operator

     Creates and starts a restore session to explore and restore data using Restore Portal.

    To use this resource, make sure to obtain a token using an assertion obtained from Microsoft
    Identity platform and log in to Veeam Backup for Microsoft 365 REST API as a restore operator. For
    more information, see the Veeam Backup for Microsoft 365 REST API Reference, section [Authorization
    for Restore Operators](https://helpcenter.veeam.com/references/vbo365/8/rest/tag/SectionOverview#sec
    tion/Authorization-and-Security/Authorization-for-Restore-Operators).

    Args:
        body (RESTOperatorExploreOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTRestoreSession
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
