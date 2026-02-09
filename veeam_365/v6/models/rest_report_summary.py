from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTReportSummary")


@_attrs_define
class RESTReportSummary:
    """
    Attributes:
        initial_users_count (int | Unset):
        reported_users_count (int | Unset):
        new_users_count (int | Unset):
    """

    initial_users_count: int | Unset = UNSET
    reported_users_count: int | Unset = UNSET
    new_users_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        initial_users_count = self.initial_users_count

        reported_users_count = self.reported_users_count

        new_users_count = self.new_users_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if initial_users_count is not UNSET:
            field_dict["initialUsersCount"] = initial_users_count
        if reported_users_count is not UNSET:
            field_dict["reportedUsersCount"] = reported_users_count
        if new_users_count is not UNSET:
            field_dict["newUsersCount"] = new_users_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        initial_users_count = d.pop("initialUsersCount", UNSET)

        reported_users_count = d.pop("reportedUsersCount", UNSET)

        new_users_count = d.pop("newUsersCount", UNSET)

        rest_report_summary = cls(
            initial_users_count=initial_users_count,
            reported_users_count=reported_users_count,
            new_users_count=new_users_count,
        )

        rest_report_summary.additional_properties = d
        return rest_report_summary

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
