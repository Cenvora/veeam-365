from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_license_auto_update_actions import RESTLicenseAutoUpdateActions
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTLicenseAutoUpdate")


@_attrs_define
class RESTLicenseAutoUpdate:
    """
    Attributes:
        is_enabled (bool | None | Unset): Defines whether automatic update is enabled for the license.
        field_links (RESTLinkHALDictionary | Unset):
        field_actions (RESTLicenseAutoUpdateActions | Unset):
    """

    is_enabled: bool | None | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTLicenseAutoUpdateActions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_license_auto_update_actions import RESTLicenseAutoUpdateActions
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTLicenseAutoUpdateActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTLicenseAutoUpdateActions.from_dict(_field_actions)

        rest_license_auto_update = cls(
            is_enabled=is_enabled,
            field_links=field_links,
            field_actions=field_actions,
        )

        rest_license_auto_update.additional_properties = d
        return rest_license_auto_update

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
