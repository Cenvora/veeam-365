from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTAutomaticUpdateSettings")


@_attrs_define
class RESTAutomaticUpdateSettings:
    """
    Attributes:
        send_email_on_available_updates (bool | None | Unset): Defines whether to notify about available updates with an
            email message.
        install_updates_automatically (bool | None | Unset): Defines whether to notify about available updates with an
            email message, download updates in the background and install them to the backup infrastructure components.
    """

    send_email_on_available_updates: bool | None | Unset = UNSET
    install_updates_automatically: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        send_email_on_available_updates: bool | None | Unset
        if isinstance(self.send_email_on_available_updates, Unset):
            send_email_on_available_updates = UNSET
        else:
            send_email_on_available_updates = self.send_email_on_available_updates

        install_updates_automatically: bool | None | Unset
        if isinstance(self.install_updates_automatically, Unset):
            install_updates_automatically = UNSET
        else:
            install_updates_automatically = self.install_updates_automatically

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if send_email_on_available_updates is not UNSET:
            field_dict["sendEmailOnAvailableUpdates"] = send_email_on_available_updates
        if install_updates_automatically is not UNSET:
            field_dict["installUpdatesAutomatically"] = install_updates_automatically

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_send_email_on_available_updates(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        send_email_on_available_updates = _parse_send_email_on_available_updates(
            d.pop("sendEmailOnAvailableUpdates", UNSET)
        )

        def _parse_install_updates_automatically(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        install_updates_automatically = _parse_install_updates_automatically(
            d.pop("installUpdatesAutomatically", UNSET)
        )

        rest_automatic_update_settings = cls(
            send_email_on_available_updates=send_email_on_available_updates,
            install_updates_automatically=install_updates_automatically,
        )

        rest_automatic_update_settings.additional_properties = d
        return rest_automatic_update_settings

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
