from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_edit_backup_job_backup_type import RESTEditBackupJobBackupType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_job_item_composed import RESTJobItemComposed
    from ..models.rest_job_schedule_policy import RESTJobSchedulePolicy


T = TypeVar("T", bound="RESTEditBackupJob")


@_attrs_define
class RESTEditBackupJob:
    """
    Attributes:
        description (None | str | Unset): Description of the backup job.
        backup_type (RESTEditBackupJobBackupType | Unset): Type of the backup job.
        run_now (bool | None | Unset): Defines whether the job will run right after it is created.
        selected_items (list[RESTJobItemComposed] | None | Unset): Array of objects that you want to back up.
        excluded_items (list[RESTJobItemComposed] | None | Unset): Array of objects that you want to exclude from a
            backup job scope.
        schedule_policy (RESTJobSchedulePolicy | Unset):
        repository_id (None | Unset | UUID): Backup repository ID. Example: 00000000-0000-0000-0000-000000000000.
        name (None | str | Unset): Name of the backup job.
        is_enabled (bool | None | Unset): Defines whether the backup job is enabled.
    """

    description: None | str | Unset = UNSET
    backup_type: RESTEditBackupJobBackupType | Unset = UNSET
    run_now: bool | None | Unset = UNSET
    selected_items: list[RESTJobItemComposed] | None | Unset = UNSET
    excluded_items: list[RESTJobItemComposed] | None | Unset = UNSET
    schedule_policy: RESTJobSchedulePolicy | Unset = UNSET
    repository_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        backup_type: str | Unset = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value

        run_now: bool | None | Unset
        if isinstance(self.run_now, Unset):
            run_now = UNSET
        else:
            run_now = self.run_now

        selected_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.selected_items, Unset):
            selected_items = UNSET
        elif isinstance(self.selected_items, list):
            selected_items = []
            for selected_items_type_0_item_data in self.selected_items:
                selected_items_type_0_item = selected_items_type_0_item_data.to_dict()
                selected_items.append(selected_items_type_0_item)

        else:
            selected_items = self.selected_items

        excluded_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.excluded_items, Unset):
            excluded_items = UNSET
        elif isinstance(self.excluded_items, list):
            excluded_items = []
            for excluded_items_type_0_item_data in self.excluded_items:
                excluded_items_type_0_item = excluded_items_type_0_item_data.to_dict()
                excluded_items.append(excluded_items_type_0_item)

        else:
            excluded_items = self.excluded_items

        schedule_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule_policy, Unset):
            schedule_policy = self.schedule_policy.to_dict()

        repository_id: None | str | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        elif isinstance(self.repository_id, UUID):
            repository_id = str(self.repository_id)
        else:
            repository_id = self.repository_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
        if run_now is not UNSET:
            field_dict["runNow"] = run_now
        if selected_items is not UNSET:
            field_dict["selectedItems"] = selected_items
        if excluded_items is not UNSET:
            field_dict["excludedItems"] = excluded_items
        if schedule_policy is not UNSET:
            field_dict["schedulePolicy"] = schedule_policy
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _backup_type = d.pop("backupType", UNSET)
        backup_type: RESTEditBackupJobBackupType | Unset
        if isinstance(_backup_type, Unset):
            backup_type = UNSET
        else:
            backup_type = RESTEditBackupJobBackupType(_backup_type)

        def _parse_run_now(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        run_now = _parse_run_now(d.pop("runNow", UNSET))

        def _parse_selected_items(data: object) -> list[RESTJobItemComposed] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_items_type_0 = []
                _selected_items_type_0 = data
                for selected_items_type_0_item_data in _selected_items_type_0:
                    selected_items_type_0_item = RESTJobItemComposed.from_dict(selected_items_type_0_item_data)

                    selected_items_type_0.append(selected_items_type_0_item)

                return selected_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RESTJobItemComposed] | None | Unset, data)

        selected_items = _parse_selected_items(d.pop("selectedItems", UNSET))

        def _parse_excluded_items(data: object) -> list[RESTJobItemComposed] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_items_type_0 = []
                _excluded_items_type_0 = data
                for excluded_items_type_0_item_data in _excluded_items_type_0:
                    excluded_items_type_0_item = RESTJobItemComposed.from_dict(excluded_items_type_0_item_data)

                    excluded_items_type_0.append(excluded_items_type_0_item)

                return excluded_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RESTJobItemComposed] | None | Unset, data)

        excluded_items = _parse_excluded_items(d.pop("excludedItems", UNSET))

        _schedule_policy = d.pop("schedulePolicy", UNSET)
        schedule_policy: RESTJobSchedulePolicy | Unset
        if isinstance(_schedule_policy, Unset):
            schedule_policy = UNSET
        else:
            schedule_policy = RESTJobSchedulePolicy.from_dict(_schedule_policy)

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        rest_edit_backup_job = cls(
            description=description,
            backup_type=backup_type,
            run_now=run_now,
            selected_items=selected_items,
            excluded_items=excluded_items,
            schedule_policy=schedule_policy,
            repository_id=repository_id,
            name=name,
            is_enabled=is_enabled,
        )

        rest_edit_backup_job.additional_properties = d
        return rest_edit_backup_job

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
