from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_backup_repository_maintenance_session_waiting_config import (
        RESTBackupRepositoryMaintenanceSessionWaitingConfig,
    )


T = TypeVar("T", bound="RESTBackupRepositoryMaintenanceSessionStartRequest")


@_attrs_define
class RESTBackupRepositoryMaintenanceSessionStartRequest:
    """
    Attributes:
        repository_ids (list[UUID]): Specifies an array of IDs of the backup repositories that you want to put under
            maintenance. For more information on how to get such IDs, see [Get Backup
            Repositories](BackupRepository#operation/BackupRepository_GetRepositories).
        waiting_config (None | RESTBackupRepositoryMaintenanceSessionWaitingConfig | Unset): Specifies the waiting
            period settings.
    """

    repository_ids: list[UUID]
    waiting_config: None | RESTBackupRepositoryMaintenanceSessionWaitingConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_backup_repository_maintenance_session_waiting_config import (
            RESTBackupRepositoryMaintenanceSessionWaitingConfig,
        )

        repository_ids = []
        for repository_ids_item_data in self.repository_ids:
            repository_ids_item = str(repository_ids_item_data)
            repository_ids.append(repository_ids_item)

        waiting_config: dict[str, Any] | None | Unset
        if isinstance(self.waiting_config, Unset):
            waiting_config = UNSET
        elif isinstance(self.waiting_config, RESTBackupRepositoryMaintenanceSessionWaitingConfig):
            waiting_config = self.waiting_config.to_dict()
        else:
            waiting_config = self.waiting_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repositoryIds": repository_ids,
            }
        )
        if waiting_config is not UNSET:
            field_dict["waitingConfig"] = waiting_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_backup_repository_maintenance_session_waiting_config import (
            RESTBackupRepositoryMaintenanceSessionWaitingConfig,
        )

        d = dict(src_dict)
        repository_ids = []
        _repository_ids = d.pop("repositoryIds")
        for repository_ids_item_data in _repository_ids:
            repository_ids_item = UUID(repository_ids_item_data)

            repository_ids.append(repository_ids_item)

        def _parse_waiting_config(data: object) -> None | RESTBackupRepositoryMaintenanceSessionWaitingConfig | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                waiting_config_type_1 = RESTBackupRepositoryMaintenanceSessionWaitingConfig.from_dict(data)

                return waiting_config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTBackupRepositoryMaintenanceSessionWaitingConfig | Unset, data)

        waiting_config = _parse_waiting_config(d.pop("waitingConfig", UNSET))

        rest_backup_repository_maintenance_session_start_request = cls(
            repository_ids=repository_ids,
            waiting_config=waiting_config,
        )

        rest_backup_repository_maintenance_session_start_request.additional_properties = d
        return rest_backup_repository_maintenance_session_start_request

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
