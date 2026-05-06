from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_teams_team_privacy import RESTTeamsTeamPrivacy
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_teams_team_links import RESTTeamsTeamLinks
  from ..models.rest_teams_team_settings import RESTTeamsTeamSettings





T = TypeVar("T", bound="RESTTeamsTeam")



@_attrs_define
class RESTTeamsTeam:
    """ 
        Attributes:
            id (UUID): ID of the backed-up team. Example: 00000000-0000-0000-0000-000000000000.
            display_name (str | Unset): Display name of the backed-up team.
            description (str | Unset): Description of the backed-up team.
            group_email (str | Unset): Email address of the backed-up team.
            alias (str | Unset): Alias of the backed-up team.
            privacy (RESTTeamsTeamPrivacy | Unset): Type of the backed-up team.
            settings (RESTTeamsTeamSettings | Unset):
            is_archived (bool | Unset): Defines whether the team is archived.
            field_links (RESTTeamsTeamLinks | Unset):
     """

    id: UUID
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    group_email: str | Unset = UNSET
    alias: str | Unset = UNSET
    privacy: RESTTeamsTeamPrivacy | Unset = UNSET
    settings: RESTTeamsTeamSettings | Unset = UNSET
    is_archived: bool | Unset = UNSET
    field_links: RESTTeamsTeamLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_teams_team_links import RESTTeamsTeamLinks
        from ..models.rest_teams_team_settings import RESTTeamsTeamSettings
        id = str(self.id)

        display_name = self.display_name

        description = self.description

        group_email = self.group_email

        alias = self.alias

        privacy: str | Unset = UNSET
        if not isinstance(self.privacy, Unset):
            privacy = self.privacy.value


        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        is_archived = self.is_archived

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
        })
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if group_email is not UNSET:
            field_dict["groupEmail"] = group_email
        if alias is not UNSET:
            field_dict["alias"] = alias
        if privacy is not UNSET:
            field_dict["privacy"] = privacy
        if settings is not UNSET:
            field_dict["settings"] = settings
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_team_links import RESTTeamsTeamLinks
        from ..models.rest_teams_team_settings import RESTTeamsTeamSettings
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        group_email = d.pop("groupEmail", UNSET)

        alias = d.pop("alias", UNSET)

        _privacy = d.pop("privacy", UNSET)
        privacy: RESTTeamsTeamPrivacy | Unset
        if isinstance(_privacy,  Unset):
            privacy = UNSET
        else:
            privacy = RESTTeamsTeamPrivacy(_privacy)




        _settings = d.pop("settings", UNSET)
        settings: RESTTeamsTeamSettings | Unset
        if isinstance(_settings,  Unset):
            settings = UNSET
        else:
            settings = RESTTeamsTeamSettings.from_dict(_settings)




        is_archived = d.pop("isArchived", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTTeamsTeamLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTTeamsTeamLinks.from_dict(_field_links)




        rest_teams_team = cls(
            id=id,
            display_name=display_name,
            description=description,
            group_email=group_email,
            alias=alias,
            privacy=privacy,
            settings=settings,
            is_archived=is_archived,
            field_links=field_links,
        )


        rest_teams_team.additional_properties = d
        return rest_teams_team

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
