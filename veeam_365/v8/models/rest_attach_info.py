from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTAttachInfo")



@_attrs_define
class RESTAttachInfo:
    """ 
        Attributes:
            name (str | Unset): Name of the attachment item.
            long_file_name (str | Unset): Name of the attachment file.
            url (str | Unset): Path to the attachment item.
     """

    name: str | Unset = UNSET
    long_file_name: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        long_file_name = self.long_file_name

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if long_file_name is not UNSET:
            field_dict["longFileName"] = long_file_name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        long_file_name = d.pop("longFileName", UNSET)

        url = d.pop("url", UNSET)

        rest_attach_info = cls(
            name=name,
            long_file_name=long_file_name,
            url=url,
        )


        rest_attach_info.additional_properties = d
        return rest_attach_info

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
