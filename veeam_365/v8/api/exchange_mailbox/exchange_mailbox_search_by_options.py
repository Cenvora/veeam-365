from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_rest_exchange_items_composed import PageOfRESTExchangeItemsComposed
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_search_options import RESTSearchOptions
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    *,
    body: RESTSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    json_set_id: str | Unset = UNSET
    if not isinstance(set_id, Unset):
        json_set_id = str(set_id)
    params["setId"] = json_set_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/mailboxes/search".format(restore_session_id=quote(str(restore_session_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageOfRESTExchangeItemsComposed | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = PageOfRESTExchangeItemsComposed.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageOfRESTExchangeItemsComposed | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,

) -> Response[PageOfRESTExchangeItemsComposed | RESTExceptionInfo]:
    """ Search for Exchange Items in Mailboxes

     Searches for items in backed-up organization mailboxes.

    Args:
        restore_session_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        body (RESTSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTExchangeItemsComposed | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
body=body,
offset=offset,
limit=limit,
set_id=set_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,

) -> PageOfRESTExchangeItemsComposed | RESTExceptionInfo | None:
    """ Search for Exchange Items in Mailboxes

     Searches for items in backed-up organization mailboxes.

    Args:
        restore_session_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        body (RESTSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTExchangeItemsComposed | RESTExceptionInfo
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
client=client,
body=body,
offset=offset,
limit=limit,
set_id=set_id,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,

) -> Response[PageOfRESTExchangeItemsComposed | RESTExceptionInfo]:
    """ Search for Exchange Items in Mailboxes

     Searches for items in backed-up organization mailboxes.

    Args:
        restore_session_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        body (RESTSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageOfRESTExchangeItemsComposed | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
body=body,
offset=offset,
limit=limit,
set_id=set_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTSearchOptions,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    set_id: UUID | Unset = UNSET,

) -> PageOfRESTExchangeItemsComposed | RESTExceptionInfo | None:
    """ Search for Exchange Items in Mailboxes

     Searches for items in backed-up organization mailboxes.

    Args:
        restore_session_id (UUID):
        offset (int | Unset):
        limit (int | Unset):
        set_id (UUID | Unset):
        body (RESTSearchOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageOfRESTExchangeItemsComposed | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
client=client,
body=body,
offset=offset,
limit=limit,
set_id=set_id,

    )).parsed
