from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTOrganizationLicensingInformation")


@_attrs_define
class RESTOrganizationLicensingInformation:
    """
    Attributes:
        licensed_users (int | Unset):
        new_users (int | Unset):
    """

    licensed_users: int | Unset = UNSET
    new_users: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        licensed_users = self.licensed_users

        new_users = self.new_users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if licensed_users is not UNSET:
            field_dict["licensedUsers"] = licensed_users
        if new_users is not UNSET:
            field_dict["newUsers"] = new_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        licensed_users = d.pop("licensedUsers", UNSET)

        new_users = d.pop("newUsers", UNSET)

        rest_organization_licensing_information = cls(
            licensed_users=licensed_users,
            new_users=new_users,
        )

        rest_organization_licensing_information.additional_properties = d
        return rest_organization_licensing_information

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
