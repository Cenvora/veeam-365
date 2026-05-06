from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_job_session import RESTJobSession
from typing import cast
from uuid import UUID



def _get_kwargs(
    job_sessions_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/JobSessions/{job_sessions_id}".format(job_sessions_id=quote(str(job_sessions_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTJobSession:
    if response.status_code == 200:
        response_200 = RESTJobSession.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTJobSession]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_sessions_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | RESTJobSession]:
    """ Get Job Session by Session ID

     Returns a resource representation of a job session with the specified ID.

    Args:
        job_sessions_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTJobSession]
     """


    kwargs = _get_kwargs(
        job_sessions_id=job_sessions_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    job_sessions_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTJobSession | None:
    """ Get Job Session by Session ID

     Returns a resource representation of a job session with the specified ID.

    Args:
        job_sessions_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTJobSession
     """


    return sync_detailed(
        job_sessions_id=job_sessions_id,
client=client,

    ).parsed

async def asyncio_detailed(
    job_sessions_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[RESTExceptionInfo | RESTJobSession]:
    """ Get Job Session by Session ID

     Returns a resource representation of a job session with the specified ID.

    Args:
        job_sessions_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTJobSession]
     """


    kwargs = _get_kwargs(
        job_sessions_id=job_sessions_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    job_sessions_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> RESTExceptionInfo | RESTJobSession | None:
    """ Get Job Session by Session ID

     Returns a resource representation of a job session with the specified ID.

    Args:
        job_sessions_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTJobSession
     """


    return (await asyncio_detailed(
        job_sessions_id=job_sessions_id,
client=client,

    )).parsed
