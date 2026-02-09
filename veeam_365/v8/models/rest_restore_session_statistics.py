from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_item_restore_details_composed import RESTItemRestoreDetailsComposed


T = TypeVar("T", bound="RESTRestoreSessionStatistics")


@_attrs_define
class RESTRestoreSessionStatistics:
    r"""
    Attributes:
        total_items_count (int): Total number of items in the backup.
        restored_items_count (int): Number of items restored from the backup.
        failed_items_count (int): Number of items for which the restore operation failed.
        skipped_items_count (int): Number of items that were skipped during the restore operation.
        items (list[RESTItemRestoreDetailsComposed]): \[If available\] Statistics for each item processed during the
            restore operation.
        warnings (list[str] | Unset): Array of warnings appeared during the restore operation.
        errors (list[str] | Unset): Array of errors occurred during the restore operation.
    """

    total_items_count: int
    restored_items_count: int
    failed_items_count: int
    skipped_items_count: int
    items: list[RESTItemRestoreDetailsComposed]
    warnings: list[str] | Unset = UNSET
    errors: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_items_count = self.total_items_count

        restored_items_count = self.restored_items_count

        failed_items_count = self.failed_items_count

        skipped_items_count = self.skipped_items_count

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalItemsCount": total_items_count,
                "restoredItemsCount": restored_items_count,
                "failedItemsCount": failed_items_count,
                "skippedItemsCount": skipped_items_count,
                "items": items,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_item_restore_details_composed import RESTItemRestoreDetailsComposed

        d = dict(src_dict)
        total_items_count = d.pop("totalItemsCount")

        restored_items_count = d.pop("restoredItemsCount")

        failed_items_count = d.pop("failedItemsCount")

        skipped_items_count = d.pop("skippedItemsCount")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = RESTItemRestoreDetailsComposed.from_dict(items_item_data)

            items.append(items_item)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        errors = cast(list[str], d.pop("errors", UNSET))

        rest_restore_session_statistics = cls(
            total_items_count=total_items_count,
            restored_items_count=restored_items_count,
            failed_items_count=failed_items_count,
            skipped_items_count=skipped_items_count,
            items=items,
            warnings=warnings,
            errors=errors,
        )

        rest_restore_session_statistics.additional_properties = d
        return rest_restore_session_statistics

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
