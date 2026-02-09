from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_create_backup_job_backup_type import RESTCreateBackupJobBackupType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_job_item_composed import RESTJobItemComposed
    from ..models.rest_job_schedule_policy import RESTJobSchedulePolicy


T = TypeVar("T", bound="RESTCreateBackupJob")


@_attrs_define
class RESTCreateBackupJob:
    """
    Attributes:
        backup_type (RESTCreateBackupJobBackupType): Type of the backup job.
        organization_id (UUID): ID of the Microsoft 365 organization. Example: 00000000-0000-0000-0000-000000000000.
        repository_id (UUID): Backup repository ID. Example: 00000000-0000-0000-0000-000000000000.
        description (str | Unset): Description of the backup job.
        run_now (bool | None | Unset): Defines whether the job will run right after it is created.
        selected_items (list[RESTJobItemComposed] | Unset): Array of objects that you want to back up.
        excluded_items (list[RESTJobItemComposed] | Unset): Array of objects that you want to exclude from a backup job
            scope.
        schedule_policy (RESTJobSchedulePolicy | Unset):
        name (str | Unset): Name of the backup job.
        is_enabled (bool | None | Unset): Defines whether the backup job is enabled.
    """

    backup_type: RESTCreateBackupJobBackupType
    organization_id: UUID
    repository_id: UUID
    description: str | Unset = UNSET
    run_now: bool | None | Unset = UNSET
    selected_items: list[RESTJobItemComposed] | Unset = UNSET
    excluded_items: list[RESTJobItemComposed] | Unset = UNSET
    schedule_policy: RESTJobSchedulePolicy | Unset = UNSET
    name: str | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_type = self.backup_type.value

        organization_id = str(self.organization_id)

        repository_id = str(self.repository_id)

        description = self.description

        run_now: bool | None | Unset
        if isinstance(self.run_now, Unset):
            run_now = UNSET
        else:
            run_now = self.run_now

        selected_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.selected_items, Unset):
            selected_items = []
            for selected_items_item_data in self.selected_items:
                selected_items_item = selected_items_item_data.to_dict()
                selected_items.append(selected_items_item)

        excluded_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.excluded_items, Unset):
            excluded_items = []
            for excluded_items_item_data in self.excluded_items:
                excluded_items_item = excluded_items_item_data.to_dict()
                excluded_items.append(excluded_items_item)

        schedule_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule_policy, Unset):
            schedule_policy = self.schedule_policy.to_dict()

        name = self.name

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backupType": backup_type,
                "organizationId": organization_id,
                "repositoryId": repository_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if run_now is not UNSET:
            field_dict["runNow"] = run_now
        if selected_items is not UNSET:
            field_dict["selectedItems"] = selected_items
        if excluded_items is not UNSET:
            field_dict["excludedItems"] = excluded_items
        if schedule_policy is not UNSET:
            field_dict["schedulePolicy"] = schedule_policy
        if name is not UNSET:
            field_dict["name"] = name
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_job_item_composed import RESTJobItemComposed
        from ..models.rest_job_schedule_policy import RESTJobSchedulePolicy

        d = dict(src_dict)
        backup_type = RESTCreateBackupJobBackupType(d.pop("backupType"))

        organization_id = UUID(d.pop("organizationId"))

        repository_id = UUID(d.pop("repositoryId"))

        description = d.pop("description", UNSET)

        def _parse_run_now(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        run_now = _parse_run_now(d.pop("runNow", UNSET))

        _selected_items = d.pop("selectedItems", UNSET)
        selected_items: list[RESTJobItemComposed] | Unset = UNSET
        if _selected_items is not UNSET:
            selected_items = []
            for selected_items_item_data in _selected_items:
                selected_items_item = RESTJobItemComposed.from_dict(selected_items_item_data)

                selected_items.append(selected_items_item)

        _excluded_items = d.pop("excludedItems", UNSET)
        excluded_items: list[RESTJobItemComposed] | Unset = UNSET
        if _excluded_items is not UNSET:
            excluded_items = []
            for excluded_items_item_data in _excluded_items:
                excluded_items_item = RESTJobItemComposed.from_dict(excluded_items_item_data)

                excluded_items.append(excluded_items_item)

        _schedule_policy = d.pop("schedulePolicy", UNSET)
        schedule_policy: RESTJobSchedulePolicy | Unset
        if isinstance(_schedule_policy, Unset):
            schedule_policy = UNSET
        else:
            schedule_policy = RESTJobSchedulePolicy.from_dict(_schedule_policy)

        name = d.pop("name", UNSET)

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        rest_create_backup_job = cls(
            backup_type=backup_type,
            organization_id=organization_id,
            repository_id=repository_id,
            description=description,
            run_now=run_now,
            selected_items=selected_items,
            excluded_items=excluded_items,
            schedule_policy=schedule_policy,
            name=name,
            is_enabled=is_enabled,
        )

        rest_create_backup_job.additional_properties = d
        return rest_create_backup_job

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
