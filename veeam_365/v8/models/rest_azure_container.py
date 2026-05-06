from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.azure_storage_endpoint_nullable import AzureStorageEndpointNullable
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary





T = TypeVar("T", bound="RESTAzureContainer")



@_attrs_define
class RESTAzureContainer:
    """ 
        Attributes:
            name (str | Unset): Container name.
            region_type (AzureStorageEndpointNullable | Unset): Region type.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
     """

    name: str | Unset = UNSET
    region_type: AzureStorageEndpointNullable | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        name = self.name

        region_type: str | Unset = UNSET
        if not isinstance(self.region_type, Unset):
            region_type = self.region_type.value


        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if region_type is not UNSET:
            field_dict["regionType"] = region_type
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _region_type = d.pop("regionType", UNSET)
        region_type: AzureStorageEndpointNullable | Unset
        if isinstance(_region_type,  Unset):
            region_type = UNSET
        else:
            region_type = AzureStorageEndpointNullable(_region_type)




        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        rest_azure_container = cls(
            name=name,
            region_type=region_type,
            field_links=field_links,
        )


        rest_azure_container.additional_properties = d
        return rest_azure_container

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
