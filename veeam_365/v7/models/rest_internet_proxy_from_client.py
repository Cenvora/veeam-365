from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTInternetProxyFromClient")


@_attrs_define
class RESTInternetProxyFromClient:
    """
    Attributes:
        use_internet_proxy (bool | None | Unset): Defines whether the internet proxy server will be used in the Veeam
            Backup for Microsoft 365 infrastructure.
        user_password (str | Unset): Specifies a password.
        host_name (str | Unset): Specifies a name of the internet proxy server.
        port (int | None | Unset): Specifies a port number which is used to connect to the internet proxy server. The
            default port for connection to the internet proxy is *3128*.
        use_authentication (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 will use an
            authentication credentials when connecting to the internet proxy server.
        username (str | Unset): Specifies the user name for authentication to the internet proxy server.
    """

    use_internet_proxy: bool | None | Unset = UNSET
    user_password: str | Unset = UNSET
    host_name: str | Unset = UNSET
    port: int | None | Unset = UNSET
    use_authentication: bool | None | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_internet_proxy: bool | None | Unset
        if isinstance(self.use_internet_proxy, Unset):
            use_internet_proxy = UNSET
        else:
            use_internet_proxy = self.use_internet_proxy

        user_password = self.user_password

        host_name = self.host_name

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        use_authentication: bool | None | Unset
        if isinstance(self.use_authentication, Unset):
            use_authentication = UNSET
        else:
            use_authentication = self.use_authentication

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if use_internet_proxy is not UNSET:
            field_dict["useInternetProxy"] = use_internet_proxy
        if user_password is not UNSET:
            field_dict["userPassword"] = user_password
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if port is not UNSET:
            field_dict["port"] = port
        if use_authentication is not UNSET:
            field_dict["useAuthentication"] = use_authentication
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_use_internet_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_internet_proxy = _parse_use_internet_proxy(d.pop("useInternetProxy", UNSET))

        user_password = d.pop("userPassword", UNSET)

        host_name = d.pop("hostName", UNSET)

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_use_authentication(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_authentication = _parse_use_authentication(d.pop("useAuthentication", UNSET))

        username = d.pop("username", UNSET)

        rest_internet_proxy_from_client = cls(
            use_internet_proxy=use_internet_proxy,
            user_password=user_password,
            host_name=host_name,
            port=port,
            use_authentication=use_authentication,
            username=username,
        )

        rest_internet_proxy_from_client.additional_properties = d
        return rest_internet_proxy_from_client

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
