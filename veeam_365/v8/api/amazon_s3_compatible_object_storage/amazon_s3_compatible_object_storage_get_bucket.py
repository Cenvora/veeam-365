from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.rest_amazon_bucket_s3_compatible import RESTAmazonBucketS3Compatible
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    account_id: UUID,
    service_point: str,
    custom_region_id: str,
    trusted_server_certificate_thumbprint: str | Unset = UNSET,
    trust_server_certificate: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_account_id = str(account_id)
    params["accountId"] = json_account_id

    params["ServicePoint"] = service_point

    params["CustomRegionId"] = custom_region_id

    params["trustedServerCertificateThumbprint"] = trusted_server_certificate_thumbprint

    params["trustServerCertificate"] = trust_server_certificate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/S3CompatibleResources/buckets/{name}".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RESTAmazonBucketS3Compatible | RESTExceptionInfo:
    if response.status_code == 200:
        response_200 = RESTAmazonBucketS3Compatible.from_dict(response.json())

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RESTAmazonBucketS3Compatible | RESTExceptionInfo]:
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
    service_point: str,
    custom_region_id: str,
    trusted_server_certificate_thumbprint: str | Unset = UNSET,
    trust_server_certificate: bool | Unset = UNSET,
) -> Response[RESTAmazonBucketS3Compatible | RESTExceptionInfo]:
    """Get Bucket by Name

     Returns information about S3 Compatible, IBM Cloud or Wasabi Cloud object storage bucket with the
    specified name.

    Args:
        name (str):
        account_id (UUID):
        service_point (str):
        custom_region_id (str):
        trusted_server_certificate_thumbprint (str | Unset):
        trust_server_certificate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAmazonBucketS3Compatible | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        name=name,
        account_id=account_id,
        service_point=service_point,
        custom_region_id=custom_region_id,
        trusted_server_certificate_thumbprint=trusted_server_certificate_thumbprint,
        trust_server_certificate=trust_server_certificate,
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
    service_point: str,
    custom_region_id: str,
    trusted_server_certificate_thumbprint: str | Unset = UNSET,
    trust_server_certificate: bool | Unset = UNSET,
) -> RESTAmazonBucketS3Compatible | RESTExceptionInfo | None:
    """Get Bucket by Name

     Returns information about S3 Compatible, IBM Cloud or Wasabi Cloud object storage bucket with the
    specified name.

    Args:
        name (str):
        account_id (UUID):
        service_point (str):
        custom_region_id (str):
        trusted_server_certificate_thumbprint (str | Unset):
        trust_server_certificate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAmazonBucketS3Compatible | RESTExceptionInfo
    """

    return sync_detailed(
        name=name,
        client=client,
        account_id=account_id,
        service_point=service_point,
        custom_region_id=custom_region_id,
        trusted_server_certificate_thumbprint=trusted_server_certificate_thumbprint,
        trust_server_certificate=trust_server_certificate,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    service_point: str,
    custom_region_id: str,
    trusted_server_certificate_thumbprint: str | Unset = UNSET,
    trust_server_certificate: bool | Unset = UNSET,
) -> Response[RESTAmazonBucketS3Compatible | RESTExceptionInfo]:
    """Get Bucket by Name

     Returns information about S3 Compatible, IBM Cloud or Wasabi Cloud object storage bucket with the
    specified name.

    Args:
        name (str):
        account_id (UUID):
        service_point (str):
        custom_region_id (str):
        trusted_server_certificate_thumbprint (str | Unset):
        trust_server_certificate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTAmazonBucketS3Compatible | RESTExceptionInfo]
    """

    kwargs = _get_kwargs(
        name=name,
        account_id=account_id,
        service_point=service_point,
        custom_region_id=custom_region_id,
        trusted_server_certificate_thumbprint=trusted_server_certificate_thumbprint,
        trust_server_certificate=trust_server_certificate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    service_point: str,
    custom_region_id: str,
    trusted_server_certificate_thumbprint: str | Unset = UNSET,
    trust_server_certificate: bool | Unset = UNSET,
) -> RESTAmazonBucketS3Compatible | RESTExceptionInfo | None:
    """Get Bucket by Name

     Returns information about S3 Compatible, IBM Cloud or Wasabi Cloud object storage bucket with the
    specified name.

    Args:
        name (str):
        account_id (UUID):
        service_point (str):
        custom_region_id (str):
        trusted_server_certificate_thumbprint (str | Unset):
        trust_server_certificate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTAmazonBucketS3Compatible | RESTExceptionInfo
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            account_id=account_id,
            service_point=service_point,
            custom_region_id=custom_region_id,
            trusted_server_certificate_thumbprint=trusted_server_certificate_thumbprint,
            trust_server_certificate=trust_server_certificate,
        )
    ).parsed
