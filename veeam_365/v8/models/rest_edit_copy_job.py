from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_copy_job_schedule_policy import RESTCopyJobSchedulePolicy





T = TypeVar("T", bound="RESTEditCopyJob")



@_attrs_define
class RESTEditCopyJob:
    """ 
        Attributes:
            backup_job_id (None | Unset | UUID): Backup job ID. Example: 00000000-0000-0000-0000-000000000000.
            schedule_policy (RESTCopyJobSchedulePolicy | Unset):
            organization_id (None | Unset | UUID): ID of the Microsoft 365 organization. Example:
                00000000-0000-0000-0000-000000000000.
            repository_id (None | Unset | UUID): ID of one of the following object storage repositories: Azure Blob Storage
                Archive access tier, Amazon S3 Glacier Instant Retrieval, Amazon S3 Glacier Flexible Retrieval or Amazon S3
                Glacier Deep Archive storage classes.
                 Example: 00000000-0000-0000-0000-000000000000.
            is_enabled (bool | None | Unset): Defines whether the backup copy job is enabled.
     """

    backup_job_id: None | Unset | UUID = UNSET
    schedule_policy: RESTCopyJobSchedulePolicy | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    repository_id: None | Unset | UUID = UNSET
    is_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_copy_job_schedule_policy import RESTCopyJobSchedulePolicy
        backup_job_id: None | str | Unset
        if isinstance(self.backup_job_id, Unset):
            backup_job_id = UNSET
        elif isinstance(self.backup_job_id, UUID):
            backup_job_id = str(self.backup_job_id)
        else:
            backup_job_id = self.backup_job_id

        schedule_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule_policy, Unset):
            schedule_policy = self.schedule_policy.to_dict()

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

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if backup_job_id is not UNSET:
            field_dict["backupJobId"] = backup_job_id
        if schedule_policy is not UNSET:
            field_dict["schedulePolicy"] = schedule_policy
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_copy_job_schedule_policy import RESTCopyJobSchedulePolicy
        d = dict(src_dict)
        def _parse_backup_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_job_id_type_0 = UUID(data)



                return backup_job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_job_id = _parse_backup_job_id(d.pop("backupJobId", UNSET))


        _schedule_policy = d.pop("schedulePolicy", UNSET)
        schedule_policy: RESTCopyJobSchedulePolicy | Unset
        if isinstance(_schedule_policy,  Unset):
            schedule_policy = UNSET
        else:
            schedule_policy = RESTCopyJobSchedulePolicy.from_dict(_schedule_policy)




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


        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))


        rest_edit_copy_job = cls(
            backup_job_id=backup_job_id,
            schedule_policy=schedule_policy,
            organization_id=organization_id,
            repository_id=repository_id,
            is_enabled=is_enabled,
        )


        rest_edit_copy_job.additional_properties = d
        return rest_edit_copy_job

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
