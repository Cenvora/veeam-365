from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTTeamsTeamMemberSettings")



@_attrs_define
class RESTTeamsTeamMemberSettings:
    """ 
        Attributes:
            allow_create_private_channel (bool | Unset): Defines whether team members are allowed to add and update private
                channels.
            allow_create_update_channel (bool | Unset): Defines whether team members are allowed to add and update channels.
            allow_delete_channel (bool | Unset): Defines whether team members are allowed to delete channels.
            allow_add_remove_app (bool | Unset): Defines whether team members are allowed to add and remove apps.
            allow_create_update_remove_tab (bool | Unset): Defines whether team members are allowed to add, update, and
                remove tabs.
            allow_create_update_remove_connector (bool | Unset): Defines whether team members are allowed to add, update,
                and remove connectors.
     """

    allow_create_private_channel: bool | Unset = UNSET
    allow_create_update_channel: bool | Unset = UNSET
    allow_delete_channel: bool | Unset = UNSET
    allow_add_remove_app: bool | Unset = UNSET
    allow_create_update_remove_tab: bool | Unset = UNSET
    allow_create_update_remove_connector: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allow_create_private_channel = self.allow_create_private_channel

        allow_create_update_channel = self.allow_create_update_channel

        allow_delete_channel = self.allow_delete_channel

        allow_add_remove_app = self.allow_add_remove_app

        allow_create_update_remove_tab = self.allow_create_update_remove_tab

        allow_create_update_remove_connector = self.allow_create_update_remove_connector


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allow_create_private_channel is not UNSET:
            field_dict["allowCreatePrivateChannel"] = allow_create_private_channel
        if allow_create_update_channel is not UNSET:
            field_dict["allowCreateUpdateChannel"] = allow_create_update_channel
        if allow_delete_channel is not UNSET:
            field_dict["allowDeleteChannel"] = allow_delete_channel
        if allow_add_remove_app is not UNSET:
            field_dict["allowAddRemoveApp"] = allow_add_remove_app
        if allow_create_update_remove_tab is not UNSET:
            field_dict["allowCreateUpdateRemoveTab"] = allow_create_update_remove_tab
        if allow_create_update_remove_connector is not UNSET:
            field_dict["allowCreateUpdateRemoveConnector"] = allow_create_update_remove_connector

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_create_private_channel = d.pop("allowCreatePrivateChannel", UNSET)

        allow_create_update_channel = d.pop("allowCreateUpdateChannel", UNSET)

        allow_delete_channel = d.pop("allowDeleteChannel", UNSET)

        allow_add_remove_app = d.pop("allowAddRemoveApp", UNSET)

        allow_create_update_remove_tab = d.pop("allowCreateUpdateRemoveTab", UNSET)

        allow_create_update_remove_connector = d.pop("allowCreateUpdateRemoveConnector", UNSET)

        rest_teams_team_member_settings = cls(
            allow_create_private_channel=allow_create_private_channel,
            allow_create_update_channel=allow_create_update_channel,
            allow_delete_channel=allow_delete_channel,
            allow_add_remove_app=allow_add_remove_app,
            allow_create_update_remove_tab=allow_create_update_remove_tab,
            allow_create_update_remove_connector=allow_create_update_remove_connector,
        )


        rest_teams_team_member_settings.additional_properties = d
        return rest_teams_team_member_settings

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
