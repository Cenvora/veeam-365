from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rest_amazon_bucket_s3_compatible import RESTAmazonBucketS3Compatible
from ...models.rest_exception_info import RESTExceptionInfo
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    account_id: UUID,
    service_point: str,
    custom_region_id: str,
    name: str | Unset = UNSET,
    trusted_server_certificate_thumbprint: str | Unset = UNSET,
    trust_server_certificate: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_account_id = str(account_id)
    params["accountId"] = json_account_id

    params["ServicePoint"] = service_point

    params["CustomRegionId"] = custom_region_id

    params["Name"] = name

    params["trustedServerCertificateThumbprint"] = trusted_server_certificate_thumbprint

    params["trustServerCertificate"] = trust_server_certificate


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v8/S3CompatibleResources/buckets",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RESTExceptionInfo | list[RESTAmazonBucketS3Compatible]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = RESTAmazonBucketS3Compatible.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    response_default = RESTExceptionInfo.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RESTExceptionInfo | list[RESTAmazonBucketS3Compatible]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    service_point: str,
    custom_region_id: str,
    name: str | Unset = UNSET,
    trusted_server_certificate_thumbprint: str | Unset = UNSET,
    trust_server_certificate: bool | Unset = UNSET,

) -> Response[RESTExceptionInfo | list[RESTAmazonBucketS3Compatible]]:
    """ Get Buckets

     Returns a list of S3 Compatible, IBM Cloud or Wasabi Cloud object storage buckets.

    Args:
        account_id (UUID):
        service_point (str):
        custom_region_id (str):
        name (str | Unset):
        trusted_server_certificate_thumbprint (str | Unset):
        trust_server_certificate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAmazonBucketS3Compatible]]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
service_point=service_point,
custom_region_id=custom_region_id,
name=name,
trusted_server_certificate_thumbprint=trusted_server_certificate_thumbprint,
trust_server_certificate=trust_server_certificate,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    service_point: str,
    custom_region_id: str,
    name: str | Unset = UNSET,
    trusted_server_certificate_thumbprint: str | Unset = UNSET,
    trust_server_certificate: bool | Unset = UNSET,

) -> RESTExceptionInfo | list[RESTAmazonBucketS3Compatible] | None:
    """ Get Buckets

     Returns a list of S3 Compatible, IBM Cloud or Wasabi Cloud object storage buckets.

    Args:
        account_id (UUID):
        service_point (str):
        custom_region_id (str):
        name (str | Unset):
        trusted_server_certificate_thumbprint (str | Unset):
        trust_server_certificate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAmazonBucketS3Compatible]
     """


    return sync_detailed(
        client=client,
account_id=account_id,
service_point=service_point,
custom_region_id=custom_region_id,
name=name,
trusted_server_certificate_thumbprint=trusted_server_certificate_thumbprint,
trust_server_certificate=trust_server_certificate,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    service_point: str,
    custom_region_id: str,
    name: str | Unset = UNSET,
    trusted_server_certificate_thumbprint: str | Unset = UNSET,
    trust_server_certificate: bool | Unset = UNSET,

) -> Response[RESTExceptionInfo | list[RESTAmazonBucketS3Compatible]]:
    """ Get Buckets

     Returns a list of S3 Compatible, IBM Cloud or Wasabi Cloud object storage buckets.

    Args:
        account_id (UUID):
        service_point (str):
        custom_region_id (str):
        name (str | Unset):
        trusted_server_certificate_thumbprint (str | Unset):
        trust_server_certificate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RESTExceptionInfo | list[RESTAmazonBucketS3Compatible]]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
service_point=service_point,
custom_region_id=custom_region_id,
name=name,
trusted_server_certificate_thumbprint=trusted_server_certificate_thumbprint,
trust_server_certificate=trust_server_certificate,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    service_point: str,
    custom_region_id: str,
    name: str | Unset = UNSET,
    trusted_server_certificate_thumbprint: str | Unset = UNSET,
    trust_server_certificate: bool | Unset = UNSET,

) -> RESTExceptionInfo | list[RESTAmazonBucketS3Compatible] | None:
    """ Get Buckets

     Returns a list of S3 Compatible, IBM Cloud or Wasabi Cloud object storage buckets.

    Args:
        account_id (UUID):
        service_point (str):
        custom_region_id (str):
        name (str | Unset):
        trusted_server_certificate_thumbprint (str | Unset):
        trust_server_certificate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RESTExceptionInfo | list[RESTAmazonBucketS3Compatible]
     """


    return (await asyncio_detailed(
        client=client,
account_id=account_id,
service_point=service_point,
custom_region_id=custom_region_id,
name=name,
trusted_server_certificate_thumbprint=trusted_server_certificate_thumbprint,
trust_server_certificate=trust_server_certificate,

    )).parsed
