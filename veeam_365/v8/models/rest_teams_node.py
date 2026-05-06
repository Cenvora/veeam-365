from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_teams_node_type import RESTTeamsNodeType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_teams_node_links import RESTTeamsNodeLinks





T = TypeVar("T", bound="RESTTeamsNode")



@_attrs_define
class RESTTeamsNode:
    """ 
        Attributes:
            team_id (UUID | Unset): Team ID.
            channel_id (str | Unset): Channel ID.
            display_name (str | Unset): Display name of the teams item.
            type_ (RESTTeamsNodeType | Unset): Type of the Microsoft Teams item.
            field_links (RESTTeamsNodeLinks | Unset):
     """

    team_id: UUID | Unset = UNSET
    channel_id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    type_: RESTTeamsNodeType | Unset = UNSET
    field_links: RESTTeamsNodeLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_teams_node_links import RESTTeamsNodeLinks
        team_id: str | Unset = UNSET
        if not isinstance(self.team_id, Unset):
            team_id = str(self.team_id)

        channel_id = self.channel_id

        display_name = self.display_name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_node_links import RESTTeamsNodeLinks
        d = dict(src_dict)
        _team_id = d.pop("teamId", UNSET)
        team_id: UUID | Unset
        if isinstance(_team_id,  Unset):
            team_id = UNSET
        else:
            team_id = UUID(_team_id)




        channel_id = d.pop("channelId", UNSET)

        display_name = d.pop("displayName", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTTeamsNodeType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RESTTeamsNodeType(_type_)




        _field_links = d.pop("_links", UNSET)
        field_links: RESTTeamsNodeLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTTeamsNodeLinks.from_dict(_field_links)




        rest_teams_node = cls(
            team_id=team_id,
            channel_id=channel_id,
            display_name=display_name,
            type_=type_,
            field_links=field_links,
        )


        rest_teams_node.additional_properties = d
        return rest_teams_node

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
