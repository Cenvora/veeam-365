from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_copy_job_schedule_policy import RESTCopyJobSchedulePolicy


T = TypeVar("T", bound="RESTCreateCopyJob")


@_attrs_define
class RESTCreateCopyJob:
    """
    Attributes:
        backup_job_id (UUID): Backup job ID. Example: 00000000-0000-0000-0000-000000000000.
        organization_id (UUID): ID of the Microsoft 365 organization. Example: 00000000-0000-0000-0000-000000000000.
        repository_id (UUID): ID of one of the following object storage repositories: Azure Blob Storage Archive access
            tier, Amazon S3 Glacier Instant Retrieval, Amazon S3 Glacier Flexible Retrieval or Amazon S3 Glacier Deep
            Archive storage classes.
             Example: 00000000-0000-0000-0000-000000000000.
        schedule_policy (RESTCopyJobSchedulePolicy | Unset):
        is_enabled (bool | None | Unset): Defines whether the backup copy job is enabled.
    """

    backup_job_id: UUID
    organization_id: UUID
    repository_id: UUID
    schedule_policy: RESTCopyJobSchedulePolicy | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_job_id = str(self.backup_job_id)

        organization_id = str(self.organization_id)

        repository_id = str(self.repository_id)

        schedule_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule_policy, Unset):
            schedule_policy = self.schedule_policy.to_dict()

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backupJobId": backup_job_id,
                "organizationId": organization_id,
                "repositoryId": repository_id,
            }
        )
        if schedule_policy is not UNSET:
            field_dict["schedulePolicy"] = schedule_policy
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_copy_job_schedule_policy import RESTCopyJobSchedulePolicy

        d = dict(src_dict)
        backup_job_id = UUID(d.pop("backupJobId"))

        organization_id = UUID(d.pop("organizationId"))

        repository_id = UUID(d.pop("repositoryId"))

        _schedule_policy = d.pop("schedulePolicy", UNSET)
        schedule_policy: RESTCopyJobSchedulePolicy | Unset
        if isinstance(_schedule_policy, Unset):
            schedule_policy = UNSET
        else:
            schedule_policy = RESTCopyJobSchedulePolicy.from_dict(_schedule_policy)

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        rest_create_copy_job = cls(
            backup_job_id=backup_job_id,
            organization_id=organization_id,
            repository_id=repository_id,
            schedule_policy=schedule_policy,
            is_enabled=is_enabled,
        )

        rest_create_copy_job.additional_properties = d
        return rest_create_copy_job

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
