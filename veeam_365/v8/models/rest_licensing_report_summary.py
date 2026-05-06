from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTLicensingReportSummary")



@_attrs_define
class RESTLicensingReportSummary:
    """ 
        Attributes:
            initial_count (int | Unset): Number of objects that consume the license within the time period covered by the
                report.
            initial_points (float | Unset): Number of licensing points that consume the license within the time period
                covered by the report.
            reported_count (int | Unset): Number of objects consuming the license that you report to Veeam.
            reported_points (float | Unset): Number of licensing points consuming the license that you report to Veeam.
            new_count (int | Unset): Number of objects that were activated within the time period covered by the report.
            new_points (float | Unset): Number of licensing points that were activated within the time period covered by the
                report.
     """

    initial_count: int | Unset = UNSET
    initial_points: float | Unset = UNSET
    reported_count: int | Unset = UNSET
    reported_points: float | Unset = UNSET
    new_count: int | Unset = UNSET
    new_points: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        initial_count = self.initial_count

        initial_points = self.initial_points

        reported_count = self.reported_count

        reported_points = self.reported_points

        new_count = self.new_count

        new_points = self.new_points


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if initial_count is not UNSET:
            field_dict["initialCount"] = initial_count
        if initial_points is not UNSET:
            field_dict["initialPoints"] = initial_points
        if reported_count is not UNSET:
            field_dict["reportedCount"] = reported_count
        if reported_points is not UNSET:
            field_dict["reportedPoints"] = reported_points
        if new_count is not UNSET:
            field_dict["newCount"] = new_count
        if new_points is not UNSET:
            field_dict["newPoints"] = new_points

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        initial_count = d.pop("initialCount", UNSET)

        initial_points = d.pop("initialPoints", UNSET)

        reported_count = d.pop("reportedCount", UNSET)

        reported_points = d.pop("reportedPoints", UNSET)

        new_count = d.pop("newCount", UNSET)

        new_points = d.pop("newPoints", UNSET)

        rest_licensing_report_summary = cls(
            initial_count=initial_count,
            initial_points=initial_points,
            reported_count=reported_count,
            reported_points=reported_points,
            new_count=new_count,
            new_points=new_points,
        )


        rest_licensing_report_summary.additional_properties = d
        return rest_licensing_report_summary

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
