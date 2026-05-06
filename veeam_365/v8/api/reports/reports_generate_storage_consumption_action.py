from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reports_generate_storage_consumption_action_response_200 import ReportsGenerateStorageConsumptionActionResponse200
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_storage_consumption_options import RESTStorageConsumptionOptions
from typing import cast



def _get_kwargs(
    *,
    body: RESTStorageConsumptionOptions,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/Reports/GenerateStorageConsumption",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | ReportsGenerateStorageConsumptionActionResponse200:
    if response.status_code == 200:
        response_200 = ReportsGenerateStorageConsumptionActionResponse200.from_dict(response.content)



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | ReportsGenerateStorageConsumptionActionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTStorageConsumptionOptions,

) -> Response[RESTExceptionInfo | ReportsGenerateStorageConsumptionActionResponse200]:
    """ Generate Storage Consumption Report

     Generates storage consumption report on the Veeam Backup for Microsoft 365 server.

    Args:
        body (RESTStorageConsumptionOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | ReportsGenerateStorageConsumptionActionResponse200]
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
    body: RESTStorageConsumptionOptions,

) -> RESTExceptionInfo | ReportsGenerateStorageConsumptionActionResponse200 | None:
    """ Generate Storage Consumption Report

     Generates storage consumption report on the Veeam Backup for Microsoft 365 server.

    Args:
        body (RESTStorageConsumptionOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | ReportsGenerateStorageConsumptionActionResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RESTStorageConsumptionOptions,

) -> Response[RESTExceptionInfo | ReportsGenerateStorageConsumptionActionResponse200]:
    """ Generate Storage Consumption Report

     Generates storage consumption report on the Veeam Backup for Microsoft 365 server.

    Args:
        body (RESTStorageConsumptionOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | ReportsGenerateStorageConsumptionActionResponse200]
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
    body: RESTStorageConsumptionOptions,

) -> RESTExceptionInfo | ReportsGenerateStorageConsumptionActionResponse200 | None:
    """ Generate Storage Consumption Report

     Generates storage consumption report on the Veeam Backup for Microsoft 365 server.

    Args:
        body (RESTStorageConsumptionOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | ReportsGenerateStorageConsumptionActionResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
