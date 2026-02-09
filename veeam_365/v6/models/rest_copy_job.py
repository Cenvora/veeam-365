from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_copy_job_last_status import RESTCopyJobLastStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_copy_job_links import RESTCopyJobLinks
    from ..models.rest_copy_job_schedule_policy import RESTCopyJobSchedulePolicy


T = TypeVar("T", bound="RESTCopyJob")


@_attrs_define
class RESTCopyJob:
    """
    Attributes:
        backup_job_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        schedule_policy (RESTCopyJobSchedulePolicy | Unset):
        id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        repository_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        name (str | Unset):
        last_run (datetime.datetime | None | Unset):
        next_run (datetime.datetime | None | Unset):
        is_enabled (bool | None | Unset):
        last_status (RESTCopyJobLastStatus | Unset):
        field_links (RESTCopyJobLinks | Unset):
    """

    backup_job_id: None | Unset | UUID = UNSET
    schedule_policy: RESTCopyJobSchedulePolicy | Unset = UNSET
    id: None | Unset | UUID = UNSET
    repository_id: None | Unset | UUID = UNSET
    name: str | Unset = UNSET
    last_run: datetime.datetime | None | Unset = UNSET
    next_run: datetime.datetime | None | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET
    last_status: RESTCopyJobLastStatus | Unset = UNSET
    field_links: RESTCopyJobLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        last_status: str | Unset = UNSET
        if not isinstance(self.last_status, Unset):
            last_status = self.last_status.value

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_job_id is not UNSET:
            field_dict["backupJobId"] = backup_job_id
        if schedule_policy is not UNSET:
            field_dict["schedulePolicy"] = schedule_policy
        if id is not UNSET:
            field_dict["id"] = id
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if name is not UNSET:
            field_dict["name"] = name
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if next_run is not UNSET:
            field_dict["nextRun"] = next_run
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if last_status is not UNSET:
            field_dict["lastStatus"] = last_status
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_copy_job_links import RESTCopyJobLinks
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
        if isinstance(_schedule_policy, Unset):
            schedule_policy = UNSET
        else:
            schedule_policy = RESTCopyJobSchedulePolicy.from_dict(_schedule_policy)

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

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        _last_status = d.pop("lastStatus", UNSET)
        last_status: RESTCopyJobLastStatus | Unset
        if isinstance(_last_status, Unset):
            last_status = UNSET
        else:
            last_status = RESTCopyJobLastStatus(_last_status)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTCopyJobLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTCopyJobLinks.from_dict(_field_links)

        rest_copy_job = cls(
            backup_job_id=backup_job_id,
            schedule_policy=schedule_policy,
            id=id,
            repository_id=repository_id,
            name=name,
            last_run=last_run,
            next_run=next_run,
            is_enabled=is_enabled,
            last_status=last_status,
            field_links=field_links,
        )

        rest_copy_job.additional_properties = d
        return rest_copy_job

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
