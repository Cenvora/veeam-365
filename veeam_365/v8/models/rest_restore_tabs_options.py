from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_teams_tab import RestTeamsTab


T = TypeVar("T", bound="RESTRestoreTabsOptions")


@_attrs_define
class RESTRestoreTabsOptions:
    """
    Attributes:
        restore_changed_tabs (bool): Defines whether to restore tabs that have been modified in the original location
            since the time when the backup was created.
        restore_missing_tabs (bool): Defines whether to restore tabs that are missed in the original location.
        tabs (list[RestTeamsTab] | Unset): Specifies IDs of the channel tabs that you want to restore. For more
            information on how to get such IDs, see [Get Tabs](TeamsTab#operation/TeamsTab_Get).

            **Note**: If you omit this property, all backed-up tabs of the specified channel will be restored.
        user_code (str | Unset): Specifies the authentication code. For more information on how to get a device code,
            see [Get Device Code](RestoreSession#operation/RestoreSession_DeviceCodeAction).
            This property is required if you want to use a device code for data restore.
        application_id (None | Unset | UUID): Specifies the ID of the Microsoft Entra application that you want to use
            for restore. Example: 00000000-0000-0000-0000-000000000000.
        application_certificate (str | Unset): Specifies the SSL certificate configured for the Microsoft Entra
            application that you want to use for data restore. You must provide the certificate as a Base64 string.
        application_certificate_password (str | Unset): Specifies a password.
        user_name (str | Unset): Specifies the user name that you want to use for authenticating to the organization.
        user_password (str | Unset): Specifies a password.
    """

    restore_changed_tabs: bool
    restore_missing_tabs: bool
    tabs: list[RestTeamsTab] | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate: str | Unset = UNSET
    application_certificate_password: str | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_changed_tabs = self.restore_changed_tabs

        restore_missing_tabs = self.restore_missing_tabs

        tabs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tabs, Unset):
            tabs = []
            for tabs_item_data in self.tabs:
                tabs_item = tabs_item_data.to_dict()
                tabs.append(tabs_item)

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
        field_dict.update(
            {
                "restoreChangedTabs": restore_changed_tabs,
                "restoreMissingTabs": restore_missing_tabs,
            }
        )
        if tabs is not UNSET:
            field_dict["tabs"] = tabs
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
        from ..models.rest_teams_tab import RestTeamsTab

        d = dict(src_dict)
        restore_changed_tabs = d.pop("restoreChangedTabs")

        restore_missing_tabs = d.pop("restoreMissingTabs")

        _tabs = d.pop("tabs", UNSET)
        tabs: list[RestTeamsTab] | Unset = UNSET
        if _tabs is not UNSET:
            tabs = []
            for tabs_item_data in _tabs:
                tabs_item = RestTeamsTab.from_dict(tabs_item_data)

                tabs.append(tabs_item)

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

        rest_restore_tabs_options = cls(
            restore_changed_tabs=restore_changed_tabs,
            restore_missing_tabs=restore_missing_tabs,
            tabs=tabs,
            user_code=user_code,
            application_id=application_id,
            application_certificate=application_certificate,
            application_certificate_password=application_certificate_password,
            user_name=user_name,
            user_password=user_password,
        )

        rest_restore_tabs_options.additional_properties = d
        return rest_restore_tabs_options

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
