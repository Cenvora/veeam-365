from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_license_overview_options_format import RESTLicenseOverviewOptionsFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTLicenseOverviewOptions")


@_attrs_define
class RESTLicenseOverviewOptions:
    """
    Attributes:
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        format_ (RESTLicenseOverviewOptionsFormat | Unset):
        timezone (str | Unset):
    """

    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    format_: RESTLicenseOverviewOptionsFormat | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if format_ is not UNSET:
            field_dict["format"] = format_
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        _format_ = d.pop("format", UNSET)
        format_: RESTLicenseOverviewOptionsFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = RESTLicenseOverviewOptionsFormat(_format_)

        timezone = d.pop("timezone", UNSET)

        rest_license_overview_options = cls(
            start_time=start_time,
            end_time=end_time,
            format_=format_,
            timezone=timezone,
        )

        rest_license_overview_options.additional_properties = d
        return rest_license_overview_options

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
