from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_backup_repository_owner_change_session_status import RESTBackupRepositoryOwnerChangeSessionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTBackupRepositoryOwnerChangeSession")


@_attrs_define
class RESTBackupRepositoryOwnerChangeSession:
    """
    Attributes:
        id (UUID): Change owner session ID. Example: 00000000-0000-0000-0000-000000000000.
        status (RESTBackupRepositoryOwnerChangeSessionStatus): Status of the change owner session.
        repository_ids (list[UUID]): Array of backup repositories involved in the change owner session. The server
            returns backup repository IDs.
        start_time (datetime.datetime | Unset): Date and time when the change owner session was started.
        end_time (datetime.datetime | None | Unset): Date and time when the change owner session ended.
        details (None | str | Unset): Change owner session details.
        wait_for_sessions_timeout (str | Unset): Timeout in *minutes*. This timeout is used to wait for the related
            sessions to finish before starting the current session. *Related sessions* are the sessions that Veeam Backup
            for Microsoft 365 creates to perform different activities: data backup and backup copy, data management, data
            restore, data retrieval, and data migration.
        force_stop_sessions (bool | Unset): Defines action that Veeam Backup for Microsoft 365 performs if the related
            sessions exceed the `waitForSessionsTimeout` value to finish. The following values are available: <ul>
            <li>*true* - the related sessions are stopped, the change owner session is created and started.</li> <li>*false*
            - the change owner session is canceled.</li> </ul>
        force_stop_sessions_timeout (str | Unset): Timeout in *minutes*. This timeout is used to wait for the related
            sessions to stop after Veeam Backup for Microsoft 365 forced them to stop.
        from_owner_id (UUID | Unset): ID of the backup proxy server or backup proxy poool from which backup repositories
            are moved. Example: 00000000-0000-0000-0000-000000000000.
        to_owner_id (UUID | Unset): ID of the backup proxy server or backup proxy poool to which backup repositories are
            moved. Example: 00000000-0000-0000-0000-000000000000.
    """

    id: UUID
    status: RESTBackupRepositoryOwnerChangeSessionStatus
    repository_ids: list[UUID]
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    details: None | str | Unset = UNSET
    wait_for_sessions_timeout: str | Unset = UNSET
    force_stop_sessions: bool | Unset = UNSET
    force_stop_sessions_timeout: str | Unset = UNSET
    from_owner_id: UUID | Unset = UNSET
    to_owner_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        repository_ids = []
        for repository_ids_item_data in self.repository_ids:
            repository_ids_item = str(repository_ids_item_data)
            repository_ids.append(repository_ids_item)

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        details: None | str | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        wait_for_sessions_timeout = self.wait_for_sessions_timeout

        force_stop_sessions = self.force_stop_sessions

        force_stop_sessions_timeout = self.force_stop_sessions_timeout

        from_owner_id: str | Unset = UNSET
        if not isinstance(self.from_owner_id, Unset):
            from_owner_id = str(self.from_owner_id)

        to_owner_id: str | Unset = UNSET
        if not isinstance(self.to_owner_id, Unset):
            to_owner_id = str(self.to_owner_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "repositoryIds": repository_ids,
            }
        )
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if details is not UNSET:
            field_dict["details"] = details
        if wait_for_sessions_timeout is not UNSET:
            field_dict["waitForSessionsTimeout"] = wait_for_sessions_timeout
        if force_stop_sessions is not UNSET:
            field_dict["forceStopSessions"] = force_stop_sessions
        if force_stop_sessions_timeout is not UNSET:
            field_dict["forceStopSessionsTimeout"] = force_stop_sessions_timeout
        if from_owner_id is not UNSET:
            field_dict["fromOwnerId"] = from_owner_id
        if to_owner_id is not UNSET:
            field_dict["toOwnerId"] = to_owner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = RESTBackupRepositoryOwnerChangeSessionStatus(d.pop("status"))

        repository_ids = []
        _repository_ids = d.pop("repositoryIds")
        for repository_ids_item_data in _repository_ids:
            repository_ids_item = UUID(repository_ids_item_data)

            repository_ids.append(repository_ids_item)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

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

        def _parse_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        wait_for_sessions_timeout = d.pop("waitForSessionsTimeout", UNSET)

        force_stop_sessions = d.pop("forceStopSessions", UNSET)

        force_stop_sessions_timeout = d.pop("forceStopSessionsTimeout", UNSET)

        _from_owner_id = d.pop("fromOwnerId", UNSET)
        from_owner_id: UUID | Unset
        if isinstance(_from_owner_id, Unset):
            from_owner_id = UNSET
        else:
            from_owner_id = UUID(_from_owner_id)

        _to_owner_id = d.pop("toOwnerId", UNSET)
        to_owner_id: UUID | Unset
        if isinstance(_to_owner_id, Unset):
            to_owner_id = UNSET
        else:
            to_owner_id = UUID(_to_owner_id)

        rest_backup_repository_owner_change_session = cls(
            id=id,
            status=status,
            repository_ids=repository_ids,
            start_time=start_time,
            end_time=end_time,
            details=details,
            wait_for_sessions_timeout=wait_for_sessions_timeout,
            force_stop_sessions=force_stop_sessions,
            force_stop_sessions_timeout=force_stop_sessions_timeout,
            from_owner_id=from_owner_id,
            to_owner_id=to_owner_id,
        )

        rest_backup_repository_owner_change_session.additional_properties = d
        return rest_backup_repository_owner_change_session

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
