from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_job_schedule_policy_daily_type import RESTJobSchedulePolicyDailyType
from ..models.rest_job_schedule_policy_periodically_every import RESTJobSchedulePolicyPeriodicallyEvery
from ..models.rest_job_schedule_policy_type import RESTJobSchedulePolicyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_backup_window_settings import RESTBackupWindowSettings


T = TypeVar("T", bound="RESTJobSchedulePolicy")


@_attrs_define
class RESTJobSchedulePolicy:
    """
    Attributes:
        schedule_enabled (bool | None | Unset):
        backup_window_enabled (bool | None | Unset):
        backup_window_settings (RESTBackupWindowSettings | Unset):
        periodically_window_settings (RESTBackupWindowSettings | Unset):
        periodically_offset_minutes (int | None | Unset):
        type_ (RESTJobSchedulePolicyType | Unset):
        periodically_every (RESTJobSchedulePolicyPeriodicallyEvery | Unset):
        daily_type (RESTJobSchedulePolicyDailyType | Unset):
        daily_time (str | Unset):
        retry_enabled (bool | None | Unset):
        retry_number (int | None | Unset):
        retry_wait_interval (int | None | Unset):
    """

    schedule_enabled: bool | None | Unset = UNSET
    backup_window_enabled: bool | None | Unset = UNSET
    backup_window_settings: RESTBackupWindowSettings | Unset = UNSET
    periodically_window_settings: RESTBackupWindowSettings | Unset = UNSET
    periodically_offset_minutes: int | None | Unset = UNSET
    type_: RESTJobSchedulePolicyType | Unset = UNSET
    periodically_every: RESTJobSchedulePolicyPeriodicallyEvery | Unset = UNSET
    daily_type: RESTJobSchedulePolicyDailyType | Unset = UNSET
    daily_time: str | Unset = UNSET
    retry_enabled: bool | None | Unset = UNSET
    retry_number: int | None | Unset = UNSET
    retry_wait_interval: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_enabled: bool | None | Unset
        if isinstance(self.schedule_enabled, Unset):
            schedule_enabled = UNSET
        else:
            schedule_enabled = self.schedule_enabled

        backup_window_enabled: bool | None | Unset
        if isinstance(self.backup_window_enabled, Unset):
            backup_window_enabled = UNSET
        else:
            backup_window_enabled = self.backup_window_enabled

        backup_window_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_window_settings, Unset):
            backup_window_settings = self.backup_window_settings.to_dict()

        periodically_window_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.periodically_window_settings, Unset):
            periodically_window_settings = self.periodically_window_settings.to_dict()

        periodically_offset_minutes: int | None | Unset
        if isinstance(self.periodically_offset_minutes, Unset):
            periodically_offset_minutes = UNSET
        else:
            periodically_offset_minutes = self.periodically_offset_minutes

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        periodically_every: str | Unset = UNSET
        if not isinstance(self.periodically_every, Unset):
            periodically_every = self.periodically_every.value

        daily_type: str | Unset = UNSET
        if not isinstance(self.daily_type, Unset):
            daily_type = self.daily_type.value

        daily_time = self.daily_time

        retry_enabled: bool | None | Unset
        if isinstance(self.retry_enabled, Unset):
            retry_enabled = UNSET
        else:
            retry_enabled = self.retry_enabled

        retry_number: int | None | Unset
        if isinstance(self.retry_number, Unset):
            retry_number = UNSET
        else:
            retry_number = self.retry_number

        retry_wait_interval: int | None | Unset
        if isinstance(self.retry_wait_interval, Unset):
            retry_wait_interval = UNSET
        else:
            retry_wait_interval = self.retry_wait_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_enabled is not UNSET:
            field_dict["scheduleEnabled"] = schedule_enabled
        if backup_window_enabled is not UNSET:
            field_dict["backupWindowEnabled"] = backup_window_enabled
        if backup_window_settings is not UNSET:
            field_dict["backupWindowSettings"] = backup_window_settings
        if periodically_window_settings is not UNSET:
            field_dict["periodicallyWindowSettings"] = periodically_window_settings
        if periodically_offset_minutes is not UNSET:
            field_dict["periodicallyOffsetMinutes"] = periodically_offset_minutes
        if type_ is not UNSET:
            field_dict["type"] = type_
        if periodically_every is not UNSET:
            field_dict["periodicallyEvery"] = periodically_every
        if daily_type is not UNSET:
            field_dict["dailyType"] = daily_type
        if daily_time is not UNSET:
            field_dict["dailyTime"] = daily_time
        if retry_enabled is not UNSET:
            field_dict["retryEnabled"] = retry_enabled
        if retry_number is not UNSET:
            field_dict["retryNumber"] = retry_number
        if retry_wait_interval is not UNSET:
            field_dict["retryWaitInterval"] = retry_wait_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_backup_window_settings import RESTBackupWindowSettings

        d = dict(src_dict)

        def _parse_schedule_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        schedule_enabled = _parse_schedule_enabled(d.pop("scheduleEnabled", UNSET))

        def _parse_backup_window_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        backup_window_enabled = _parse_backup_window_enabled(d.pop("backupWindowEnabled", UNSET))

        _backup_window_settings = d.pop("backupWindowSettings", UNSET)
        backup_window_settings: RESTBackupWindowSettings | Unset
        if isinstance(_backup_window_settings, Unset):
            backup_window_settings = UNSET
        else:
            backup_window_settings = RESTBackupWindowSettings.from_dict(_backup_window_settings)

        _periodically_window_settings = d.pop("periodicallyWindowSettings", UNSET)
        periodically_window_settings: RESTBackupWindowSettings | Unset
        if isinstance(_periodically_window_settings, Unset):
            periodically_window_settings = UNSET
        else:
            periodically_window_settings = RESTBackupWindowSettings.from_dict(_periodically_window_settings)

        def _parse_periodically_offset_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        periodically_offset_minutes = _parse_periodically_offset_minutes(d.pop("periodicallyOffsetMinutes", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: RESTJobSchedulePolicyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTJobSchedulePolicyType(_type_)

        _periodically_every = d.pop("periodicallyEvery", UNSET)
        periodically_every: RESTJobSchedulePolicyPeriodicallyEvery | Unset
        if isinstance(_periodically_every, Unset):
            periodically_every = UNSET
        else:
            periodically_every = RESTJobSchedulePolicyPeriodicallyEvery(_periodically_every)

        _daily_type = d.pop("dailyType", UNSET)
        daily_type: RESTJobSchedulePolicyDailyType | Unset
        if isinstance(_daily_type, Unset):
            daily_type = UNSET
        else:
            daily_type = RESTJobSchedulePolicyDailyType(_daily_type)

        daily_time = d.pop("dailyTime", UNSET)

        def _parse_retry_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        retry_enabled = _parse_retry_enabled(d.pop("retryEnabled", UNSET))

        def _parse_retry_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retry_number = _parse_retry_number(d.pop("retryNumber", UNSET))

        def _parse_retry_wait_interval(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retry_wait_interval = _parse_retry_wait_interval(d.pop("retryWaitInterval", UNSET))

        rest_job_schedule_policy = cls(
            schedule_enabled=schedule_enabled,
            backup_window_enabled=backup_window_enabled,
            backup_window_settings=backup_window_settings,
            periodically_window_settings=periodically_window_settings,
            periodically_offset_minutes=periodically_offset_minutes,
            type_=type_,
            periodically_every=periodically_every,
            daily_type=daily_type,
            daily_time=daily_time,
            retry_enabled=retry_enabled,
            retry_number=retry_number,
            retry_wait_interval=retry_wait_interval,
        )

        rest_job_schedule_policy.additional_properties = d
        return rest_job_schedule_policy

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
