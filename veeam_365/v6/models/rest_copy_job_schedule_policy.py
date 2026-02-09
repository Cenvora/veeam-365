from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_copy_job_schedule_policy_daily_type import RESTCopyJobSchedulePolicyDailyType
from ..models.rest_copy_job_schedule_policy_periodically_every import RESTCopyJobSchedulePolicyPeriodicallyEvery
from ..models.rest_copy_job_schedule_policy_type import RESTCopyJobSchedulePolicyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_backup_window_settings import RESTBackupWindowSettings


T = TypeVar("T", bound="RESTCopyJobSchedulePolicy")


@_attrs_define
class RESTCopyJobSchedulePolicy:
    """
    Attributes:
        type_ (RESTCopyJobSchedulePolicyType | Unset):
        periodically_every (RESTCopyJobSchedulePolicyPeriodicallyEvery | Unset):
        daily_type (RESTCopyJobSchedulePolicyDailyType | Unset):
        daily_time (str | Unset):
        backup_copy_window_enabled (bool | None | Unset):
        backup_copy_window_settings (RESTBackupWindowSettings | Unset):
    """

    type_: RESTCopyJobSchedulePolicyType | Unset = UNSET
    periodically_every: RESTCopyJobSchedulePolicyPeriodicallyEvery | Unset = UNSET
    daily_type: RESTCopyJobSchedulePolicyDailyType | Unset = UNSET
    daily_time: str | Unset = UNSET
    backup_copy_window_enabled: bool | None | Unset = UNSET
    backup_copy_window_settings: RESTBackupWindowSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        backup_copy_window_enabled: bool | None | Unset
        if isinstance(self.backup_copy_window_enabled, Unset):
            backup_copy_window_enabled = UNSET
        else:
            backup_copy_window_enabled = self.backup_copy_window_enabled

        backup_copy_window_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_copy_window_settings, Unset):
            backup_copy_window_settings = self.backup_copy_window_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if periodically_every is not UNSET:
            field_dict["periodicallyEvery"] = periodically_every
        if daily_type is not UNSET:
            field_dict["dailyType"] = daily_type
        if daily_time is not UNSET:
            field_dict["dailyTime"] = daily_time
        if backup_copy_window_enabled is not UNSET:
            field_dict["backupCopyWindowEnabled"] = backup_copy_window_enabled
        if backup_copy_window_settings is not UNSET:
            field_dict["backupCopyWindowSettings"] = backup_copy_window_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_backup_window_settings import RESTBackupWindowSettings

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTCopyJobSchedulePolicyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTCopyJobSchedulePolicyType(_type_)

        _periodically_every = d.pop("periodicallyEvery", UNSET)
        periodically_every: RESTCopyJobSchedulePolicyPeriodicallyEvery | Unset
        if isinstance(_periodically_every, Unset):
            periodically_every = UNSET
        else:
            periodically_every = RESTCopyJobSchedulePolicyPeriodicallyEvery(_periodically_every)

        _daily_type = d.pop("dailyType", UNSET)
        daily_type: RESTCopyJobSchedulePolicyDailyType | Unset
        if isinstance(_daily_type, Unset):
            daily_type = UNSET
        else:
            daily_type = RESTCopyJobSchedulePolicyDailyType(_daily_type)

        daily_time = d.pop("dailyTime", UNSET)

        def _parse_backup_copy_window_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        backup_copy_window_enabled = _parse_backup_copy_window_enabled(d.pop("backupCopyWindowEnabled", UNSET))

        _backup_copy_window_settings = d.pop("backupCopyWindowSettings", UNSET)
        backup_copy_window_settings: RESTBackupWindowSettings | Unset
        if isinstance(_backup_copy_window_settings, Unset):
            backup_copy_window_settings = UNSET
        else:
            backup_copy_window_settings = RESTBackupWindowSettings.from_dict(_backup_copy_window_settings)

        rest_copy_job_schedule_policy = cls(
            type_=type_,
            periodically_every=periodically_every,
            daily_type=daily_type,
            daily_time=daily_time,
            backup_copy_window_enabled=backup_copy_window_enabled,
            backup_copy_window_settings=backup_copy_window_settings,
        )

        rest_copy_job_schedule_policy.additional_properties = d
        return rest_copy_job_schedule_policy

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
