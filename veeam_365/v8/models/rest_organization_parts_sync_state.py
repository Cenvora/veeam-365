from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_organization_part_sync_state import RESTOrganizationPartSyncState


T = TypeVar("T", bound="RESTOrganizationPartsSyncState")


@_attrs_define
class RESTOrganizationPartsSyncState:
    """
    Attributes:
        users (None | RESTOrganizationPartSyncState | Unset): Details of the users synchronization.
        groups (None | RESTOrganizationPartSyncState | Unset): Details of the groups synchronization.
        group_members (None | RESTOrganizationPartSyncState | Unset): Details of the group members synchronization.
        sites (None | RESTOrganizationPartSyncState | Unset): Details of the sites synchronization.
    """

    users: None | RESTOrganizationPartSyncState | Unset = UNSET
    groups: None | RESTOrganizationPartSyncState | Unset = UNSET
    group_members: None | RESTOrganizationPartSyncState | Unset = UNSET
    sites: None | RESTOrganizationPartSyncState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_organization_part_sync_state import RESTOrganizationPartSyncState

        users: dict[str, Any] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, RESTOrganizationPartSyncState):
            users = self.users.to_dict()
        else:
            users = self.users

        groups: dict[str, Any] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, RESTOrganizationPartSyncState):
            groups = self.groups.to_dict()
        else:
            groups = self.groups

        group_members: dict[str, Any] | None | Unset
        if isinstance(self.group_members, Unset):
            group_members = UNSET
        elif isinstance(self.group_members, RESTOrganizationPartSyncState):
            group_members = self.group_members.to_dict()
        else:
            group_members = self.group_members

        sites: dict[str, Any] | None | Unset
        if isinstance(self.sites, Unset):
            sites = UNSET
        elif isinstance(self.sites, RESTOrganizationPartSyncState):
            sites = self.sites.to_dict()
        else:
            sites = self.sites

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users
        if groups is not UNSET:
            field_dict["groups"] = groups
        if group_members is not UNSET:
            field_dict["groupMembers"] = group_members
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_organization_part_sync_state import RESTOrganizationPartSyncState

        d = dict(src_dict)

        def _parse_users(data: object) -> None | RESTOrganizationPartSyncState | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                users_type_1 = RESTOrganizationPartSyncState.from_dict(data)

                return users_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTOrganizationPartSyncState | Unset, data)

        users = _parse_users(d.pop("users", UNSET))

        def _parse_groups(data: object) -> None | RESTOrganizationPartSyncState | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                groups_type_1 = RESTOrganizationPartSyncState.from_dict(data)

                return groups_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTOrganizationPartSyncState | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))

        def _parse_group_members(data: object) -> None | RESTOrganizationPartSyncState | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_members_type_1 = RESTOrganizationPartSyncState.from_dict(data)

                return group_members_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTOrganizationPartSyncState | Unset, data)

        group_members = _parse_group_members(d.pop("groupMembers", UNSET))

        def _parse_sites(data: object) -> None | RESTOrganizationPartSyncState | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sites_type_1 = RESTOrganizationPartSyncState.from_dict(data)

                return sites_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTOrganizationPartSyncState | Unset, data)

        sites = _parse_sites(d.pop("sites", UNSET))

        rest_organization_parts_sync_state = cls(
            users=users,
            groups=groups,
            group_members=group_members,
            sites=sites,
        )

        rest_organization_parts_sync_state.additional_properties = d
        return rest_organization_parts_sync_state

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
