from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_teams_team_fun_settings import RESTTeamsTeamFunSettings
  from ..models.rest_teams_team_guest_settings import RESTTeamsTeamGuestSettings
  from ..models.rest_teams_team_member_settings import RESTTeamsTeamMemberSettings
  from ..models.rest_teams_team_messaging_settings import RESTTeamsTeamMessagingSettings





T = TypeVar("T", bound="RESTTeamsTeamSettings")



@_attrs_define
class RESTTeamsTeamSettings:
    """ 
        Attributes:
            preferred_data_location (str | Unset): Preferred geographic location to create a new M365 group for a Multi-Geo
                tenant.
            allow_external_senders (bool | Unset): Defines whether people external to the organization can send messages to
                the group.
            auto_subscribe_new_members (bool | Unset): Defines whether new members added to the group will be auto-
                subscribed to receive email notifications.
            fun_settings (RESTTeamsTeamFunSettings | Unset):
            guest_settings (RESTTeamsTeamGuestSettings | Unset):
            member_settings (RESTTeamsTeamMemberSettings | Unset):
            messaging_settings (RESTTeamsTeamMessagingSettings | Unset):
     """

    preferred_data_location: str | Unset = UNSET
    allow_external_senders: bool | Unset = UNSET
    auto_subscribe_new_members: bool | Unset = UNSET
    fun_settings: RESTTeamsTeamFunSettings | Unset = UNSET
    guest_settings: RESTTeamsTeamGuestSettings | Unset = UNSET
    member_settings: RESTTeamsTeamMemberSettings | Unset = UNSET
    messaging_settings: RESTTeamsTeamMessagingSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_teams_team_fun_settings import RESTTeamsTeamFunSettings
        from ..models.rest_teams_team_guest_settings import RESTTeamsTeamGuestSettings
        from ..models.rest_teams_team_member_settings import RESTTeamsTeamMemberSettings
        from ..models.rest_teams_team_messaging_settings import RESTTeamsTeamMessagingSettings
        preferred_data_location = self.preferred_data_location

        allow_external_senders = self.allow_external_senders

        auto_subscribe_new_members = self.auto_subscribe_new_members

        fun_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fun_settings, Unset):
            fun_settings = self.fun_settings.to_dict()

        guest_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest_settings, Unset):
            guest_settings = self.guest_settings.to_dict()

        member_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.member_settings, Unset):
            member_settings = self.member_settings.to_dict()

        messaging_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.messaging_settings, Unset):
            messaging_settings = self.messaging_settings.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if preferred_data_location is not UNSET:
            field_dict["preferredDataLocation"] = preferred_data_location
        if allow_external_senders is not UNSET:
            field_dict["allowExternalSenders"] = allow_external_senders
        if auto_subscribe_new_members is not UNSET:
            field_dict["autoSubscribeNewMembers"] = auto_subscribe_new_members
        if fun_settings is not UNSET:
            field_dict["funSettings"] = fun_settings
        if guest_settings is not UNSET:
            field_dict["guestSettings"] = guest_settings
        if member_settings is not UNSET:
            field_dict["memberSettings"] = member_settings
        if messaging_settings is not UNSET:
            field_dict["messagingSettings"] = messaging_settings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_team_fun_settings import RESTTeamsTeamFunSettings
        from ..models.rest_teams_team_guest_settings import RESTTeamsTeamGuestSettings
        from ..models.rest_teams_team_member_settings import RESTTeamsTeamMemberSettings
        from ..models.rest_teams_team_messaging_settings import RESTTeamsTeamMessagingSettings
        d = dict(src_dict)
        preferred_data_location = d.pop("preferredDataLocation", UNSET)

        allow_external_senders = d.pop("allowExternalSenders", UNSET)

        auto_subscribe_new_members = d.pop("autoSubscribeNewMembers", UNSET)

        _fun_settings = d.pop("funSettings", UNSET)
        fun_settings: RESTTeamsTeamFunSettings | Unset
        if isinstance(_fun_settings,  Unset):
            fun_settings = UNSET
        else:
            fun_settings = RESTTeamsTeamFunSettings.from_dict(_fun_settings)




        _guest_settings = d.pop("guestSettings", UNSET)
        guest_settings: RESTTeamsTeamGuestSettings | Unset
        if isinstance(_guest_settings,  Unset):
            guest_settings = UNSET
        else:
            guest_settings = RESTTeamsTeamGuestSettings.from_dict(_guest_settings)




        _member_settings = d.pop("memberSettings", UNSET)
        member_settings: RESTTeamsTeamMemberSettings | Unset
        if isinstance(_member_settings,  Unset):
            member_settings = UNSET
        else:
            member_settings = RESTTeamsTeamMemberSettings.from_dict(_member_settings)




        _messaging_settings = d.pop("messagingSettings", UNSET)
        messaging_settings: RESTTeamsTeamMessagingSettings | Unset
        if isinstance(_messaging_settings,  Unset):
            messaging_settings = UNSET
        else:
            messaging_settings = RESTTeamsTeamMessagingSettings.from_dict(_messaging_settings)




        rest_teams_team_settings = cls(
            preferred_data_location=preferred_data_location,
            allow_external_senders=allow_external_senders,
            auto_subscribe_new_members=auto_subscribe_new_members,
            fun_settings=fun_settings,
            guest_settings=guest_settings,
            member_settings=member_settings,
            messaging_settings=messaging_settings,
        )


        rest_teams_team_settings.additional_properties = d
        return rest_teams_team_settings

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
