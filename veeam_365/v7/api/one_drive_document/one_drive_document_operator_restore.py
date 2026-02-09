from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_operator_restore_session_response import RESTOperatorRestoreSessionResponse
from ...models.rest_operator_restore_to_original_one_drive_documents import (
    RESTOperatorRestoreToOriginalOneDriveDocuments,
)
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    body: RESTOperatorRestoreToOriginalOneDriveDocuments,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v7/RestoreSessions/{restore_session_id}/Organization/OneDrives/{one_drive_id}/Documents/operatorRestore".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
            one_drive_id=quote(str(one_drive_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | RESTOperatorRestoreSessionResponse:
    if response.status_code == 200:
        response_200 = RESTOperatorRestoreSessionResponse.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | RESTOperatorRestoreSessionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTOperatorRestoreToOriginalOneDriveDocuments,
) -> Response[RESTExceptionInfo | RESTOperatorRestoreSessionResponse]:
    r"""Restore OneDrive Documents by Restore Operator

     Restores backed-up OneDrive documents using Restore Portal. For more information about Restore
    Portal, see the [Data Restore Using Restore
    Portal](https://helpcenter.veeam.com/docs/vbo365/guide/ssp_restore.html?ver=70) section of the Veeam
    Backup for Microsoft 365 User Guide. <div class=\"note\"><strong>NOTE</strong>  </br> To restore
    data using Restore Portal, you must create a restore session for a restore operator. For more
    information, see [Create Restore Session for Restore
    Operator](#tag/RestoreSession/operation/RestoreSession_OperatorExploreAction). </div>

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTOperatorRestoreToOriginalOneDriveDocuments):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTOperatorRestoreSessionResponse]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTOperatorRestoreToOriginalOneDriveDocuments,
) -> RESTExceptionInfo | RESTOperatorRestoreSessionResponse | None:
    r"""Restore OneDrive Documents by Restore Operator

     Restores backed-up OneDrive documents using Restore Portal. For more information about Restore
    Portal, see the [Data Restore Using Restore
    Portal](https://helpcenter.veeam.com/docs/vbo365/guide/ssp_restore.html?ver=70) section of the Veeam
    Backup for Microsoft 365 User Guide. <div class=\"note\"><strong>NOTE</strong>  </br> To restore
    data using Restore Portal, you must create a restore session for a restore operator. For more
    information, see [Create Restore Session for Restore
    Operator](#tag/RestoreSession/operation/RestoreSession_OperatorExploreAction). </div>

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTOperatorRestoreToOriginalOneDriveDocuments):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTOperatorRestoreSessionResponse
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTOperatorRestoreToOriginalOneDriveDocuments,
) -> Response[RESTExceptionInfo | RESTOperatorRestoreSessionResponse]:
    r"""Restore OneDrive Documents by Restore Operator

     Restores backed-up OneDrive documents using Restore Portal. For more information about Restore
    Portal, see the [Data Restore Using Restore
    Portal](https://helpcenter.veeam.com/docs/vbo365/guide/ssp_restore.html?ver=70) section of the Veeam
    Backup for Microsoft 365 User Guide. <div class=\"note\"><strong>NOTE</strong>  </br> To restore
    data using Restore Portal, you must create a restore session for a restore operator. For more
    information, see [Create Restore Session for Restore
    Operator](#tag/RestoreSession/operation/RestoreSession_OperatorExploreAction). </div>

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTOperatorRestoreToOriginalOneDriveDocuments):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | RESTOperatorRestoreSessionResponse]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        one_drive_id=one_drive_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    one_drive_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTOperatorRestoreToOriginalOneDriveDocuments,
) -> RESTExceptionInfo | RESTOperatorRestoreSessionResponse | None:
    r"""Restore OneDrive Documents by Restore Operator

     Restores backed-up OneDrive documents using Restore Portal. For more information about Restore
    Portal, see the [Data Restore Using Restore
    Portal](https://helpcenter.veeam.com/docs/vbo365/guide/ssp_restore.html?ver=70) section of the Veeam
    Backup for Microsoft 365 User Guide. <div class=\"note\"><strong>NOTE</strong>  </br> To restore
    data using Restore Portal, you must create a restore session for a restore operator. For more
    information, see [Create Restore Session for Restore
    Operator](#tag/RestoreSession/operation/RestoreSession_OperatorExploreAction). </div>

    Args:
        restore_session_id (UUID):
        one_drive_id (str):
        body (RESTOperatorRestoreToOriginalOneDriveDocuments):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | RESTOperatorRestoreSessionResponse
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            one_drive_id=one_drive_id,
            client=client,
            body=body,
        )
    ).parsed
