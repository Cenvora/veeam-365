from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_backup_repository_from_client_daily_type import RESTBackupRepositoryFromClientDailyType
from ..models.rest_backup_repository_from_client_monthly_daynumber import RESTBackupRepositoryFromClientMonthlyDaynumber
from ..models.rest_backup_repository_from_client_monthly_dayofweek import RESTBackupRepositoryFromClientMonthlyDayofweek
from ..models.rest_backup_repository_from_client_retention_frequency_type import (
    RESTBackupRepositoryFromClientRetentionFrequencyType,
)
from ..models.rest_backup_repository_from_client_retention_period_type import (
    RESTBackupRepositoryFromClientRetentionPeriodType,
)
from ..models.rest_backup_repository_from_client_retention_type import RESTBackupRepositoryFromClientRetentionType
from ..models.rest_backup_repository_from_client_yearly_retention_period import (
    RESTBackupRepositoryFromClientYearlyRetentionPeriod,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTBackupRepositoryFromClient")


@_attrs_define
class RESTBackupRepositoryFromClient:
    """
    Attributes:
        retention_type (RESTBackupRepositoryFromClientRetentionType):
        object_storage_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        object_storage_cache_path (str | Unset):
        object_storage_encryption_enabled (bool | None | Unset):
        encryption_key_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        name (str | Unset):
        description (str | Unset):
        path (str | Unset):
        retention_period_type (RESTBackupRepositoryFromClientRetentionPeriodType | Unset):
        daily_retention_period (int | None | Unset):
        monthly_retention_period (int | None | Unset):
        yearly_retention_period (RESTBackupRepositoryFromClientYearlyRetentionPeriod | Unset):
        retention_frequency_type (RESTBackupRepositoryFromClientRetentionFrequencyType | Unset):
        daily_time (str | Unset):
        daily_type (RESTBackupRepositoryFromClientDailyType | Unset):
        monthly_time (str | Unset):
        monthly_daynumber (RESTBackupRepositoryFromClientMonthlyDaynumber | Unset):
        monthly_dayofweek (RESTBackupRepositoryFromClientMonthlyDayofweek | Unset):
        proxy_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        attach_used_repository (bool | None | Unset):
    """

    retention_type: RESTBackupRepositoryFromClientRetentionType
    object_storage_id: None | Unset | UUID = UNSET
    object_storage_cache_path: str | Unset = UNSET
    object_storage_encryption_enabled: bool | None | Unset = UNSET
    encryption_key_id: None | Unset | UUID = UNSET
    id: None | Unset | UUID = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    path: str | Unset = UNSET
    retention_period_type: RESTBackupRepositoryFromClientRetentionPeriodType | Unset = UNSET
    daily_retention_period: int | None | Unset = UNSET
    monthly_retention_period: int | None | Unset = UNSET
    yearly_retention_period: RESTBackupRepositoryFromClientYearlyRetentionPeriod | Unset = UNSET
    retention_frequency_type: RESTBackupRepositoryFromClientRetentionFrequencyType | Unset = UNSET
    daily_time: str | Unset = UNSET
    daily_type: RESTBackupRepositoryFromClientDailyType | Unset = UNSET
    monthly_time: str | Unset = UNSET
    monthly_daynumber: RESTBackupRepositoryFromClientMonthlyDaynumber | Unset = UNSET
    monthly_dayofweek: RESTBackupRepositoryFromClientMonthlyDayofweek | Unset = UNSET
    proxy_id: None | Unset | UUID = UNSET
    attach_used_repository: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retention_type = self.retention_type.value

        object_storage_id: None | str | Unset
        if isinstance(self.object_storage_id, Unset):
            object_storage_id = UNSET
        elif isinstance(self.object_storage_id, UUID):
            object_storage_id = str(self.object_storage_id)
        else:
            object_storage_id = self.object_storage_id

        object_storage_cache_path = self.object_storage_cache_path

        object_storage_encryption_enabled: bool | None | Unset
        if isinstance(self.object_storage_encryption_enabled, Unset):
            object_storage_encryption_enabled = UNSET
        else:
            object_storage_encryption_enabled = self.object_storage_encryption_enabled

        encryption_key_id: None | str | Unset
        if isinstance(self.encryption_key_id, Unset):
            encryption_key_id = UNSET
        elif isinstance(self.encryption_key_id, UUID):
            encryption_key_id = str(self.encryption_key_id)
        else:
            encryption_key_id = self.encryption_key_id

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        name = self.name

        description = self.description

        path = self.path

        retention_period_type: str | Unset = UNSET
        if not isinstance(self.retention_period_type, Unset):
            retention_period_type = self.retention_period_type.value

        daily_retention_period: int | None | Unset
        if isinstance(self.daily_retention_period, Unset):
            daily_retention_period = UNSET
        else:
            daily_retention_period = self.daily_retention_period

        monthly_retention_period: int | None | Unset
        if isinstance(self.monthly_retention_period, Unset):
            monthly_retention_period = UNSET
        else:
            monthly_retention_period = self.monthly_retention_period

        yearly_retention_period: str | Unset = UNSET
        if not isinstance(self.yearly_retention_period, Unset):
            yearly_retention_period = self.yearly_retention_period.value

        retention_frequency_type: str | Unset = UNSET
        if not isinstance(self.retention_frequency_type, Unset):
            retention_frequency_type = self.retention_frequency_type.value

        daily_time = self.daily_time

        daily_type: str | Unset = UNSET
        if not isinstance(self.daily_type, Unset):
            daily_type = self.daily_type.value

        monthly_time = self.monthly_time

        monthly_daynumber: str | Unset = UNSET
        if not isinstance(self.monthly_daynumber, Unset):
            monthly_daynumber = self.monthly_daynumber.value

        monthly_dayofweek: str | Unset = UNSET
        if not isinstance(self.monthly_dayofweek, Unset):
            monthly_dayofweek = self.monthly_dayofweek.value

        proxy_id: None | str | Unset
        if isinstance(self.proxy_id, Unset):
            proxy_id = UNSET
        elif isinstance(self.proxy_id, UUID):
            proxy_id = str(self.proxy_id)
        else:
            proxy_id = self.proxy_id

        attach_used_repository: bool | None | Unset
        if isinstance(self.attach_used_repository, Unset):
            attach_used_repository = UNSET
        else:
            attach_used_repository = self.attach_used_repository

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retentionType": retention_type,
            }
        )
        if object_storage_id is not UNSET:
            field_dict["objectStorageId"] = object_storage_id
        if object_storage_cache_path is not UNSET:
            field_dict["objectStorageCachePath"] = object_storage_cache_path
        if object_storage_encryption_enabled is not UNSET:
            field_dict["objectStorageEncryptionEnabled"] = object_storage_encryption_enabled
        if encryption_key_id is not UNSET:
            field_dict["encryptionKeyId"] = encryption_key_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if path is not UNSET:
            field_dict["path"] = path
        if retention_period_type is not UNSET:
            field_dict["retentionPeriodType"] = retention_period_type
        if daily_retention_period is not UNSET:
            field_dict["dailyRetentionPeriod"] = daily_retention_period
        if monthly_retention_period is not UNSET:
            field_dict["monthlyRetentionPeriod"] = monthly_retention_period
        if yearly_retention_period is not UNSET:
            field_dict["yearlyRetentionPeriod"] = yearly_retention_period
        if retention_frequency_type is not UNSET:
            field_dict["retentionFrequencyType"] = retention_frequency_type
        if daily_time is not UNSET:
            field_dict["dailyTime"] = daily_time
        if daily_type is not UNSET:
            field_dict["dailyType"] = daily_type
        if monthly_time is not UNSET:
            field_dict["monthlyTime"] = monthly_time
        if monthly_daynumber is not UNSET:
            field_dict["monthlyDaynumber"] = monthly_daynumber
        if monthly_dayofweek is not UNSET:
            field_dict["monthlyDayofweek"] = monthly_dayofweek
        if proxy_id is not UNSET:
            field_dict["proxyId"] = proxy_id
        if attach_used_repository is not UNSET:
            field_dict["attachUsedRepository"] = attach_used_repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retention_type = RESTBackupRepositoryFromClientRetentionType(d.pop("retentionType"))

        def _parse_object_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_storage_id_type_0 = UUID(data)

                return object_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        object_storage_id = _parse_object_storage_id(d.pop("objectStorageId", UNSET))

        object_storage_cache_path = d.pop("objectStorageCachePath", UNSET)

        def _parse_object_storage_encryption_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        object_storage_encryption_enabled = _parse_object_storage_encryption_enabled(
            d.pop("objectStorageEncryptionEnabled", UNSET)
        )

        def _parse_encryption_key_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                encryption_key_id_type_0 = UUID(data)

                return encryption_key_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        encryption_key_id = _parse_encryption_key_id(d.pop("encryptionKeyId", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        path = d.pop("path", UNSET)

        _retention_period_type = d.pop("retentionPeriodType", UNSET)
        retention_period_type: RESTBackupRepositoryFromClientRetentionPeriodType | Unset
        if isinstance(_retention_period_type, Unset):
            retention_period_type = UNSET
        else:
            retention_period_type = RESTBackupRepositoryFromClientRetentionPeriodType(_retention_period_type)

        def _parse_daily_retention_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        daily_retention_period = _parse_daily_retention_period(d.pop("dailyRetentionPeriod", UNSET))

        def _parse_monthly_retention_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        monthly_retention_period = _parse_monthly_retention_period(d.pop("monthlyRetentionPeriod", UNSET))

        _yearly_retention_period = d.pop("yearlyRetentionPeriod", UNSET)
        yearly_retention_period: RESTBackupRepositoryFromClientYearlyRetentionPeriod | Unset
        if isinstance(_yearly_retention_period, Unset):
            yearly_retention_period = UNSET
        else:
            yearly_retention_period = RESTBackupRepositoryFromClientYearlyRetentionPeriod(_yearly_retention_period)

        _retention_frequency_type = d.pop("retentionFrequencyType", UNSET)
        retention_frequency_type: RESTBackupRepositoryFromClientRetentionFrequencyType | Unset
        if isinstance(_retention_frequency_type, Unset):
            retention_frequency_type = UNSET
        else:
            retention_frequency_type = RESTBackupRepositoryFromClientRetentionFrequencyType(_retention_frequency_type)

        daily_time = d.pop("dailyTime", UNSET)

        _daily_type = d.pop("dailyType", UNSET)
        daily_type: RESTBackupRepositoryFromClientDailyType | Unset
        if isinstance(_daily_type, Unset):
            daily_type = UNSET
        else:
            daily_type = RESTBackupRepositoryFromClientDailyType(_daily_type)

        monthly_time = d.pop("monthlyTime", UNSET)

        _monthly_daynumber = d.pop("monthlyDaynumber", UNSET)
        monthly_daynumber: RESTBackupRepositoryFromClientMonthlyDaynumber | Unset
        if isinstance(_monthly_daynumber, Unset):
            monthly_daynumber = UNSET
        else:
            monthly_daynumber = RESTBackupRepositoryFromClientMonthlyDaynumber(_monthly_daynumber)

        _monthly_dayofweek = d.pop("monthlyDayofweek", UNSET)
        monthly_dayofweek: RESTBackupRepositoryFromClientMonthlyDayofweek | Unset
        if isinstance(_monthly_dayofweek, Unset):
            monthly_dayofweek = UNSET
        else:
            monthly_dayofweek = RESTBackupRepositoryFromClientMonthlyDayofweek(_monthly_dayofweek)

        def _parse_proxy_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_id_type_0 = UUID(data)

                return proxy_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        proxy_id = _parse_proxy_id(d.pop("proxyId", UNSET))

        def _parse_attach_used_repository(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        attach_used_repository = _parse_attach_used_repository(d.pop("attachUsedRepository", UNSET))

        rest_backup_repository_from_client = cls(
            retention_type=retention_type,
            object_storage_id=object_storage_id,
            object_storage_cache_path=object_storage_cache_path,
            object_storage_encryption_enabled=object_storage_encryption_enabled,
            encryption_key_id=encryption_key_id,
            id=id,
            name=name,
            description=description,
            path=path,
            retention_period_type=retention_period_type,
            daily_retention_period=daily_retention_period,
            monthly_retention_period=monthly_retention_period,
            yearly_retention_period=yearly_retention_period,
            retention_frequency_type=retention_frequency_type,
            daily_time=daily_time,
            daily_type=daily_type,
            monthly_time=monthly_time,
            monthly_daynumber=monthly_daynumber,
            monthly_dayofweek=monthly_dayofweek,
            proxy_id=proxy_id,
            attach_used_repository=attach_used_repository,
        )

        rest_backup_repository_from_client.additional_properties = d
        return rest_backup_repository_from_client

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
