from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_teams_tab_links import RestTeamsTabLinks





T = TypeVar("T", bound="RestTeamsTab")



@_attrs_define
class RestTeamsTab:
    """ 
        Attributes:
            id (UUID): Tab ID. Example: 00000000-0000-0000-0000-000000000000.
            display_name (str | Unset): Display name of the tab.
            content_url (str | Unset): Path to the object published on the tab.
            type_ (str | Unset): Type of the tab.
            channel_id (str | Unset): Channel ID.
            team_id (UUID | Unset): Team ID.
            field_links (RestTeamsTabLinks | Unset):
     """

    id: UUID
    display_name: str | Unset = UNSET
    content_url: str | Unset = UNSET
    type_: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    team_id: UUID | Unset = UNSET
    field_links: RestTeamsTabLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_teams_tab_links import RestTeamsTabLinks
        id = str(self.id)

        display_name = self.display_name

        content_url = self.content_url

        type_ = self.type_

        channel_id = self.channel_id

        team_id: str | Unset = UNSET
        if not isinstance(self.team_id, Unset):
            team_id = str(self.team_id)

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
        if content_url is not UNSET:
            field_dict["contentUrl"] = content_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_tab_links import RestTeamsTabLinks
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        display_name = d.pop("displayName", UNSET)

        content_url = d.pop("contentUrl", UNSET)

        type_ = d.pop("type", UNSET)

        channel_id = d.pop("channelId", UNSET)

        _team_id = d.pop("teamId", UNSET)
        team_id: UUID | Unset
        if isinstance(_team_id,  Unset):
            team_id = UNSET
        else:
            team_id = UUID(_team_id)




        _field_links = d.pop("_links", UNSET)
        field_links: RestTeamsTabLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RestTeamsTabLinks.from_dict(_field_links)




        rest_teams_tab = cls(
            id=id,
            display_name=display_name,
            content_url=content_url,
            type_=type_,
            channel_id=channel_id,
            team_id=team_id,
            field_links=field_links,
        )


        rest_teams_tab.additional_properties = d
        return rest_teams_tab

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
