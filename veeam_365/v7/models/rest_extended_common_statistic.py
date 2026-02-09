from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_extended_common_statistic_status import RESTExtendedCommonStatisticStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_one_drive import RESTOneDrive
    from ..models.rest_share_point_common_restore_statistics import RESTSharePointCommonRestoreStatistics


T = TypeVar("T", bound="RESTExtendedCommonStatistic")


@_attrs_define
class RESTExtendedCommonStatistic:
    """
    Attributes:
        one_drive (RESTOneDrive | Unset):
        status (RESTExtendedCommonStatisticStatus | Unset):
        error (str | Unset):
        details (RESTSharePointCommonRestoreStatistics | Unset):
    """

    one_drive: RESTOneDrive | Unset = UNSET
    status: RESTExtendedCommonStatisticStatus | Unset = UNSET
    error: str | Unset = UNSET
    details: RESTSharePointCommonRestoreStatistics | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        one_drive: dict[str, Any] | Unset = UNSET
        if not isinstance(self.one_drive, Unset):
            one_drive = self.one_drive.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        error = self.error

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if one_drive is not UNSET:
            field_dict["oneDrive"] = one_drive
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_one_drive import RESTOneDrive
        from ..models.rest_share_point_common_restore_statistics import RESTSharePointCommonRestoreStatistics

        d = dict(src_dict)
        _one_drive = d.pop("oneDrive", UNSET)
        one_drive: RESTOneDrive | Unset
        if isinstance(_one_drive, Unset):
            one_drive = UNSET
        else:
            one_drive = RESTOneDrive.from_dict(_one_drive)

        _status = d.pop("status", UNSET)
        status: RESTExtendedCommonStatisticStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTExtendedCommonStatisticStatus(_status)

        error = d.pop("error", UNSET)

        _details = d.pop("details", UNSET)
        details: RESTSharePointCommonRestoreStatistics | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = RESTSharePointCommonRestoreStatistics.from_dict(_details)

        rest_extended_common_statistic = cls(
            one_drive=one_drive,
            status=status,
            error=error,
            details=details,
        )

        rest_extended_common_statistic.additional_properties = d
        return rest_extended_common_statistic

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
