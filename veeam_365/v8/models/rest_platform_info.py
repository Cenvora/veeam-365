from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_platform_type_info import RESTPlatformTypeInfo





T = TypeVar("T", bound="RESTPlatformInfo")



@_attrs_define
class RESTPlatformInfo:
    """ 
        Attributes:
            id (UUID | Unset): ID of the licensing platform.
            name (str | Unset): Name of the licensing platform.
            types (list[RESTPlatformTypeInfo] | Unset): Information about license usage counter types.
     """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    types: list[RESTPlatformTypeInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_platform_type_info import RESTPlatformTypeInfo
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item = types_item_data.to_dict()
                types.append(types_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_platform_type_info import RESTPlatformTypeInfo
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        name = d.pop("name", UNSET)

        _types = d.pop("types", UNSET)
        types: list[RESTPlatformTypeInfo] | Unset = UNSET
        if _types is not UNSET:
            types = []
            for types_item_data in _types:
                types_item = RESTPlatformTypeInfo.from_dict(types_item_data)



                types.append(types_item)


        rest_platform_info = cls(
            id=id,
            name=name,
            types=types,
        )


        rest_platform_info.additional_properties = d
        return rest_platform_info

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
