from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_rbac_user_type import RESTRbacUserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTRbacUser")


@_attrs_define
class RESTRbacUser:
    """
    Attributes:
        id (str): ID of the organization user.
        display_name (str): Display name of the organization user.
        name (str): Email address of the organization user.
        type_ (RESTRbacUserType): Type of the organization user.
        on_premises_sid (str | Unset): ID of the organization user in the on-premises organization.
    """

    id: str
    display_name: str
    name: str
    type_: RESTRbacUserType
    on_premises_sid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        name = self.name

        type_ = self.type_.value

        on_premises_sid = self.on_premises_sid

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
        if on_premises_sid is not UNSET:
            field_dict["onPremisesSid"] = on_premises_sid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("displayName")

        name = d.pop("name")

        type_ = RESTRbacUserType(d.pop("type"))

        on_premises_sid = d.pop("onPremisesSid", UNSET)

        rest_rbac_user = cls(
            id=id,
            display_name=display_name,
            name=name,
            type_=type_,
            on_premises_sid=on_premises_sid,
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
