from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTTeamsTeamMessagingSettings")



@_attrs_define
class RESTTeamsTeamMessagingSettings:
    r""" 
        Attributes:
            allow_user_edit_message (bool | Unset): Defines whether users are allowed to edit their messages.
            allow_user_delete_message (bool | Unset): Defines whether users are allowed to delete their messages.
            allow_owner_delete_message (bool | Unset): Defines whether team owners are allowed to delete any message.
            allow_team_mention (bool | Unset): Defines whether *\@team* mentions are allowed.
            allow_channel_mention (bool | Unset): Defines whether *\@channel* mentions are allowed.
     """

    allow_user_edit_message: bool | Unset = UNSET
    allow_user_delete_message: bool | Unset = UNSET
    allow_owner_delete_message: bool | Unset = UNSET
    allow_team_mention: bool | Unset = UNSET
    allow_channel_mention: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allow_user_edit_message = self.allow_user_edit_message

        allow_user_delete_message = self.allow_user_delete_message

        allow_owner_delete_message = self.allow_owner_delete_message

        allow_team_mention = self.allow_team_mention

        allow_channel_mention = self.allow_channel_mention


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allow_user_edit_message is not UNSET:
            field_dict["allowUserEditMessage"] = allow_user_edit_message
        if allow_user_delete_message is not UNSET:
            field_dict["allowUserDeleteMessage"] = allow_user_delete_message
        if allow_owner_delete_message is not UNSET:
            field_dict["allowOwnerDeleteMessage"] = allow_owner_delete_message
        if allow_team_mention is not UNSET:
            field_dict["allowTeamMention"] = allow_team_mention
        if allow_channel_mention is not UNSET:
            field_dict["allowChannelMention"] = allow_channel_mention

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_user_edit_message = d.pop("allowUserEditMessage", UNSET)

        allow_user_delete_message = d.pop("allowUserDeleteMessage", UNSET)

        allow_owner_delete_message = d.pop("allowOwnerDeleteMessage", UNSET)

        allow_team_mention = d.pop("allowTeamMention", UNSET)

        allow_channel_mention = d.pop("allowChannelMention", UNSET)

        rest_teams_team_messaging_settings = cls(
            allow_user_edit_message=allow_user_edit_message,
            allow_user_delete_message=allow_user_delete_message,
            allow_owner_delete_message=allow_owner_delete_message,
            allow_team_mention=allow_team_mention,
            allow_channel_mention=allow_channel_mention,
        )


        rest_teams_team_messaging_settings.additional_properties = d
        return rest_teams_team_messaging_settings

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
