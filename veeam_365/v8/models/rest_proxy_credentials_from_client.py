from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_ssh_settings_from_client import RESTSshSettingsFromClient


T = TypeVar("T", bound="RESTProxyCredentialsFromClient")


@_attrs_define
class RESTProxyCredentialsFromClient:
    """
    Attributes:
        ssh_settings (RESTSshSettingsFromClient | Unset): Specifies credentials to access the Linux-based backup proxy
            server.
        username (str | Unset): Specifies a user name to access the Windows-based backup proxy server.
        password (str | Unset): Specifies a password.
    """

    ssh_settings: RESTSshSettingsFromClient | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssh_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssh_settings, Unset):
            ssh_settings = self.ssh_settings.to_dict()

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssh_settings is not UNSET:
            field_dict["sshSettings"] = ssh_settings
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_ssh_settings_from_client import RESTSshSettingsFromClient

        d = dict(src_dict)
        _ssh_settings = d.pop("sshSettings", UNSET)
        ssh_settings: RESTSshSettingsFromClient | Unset
        if isinstance(_ssh_settings, Unset):
            ssh_settings = UNSET
        else:
            ssh_settings = RESTSshSettingsFromClient.from_dict(_ssh_settings)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        rest_proxy_credentials_from_client = cls(
            ssh_settings=ssh_settings,
            username=username,
            password=password,
        )

        rest_proxy_credentials_from_client.additional_properties = d
        return rest_proxy_credentials_from_client

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
