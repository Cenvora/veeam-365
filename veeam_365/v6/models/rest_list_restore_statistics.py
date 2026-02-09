from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_restore_object import RESTRestoreObject


T = TypeVar("T", bound="RESTListRestoreStatistics")


@_attrs_define
class RESTListRestoreStatistics:
    """
    Attributes:
        restored_lists_count (int | Unset):
        failed_lists_count (int | Unset):
        total_items_count (int | Unset):
        restored_items_count (int | Unset):
        failed_items_count (int | Unset):
        skipped_items_by_error_count (int | Unset):
        skipped_items_by_no_changes_count (int | Unset):
        failed_restrictions_count (int | None | Unset):
        restore_issues (list[RESTRestoreObject] | Unset):
    """

    restored_lists_count: int | Unset = UNSET
    failed_lists_count: int | Unset = UNSET
    total_items_count: int | Unset = UNSET
    restored_items_count: int | Unset = UNSET
    failed_items_count: int | Unset = UNSET
    skipped_items_by_error_count: int | Unset = UNSET
    skipped_items_by_no_changes_count: int | Unset = UNSET
    failed_restrictions_count: int | None | Unset = UNSET
    restore_issues: list[RESTRestoreObject] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restored_lists_count = self.restored_lists_count

        failed_lists_count = self.failed_lists_count

        total_items_count = self.total_items_count

        restored_items_count = self.restored_items_count

        failed_items_count = self.failed_items_count

        skipped_items_by_error_count = self.skipped_items_by_error_count

        skipped_items_by_no_changes_count = self.skipped_items_by_no_changes_count

        failed_restrictions_count: int | None | Unset
        if isinstance(self.failed_restrictions_count, Unset):
            failed_restrictions_count = UNSET
        else:
            failed_restrictions_count = self.failed_restrictions_count

        restore_issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.restore_issues, Unset):
            restore_issues = []
            for restore_issues_item_data in self.restore_issues:
                restore_issues_item = restore_issues_item_data.to_dict()
                restore_issues.append(restore_issues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if restored_lists_count is not UNSET:
            field_dict["restoredListsCount"] = restored_lists_count
        if failed_lists_count is not UNSET:
            field_dict["failedListsCount"] = failed_lists_count
        if total_items_count is not UNSET:
            field_dict["totalItemsCount"] = total_items_count
        if restored_items_count is not UNSET:
            field_dict["restoredItemsCount"] = restored_items_count
        if failed_items_count is not UNSET:
            field_dict["failedItemsCount"] = failed_items_count
        if skipped_items_by_error_count is not UNSET:
            field_dict["skippedItemsByErrorCount"] = skipped_items_by_error_count
        if skipped_items_by_no_changes_count is not UNSET:
            field_dict["skippedItemsByNoChangesCount"] = skipped_items_by_no_changes_count
        if failed_restrictions_count is not UNSET:
            field_dict["failedRestrictionsCount"] = failed_restrictions_count
        if restore_issues is not UNSET:
            field_dict["restoreIssues"] = restore_issues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_restore_object import RESTRestoreObject

        d = dict(src_dict)
        restored_lists_count = d.pop("restoredListsCount", UNSET)

        failed_lists_count = d.pop("failedListsCount", UNSET)

        total_items_count = d.pop("totalItemsCount", UNSET)

        restored_items_count = d.pop("restoredItemsCount", UNSET)

        failed_items_count = d.pop("failedItemsCount", UNSET)

        skipped_items_by_error_count = d.pop("skippedItemsByErrorCount", UNSET)

        skipped_items_by_no_changes_count = d.pop("skippedItemsByNoChangesCount", UNSET)

        def _parse_failed_restrictions_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        failed_restrictions_count = _parse_failed_restrictions_count(d.pop("failedRestrictionsCount", UNSET))

        _restore_issues = d.pop("restoreIssues", UNSET)
        restore_issues: list[RESTRestoreObject] | Unset = UNSET
        if _restore_issues is not UNSET:
            restore_issues = []
            for restore_issues_item_data in _restore_issues:
                restore_issues_item = RESTRestoreObject.from_dict(restore_issues_item_data)

                restore_issues.append(restore_issues_item)

        rest_list_restore_statistics = cls(
            restored_lists_count=restored_lists_count,
            failed_lists_count=failed_lists_count,
            total_items_count=total_items_count,
            restored_items_count=restored_items_count,
            failed_items_count=failed_items_count,
            skipped_items_by_error_count=skipped_items_by_error_count,
            skipped_items_by_no_changes_count=skipped_items_by_no_changes_count,
            failed_restrictions_count=failed_restrictions_count,
            restore_issues=restore_issues,
        )

        rest_list_restore_statistics.additional_properties = d
        return rest_list_restore_statistics

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
