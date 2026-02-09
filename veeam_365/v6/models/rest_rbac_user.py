from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_rbac_user_type import RESTRbacUserType

T = TypeVar("T", bound="RESTRbacUser")


@_attrs_define
class RESTRbacUser:
    """
    Attributes:
        id (str):
        display_name (str):
        name (str):
        type_ (RESTRbacUserType):
    """

    id: str
    display_name: str
    name: str
    type_: RESTRbacUserType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        name = self.name

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
                "name": name,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("displayName")

        name = d.pop("name")

        type_ = RESTRbacUserType(d.pop("type"))

        rest_rbac_user = cls(
            id=id,
            display_name=display_name,
            name=name,
            type_=type_,
        )

        rest_rbac_user.additional_properties = d
        return rest_rbac_user

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
