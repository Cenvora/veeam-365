from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_platform_type_license_usage import RESTPlatformTypeLicenseUsage


T = TypeVar("T", bound="RESTLicenseUsage")


@_attrs_define
class RESTLicenseUsage:
    """
    Attributes:
        platform_types (list[RESTPlatformTypeLicenseUsage] | Unset): Information about license usage counter types for
            each licensing platform.
    """

    platform_types: list[RESTPlatformTypeLicenseUsage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.platform_types, Unset):
            platform_types = []
            for platform_types_item_data in self.platform_types:
                platform_types_item = platform_types_item_data.to_dict()
                platform_types.append(platform_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform_types is not UNSET:
            field_dict["platformTypes"] = platform_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_platform_type_license_usage import RESTPlatformTypeLicenseUsage

        d = dict(src_dict)
        _platform_types = d.pop("platformTypes", UNSET)
        platform_types: list[RESTPlatformTypeLicenseUsage] | Unset = UNSET
        if _platform_types is not UNSET:
            platform_types = []
            for platform_types_item_data in _platform_types:
                platform_types_item = RESTPlatformTypeLicenseUsage.from_dict(platform_types_item_data)

                platform_types.append(platform_types_item)

        rest_license_usage = cls(
            platform_types=platform_types,
        )

        rest_license_usage.additional_properties = d
        return rest_license_usage

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
