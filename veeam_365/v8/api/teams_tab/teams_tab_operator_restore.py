from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_operator_restore_tabs_options import RESTOperatorRestoreTabsOptions
from ...models.rest_teams_operator_restore_session_response import RESTTeamsOperatorRestoreSessionResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    body: RESTOperatorRestoreTabsOptions,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/RestoreSessions/{restore_session_id}/organization/teams/{team_id}/channels/{channel_id}/tabs/operatorRestore".format(restore_session_id=quote(str(restore_session_id), safe=""),team_id=quote(str(team_id), safe=""),channel_id=quote(str(channel_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | RESTTeamsOperatorRestoreSessionResponse:
    if response.status_code == 200:
        response_200 = RESTTeamsOperatorRestoreSessionResponse.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | RESTTeamsOperatorRestoreSessionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTOperatorRestoreTabsOptions,

) -> Response[RESTExceptionInfo | RESTTeamsOperatorRestoreSessionResponse]:
    r""" Restore Channel Tabs by Restore Operator

     Restores backed-up Microsoft Teams tabs of a channel with the specified ID using Restore Portal. For
    more information about Restore Portal, see the [Data Restore Using Restore
    Portal](https://helpcenter.veeam.com/docs/vbo365/guide/ssp_restore.html?ver=80) section of the Veeam
    Backup for Microsoft 365 User Guide. <div class=\"note\"><strong>NOTE</strong> </br> To restore data
    using Restore Portal, you must create a restore session for a restore operator. For more
    information, see [Create Restore Session for Restore
    Operator](#/RestoreSession/RestoreSession_OperatorExploreAction). </div>

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        body (RESTOperatorRestoreTabsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTTeamsOperatorRestoreSessionResponse]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTOperatorRestoreTabsOptions,

) -> RESTExceptionInfo | RESTTeamsOperatorRestoreSessionResponse | None:
    r""" Restore Channel Tabs by Restore Operator

     Restores backed-up Microsoft Teams tabs of a channel with the specified ID using Restore Portal. For
    more information about Restore Portal, see the [Data Restore Using Restore
    Portal](https://helpcenter.veeam.com/docs/vbo365/guide/ssp_restore.html?ver=80) section of the Veeam
    Backup for Microsoft 365 User Guide. <div class=\"note\"><strong>NOTE</strong> </br> To restore data
    using Restore Portal, you must create a restore session for a restore operator. For more
    information, see [Create Restore Session for Restore
    Operator](#/RestoreSession/RestoreSession_OperatorExploreAction). </div>

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        body (RESTOperatorRestoreTabsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTTeamsOperatorRestoreSessionResponse
     """


    return sync_detailed(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTOperatorRestoreTabsOptions,

) -> Response[RESTExceptionInfo | RESTTeamsOperatorRestoreSessionResponse]:
    r""" Restore Channel Tabs by Restore Operator

     Restores backed-up Microsoft Teams tabs of a channel with the specified ID using Restore Portal. For
    more information about Restore Portal, see the [Data Restore Using Restore
    Portal](https://helpcenter.veeam.com/docs/vbo365/guide/ssp_restore.html?ver=80) section of the Veeam
    Backup for Microsoft 365 User Guide. <div class=\"note\"><strong>NOTE</strong> </br> To restore data
    using Restore Portal, you must create a restore session for a restore operator. For more
    information, see [Create Restore Session for Restore
    Operator](#/RestoreSession/RestoreSession_OperatorExploreAction). </div>

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        body (RESTOperatorRestoreTabsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTTeamsOperatorRestoreSessionResponse]
     """


    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    restore_session_id: UUID,
    team_id: UUID,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTOperatorRestoreTabsOptions,

) -> RESTExceptionInfo | RESTTeamsOperatorRestoreSessionResponse | None:
    r""" Restore Channel Tabs by Restore Operator

     Restores backed-up Microsoft Teams tabs of a channel with the specified ID using Restore Portal. For
    more information about Restore Portal, see the [Data Restore Using Restore
    Portal](https://helpcenter.veeam.com/docs/vbo365/guide/ssp_restore.html?ver=80) section of the Veeam
    Backup for Microsoft 365 User Guide. <div class=\"note\"><strong>NOTE</strong> </br> To restore data
    using Restore Portal, you must create a restore session for a restore operator. For more
    information, see [Create Restore Session for Restore
    Operator](#/RestoreSession/RestoreSession_OperatorExploreAction). </div>

    Args:
        restore_session_id (UUID):
        team_id (UUID):
        channel_id (str):
        body (RESTOperatorRestoreTabsOptions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTTeamsOperatorRestoreSessionResponse
     """


    return (await asyncio_detailed(
        restore_session_id=restore_session_id,
team_id=team_id,
channel_id=channel_id,
client=client,
body=body,

    )).parsed
