from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_health_status import RESTHealthStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_health_report_entries import RESTHealthReportEntries





T = TypeVar("T", bound="RESTHealthReport")



@_attrs_define
class RESTHealthReport:
    """ 
        Attributes:
            status (RESTHealthStatus | Unset): Status that Veeam Backup for Microsoft assigns as a result of a health check.
            entries (RESTHealthReportEntries | Unset):
     """

    status: RESTHealthStatus | Unset = UNSET
    entries: RESTHealthReportEntries | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_health_report_entries import RESTHealthReportEntries
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        entries: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = self.entries.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_health_report_entries import RESTHealthReportEntries
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: RESTHealthStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = RESTHealthStatus(_status)




        _entries = d.pop("entries", UNSET)
        entries: RESTHealthReportEntries | Unset
        if isinstance(_entries,  Unset):
            entries = UNSET
        else:
            entries = RESTHealthReportEntries.from_dict(_entries)




        rest_health_report = cls(
            status=status,
            entries=entries,
        )


        rest_health_report.additional_properties = d
        return rest_health_report

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
