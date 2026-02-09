from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTInternetProxy")


@_attrs_define
class RESTInternetProxy:
    """
    Attributes:
        use_internet_proxy (bool | Unset):
        field_links (RESTLinkHALDictionary | Unset):
        host_name (str | Unset):
        port (int | None | Unset):
        use_authentication (bool | None | Unset):
        username (str | Unset):
    """

    use_internet_proxy: bool | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    host_name: str | Unset = UNSET
    port: int | None | Unset = UNSET
    use_authentication: bool | None | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_internet_proxy = self.use_internet_proxy

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

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
        if field_links is not UNSET:
            field_dict["_links"] = field_links
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
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        use_internet_proxy = d.pop("useInternetProxy", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

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

        rest_internet_proxy = cls(
            use_internet_proxy=use_internet_proxy,
            field_links=field_links,
            host_name=host_name,
            port=port,
            use_authentication=use_authentication,
            username=username,
        )

        rest_internet_proxy.additional_properties = d
        return rest_internet_proxy

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
