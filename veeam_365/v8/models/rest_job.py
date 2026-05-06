from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_job_backup_type import RESTJobBackupType
from ..models.rest_job_last_status import RESTJobLastStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.rest_job_links import RESTJobLinks
  from ..models.rest_job_schedule_policy import RESTJobSchedulePolicy





T = TypeVar("T", bound="RESTJob")



@_attrs_define
class RESTJob:
    """ 
        Attributes:
            description (str | Unset): Description of the backup job.
            backup_type (RESTJobBackupType | Unset): Type of the backup job.
            schedule_policy (RESTJobSchedulePolicy | Unset):
            id (None | Unset | UUID): Backup job ID. Example: 00000000-0000-0000-0000-000000000000.
            organization_id (None | Unset | UUID): ID of the Microsoft 365 organization. Example:
                00000000-0000-0000-0000-000000000000.
            repository_id (None | Unset | UUID): Backup repository ID. Example: 00000000-0000-0000-0000-000000000000.
            name (str | Unset): Name of the backup job.
            last_run (datetime.datetime | None | Unset): Date and time of the last run of the backup job.
            next_run (datetime.datetime | None | Unset): Date and time of the next run of the backup job per schedule.
            last_backup (datetime.datetime | None | Unset): Date and time of the last successful run of the backup job.
            is_enabled (bool | None | Unset): Defines whether the backup job is enabled.
            last_status (RESTJobLastStatus | Unset): Latest status of the backup job.
            e_tag (int | Unset): Version number that Veeam Backup for Microsoft 365 assigns if the backup job was modified.
            field_links (RESTJobLinks | Unset):
     """

    description: str | Unset = UNSET
    backup_type: RESTJobBackupType | Unset = UNSET
    schedule_policy: RESTJobSchedulePolicy | Unset = UNSET
    id: None | Unset | UUID = UNSET
    organization_id: None | Unset | UUID = UNSET
    repository_id: None | Unset | UUID = UNSET
    name: str | Unset = UNSET
    last_run: datetime.datetime | None | Unset = UNSET
    next_run: datetime.datetime | None | Unset = UNSET
    last_backup: datetime.datetime | None | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET
    last_status: RESTJobLastStatus | Unset = UNSET
    e_tag: int | Unset = UNSET
    field_links: RESTJobLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_job_links import RESTJobLinks
        from ..models.rest_job_schedule_policy import RESTJobSchedulePolicy
        description = self.description

        backup_type: str | Unset = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value


        schedule_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule_policy, Unset):
            schedule_policy = self.schedule_policy.to_dict()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        repository_id: None | str | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        elif isinstance(self.repository_id, UUID):
            repository_id = str(self.repository_id)
        else:
            repository_id = self.repository_id

        name = self.name

        last_run: None | str | Unset
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        next_run: None | str | Unset
        if isinstance(self.next_run, Unset):
            next_run = UNSET
        elif isinstance(self.next_run, datetime.datetime):
            next_run = self.next_run.isoformat()
        else:
            next_run = self.next_run

        last_backup: None | str | Unset
        if isinstance(self.last_backup, Unset):
            last_backup = UNSET
        elif isinstance(self.last_backup, datetime.datetime):
            last_backup = self.last_backup.isoformat()
        else:
            last_backup = self.last_backup

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        last_status: str | Unset = UNSET
        if not isinstance(self.last_status, Unset):
            last_status = self.last_status.value


        e_tag = self.e_tag

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
        if schedule_policy is not UNSET:
            field_dict["schedulePolicy"] = schedule_policy
        if id is not UNSET:
            field_dict["id"] = id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if name is not UNSET:
            field_dict["name"] = name
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if next_run is not UNSET:
            field_dict["nextRun"] = next_run
        if last_backup is not UNSET:
            field_dict["lastBackup"] = last_backup
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if last_status is not UNSET:
            field_dict["lastStatus"] = last_status
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_job_links import RESTJobLinks
        from ..models.rest_job_schedule_policy import RESTJobSchedulePolicy
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _backup_type = d.pop("backupType", UNSET)
        backup_type: RESTJobBackupType | Unset
        if isinstance(_backup_type,  Unset):
            backup_type = UNSET
        else:
            backup_type = RESTJobBackupType(_backup_type)




        _schedule_policy = d.pop("schedulePolicy", UNSET)
        schedule_policy: RESTJobSchedulePolicy | Unset
        if isinstance(_schedule_policy,  Unset):
            schedule_policy = UNSET
        else:
            schedule_policy = RESTJobSchedulePolicy.from_dict(_schedule_policy)




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


        def _parse_repository_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_id_type_0 = UUID(data)



                return repository_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        repository_id = _parse_repository_id(d.pop("repositoryId", UNSET))


        name = d.pop("name", UNSET)

        def _parse_last_run(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_type_0 = isoparse(data)



                return last_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run = _parse_last_run(d.pop("lastRun", UNSET))


        def _parse_next_run(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_run_type_0 = isoparse(data)



                return next_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_run = _parse_next_run(d.pop("nextRun", UNSET))


        def _parse_last_backup(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_type_0 = isoparse(data)



                return last_backup_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_backup = _parse_last_backup(d.pop("lastBackup", UNSET))


        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))


        _last_status = d.pop("lastStatus", UNSET)
        last_status: RESTJobLastStatus | Unset
        if isinstance(_last_status,  Unset):
            last_status = UNSET
        else:
            last_status = RESTJobLastStatus(_last_status)




        e_tag = d.pop("eTag", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTJobLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTJobLinks.from_dict(_field_links)




        rest_job = cls(
            description=description,
            backup_type=backup_type,
            schedule_policy=schedule_policy,
            id=id,
            organization_id=organization_id,
            repository_id=repository_id,
            name=name,
            last_run=last_run,
            next_run=next_run,
            last_backup=last_backup,
            is_enabled=is_enabled,
            last_status=last_status,
            e_tag=e_tag,
            field_links=field_links,
        )


        rest_job.additional_properties = d
        return rest_job

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
