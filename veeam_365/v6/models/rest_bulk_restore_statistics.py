from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_bulk_restore_statistics_status import RESTBulkRestoreStatisticsStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_bulk_mailbox_restore_statistics import RESTBulkMailboxRestoreStatistics


T = TypeVar("T", bound="RESTBulkRestoreStatistics")


@_attrs_define
class RESTBulkRestoreStatistics:
    """
    Attributes:
        status (RESTBulkRestoreStatisticsStatus | Unset):
        error (str | Unset):
        details (list[RESTBulkMailboxRestoreStatistics] | Unset):
    """

    status: RESTBulkRestoreStatisticsStatus | Unset = UNSET
    error: str | Unset = UNSET
    details: list[RESTBulkMailboxRestoreStatistics] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        error = self.error

        details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_bulk_mailbox_restore_statistics import RESTBulkMailboxRestoreStatistics

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: RESTBulkRestoreStatisticsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTBulkRestoreStatisticsStatus(_status)

        error = d.pop("error", UNSET)

        _details = d.pop("details", UNSET)
        details: list[RESTBulkMailboxRestoreStatistics] | Unset = UNSET
        if _details is not UNSET:
            details = []
            for details_item_data in _details:
                details_item = RESTBulkMailboxRestoreStatistics.from_dict(details_item_data)

                details.append(details_item)

        rest_bulk_restore_statistics = cls(
            status=status,
            error=error,
            details=details,
        )

        rest_bulk_restore_statistics.additional_properties = d
        return rest_bulk_restore_statistics

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
