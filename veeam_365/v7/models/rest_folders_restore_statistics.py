from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTFoldersRestoreStatistics")


@_attrs_define
class RESTFoldersRestoreStatistics:
    """
    Attributes:
        failed_folders_count (int | Unset): Number of folders for which the restore operation failed.
        exceptions (list[str] | Unset): Array of exceptions from the restore operation.
        created_items_count (int | Unset): Number of missed items restored from the backup.
        merged_items_count (int | Unset): Number of changed items restored from the backup.
        failed_items_count (int | Unset): Number of items for which the restore operation failed.
        skipped_items_count (int | Unset): Number of items that were not changed or missed in the original location.
            Such items are skipped during the restore operation.
        cannot_continue_error (str | Unset): Error occurred during the restore operation.
        warnings (list[str] | Unset): Array of warnings appeared during the restore operation.
    """

    failed_folders_count: int | Unset = UNSET
    exceptions: list[str] | Unset = UNSET
    created_items_count: int | Unset = UNSET
    merged_items_count: int | Unset = UNSET
    failed_items_count: int | Unset = UNSET
    skipped_items_count: int | Unset = UNSET
    cannot_continue_error: str | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed_folders_count = self.failed_folders_count

        exceptions: list[str] | Unset = UNSET
        if not isinstance(self.exceptions, Unset):
            exceptions = self.exceptions

        created_items_count = self.created_items_count

        merged_items_count = self.merged_items_count

        failed_items_count = self.failed_items_count

        skipped_items_count = self.skipped_items_count

        cannot_continue_error = self.cannot_continue_error

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failed_folders_count is not UNSET:
            field_dict["failedFoldersCount"] = failed_folders_count
        if exceptions is not UNSET:
            field_dict["exceptions"] = exceptions
        if created_items_count is not UNSET:
            field_dict["createdItemsCount"] = created_items_count
        if merged_items_count is not UNSET:
            field_dict["mergedItemsCount"] = merged_items_count
        if failed_items_count is not UNSET:
            field_dict["failedItemsCount"] = failed_items_count
        if skipped_items_count is not UNSET:
            field_dict["skippedItemsCount"] = skipped_items_count
        if cannot_continue_error is not UNSET:
            field_dict["cannotContinueError"] = cannot_continue_error
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed_folders_count = d.pop("failedFoldersCount", UNSET)

        exceptions = cast(list[str], d.pop("exceptions", UNSET))

        created_items_count = d.pop("createdItemsCount", UNSET)

        merged_items_count = d.pop("mergedItemsCount", UNSET)

        failed_items_count = d.pop("failedItemsCount", UNSET)

        skipped_items_count = d.pop("skippedItemsCount", UNSET)

        cannot_continue_error = d.pop("cannotContinueError", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        rest_folders_restore_statistics = cls(
            failed_folders_count=failed_folders_count,
            exceptions=exceptions,
            created_items_count=created_items_count,
            merged_items_count=merged_items_count,
            failed_items_count=failed_items_count,
            skipped_items_count=skipped_items_count,
            cannot_continue_error=cannot_continue_error,
            warnings=warnings,
        )

        rest_folders_restore_statistics.additional_properties = d
        return rest_folders_restore_statistics

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
