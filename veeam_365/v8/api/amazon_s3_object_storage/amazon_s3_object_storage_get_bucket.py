from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.amazon_s3_aws_region_type import AmazonS3AwsRegionType
from ...models.rest_amazon_bucket_s3_aws import RESTAmazonBucketS3Aws
from ...models.rest_exception_info import RESTExceptionInfo
from typing import cast
from uuid import UUID



def _get_kwargs(
    name: str,
    *,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_account_id = str(account_id)
    params["accountId"] = json_account_id

    json_region_type = region_type.value
    params["RegionType"] = json_region_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/S3Resources/buckets/{name}".format(name=quote(str(name), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTAmazonBucketS3Aws | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTAmazonBucketS3Aws.from_dict(response.json())



        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTAmazonBucketS3Aws | RESTExceptionInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,

) -> Response[RESTAmazonBucketS3Aws | RESTExceptionInfo]:
    """ Get Bucket by Name

     Returns information about an Amazon S3 bucket with the specified name.

    Args:
        name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAmazonBucketS3Aws | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        name=name,
account_id=account_id,
region_type=region_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,

) -> RESTAmazonBucketS3Aws | RESTExceptionInfo | None:
    """ Get Bucket by Name

     Returns information about an Amazon S3 bucket with the specified name.

    Args:
        name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAmazonBucketS3Aws | RESTExceptionInfo
     """


    return sync_detailed(
        name=name,
client=client,
account_id=account_id,
region_type=region_type,

    ).parsed

async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,

) -> Response[RESTAmazonBucketS3Aws | RESTExceptionInfo]:
    """ Get Bucket by Name

     Returns information about an Amazon S3 bucket with the specified name.

    Args:
        name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAmazonBucketS3Aws | RESTExceptionInfo]
     """


    kwargs = _get_kwargs(
        name=name,
account_id=account_id,
region_type=region_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,

) -> RESTAmazonBucketS3Aws | RESTExceptionInfo | None:
    """ Get Bucket by Name

     Returns information about an Amazon S3 bucket with the specified name.

    Args:
        name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAmazonBucketS3Aws | RESTExceptionInfo
     """


    return (await asyncio_detailed(
        name=name,
client=client,
account_id=account_id,
region_type=region_type,

    )).parsed
