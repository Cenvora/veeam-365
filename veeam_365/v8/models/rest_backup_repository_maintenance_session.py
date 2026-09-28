from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_backup_repository_maintenance_session_status import RESTBackupRepositoryMaintenanceSessionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_backup_repository_maintenance_session_waiting_config import (
        RESTBackupRepositoryMaintenanceSessionWaitingConfig,
    )


T = TypeVar("T", bound="RESTBackupRepositoryMaintenanceSession")


@_attrs_define
class RESTBackupRepositoryMaintenanceSession:
    """
    Attributes:
        id (UUID): Maintenance session ID. Example: 00000000-0000-0000-0000-000000000000.
        status (RESTBackupRepositoryMaintenanceSessionStatus): Status of the maintenance session.
        start_time (datetime.datetime): Date and time when the maintenance session was started.
        repository_ids (list[UUID]): Array of backup repositories involved in the maintenance session. The server
            returns backup repository IDs.
        waiting_config (RESTBackupRepositoryMaintenanceSessionWaitingConfig):
        end_time (datetime.datetime | None | Unset): Date and time when the maintenance session ended.
        error_message (None | str | Unset): Error message when the maintenance session failed.
    """

    id: UUID
    status: RESTBackupRepositoryMaintenanceSessionStatus
    start_time: datetime.datetime
    repository_ids: list[UUID]
    waiting_config: RESTBackupRepositoryMaintenanceSessionWaitingConfig
    end_time: datetime.datetime | None | Unset = UNSET
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        start_time = self.start_time.isoformat()

        repository_ids = []
        for repository_ids_item_data in self.repository_ids:
            repository_ids_item = str(repository_ids_item_data)
            repository_ids.append(repository_ids_item)

        waiting_config = self.waiting_config.to_dict()

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "startTime": start_time,
                "repositoryIds": repository_ids,
                "waitingConfig": waiting_config,
            }
        )
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_backup_repository_maintenance_session_waiting_config import (
            RESTBackupRepositoryMaintenanceSessionWaitingConfig,
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = RESTBackupRepositoryMaintenanceSessionStatus(d.pop("status"))

        start_time = isoparse(d.pop("startTime"))

        repository_ids = []
        _repository_ids = d.pop("repositoryIds")
        for repository_ids_item_data in _repository_ids:
            repository_ids_item = UUID(repository_ids_item_data)

            repository_ids.append(repository_ids_item)

        waiting_config = RESTBackupRepositoryMaintenanceSessionWaitingConfig.from_dict(d.pop("waitingConfig"))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        rest_backup_repository_maintenance_session = cls(
            id=id,
            status=status,
            start_time=start_time,
            repository_ids=repository_ids,
            waiting_config=waiting_config,
            end_time=end_time,
            error_message=error_message,
        )

        rest_backup_repository_maintenance_session.additional_properties = d
        return rest_backup_repository_maintenance_session

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
