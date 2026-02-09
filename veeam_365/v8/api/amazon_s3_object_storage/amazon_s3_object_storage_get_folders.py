from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.amazon_s3_aws_region_type import AmazonS3AwsRegionType
from ...models.rest_amazon_folder_to_receive_s3_aws import RESTAmazonFolderToReceiveS3Aws
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_name: str,
    *,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,
    name: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_account_id = str(account_id)
    params["accountId"] = json_account_id

    json_region_type = region_type.value
    params["RegionType"] = json_region_type

    params["Name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/S3Resources/buckets/{bucket_name}/folders".format(
            bucket_name=quote(str(bucket_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTExceptionInfo | list[RESTAmazonFolderToReceiveS3Aws]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RESTAmazonFolderToReceiveS3Aws.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTExceptionInfo | list[RESTAmazonFolderToReceiveS3Aws]]:
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
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,
    name: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTAmazonFolderToReceiveS3Aws]]:
    """Get Folders

     Returns a list of Amazon folders created in the specified bucket.

    Args:
        bucket_name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAmazonFolderToReceiveS3Aws]]
    """

    kwargs = _get_kwargs(
        bucket_name=bucket_name,
        account_id=account_id,
        region_type=region_type,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bucket_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,
    name: str | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTAmazonFolderToReceiveS3Aws] | None:
    """Get Folders

     Returns a list of Amazon folders created in the specified bucket.

    Args:
        bucket_name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAmazonFolderToReceiveS3Aws]
    """

    return sync_detailed(
        bucket_name=bucket_name,
        client=client,
        account_id=account_id,
        region_type=region_type,
        name=name,
    ).parsed


async def asyncio_detailed(
    bucket_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,
    name: str | Unset = UNSET,
) -> Response[RESTExceptionInfo | list[RESTAmazonFolderToReceiveS3Aws]]:
    """Get Folders

     Returns a list of Amazon folders created in the specified bucket.

    Args:
        bucket_name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAmazonFolderToReceiveS3Aws]]
    """

    kwargs = _get_kwargs(
        bucket_name=bucket_name,
        account_id=account_id,
        region_type=region_type,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    region_type: AmazonS3AwsRegionType,
    name: str | Unset = UNSET,
) -> RESTExceptionInfo | list[RESTAmazonFolderToReceiveS3Aws] | None:
    """Get Folders

     Returns a list of Amazon folders created in the specified bucket.

    Args:
        bucket_name (str):
        account_id (UUID):
        region_type (AmazonS3AwsRegionType): Region type.
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAmazonFolderToReceiveS3Aws]
    """

    return (
        await asyncio_detailed(
            bucket_name=bucket_name,
            client=client,
            account_id=account_id,
            region_type=region_type,
            name=name,
        )
    ).parsed
