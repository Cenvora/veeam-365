from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTMonthlyReportInterval")


@_attrs_define
class RESTMonthlyReportInterval:
    """
    Attributes:
        start_of_interval (datetime.datetime | Unset):
        end_of_interval (datetime.datetime | Unset):
    """

    start_of_interval: datetime.datetime | Unset = UNSET
    end_of_interval: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_of_interval: str | Unset = UNSET
        if not isinstance(self.start_of_interval, Unset):
            start_of_interval = self.start_of_interval.isoformat()

        end_of_interval: str | Unset = UNSET
        if not isinstance(self.end_of_interval, Unset):
            end_of_interval = self.end_of_interval.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_of_interval is not UNSET:
            field_dict["startOfInterval"] = start_of_interval
        if end_of_interval is not UNSET:
            field_dict["endOfInterval"] = end_of_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _start_of_interval = d.pop("startOfInterval", UNSET)
        start_of_interval: datetime.datetime | Unset
        if isinstance(_start_of_interval, Unset):
            start_of_interval = UNSET
        else:
            start_of_interval = isoparse(_start_of_interval)

        _end_of_interval = d.pop("endOfInterval", UNSET)
        end_of_interval: datetime.datetime | Unset
        if isinstance(_end_of_interval, Unset):
            end_of_interval = UNSET
        else:
            end_of_interval = isoparse(_end_of_interval)

        rest_monthly_report_interval = cls(
            start_of_interval=start_of_interval,
            end_of_interval=end_of_interval,
        )

        rest_monthly_report_interval.additional_properties = d
        return rest_monthly_report_interval

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
