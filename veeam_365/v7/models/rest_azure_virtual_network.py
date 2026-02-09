from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTAzureVirtualNetwork")


@_attrs_define
class RESTAzureVirtualNetwork:
    """
    Attributes:
        id (str | Unset): Virtual network ID.
        name (str | Unset): Name of the virtual network.
        type_ (str | Unset): Virtual network type.
        location (str | Unset): Name of the Microsoft Azure region.
        address_spaces (list[str] | Unset): Array of ranges of IPv4 addresses.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    location: str | Unset = UNSET
    address_spaces: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        location = self.location

        address_spaces: list[str] | Unset = UNSET
        if not isinstance(self.address_spaces, Unset):
            address_spaces = self.address_spaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if location is not UNSET:
            field_dict["location"] = location
        if address_spaces is not UNSET:
            field_dict["addressSpaces"] = address_spaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        location = d.pop("location", UNSET)

        address_spaces = cast(list[str], d.pop("addressSpaces", UNSET))

        rest_azure_virtual_network = cls(
            id=id,
            name=name,
            type_=type_,
            location=location,
            address_spaces=address_spaces,
        )

        rest_azure_virtual_network.additional_properties = d
        return rest_azure_virtual_network

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
