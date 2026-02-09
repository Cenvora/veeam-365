from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTOrganizationRemovedUsers")


@_attrs_define
class RESTOrganizationRemovedUsers:
    """
    Attributes:
        organization_id (str | Unset):
        removed_users_count (int | Unset):
        removal_reason (str | Unset):
    """

    organization_id: str | Unset = UNSET
    removed_users_count: int | Unset = UNSET
    removal_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        removed_users_count = self.removed_users_count

        removal_reason = self.removal_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if removed_users_count is not UNSET:
            field_dict["removedUsersCount"] = removed_users_count
        if removal_reason is not UNSET:
            field_dict["removalReason"] = removal_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_id = d.pop("organizationId", UNSET)

        removed_users_count = d.pop("removedUsersCount", UNSET)

        removal_reason = d.pop("removalReason", UNSET)

        rest_organization_removed_users = cls(
            organization_id=organization_id,
            removed_users_count=removed_users_count,
            removal_reason=removal_reason,
        )

        rest_organization_removed_users.additional_properties = d
        return rest_organization_removed_users

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
