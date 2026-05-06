from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTAmazonVpc")



@_attrs_define
class RESTAmazonVpc:
    """ 
        Attributes:
            id (str | Unset): Amazon Virtual Private Cloud ID.
            name (str | Unset): Amazon Virtual Private Cloud name.
            cidr (str | Unset): Range of IPv4 addresses for the Amazon Virtual Private Cloud in the form of a Classless
                Inter-Domain Routing (CIDR) block.
                For more information, see [this Amazon
                article](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html).
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    cidr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        cidr = self.cidr


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if cidr is not UNSET:
            field_dict["CIDR"] = cidr

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        cidr = d.pop("CIDR", UNSET)

        rest_amazon_vpc = cls(
            id=id,
            name=name,
            cidr=cidr,
        )


        rest_amazon_vpc.additional_properties = d
        return rest_amazon_vpc

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
