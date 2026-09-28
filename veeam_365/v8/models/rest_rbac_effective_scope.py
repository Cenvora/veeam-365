from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_rbac_site_item import RESTRbacSiteItem
    from ..models.rest_rbac_team_item import RESTRbacTeamItem
    from ..models.rest_rbac_user_item import RESTRbacUserItem


T = TypeVar("T", bound="RESTRbacEffectiveScope")


@_attrs_define
class RESTRbacEffectiveScope:
    """
    Attributes:
        users (list[RESTRbacUserItem] | Unset): Users that are added to the list of objects to manage.
        sites (list[RESTRbacSiteItem] | Unset): Sites that are added to the list of objects to manage.
        teams (list[RESTRbacTeamItem] | Unset): Teams that are added to the list of objects to manage.
    """

    users: list[RESTRbacUserItem] | Unset = UNSET
    sites: list[RESTRbacSiteItem] | Unset = UNSET
    teams: list[RESTRbacTeamItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        sites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users
        if sites is not UNSET:
            field_dict["sites"] = sites
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_rbac_site_item import RESTRbacSiteItem
        from ..models.rest_rbac_team_item import RESTRbacTeamItem
        from ..models.rest_rbac_user_item import RESTRbacUserItem

        d = dict(src_dict)
        _users = d.pop("users", UNSET)
        users: list[RESTRbacUserItem] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = RESTRbacUserItem.from_dict(users_item_data)

                users.append(users_item)

        _sites = d.pop("sites", UNSET)
        sites: list[RESTRbacSiteItem] | Unset = UNSET
        if _sites is not UNSET:
            sites = []
            for sites_item_data in _sites:
                sites_item = RESTRbacSiteItem.from_dict(sites_item_data)

                sites.append(sites_item)

        _teams = d.pop("teams", UNSET)
        teams: list[RESTRbacTeamItem] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = RESTRbacTeamItem.from_dict(teams_item_data)

                teams.append(teams_item)

        rest_rbac_effective_scope = cls(
            users=users,
            sites=sites,
            teams=teams,
        )

        rest_rbac_effective_scope.additional_properties = d
        return rest_rbac_effective_scope

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
