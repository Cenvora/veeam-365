from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.amazon_s3_aws_region_type import AmazonS3AwsRegionType
from ...models.rest_amazon_folder_to_receive_s3_aws import RESTAmazonFolderToReceiveS3Aws
from ...models.rest_amazon_folder_to_send import RESTAmazonFolderToSend
from ...models.rest_exception_info import RESTExceptionInfo
from typing import cast
from uuid import UUID



def _get_kwargs(
    bucket_name: str,
    *,
    body: RESTAmazonFolderToSend,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_account_id = str(account_id)
    params["accountId"] = json_account_id

    json_region_type = region_type.value
    params["RegionType"] = json_region_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v8/S3Resources/buckets/{bucket_name}/folders".format(bucket_name=quote(str(bucket_name), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTAmazonFolderToReceiveS3Aws | RESTExceptionInfo:
    if response.status_code == 201:
        response_201 = RESTAmazonFolderToReceiveS3Aws.from_dict(response.json())



        return response_201

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTAmazonFolderToReceiveS3Aws | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bucket_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTAmazonFolderToSend,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,

) -> Response[RESTAmazonFolderToReceiveS3Aws | RESTExceptionInfo]:
    """ Create Folders

     Creates a new folder in the specified Amazon bucket.

    Args:
        bucket_name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.
        body (RESTAmazonFolderToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAmazonFolderToReceiveS3Aws | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        bucket_name=bucket_name,
body=body,
account_id=account_id,
region_type=region_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    bucket_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTAmazonFolderToSend,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,

) -> RESTAmazonFolderToReceiveS3Aws | RESTExceptionInfo | None:
    """ Create Folders

     Creates a new folder in the specified Amazon bucket.

    Args:
        bucket_name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.
        body (RESTAmazonFolderToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAmazonFolderToReceiveS3Aws | RESTExceptionInfo
     """


    return sync_detailed(
        bucket_name=bucket_name,
client=client,
body=body,
account_id=account_id,
region_type=region_type,

    ).parsed

async def asyncio_detailed(
    bucket_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTAmazonFolderToSend,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,

) -> Response[RESTAmazonFolderToReceiveS3Aws | RESTExceptionInfo]:
    """ Create Folders

     Creates a new folder in the specified Amazon bucket.

    Args:
        bucket_name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.
        body (RESTAmazonFolderToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAmazonFolderToReceiveS3Aws | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        bucket_name=bucket_name,
body=body,
account_id=account_id,
region_type=region_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    bucket_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RESTAmazonFolderToSend,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,

) -> RESTAmazonFolderToReceiveS3Aws | RESTExceptionInfo | None:
    """ Create Folders

     Creates a new folder in the specified Amazon bucket.

    Args:
        bucket_name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.
        body (RESTAmazonFolderToSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAmazonFolderToReceiveS3Aws | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        bucket_name=bucket_name,
client=client,
body=body,
account_id=account_id,
region_type=region_type,

    )).parsed
