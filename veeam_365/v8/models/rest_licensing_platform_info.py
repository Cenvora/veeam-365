from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_licensing_group_info import RESTLicensingGroupInfo
    from ..models.rest_platform_info import RESTPlatformInfo


T = TypeVar("T", bound="RESTLicensingPlatformInfo")


@_attrs_define
class RESTLicensingPlatformInfo:
    """
    Attributes:
        groups (list[RESTLicensingGroupInfo] | None | Unset): Array of licensing groups.
        platforms (list[RESTPlatformInfo] | Unset): Array of licensing platforms.
    """

    groups: list[RESTLicensingGroupInfo] | None | Unset = UNSET
    platforms: list[RESTPlatformInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

        platforms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.to_dict()
                platforms.append(platforms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if platforms is not UNSET:
            field_dict["platforms"] = platforms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_licensing_group_info import RESTLicensingGroupInfo
        from ..models.rest_platform_info import RESTPlatformInfo

        d = dict(src_dict)

        def _parse_groups(data: object) -> list[RESTLicensingGroupInfo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = RESTLicensingGroupInfo.from_dict(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RESTLicensingGroupInfo] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))

        _platforms = d.pop("platforms", UNSET)
        platforms: list[RESTPlatformInfo] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = RESTPlatformInfo.from_dict(platforms_item_data)

                platforms.append(platforms_item)

        rest_licensing_platform_info = cls(
            groups=groups,
            platforms=platforms,
        )

        rest_licensing_platform_info.additional_properties = d
        return rest_licensing_platform_info

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
