from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_teams_team import RESTTeamsTeam





T = TypeVar("T", bound="RESTOperatorRestoreTeamOptions")



@_attrs_define
class RESTOperatorRestoreTeamOptions:
    """ 
        Attributes:
            restore_changed_items (bool | None): Defines whether to restore team items that have been modified in the
                original location since the time when the backup was created.
            restore_missing_items (bool | None): Defines whether to restore team items that are missed in the original
                location.
            restore_members (bool | None): Defines whether to restore members of the restored team along with their roles.
            restore_settings (bool | None): Defines whether to restore settings of the restored team.
            impersonation_account_name (str): Specifies a user name of the account that will be used as a team owner account
                to restore a team. This may be useful if you restore a previously removed team at the time when the original
                team owner account does not exist in Microsoft 365.

                **Note**: This property is required if you want to use an application certificate for data restore. Use this
                property only with the `applicationCertificate` property. If you omit this property, Veeam Backup for Microsoft
                365 will restore a team using an original team owner account from the backup.
            teams (list[RESTTeamsTeam] | Unset): Specifies IDs of the teams that you want to restore. For more information
                on how to get such IDs, see [Get Teams](#/TeamsTeam/TeamsTeam_Get).
            reason (str | Unset): Specifies a reason for the restore operation.
     """

    restore_changed_items: bool | None
    restore_missing_items: bool | None
    restore_members: bool | None
    restore_settings: bool | None
    impersonation_account_name: str
    teams: list[RESTTeamsTeam] | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_teams_team import RESTTeamsTeam
        restore_changed_items: bool | None
        restore_changed_items = self.restore_changed_items

        restore_missing_items: bool | None
        restore_missing_items = self.restore_missing_items

        restore_members: bool | None
        restore_members = self.restore_members

        restore_settings: bool | None
        restore_settings = self.restore_settings

        impersonation_account_name = self.impersonation_account_name

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)



        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "restoreChangedItems": restore_changed_items,
            "restoreMissingItems": restore_missing_items,
            "restoreMembers": restore_members,
            "restoreSettings": restore_settings,
            "impersonationAccountName": impersonation_account_name,
        })
        if teams is not UNSET:
            field_dict["teams"] = teams
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_team import RESTTeamsTeam
        d = dict(src_dict)
        def _parse_restore_changed_items(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        restore_changed_items = _parse_restore_changed_items(d.pop("restoreChangedItems"))


        def _parse_restore_missing_items(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        restore_missing_items = _parse_restore_missing_items(d.pop("restoreMissingItems"))


        def _parse_restore_members(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        restore_members = _parse_restore_members(d.pop("restoreMembers"))


        def _parse_restore_settings(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        restore_settings = _parse_restore_settings(d.pop("restoreSettings"))


        impersonation_account_name = d.pop("impersonationAccountName")

        _teams = d.pop("teams", UNSET)
        teams: list[RESTTeamsTeam] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = RESTTeamsTeam.from_dict(teams_item_data)



                teams.append(teams_item)


        reason = d.pop("reason", UNSET)

        rest_operator_restore_team_options = cls(
            restore_changed_items=restore_changed_items,
            restore_missing_items=restore_missing_items,
            restore_members=restore_members,
            restore_settings=restore_settings,
            impersonation_account_name=impersonation_account_name,
            teams=teams,
            reason=reason,
        )


        rest_operator_restore_team_options.additional_properties = d
        return rest_operator_restore_team_options

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
