from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTBackupRepositoryStorageUsageInfo")


@_attrs_define
class RESTBackupRepositoryStorageUsageInfo:
    """
    Attributes:
        name (str | Unset): Name of the backed-up organization
        id (str | Unset): Backed-up organization ID.
        used_space_bytes (int | None | Unset): Amount of space used by the organization in the repository in *Bytes*.
        local_cache_used_space_bytes (int | None | Unset): Amount of space occupied by cache for object storage
            repository.
        object_storage_used_space_bytes (int | None | Unset): Amount of space occupied in object storage repository in
            *Bytes*.
    """

    name: str | Unset = UNSET
    id: str | Unset = UNSET
    used_space_bytes: int | None | Unset = UNSET
    local_cache_used_space_bytes: int | None | Unset = UNSET
    object_storage_used_space_bytes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        used_space_bytes: int | None | Unset
        if isinstance(self.used_space_bytes, Unset):
            used_space_bytes = UNSET
        else:
            used_space_bytes = self.used_space_bytes

        local_cache_used_space_bytes: int | None | Unset
        if isinstance(self.local_cache_used_space_bytes, Unset):
            local_cache_used_space_bytes = UNSET
        else:
            local_cache_used_space_bytes = self.local_cache_used_space_bytes

        object_storage_used_space_bytes: int | None | Unset
        if isinstance(self.object_storage_used_space_bytes, Unset):
            object_storage_used_space_bytes = UNSET
        else:
            object_storage_used_space_bytes = self.object_storage_used_space_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if used_space_bytes is not UNSET:
            field_dict["usedSpaceBytes"] = used_space_bytes
        if local_cache_used_space_bytes is not UNSET:
            field_dict["localCacheUsedSpaceBytes"] = local_cache_used_space_bytes
        if object_storage_used_space_bytes is not UNSET:
            field_dict["objectStorageUsedSpaceBytes"] = object_storage_used_space_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        def _parse_used_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used_space_bytes = _parse_used_space_bytes(d.pop("usedSpaceBytes", UNSET))

        def _parse_local_cache_used_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        local_cache_used_space_bytes = _parse_local_cache_used_space_bytes(d.pop("localCacheUsedSpaceBytes", UNSET))

        def _parse_object_storage_used_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        object_storage_used_space_bytes = _parse_object_storage_used_space_bytes(
            d.pop("objectStorageUsedSpaceBytes", UNSET)
        )

        rest_backup_repository_storage_usage_info = cls(
            name=name,
            id=id,
            used_space_bytes=used_space_bytes,
            local_cache_used_space_bytes=local_cache_used_space_bytes,
            object_storage_used_space_bytes=object_storage_used_space_bytes,
        )

        rest_backup_repository_storage_usage_info.additional_properties = d
        return rest_backup_repository_storage_usage_info

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
