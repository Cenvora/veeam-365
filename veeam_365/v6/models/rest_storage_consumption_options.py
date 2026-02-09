from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_storage_consumption_options_format import RESTStorageConsumptionOptionsFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTStorageConsumptionOptions")


@_attrs_define
class RESTStorageConsumptionOptions:
    """
    Attributes:
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
        format_ (RESTStorageConsumptionOptionsFormat | Unset):
        timezone (str | Unset):
    """

    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    format_: RESTStorageConsumptionOptionsFormat | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

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

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        _format_ = d.pop("format", UNSET)
        format_: RESTStorageConsumptionOptionsFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = RESTStorageConsumptionOptionsFormat(_format_)

        timezone = d.pop("timezone", UNSET)

        rest_storage_consumption_options = cls(
            start_time=start_time,
            end_time=end_time,
            format_=format_,
            timezone=timezone,
        )

        rest_storage_consumption_options.additional_properties = d
        return rest_storage_consumption_options

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
