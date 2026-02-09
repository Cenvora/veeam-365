from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_teams_team_privacy import RESTTeamsTeamPrivacy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_teams_team_links import RESTTeamsTeamLinks


T = TypeVar("T", bound="RESTTeamsTeam")


@_attrs_define
class RESTTeamsTeam:
    """
    Attributes:
        id (UUID):  Example: 00000000-0000-0000-0000-000000000000.
        display_name (str | Unset):
        description (str | Unset):
        group_email (str | Unset):
        alias (str | Unset):
        privacy (RESTTeamsTeamPrivacy | Unset):
        is_archived (bool | Unset):
        field_links (RESTTeamsTeamLinks | Unset):
    """

    id: UUID
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    group_email: str | Unset = UNSET
    alias: str | Unset = UNSET
    privacy: RESTTeamsTeamPrivacy | Unset = UNSET
    is_archived: bool | Unset = UNSET
    field_links: RESTTeamsTeamLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        display_name = self.display_name

        description = self.description

        group_email = self.group_email

        alias = self.alias

        privacy: str | Unset = UNSET
        if not isinstance(self.privacy, Unset):
            privacy = self.privacy.value

        is_archived = self.is_archived

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
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
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_team_links import RESTTeamsTeamLinks

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        group_email = d.pop("groupEmail", UNSET)

        alias = d.pop("alias", UNSET)

        _privacy = d.pop("privacy", UNSET)
        privacy: RESTTeamsTeamPrivacy | Unset
        if isinstance(_privacy, Unset):
            privacy = UNSET
        else:
            privacy = RESTTeamsTeamPrivacy(_privacy)

        is_archived = d.pop("isArchived", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTTeamsTeamLinks | Unset
        if isinstance(_field_links, Unset):
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
