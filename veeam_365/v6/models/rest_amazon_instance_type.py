from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTAmazonInstanceType")


@_attrs_define
class RESTAmazonInstanceType:
    """
    Attributes:
        type_ (str | Unset):
        cores (int | Unset):
        memory (int | Unset):
    """

    type_: str | Unset = UNSET
    cores: int | Unset = UNSET
    memory: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        cores = self.cores

        memory = self.memory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if cores is not UNSET:
            field_dict["cores"] = cores
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        cores = d.pop("cores", UNSET)

        memory = d.pop("memory", UNSET)

        rest_amazon_instance_type = cls(
            type_=type_,
            cores=cores,
            memory=memory,
        )

        rest_amazon_instance_type.additional_properties = d
        return rest_amazon_instance_type

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
