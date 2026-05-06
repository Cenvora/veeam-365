from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_backup_repository_daily_type import RESTBackupRepositoryDailyType
from ..models.rest_backup_repository_monthly_daynumber import RESTBackupRepositoryMonthlyDaynumber
from ..models.rest_backup_repository_monthly_dayofweek import RESTBackupRepositoryMonthlyDayofweek
from ..models.rest_backup_repository_retention_frequency_type import RESTBackupRepositoryRetentionFrequencyType
from ..models.rest_backup_repository_retention_period_type import RESTBackupRepositoryRetentionPeriodType
from ..models.rest_backup_repository_retention_type import RESTBackupRepositoryRetentionType
from ..models.rest_backup_repository_yearly_retention_period import RESTBackupRepositoryYearlyRetentionPeriod
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
  from ..models.rest_object_storage_composed import RESTObjectStorageComposed





T = TypeVar("T", bound="RESTBackupRepository")



@_attrs_define
class RESTBackupRepository:
    """ 
        Attributes:
            object_storage_encryption_enabled (bool | None | Unset): Defines whether the object storage encryption is
                enabled.
            encryption_key_id (None | Unset | UUID): Encryption key ID. Example: 00000000-0000-0000-0000-000000000000.
            capacity_bytes (int | None | Unset): Size of the JET-based backup repository in *Bytes*.
            free_space_bytes (int | None | Unset): Available space on the JET-based backup repository in *Bytes*.
            id (None | Unset | UUID): Backup repository ID. Example: 00000000-0000-0000-0000-000000000000.
            name (str | Unset): Name of the backup repository.
            description (str | Unset): Description of the backup repository.
            path (str | Unset): Path to the directory where backups are stored.
            retention_type (RESTBackupRepositoryRetentionType | Unset): Type of the retention policy.
            retention_period_type (RESTBackupRepositoryRetentionPeriodType | Unset): Type of the retention period.
            daily_retention_period (int | None | Unset): Retention period in days. This property is valid if
                `retentionPeriodType` is set to *Daily*.
            monthly_retention_period (int | None | Unset): Retention period in months. This property is valid if
                `retentionPeriodType` is set to *Monthly*.
            yearly_retention_period (RESTBackupRepositoryYearlyRetentionPeriod | Unset): Retention period in years. This
                property is valid if `retentionPeriodType` is set to *Yearly*. If set to *Keep*, the backup job will back up all
                selected items and will never remove them.
            retention_frequency_type (RESTBackupRepositoryRetentionFrequencyType | Unset): Type of the clean-up schedule.
                The following types are available: <ul> <li>*Daily*. Veeam Backup for Microsoft 365 checks and removes the
                outdated backups once a day. Use the `dailyTime` property to set the time of the day for performing clean-up.
                Use the `dailyType` property to set the days for performing clean-up.</li> <li>*Monthly*. Veeam Backup for
                Microsoft 365 checks and removes the outdated backups once a month. Use the `monthlyTime` property to set the
                time of the day for performing clean-up. Use the `monthlyDaynumber` and `monthlyDayofweek` properties to set the
                day for performing clean-up.</li> </ul>
            daily_time (str | Unset): Time of the day when clean-up must be performed.
            daily_type (RESTBackupRepositoryDailyType | Unset): Days when clean-up must be performed.
            monthly_time (str | Unset): Time of the day when clean-up must be performed.
            monthly_daynumber (RESTBackupRepositoryMonthlyDaynumber | Unset): Order number for the day of the week when
                clean-up must be performed.
            monthly_dayofweek (RESTBackupRepositoryMonthlyDayofweek | Unset): Day of the week when clean-up must be
                performed.
            proxy_id (None | Unset | UUID): Backup proxy server ID. Example: 00000000-0000-0000-0000-000000000000.
            proxy_pool_id (None | Unset | UUID): Backup proxy pool ID. Example: 00000000-0000-0000-0000-000000000000.
            organization_id (None | Unset | UUID): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
            is_long_term (bool | None | Unset): Defines whether object storage repository is one of the following: Azure
                Blob Storage Archive access tier, Amazon S3 Glacier Instant Retrieval, Amazon S3 Glacier Flexible Retrieval or
                Amazon S3 Glacier Deep Archive storage classes.
            is_outdated (bool | Unset): Defines whether a backup repository has the *Out of Date* state and must be
                upgraded.
            is_out_of_sync (bool | Unset): Defines whether object storage repository has the *Out of Sync* state.
                Synchronization of cache between object storage repository and the *PersistentCache* is required.
            is_indexed (bool | Unset): Defines whether a backup repository was indexed.
            is_migration_locked (bool | Unset): Defines whether a backup repository is locked after a migration was
                performed.
            is_out_of_order (bool | Unset): Defines whether a backup repository has the *Invalid* state.
            out_of_order_reason (None | str | Unset): Reason why a backup repository has the *Invalid* state.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
            object_storage (RESTObjectStorageComposed | Unset):
     """

    object_storage_encryption_enabled: bool | None | Unset = UNSET
    encryption_key_id: None | Unset | UUID = UNSET
    capacity_bytes: int | None | Unset = UNSET
    free_space_bytes: int | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    path: str | Unset = UNSET
    retention_type: RESTBackupRepositoryRetentionType | Unset = UNSET
    retention_period_type: RESTBackupRepositoryRetentionPeriodType | Unset = UNSET
    daily_retention_period: int | None | Unset = UNSET
    monthly_retention_period: int | None | Unset = UNSET
    yearly_retention_period: RESTBackupRepositoryYearlyRetentionPeriod | Unset = UNSET
    retention_frequency_type: RESTBackupRepositoryRetentionFrequencyType | Unset = UNSET
    daily_time: str | Unset = UNSET
    daily_type: RESTBackupRepositoryDailyType | Unset = UNSET
    monthly_time: str | Unset = UNSET
    monthly_daynumber: RESTBackupRepositoryMonthlyDaynumber | Unset = UNSET
    monthly_dayofweek: RESTBackupRepositoryMonthlyDayofweek | Unset = UNSET
    proxy_id: None | Unset | UUID = UNSET
    proxy_pool_id: None | Unset | UUID = UNSET
    organization_id: None | Unset | UUID = UNSET
    is_long_term: bool | None | Unset = UNSET
    is_outdated: bool | Unset = UNSET
    is_out_of_sync: bool | Unset = UNSET
    is_indexed: bool | Unset = UNSET
    is_migration_locked: bool | Unset = UNSET
    is_out_of_order: bool | Unset = UNSET
    out_of_order_reason: None | str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    object_storage: RESTObjectStorageComposed | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_object_storage_composed import RESTObjectStorageComposed
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

        capacity_bytes: int | None | Unset
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        free_space_bytes: int | None | Unset
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

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

        retention_type: str | Unset = UNSET
        if not isinstance(self.retention_type, Unset):
            retention_type = self.retention_type.value


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

        proxy_pool_id: None | str | Unset
        if isinstance(self.proxy_pool_id, Unset):
            proxy_pool_id = UNSET
        elif isinstance(self.proxy_pool_id, UUID):
            proxy_pool_id = str(self.proxy_pool_id)
        else:
            proxy_pool_id = self.proxy_pool_id

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        is_long_term: bool | None | Unset
        if isinstance(self.is_long_term, Unset):
            is_long_term = UNSET
        else:
            is_long_term = self.is_long_term

        is_outdated = self.is_outdated

        is_out_of_sync = self.is_out_of_sync

        is_indexed = self.is_indexed

        is_migration_locked = self.is_migration_locked

        is_out_of_order = self.is_out_of_order

        out_of_order_reason: None | str | Unset
        if isinstance(self.out_of_order_reason, Unset):
            out_of_order_reason = UNSET
        else:
            out_of_order_reason = self.out_of_order_reason

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        object_storage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.object_storage, Unset):
            object_storage = self.object_storage.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if object_storage_encryption_enabled is not UNSET:
            field_dict["objectStorageEncryptionEnabled"] = object_storage_encryption_enabled
        if encryption_key_id is not UNSET:
            field_dict["encryptionKeyId"] = encryption_key_id
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if path is not UNSET:
            field_dict["path"] = path
        if retention_type is not UNSET:
            field_dict["retentionType"] = retention_type
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
        if proxy_pool_id is not UNSET:
            field_dict["proxyPoolId"] = proxy_pool_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if is_long_term is not UNSET:
            field_dict["isLongTerm"] = is_long_term
        if is_outdated is not UNSET:
            field_dict["isOutdated"] = is_outdated
        if is_out_of_sync is not UNSET:
            field_dict["isOutOfSync"] = is_out_of_sync
        if is_indexed is not UNSET:
            field_dict["isIndexed"] = is_indexed
        if is_migration_locked is not UNSET:
            field_dict["isMigrationLocked"] = is_migration_locked
        if is_out_of_order is not UNSET:
            field_dict["isOutOfOrder"] = is_out_of_order
        if out_of_order_reason is not UNSET:
            field_dict["outOfOrderReason"] = out_of_order_reason
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if object_storage is not UNSET:
            field_dict["objectStorage"] = object_storage

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_object_storage_composed import RESTObjectStorageComposed
        d = dict(src_dict)
        def _parse_object_storage_encryption_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        object_storage_encryption_enabled = _parse_object_storage_encryption_enabled(d.pop("objectStorageEncryptionEnabled", UNSET))


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


        def _parse_capacity_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))


        def _parse_free_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))


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

        _retention_type = d.pop("retentionType", UNSET)
        retention_type: RESTBackupRepositoryRetentionType | Unset
        if isinstance(_retention_type,  Unset):
            retention_type = UNSET
        else:
            retention_type = RESTBackupRepositoryRetentionType(_retention_type)




        _retention_period_type = d.pop("retentionPeriodType", UNSET)
        retention_period_type: RESTBackupRepositoryRetentionPeriodType | Unset
        if isinstance(_retention_period_type,  Unset):
            retention_period_type = UNSET
        else:
            retention_period_type = RESTBackupRepositoryRetentionPeriodType(_retention_period_type)




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
        yearly_retention_period: RESTBackupRepositoryYearlyRetentionPeriod | Unset
        if isinstance(_yearly_retention_period,  Unset):
            yearly_retention_period = UNSET
        else:
            yearly_retention_period = RESTBackupRepositoryYearlyRetentionPeriod(_yearly_retention_period)




        _retention_frequency_type = d.pop("retentionFrequencyType", UNSET)
        retention_frequency_type: RESTBackupRepositoryRetentionFrequencyType | Unset
        if isinstance(_retention_frequency_type,  Unset):
            retention_frequency_type = UNSET
        else:
            retention_frequency_type = RESTBackupRepositoryRetentionFrequencyType(_retention_frequency_type)




        daily_time = d.pop("dailyTime", UNSET)

        _daily_type = d.pop("dailyType", UNSET)
        daily_type: RESTBackupRepositoryDailyType | Unset
        if isinstance(_daily_type,  Unset):
            daily_type = UNSET
        else:
            daily_type = RESTBackupRepositoryDailyType(_daily_type)




        monthly_time = d.pop("monthlyTime", UNSET)

        _monthly_daynumber = d.pop("monthlyDaynumber", UNSET)
        monthly_daynumber: RESTBackupRepositoryMonthlyDaynumber | Unset
        if isinstance(_monthly_daynumber,  Unset):
            monthly_daynumber = UNSET
        else:
            monthly_daynumber = RESTBackupRepositoryMonthlyDaynumber(_monthly_daynumber)




        _monthly_dayofweek = d.pop("monthlyDayofweek", UNSET)
        monthly_dayofweek: RESTBackupRepositoryMonthlyDayofweek | Unset
        if isinstance(_monthly_dayofweek,  Unset):
            monthly_dayofweek = UNSET
        else:
            monthly_dayofweek = RESTBackupRepositoryMonthlyDayofweek(_monthly_dayofweek)




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


        def _parse_proxy_pool_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_pool_id_type_0 = UUID(data)



                return proxy_pool_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        proxy_pool_id = _parse_proxy_pool_id(d.pop("proxyPoolId", UNSET))


        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)



                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organizationId", UNSET))


        def _parse_is_long_term(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_long_term = _parse_is_long_term(d.pop("isLongTerm", UNSET))


        is_outdated = d.pop("isOutdated", UNSET)

        is_out_of_sync = d.pop("isOutOfSync", UNSET)

        is_indexed = d.pop("isIndexed", UNSET)

        is_migration_locked = d.pop("isMigrationLocked", UNSET)

        is_out_of_order = d.pop("isOutOfOrder", UNSET)

        def _parse_out_of_order_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        out_of_order_reason = _parse_out_of_order_reason(d.pop("outOfOrderReason", UNSET))


        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        _object_storage = d.pop("objectStorage", UNSET)
        object_storage: RESTObjectStorageComposed | Unset
        if isinstance(_object_storage,  Unset):
            object_storage = UNSET
        else:
            object_storage = RESTObjectStorageComposed.from_dict(_object_storage)




        rest_backup_repository = cls(
            object_storage_encryption_enabled=object_storage_encryption_enabled,
            encryption_key_id=encryption_key_id,
            capacity_bytes=capacity_bytes,
            free_space_bytes=free_space_bytes,
            id=id,
            name=name,
            description=description,
            path=path,
            retention_type=retention_type,
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
            proxy_pool_id=proxy_pool_id,
            organization_id=organization_id,
            is_long_term=is_long_term,
            is_outdated=is_outdated,
            is_out_of_sync=is_out_of_sync,
            is_indexed=is_indexed,
            is_migration_locked=is_migration_locked,
            is_out_of_order=is_out_of_order,
            out_of_order_reason=out_of_order_reason,
            field_links=field_links,
            object_storage=object_storage,
        )


        rest_backup_repository.additional_properties = d
        return rest_backup_repository

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
