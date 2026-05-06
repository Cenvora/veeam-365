from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTTeamsTeamGuestSettings")



@_attrs_define
class RESTTeamsTeamGuestSettings:
    """ 
        Attributes:
            allow_create_update_channels (bool | Unset): Defines whether guests are allowed to add and update team channels.
            allow_delete_channels (bool | Unset): Defines whether guests are allowed to delete team channels.
     """

    allow_create_update_channels: bool | Unset = UNSET
    allow_delete_channels: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allow_create_update_channels = self.allow_create_update_channels

        allow_delete_channels = self.allow_delete_channels


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allow_create_update_channels is not UNSET:
            field_dict["allowCreateUpdateChannels"] = allow_create_update_channels
        if allow_delete_channels is not UNSET:
            field_dict["allowDeleteChannels"] = allow_delete_channels

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_create_update_channels = d.pop("allowCreateUpdateChannels", UNSET)

        allow_delete_channels = d.pop("allowDeleteChannels", UNSET)

        rest_teams_team_guest_settings = cls(
            allow_create_update_channels=allow_create_update_channels,
            allow_delete_channels=allow_delete_channels,
        )


        rest_teams_team_guest_settings.additional_properties = d
        return rest_teams_team_guest_settings

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
