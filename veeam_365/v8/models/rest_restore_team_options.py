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
  from ..models.rest_teams_team import RESTTeamsTeam





T = TypeVar("T", bound="RESTRestoreTeamOptions")



@_attrs_define
class RESTRestoreTeamOptions:
    """ 
        Attributes:
            restore_changed_items (bool | None): Defines whether to restore team items that have been modified in the
                original location since the time when the backup was created.
            restore_missing_items (bool | None): Defines whether to restore team items that are missed in the original
                location.
            restore_members (bool | None): Defines whether to restore members of the restored team along with their roles.
            restore_settings (bool | None): Defines whether to restore settings of the restored team.
            teams (list[RESTTeamsTeam] | Unset): Specifies IDs of the teams that you want to restore. For more information
                on how to get such IDs, see [Get Teams](#/TeamsTeam/TeamsTeam_Get).
            impersonation_account_name (str | Unset): Specifies a user name of the account that will be used as a team owner
                account to restore a team. This may be useful if you restore a previously removed team at the time when the
                original team owner account does not exist in Microsoft 365.

                **Note**: This property is required if you want to use an application certificate for data restore. Use this
                property only with the `applicationCertificate` property. If you omit this property, Veeam Backup for Microsoft
                365 will restore a team using an original team owner account from the backup.
            user_code (str | Unset): Specifies the authentication code. For more information on how to get a device code,
                see [Get Device Code](#/RestoreSession/RestoreSession_DeviceCodeAction).
                This property is required if you want to use a device code for data restore.
            application_id (None | Unset | UUID): Specifies the ID of the Microsoft Entra application that you want to use
                for restore. Example: 00000000-0000-0000-0000-000000000000.
            application_certificate (str | Unset): Specifies the TLS certificate configured for the Microsoft Entra
                application that you want to use for data restore. You must provide the certificate as a Base64 string.
            application_certificate_password (str | Unset): Specifies a password.
            user_name (str | Unset): Specifies the user name that you want to use for authenticating to the organization.
            user_password (str | Unset): Specifies a password.
     """

    restore_changed_items: bool | None
    restore_missing_items: bool | None
    restore_members: bool | None
    restore_settings: bool | None
    teams: list[RESTTeamsTeam] | Unset = UNSET
    impersonation_account_name: str | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate: str | Unset = UNSET
    application_certificate_password: str | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
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

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)



        impersonation_account_name = self.impersonation_account_name

        user_code = self.user_code

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        elif isinstance(self.application_id, UUID):
            application_id = str(self.application_id)
        else:
            application_id = self.application_id

        application_certificate = self.application_certificate

        application_certificate_password = self.application_certificate_password

        user_name = self.user_name

        user_password = self.user_password


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "restoreChangedItems": restore_changed_items,
            "restoreMissingItems": restore_missing_items,
            "restoreMembers": restore_members,
            "restoreSettings": restore_settings,
        })
        if teams is not UNSET:
            field_dict["teams"] = teams
        if impersonation_account_name is not UNSET:
            field_dict["impersonationAccountName"] = impersonation_account_name
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_password is not UNSET:
            field_dict["userPassword"] = user_password

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


        _teams = d.pop("teams", UNSET)
        teams: list[RESTTeamsTeam] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = RESTTeamsTeam.from_dict(teams_item_data)



                teams.append(teams_item)


        impersonation_account_name = d.pop("impersonationAccountName", UNSET)

        user_code = d.pop("userCode", UNSET)

        def _parse_application_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_id_type_0 = UUID(data)



                return application_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        application_id = _parse_application_id(d.pop("applicationId", UNSET))


        application_certificate = d.pop("applicationCertificate", UNSET)

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        user_name = d.pop("userName", UNSET)

        user_password = d.pop("userPassword", UNSET)

        rest_restore_team_options = cls(
            restore_changed_items=restore_changed_items,
            restore_missing_items=restore_missing_items,
            restore_members=restore_members,
            restore_settings=restore_settings,
            teams=teams,
            impersonation_account_name=impersonation_account_name,
            user_code=user_code,
            application_id=application_id,
            application_certificate=application_certificate,
            application_certificate_password=application_certificate_password,
            user_name=user_name,
            user_password=user_password,
        )


        rest_restore_team_options.additional_properties = d
        return rest_restore_team_options

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
