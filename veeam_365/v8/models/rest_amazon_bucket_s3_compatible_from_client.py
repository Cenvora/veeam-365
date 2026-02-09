from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTAmazonBucketS3CompatibleFromClient")


@_attrs_define
class RESTAmazonBucketS3CompatibleFromClient:
    """
    Attributes:
        service_point (str | Unset): Endpoint address.
        custom_region_id (str | Unset): Region ID.
        name (str | Unset): Bucket name.
        trusted_server_certificate_thumbprint (None | str | Unset): String that represents thumbprint of a not trusted
            S3 Compatible self-signed certificate.
        trust_server_certificate (bool | None | Unset): Defines whether to trust S3 Compatible self-signed certificates.
            If set to *true*, you can omit specifying the `TrustedServerCertificateThumbprint` parameter value.
        field_links (RESTLinkHALDictionary | Unset): Related resources.
    """

    service_point: str | Unset = UNSET
    custom_region_id: str | Unset = UNSET
    name: str | Unset = UNSET
    trusted_server_certificate_thumbprint: None | str | Unset = UNSET
    trust_server_certificate: bool | None | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_point = self.service_point

        custom_region_id = self.custom_region_id

        name = self.name

        trusted_server_certificate_thumbprint: None | str | Unset
        if isinstance(self.trusted_server_certificate_thumbprint, Unset):
            trusted_server_certificate_thumbprint = UNSET
        else:
            trusted_server_certificate_thumbprint = self.trusted_server_certificate_thumbprint

        trust_server_certificate: bool | None | Unset
        if isinstance(self.trust_server_certificate, Unset):
            trust_server_certificate = UNSET
        else:
            trust_server_certificate = self.trust_server_certificate

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_point is not UNSET:
            field_dict["servicePoint"] = service_point
        if custom_region_id is not UNSET:
            field_dict["customRegionId"] = custom_region_id
        if name is not UNSET:
            field_dict["name"] = name
        if trusted_server_certificate_thumbprint is not UNSET:
            field_dict["trustedServerCertificateThumbprint"] = trusted_server_certificate_thumbprint
        if trust_server_certificate is not UNSET:
            field_dict["trustServerCertificate"] = trust_server_certificate
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        service_point = d.pop("servicePoint", UNSET)

        custom_region_id = d.pop("customRegionId", UNSET)

        name = d.pop("name", UNSET)

        def _parse_trusted_server_certificate_thumbprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trusted_server_certificate_thumbprint = _parse_trusted_server_certificate_thumbprint(
            d.pop("trustedServerCertificateThumbprint", UNSET)
        )

        def _parse_trust_server_certificate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        trust_server_certificate = _parse_trust_server_certificate(d.pop("trustServerCertificate", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_amazon_bucket_s3_compatible_from_client = cls(
            service_point=service_point,
            custom_region_id=custom_region_id,
            name=name,
            trusted_server_certificate_thumbprint=trusted_server_certificate_thumbprint,
            trust_server_certificate=trust_server_certificate,
            field_links=field_links,
        )

        rest_amazon_bucket_s3_compatible_from_client.additional_properties = d
        return rest_amazon_bucket_s3_compatible_from_client

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
