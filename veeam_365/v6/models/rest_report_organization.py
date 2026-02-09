from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTReportOrganization")


@_attrs_define
class RESTReportOrganization:
    """
    Attributes:
        organization_id (str | Unset):
        organization_name (str | Unset):
        removed_users_count (int | Unset):
        removal_reason (str | Unset):
        reported_users_count (int | Unset):
        new_users_count (int | Unset):
        initial_users_count (int | Unset):
    """

    organization_id: str | Unset = UNSET
    organization_name: str | Unset = UNSET
    removed_users_count: int | Unset = UNSET
    removal_reason: str | Unset = UNSET
    reported_users_count: int | Unset = UNSET
    new_users_count: int | Unset = UNSET
    initial_users_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        organization_name = self.organization_name

        removed_users_count = self.removed_users_count

        removal_reason = self.removal_reason

        reported_users_count = self.reported_users_count

        new_users_count = self.new_users_count

        initial_users_count = self.initial_users_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if removed_users_count is not UNSET:
            field_dict["removedUsersCount"] = removed_users_count
        if removal_reason is not UNSET:
            field_dict["removalReason"] = removal_reason
        if reported_users_count is not UNSET:
            field_dict["reportedUsersCount"] = reported_users_count
        if new_users_count is not UNSET:
            field_dict["newUsersCount"] = new_users_count
        if initial_users_count is not UNSET:
            field_dict["initialUsersCount"] = initial_users_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_id = d.pop("organizationId", UNSET)

        organization_name = d.pop("organizationName", UNSET)

        removed_users_count = d.pop("removedUsersCount", UNSET)

        removal_reason = d.pop("removalReason", UNSET)

        reported_users_count = d.pop("reportedUsersCount", UNSET)

        new_users_count = d.pop("newUsersCount", UNSET)

        initial_users_count = d.pop("initialUsersCount", UNSET)

        rest_report_organization = cls(
            organization_id=organization_id,
            organization_name=organization_name,
            removed_users_count=removed_users_count,
            removal_reason=removal_reason,
            reported_users_count=reported_users_count,
            new_users_count=new_users_count,
            initial_users_count=initial_users_count,
        )

        rest_report_organization.additional_properties = d
        return rest_report_organization

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
