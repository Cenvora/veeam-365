from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_summary_item import RESTSummaryItem


T = TypeVar("T", bound="RESTRestoreStatistics")


@_attrs_define
class RESTRestoreStatistics:
    """
    Attributes:
        total_items_count (int | Unset):
        restored_items_count (int | Unset):
        failed_items_count (int | Unset):
        skipped_items_count (int | Unset):
        restore_issues (list[RESTSummaryItem] | Unset):
    """

    total_items_count: int | Unset = UNSET
    restored_items_count: int | Unset = UNSET
    failed_items_count: int | Unset = UNSET
    skipped_items_count: int | Unset = UNSET
    restore_issues: list[RESTSummaryItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_items_count = self.total_items_count

        restored_items_count = self.restored_items_count

        failed_items_count = self.failed_items_count

        skipped_items_count = self.skipped_items_count

        restore_issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.restore_issues, Unset):
            restore_issues = []
            for restore_issues_item_data in self.restore_issues:
                restore_issues_item = restore_issues_item_data.to_dict()
                restore_issues.append(restore_issues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_items_count is not UNSET:
            field_dict["totalItemsCount"] = total_items_count
        if restored_items_count is not UNSET:
            field_dict["restoredItemsCount"] = restored_items_count
        if failed_items_count is not UNSET:
            field_dict["failedItemsCount"] = failed_items_count
        if skipped_items_count is not UNSET:
            field_dict["skippedItemsCount"] = skipped_items_count
        if restore_issues is not UNSET:
            field_dict["restoreIssues"] = restore_issues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_summary_item import RESTSummaryItem

        d = dict(src_dict)
        total_items_count = d.pop("totalItemsCount", UNSET)

        restored_items_count = d.pop("restoredItemsCount", UNSET)

        failed_items_count = d.pop("failedItemsCount", UNSET)

        skipped_items_count = d.pop("skippedItemsCount", UNSET)

        _restore_issues = d.pop("restoreIssues", UNSET)
        restore_issues: list[RESTSummaryItem] | Unset = UNSET
        if _restore_issues is not UNSET:
            restore_issues = []
            for restore_issues_item_data in _restore_issues:
                restore_issues_item = RESTSummaryItem.from_dict(restore_issues_item_data)

                restore_issues.append(restore_issues_item)

        rest_restore_statistics = cls(
            total_items_count=total_items_count,
            restored_items_count=restored_items_count,
            failed_items_count=failed_items_count,
            skipped_items_count=skipped_items_count,
            restore_issues=restore_issues,
        )

        rest_restore_statistics.additional_properties = d
        return rest_restore_statistics

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
