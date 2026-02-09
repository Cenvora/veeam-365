from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_share_point_bulk_restore_statistics_status import RESTSharePointBulkRestoreStatisticsStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_extended_common_statistic import RESTExtendedCommonStatistic


T = TypeVar("T", bound="RESTSharePointBulkRestoreStatistics")


@_attrs_define
class RESTSharePointBulkRestoreStatistics:
    """
    Attributes:
        status (RESTSharePointBulkRestoreStatisticsStatus | Unset): Status of the restore operation.
        details (list[RESTExtendedCommonStatistic] | Unset): Restore operation details.
        error (str | Unset): Error occurred during the restore operation.
    """

    status: RESTSharePointBulkRestoreStatisticsStatus | Unset = UNSET
    details: list[RESTExtendedCommonStatistic] | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_extended_common_statistic import RESTExtendedCommonStatistic

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: RESTSharePointBulkRestoreStatisticsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTSharePointBulkRestoreStatisticsStatus(_status)

        _details = d.pop("details", UNSET)
        details: list[RESTExtendedCommonStatistic] | Unset = UNSET
        if _details is not UNSET:
            details = []
            for details_item_data in _details:
                details_item = RESTExtendedCommonStatistic.from_dict(details_item_data)

                details.append(details_item)

        error = d.pop("error", UNSET)

        rest_share_point_bulk_restore_statistics = cls(
            status=status,
            details=details,
            error=error,
        )

        rest_share_point_bulk_restore_statistics.additional_properties = d
        return rest_share_point_bulk_restore_statistics

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
