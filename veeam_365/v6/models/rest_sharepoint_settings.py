from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTSharepointSettings")


@_attrs_define
class RESTSharepointSettings:
    """
    Attributes:
        server_name (str | Unset):
        username (str | Unset):
        password (str | Unset):
        use_ssl (bool | None | Unset):
        skip_c_averification (bool | None | Unset):
        skip_commonnameverification (bool | None | Unset):
        skip_revocationcheck (bool | None | Unset):
        server_port (int | None | Unset):
        grant_accesstositecollections (bool | None | Unset):
    """

    server_name: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    use_ssl: bool | None | Unset = UNSET
    skip_c_averification: bool | None | Unset = UNSET
    skip_commonnameverification: bool | None | Unset = UNSET
    skip_revocationcheck: bool | None | Unset = UNSET
    server_port: int | None | Unset = UNSET
    grant_accesstositecollections: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_name = self.server_name

        username = self.username

        password = self.password

        use_ssl: bool | None | Unset
        if isinstance(self.use_ssl, Unset):
            use_ssl = UNSET
        else:
            use_ssl = self.use_ssl

        skip_c_averification: bool | None | Unset
        if isinstance(self.skip_c_averification, Unset):
            skip_c_averification = UNSET
        else:
            skip_c_averification = self.skip_c_averification

        skip_commonnameverification: bool | None | Unset
        if isinstance(self.skip_commonnameverification, Unset):
            skip_commonnameverification = UNSET
        else:
            skip_commonnameverification = self.skip_commonnameverification

        skip_revocationcheck: bool | None | Unset
        if isinstance(self.skip_revocationcheck, Unset):
            skip_revocationcheck = UNSET
        else:
            skip_revocationcheck = self.skip_revocationcheck

        server_port: int | None | Unset
        if isinstance(self.server_port, Unset):
            server_port = UNSET
        else:
            server_port = self.server_port

        grant_accesstositecollections: bool | None | Unset
        if isinstance(self.grant_accesstositecollections, Unset):
            grant_accesstositecollections = UNSET
        else:
            grant_accesstositecollections = self.grant_accesstositecollections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if use_ssl is not UNSET:
            field_dict["useSSL"] = use_ssl
        if skip_c_averification is not UNSET:
            field_dict["skipCAverification"] = skip_c_averification
        if skip_commonnameverification is not UNSET:
            field_dict["skipCommonnameverification"] = skip_commonnameverification
        if skip_revocationcheck is not UNSET:
            field_dict["skipRevocationcheck"] = skip_revocationcheck
        if server_port is not UNSET:
            field_dict["serverPort"] = server_port
        if grant_accesstositecollections is not UNSET:
            field_dict["grantAccesstositecollections"] = grant_accesstositecollections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server_name = d.pop("serverName", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        def _parse_use_ssl(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_ssl = _parse_use_ssl(d.pop("useSSL", UNSET))

        def _parse_skip_c_averification(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_c_averification = _parse_skip_c_averification(d.pop("skipCAverification", UNSET))

        def _parse_skip_commonnameverification(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_commonnameverification = _parse_skip_commonnameverification(d.pop("skipCommonnameverification", UNSET))

        def _parse_skip_revocationcheck(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_revocationcheck = _parse_skip_revocationcheck(d.pop("skipRevocationcheck", UNSET))

        def _parse_server_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        server_port = _parse_server_port(d.pop("serverPort", UNSET))

        def _parse_grant_accesstositecollections(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grant_accesstositecollections = _parse_grant_accesstositecollections(
            d.pop("grantAccesstositecollections", UNSET)
        )

        rest_sharepoint_settings = cls(
            server_name=server_name,
            username=username,
            password=password,
            use_ssl=use_ssl,
            skip_c_averification=skip_c_averification,
            skip_commonnameverification=skip_commonnameverification,
            skip_revocationcheck=skip_revocationcheck,
            server_port=server_port,
            grant_accesstositecollections=grant_accesstositecollections,
        )

        rest_sharepoint_settings.additional_properties = d
        return rest_sharepoint_settings

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
