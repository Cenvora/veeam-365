from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.amazon_s3_aws_region_type import AmazonS3AwsRegionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary





T = TypeVar("T", bound="RESTAmazonBucketS3Aws")



@_attrs_define
class RESTAmazonBucketS3Aws:
    """ 
        Attributes:
            region_type (AmazonS3AwsRegionType | Unset): Region type.
            region_name (str | Unset): Region name.
            region_id (str | Unset): Region ID.
            name (str | Unset): Bucket name.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
     """

    region_type: AmazonS3AwsRegionType | Unset = UNSET
    region_name: str | Unset = UNSET
    region_id: str | Unset = UNSET
    name: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        region_type: str | Unset = UNSET
        if not isinstance(self.region_type, Unset):
            region_type = self.region_type.value


        region_name = self.region_name

        region_id = self.region_id

        name = self.name

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if region_type is not UNSET:
            field_dict["regionType"] = region_type
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if name is not UNSET:
            field_dict["name"] = name
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        d = dict(src_dict)
        _region_type = d.pop("regionType", UNSET)
        region_type: AmazonS3AwsRegionType | Unset
        if isinstance(_region_type,  Unset):
            region_type = UNSET
        else:
            region_type = AmazonS3AwsRegionType(_region_type)




        region_name = d.pop("regionName", UNSET)

        region_id = d.pop("regionId", UNSET)

        name = d.pop("name", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        rest_amazon_bucket_s3_aws = cls(
            region_type=region_type,
            region_name=region_name,
            region_id=region_id,
            name=name,
            field_links=field_links,
        )


        rest_amazon_bucket_s3_aws.additional_properties = d
        return rest_amazon_bucket_s3_aws

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
