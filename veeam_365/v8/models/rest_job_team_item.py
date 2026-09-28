from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_job_backup_item_type import RESTJobBackupItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_job_team_item_links_type_0 import RESTJobTeamItemLinksType0
    from ..models.rest_team import RESTTeam


T = TypeVar("T", bound="RESTJobTeamItem")


@_attrs_define
class RESTJobTeamItem:
    """
    Attributes:
        type_ (RESTJobBackupItemType | Unset): Type of the backup item.
        team (RESTTeam | Unset):
        teams_chats (bool | None | Unset): Defines whether this backup job will include/exclude the *Chats* processing
            option.
        id (None | str | Unset): Backup item ID.
        field_links (None | RESTJobTeamItemLinksType0 | Unset):
    """

    type_: RESTJobBackupItemType | Unset = UNSET
    team: RESTTeam | Unset = UNSET
    teams_chats: bool | None | Unset = UNSET
    id: None | str | Unset = UNSET
    field_links: None | RESTJobTeamItemLinksType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_job_team_item_links_type_0 import RESTJobTeamItemLinksType0

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        team: dict[str, Any] | Unset = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        teams_chats: bool | None | Unset
        if isinstance(self.teams_chats, Unset):
            teams_chats = UNSET
        else:
            teams_chats = self.teams_chats

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, RESTJobTeamItemLinksType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if team is not UNSET:
            field_dict["team"] = team
        if teams_chats is not UNSET:
            field_dict["teamsChats"] = teams_chats
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_job_team_item_links_type_0 import RESTJobTeamItemLinksType0
        from ..models.rest_team import RESTTeam

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTJobBackupItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTJobBackupItemType(_type_)

        _team = d.pop("team", UNSET)
        team: RESTTeam | Unset
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = RESTTeam.from_dict(_team)

        def _parse_teams_chats(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        teams_chats = _parse_teams_chats(d.pop("teamsChats", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_field_links(data: object) -> None | RESTJobTeamItemLinksType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_links_type_0 = RESTJobTeamItemLinksType0.from_dict(data)

                return field_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTJobTeamItemLinksType0 | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        rest_job_team_item = cls(
            type_=type_,
            team=team,
            teams_chats=teams_chats,
            id=id,
            field_links=field_links,
        )

        rest_job_team_item.additional_properties = d
        return rest_job_team_item

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
