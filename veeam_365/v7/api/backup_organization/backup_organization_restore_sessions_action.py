from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.backup_organization_restore_sessions_action_response_200 import (
    BackupOrganizationRestoreSessionsActionResponse200,
)
from ...models.rest_exception_info import RESTExceptionInfo
from ...models.rest_export_folder_to_pst import RESTExportFolderToPst
from ...types import Response


def _get_kwargs(
    restore_session_id: UUID,
    *,
    body: RESTExportFolderToPst,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v7/RestoreSessions/{restore_session_id}/organization/exportToPst".format(
            restore_session_id=quote(str(restore_session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BackupOrganizationRestoreSessionsActionResponse200 | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = BackupOrganizationRestoreSessionsActionResponse200.from_dict(response.content)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BackupOrganizationRestoreSessionsActionResponse200 | RESTExceptionInfo]:
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
    body: RESTExportFolderToPst,
) -> Response[BackupOrganizationRestoreSessionsActionResponse200 | RESTExceptionInfo]:
    r"""Export Data to PST

     Exports backup items to a PST file. <div class=\"important\"><strong> IMPORTANT</strong> </br> To
    export data to PST (Personal Storage Table) files, you must have a 64-bit version of Microsoft
    Outlook 2016, Microsoft Outlook 2013 or Microsoft Outlook 2010 installed on a computer running
    restore sessions. </div>
    The request command will look for a specified keyword in Exchange organization data. The backed-up
    data with a specified keyword then will be exported to a PST file and placed to a temporary folder
    on the Veeam Backup for Microsoft 365 server. After that, the PST file will be transferred as
    application/octet-stream media to the client. To download, read, convert to PST or perform other
    actions with the octet-stream, use features of programming languages.

    If the size of the exported data exceeds the limit specified for the PST file, Veeam Backup for
    Microsoft 365 splits the PST file into separate files and exports these files to an archive file of
    the ZIP format. For example, you specified 1 GB as the PST file size limit. The size of the exported
    data is 1.5 GB. In this case, Veeam Backup for Microsoft 365 will export data to a ZIP archive. The
    archive will contain two PST files: one PST file of the 1 GB size and another PST file of the 0.5 GB
    size.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        body (RESTExportFolderToPst):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupOrganizationRestoreSessionsActionResponse200 | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExportFolderToPst,
) -> BackupOrganizationRestoreSessionsActionResponse200 | RESTExceptionInfo | None:
    r"""Export Data to PST

     Exports backup items to a PST file. <div class=\"important\"><strong> IMPORTANT</strong> </br> To
    export data to PST (Personal Storage Table) files, you must have a 64-bit version of Microsoft
    Outlook 2016, Microsoft Outlook 2013 or Microsoft Outlook 2010 installed on a computer running
    restore sessions. </div>
    The request command will look for a specified keyword in Exchange organization data. The backed-up
    data with a specified keyword then will be exported to a PST file and placed to a temporary folder
    on the Veeam Backup for Microsoft 365 server. After that, the PST file will be transferred as
    application/octet-stream media to the client. To download, read, convert to PST or perform other
    actions with the octet-stream, use features of programming languages.

    If the size of the exported data exceeds the limit specified for the PST file, Veeam Backup for
    Microsoft 365 splits the PST file into separate files and exports these files to an archive file of
    the ZIP format. For example, you specified 1 GB as the PST file size limit. The size of the exported
    data is 1.5 GB. In this case, Veeam Backup for Microsoft 365 will export data to a ZIP archive. The
    archive will contain two PST files: one PST file of the 1 GB size and another PST file of the 0.5 GB
    size.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        body (RESTExportFolderToPst):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupOrganizationRestoreSessionsActionResponse200 | RESTExceptionInfo
    """

    return sync_detailed(
        restore_session_id=restore_session_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExportFolderToPst,
) -> Response[BackupOrganizationRestoreSessionsActionResponse200 | RESTExceptionInfo]:
    r"""Export Data to PST

     Exports backup items to a PST file. <div class=\"important\"><strong> IMPORTANT</strong> </br> To
    export data to PST (Personal Storage Table) files, you must have a 64-bit version of Microsoft
    Outlook 2016, Microsoft Outlook 2013 or Microsoft Outlook 2010 installed on a computer running
    restore sessions. </div>
    The request command will look for a specified keyword in Exchange organization data. The backed-up
    data with a specified keyword then will be exported to a PST file and placed to a temporary folder
    on the Veeam Backup for Microsoft 365 server. After that, the PST file will be transferred as
    application/octet-stream media to the client. To download, read, convert to PST or perform other
    actions with the octet-stream, use features of programming languages.

    If the size of the exported data exceeds the limit specified for the PST file, Veeam Backup for
    Microsoft 365 splits the PST file into separate files and exports these files to an archive file of
    the ZIP format. For example, you specified 1 GB as the PST file size limit. The size of the exported
    data is 1.5 GB. In this case, Veeam Backup for Microsoft 365 will export data to a ZIP archive. The
    archive will contain two PST files: one PST file of the 1 GB size and another PST file of the 0.5 GB
    size.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        body (RESTExportFolderToPst):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupOrganizationRestoreSessionsActionResponse200 | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        restore_session_id=restore_session_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    restore_session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RESTExportFolderToPst,
) -> BackupOrganizationRestoreSessionsActionResponse200 | RESTExceptionInfo | None:
    r"""Export Data to PST

     Exports backup items to a PST file. <div class=\"important\"><strong> IMPORTANT</strong> </br> To
    export data to PST (Personal Storage Table) files, you must have a 64-bit version of Microsoft
    Outlook 2016, Microsoft Outlook 2013 or Microsoft Outlook 2010 installed on a computer running
    restore sessions. </div>
    The request command will look for a specified keyword in Exchange organization data. The backed-up
    data with a specified keyword then will be exported to a PST file and placed to a temporary folder
    on the Veeam Backup for Microsoft 365 server. After that, the PST file will be transferred as
    application/octet-stream media to the client. To download, read, convert to PST or perform other
    actions with the octet-stream, use features of programming languages.

    If the size of the exported data exceeds the limit specified for the PST file, Veeam Backup for
    Microsoft 365 splits the PST file into separate files and exports these files to an archive file of
    the ZIP format. For example, you specified 1 GB as the PST file size limit. The size of the exported
    data is 1.5 GB. In this case, Veeam Backup for Microsoft 365 will export data to a ZIP archive. The
    archive will contain two PST files: one PST file of the 1 GB size and another PST file of the 0.5 GB
    size.

    If downloading of the octet-stream was interrupted for some reason, you can send the request again
    and download the file from the temporary folder.

    Args:
        restore_session_id (UUID):
        body (RESTExportFolderToPst):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupOrganizationRestoreSessionsActionResponse200 | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            restore_session_id=restore_session_id,
            client=client,
            body=body,
        )
    ).parsed
