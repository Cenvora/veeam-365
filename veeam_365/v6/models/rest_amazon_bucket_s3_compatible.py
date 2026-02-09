from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTAmazonBucketS3Compatible")


@_attrs_define
class RESTAmazonBucketS3Compatible:
    """
    Attributes:
        service_point (str | Unset):
        custom_region_id (str | Unset):
        name (str | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    service_point: str | Unset = UNSET
    custom_region_id: str | Unset = UNSET
    name: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_point = self.service_point

        custom_region_id = self.custom_region_id

        name = self.name

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

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_amazon_bucket_s3_compatible = cls(
            service_point=service_point,
            custom_region_id=custom_region_id,
            name=name,
            field_links=field_links,
        )

        rest_amazon_bucket_s3_compatible.additional_properties = d
        return rest_amazon_bucket_s3_compatible

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
