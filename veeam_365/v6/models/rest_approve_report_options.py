from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_organization_removed_users import RESTOrganizationRemovedUsers


T = TypeVar("T", bound="RESTApproveReportOptions")


@_attrs_define
class RESTApproveReportOptions:
    """
    Attributes:
        removed_users (list[RESTOrganizationRemovedUsers] | Unset):
    """

    removed_users: list[RESTOrganizationRemovedUsers] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        removed_users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.removed_users, Unset):
            removed_users = []
            for removed_users_item_data in self.removed_users:
                removed_users_item = removed_users_item_data.to_dict()
                removed_users.append(removed_users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if removed_users is not UNSET:
            field_dict["removedUsers"] = removed_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_organization_removed_users import RESTOrganizationRemovedUsers

        d = dict(src_dict)
        _removed_users = d.pop("removedUsers", UNSET)
        removed_users: list[RESTOrganizationRemovedUsers] | Unset = UNSET
        if _removed_users is not UNSET:
            removed_users = []
            for removed_users_item_data in _removed_users:
                removed_users_item = RESTOrganizationRemovedUsers.from_dict(removed_users_item_data)

                removed_users.append(removed_users_item)

        rest_approve_report_options = cls(
            removed_users=removed_users,
        )

        rest_approve_report_options.additional_properties = d
        return rest_approve_report_options

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
