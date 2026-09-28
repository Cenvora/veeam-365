from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTBackupRepositoryMaintenanceSessionWaitingConfig")


@_attrs_define
class RESTBackupRepositoryMaintenanceSessionWaitingConfig:
    """
    Attributes:
        wait_for_sessions_timeout (int | Unset): Timeout in *minutes*. This timeout is used to wait for the related
            sessions on the affected repositories to finish before starting the current maintenance session. Default: 60.
        force_stop_sessions (bool | Unset): Defines action that Veeam Backup for Microsoft 365 performs if the related
            sessions exceed the `waitForSessionsTimeout` value to finish. The following values are available: <ul>
            <li>*true* - the related sessions will be stopped, the maintenance session will be created and started.</li>
            <li>*false* - the maintenance session will be canceled.</li> </ul>
             Default: False.
        force_stop_sessions_timeout (int | Unset): Timeout in *minutes*. This timeout is used to wait for the related
            sessions to stop after Veeam Backup for Microsoft 365 forced them to stop. Default: 10.
    """

    wait_for_sessions_timeout: int | Unset = 60
    force_stop_sessions: bool | Unset = False
    force_stop_sessions_timeout: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wait_for_sessions_timeout = self.wait_for_sessions_timeout

        force_stop_sessions = self.force_stop_sessions

        force_stop_sessions_timeout = self.force_stop_sessions_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wait_for_sessions_timeout is not UNSET:
            field_dict["waitForSessionsTimeout"] = wait_for_sessions_timeout
        if force_stop_sessions is not UNSET:
            field_dict["forceStopSessions"] = force_stop_sessions
        if force_stop_sessions_timeout is not UNSET:
            field_dict["forceStopSessionsTimeout"] = force_stop_sessions_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wait_for_sessions_timeout = d.pop("waitForSessionsTimeout", UNSET)

        force_stop_sessions = d.pop("forceStopSessions", UNSET)

        force_stop_sessions_timeout = d.pop("forceStopSessionsTimeout", UNSET)

        rest_backup_repository_maintenance_session_waiting_config = cls(
            wait_for_sessions_timeout=wait_for_sessions_timeout,
            force_stop_sessions=force_stop_sessions,
            force_stop_sessions_timeout=force_stop_sessions_timeout,
        )

        rest_backup_repository_maintenance_session_waiting_config.additional_properties = d
        return rest_backup_repository_maintenance_session_waiting_config

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
