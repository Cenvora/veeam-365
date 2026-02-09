from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_organization_storage_space_usage_links import RESTOrganizationStorageSpaceUsageLinks


T = TypeVar("T", bound="RESTOrganizationStorageSpaceUsage")


@_attrs_define
class RESTOrganizationStorageSpaceUsage:
    """
    Attributes:
        used_space_bytes (int | None | Unset):
        local_cache_used_space_bytes (int | None | Unset):
        object_storage_used_space_bytes (int | None | Unset):
        is_available (bool | Unset):
        details (str | Unset):
        field_links (RESTOrganizationStorageSpaceUsageLinks | Unset):
    """

    used_space_bytes: int | None | Unset = UNSET
    local_cache_used_space_bytes: int | None | Unset = UNSET
    object_storage_used_space_bytes: int | None | Unset = UNSET
    is_available: bool | Unset = UNSET
    details: str | Unset = UNSET
    field_links: RESTOrganizationStorageSpaceUsageLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        is_available = self.is_available

        details = self.details

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if used_space_bytes is not UNSET:
            field_dict["usedSpaceBytes"] = used_space_bytes
        if local_cache_used_space_bytes is not UNSET:
            field_dict["localCacheUsedSpaceBytes"] = local_cache_used_space_bytes
        if object_storage_used_space_bytes is not UNSET:
            field_dict["objectStorageUsedSpaceBytes"] = object_storage_used_space_bytes
        if is_available is not UNSET:
            field_dict["isAvailable"] = is_available
        if details is not UNSET:
            field_dict["details"] = details
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_organization_storage_space_usage_links import RESTOrganizationStorageSpaceUsageLinks

        d = dict(src_dict)

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

        is_available = d.pop("isAvailable", UNSET)

        details = d.pop("details", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTOrganizationStorageSpaceUsageLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTOrganizationStorageSpaceUsageLinks.from_dict(_field_links)

        rest_organization_storage_space_usage = cls(
            used_space_bytes=used_space_bytes,
            local_cache_used_space_bytes=local_cache_used_space_bytes,
            object_storage_used_space_bytes=object_storage_used_space_bytes,
            is_available=is_available,
            details=details,
            field_links=field_links,
        )

        rest_organization_storage_space_usage.additional_properties = d
        return rest_organization_storage_space_usage

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
