from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_ssh_settings_from_client import RESTSshSettingsFromClient


T = TypeVar("T", bound="RESTRemoveProxyOptions")


@_attrs_define
class RESTRemoveProxyOptions:
    """
    Attributes:
        force (bool | Unset): Defines whether Veeam Backup for Microsoft 365 must remove the backup proxy server in the
            following cases: <ul> <li>Veeam Backup for Microsoft 365 cannot connect to the backup proxy server.</li> <li>The
            backup proxy server is in use by Veeam Backup for Microsoft 365.</li> <li>The backup proxy server you want to
            remove is the default backup proxy server in Veeam Backup for Microsoft 365.</li> </ul> If you do not set this
            property to *true*, Veeam Backup for Microsoft 365 will not remove a backup proxy server in these conditions.
        user_name (str | Unset): Specifies the user name of the account used for authentication to the server on which
            the backup proxy server is installed.
        user_password (str | Unset): Specifies a password.
        ssh_settings (RESTSshSettingsFromClient | Unset): Specifies credentials to access the Linux-based backup proxy
            server.
    """

    force: bool | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    ssh_settings: RESTSshSettingsFromClient | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        force = self.force

        user_name = self.user_name

        user_password = self.user_password

        ssh_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssh_settings, Unset):
            ssh_settings = self.ssh_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if force is not UNSET:
            field_dict["force"] = force
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_password is not UNSET:
            field_dict["userPassword"] = user_password
        if ssh_settings is not UNSET:
            field_dict["sshSettings"] = ssh_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_ssh_settings_from_client import RESTSshSettingsFromClient

        d = dict(src_dict)
        force = d.pop("force", UNSET)

        user_name = d.pop("userName", UNSET)

        user_password = d.pop("userPassword", UNSET)

        _ssh_settings = d.pop("sshSettings", UNSET)
        ssh_settings: RESTSshSettingsFromClient | Unset
        if isinstance(_ssh_settings, Unset):
            ssh_settings = UNSET
        else:
            ssh_settings = RESTSshSettingsFromClient.from_dict(_ssh_settings)

        rest_remove_proxy_options = cls(
            force=force,
            user_name=user_name,
            user_password=user_password,
            ssh_settings=ssh_settings,
        )

        rest_remove_proxy_options.additional_properties = d
        return rest_remove_proxy_options

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
