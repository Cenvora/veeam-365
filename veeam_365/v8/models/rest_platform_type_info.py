from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="RESTPlatformTypeInfo")



@_attrs_define
class RESTPlatformTypeInfo:
    """ 
        Attributes:
            id (int | Unset): ID of the license usage counter type.
            name (str | Unset): Name of the license usage counter type.
            cis_counter_name (str | Unset): Unique name of the license usage counter within the Veeam infrastructure.
            weight (float | Unset): Number of licensing points.
            group_id (UUID | Unset): ID of a licensing group of objects.
     """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    cis_counter_name: str | Unset = UNSET
    weight: float | Unset = UNSET
    group_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        cis_counter_name = self.cis_counter_name

        weight = self.weight

        group_id: str | Unset = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if cis_counter_name is not UNSET:
            field_dict["cisCounterName"] = cis_counter_name
        if weight is not UNSET:
            field_dict["weight"] = weight
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        cis_counter_name = d.pop("cisCounterName", UNSET)

        weight = d.pop("weight", UNSET)

        _group_id = d.pop("groupId", UNSET)
        group_id: UUID | Unset
        if isinstance(_group_id,  Unset):
            group_id = UNSET
        else:
            group_id = UUID(_group_id)




        rest_platform_type_info = cls(
            id=id,
            name=name,
            cis_counter_name=cis_counter_name,
            weight=weight,
            group_id=group_id,
        )


        rest_platform_type_info.additional_properties = d
        return rest_platform_type_info

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
