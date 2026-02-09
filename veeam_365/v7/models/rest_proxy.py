from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_proxy_internet_proxy_type import RESTProxyInternetProxyType
from ..models.rest_proxy_status import RESTProxyStatus
from ..models.rest_proxy_throttling_unit import RESTProxyThrottlingUnit
from ..models.rest_proxy_type import RESTProxyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_internet_proxy_settings import RESTInternetProxySettings
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTProxy")


@_attrs_define
class RESTProxy:
    """
    Attributes:
        type_ (RESTProxyType | Unset): Type of the backup proxy server.
        use_internet_proxy (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 will use an internet
            proxy server to process backup and backup copy jobs.
        internet_proxy_type (RESTProxyInternetProxyType | Unset): Type of the internet proxy server.
        internet_proxy_settings (RESTInternetProxySettings | Unset):
        id (None | Unset | UUID): Backup proxy server ID. Example: 00000000-0000-0000-0000-000000000000.
        host_name (str | Unset): DNS name or IP address of the backup proxy server.
        fqdn (str | Unset): Fully qualified domain name of the backup proxy server.
        description (str | Unset): Description of the backup proxy server.
        port (int | None | Unset): Port number to connect to the backup proxy server.
        threads_number (int | None | Unset): Number of threads that the backup proxy server can process.
        enable_network_throttling (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 limits the
            network bandwidth for performance optimization.
        throttling_value (int | None | Unset): Value of the network bandwidth limit.
        throttling_unit (RESTProxyThrottlingUnit | Unset): Measuring unit for the network bandwidth limit.
        status (RESTProxyStatus | Unset): Status of the backup proxy server.
        field_links (RESTLinkHALDictionary | Unset):
    """

    type_: RESTProxyType | Unset = UNSET
    use_internet_proxy: bool | None | Unset = UNSET
    internet_proxy_type: RESTProxyInternetProxyType | Unset = UNSET
    internet_proxy_settings: RESTInternetProxySettings | Unset = UNSET
    id: None | Unset | UUID = UNSET
    host_name: str | Unset = UNSET
    fqdn: str | Unset = UNSET
    description: str | Unset = UNSET
    port: int | None | Unset = UNSET
    threads_number: int | None | Unset = UNSET
    enable_network_throttling: bool | None | Unset = UNSET
    throttling_value: int | None | Unset = UNSET
    throttling_unit: RESTProxyThrottlingUnit | Unset = UNSET
    status: RESTProxyStatus | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        use_internet_proxy: bool | None | Unset
        if isinstance(self.use_internet_proxy, Unset):
            use_internet_proxy = UNSET
        else:
            use_internet_proxy = self.use_internet_proxy

        internet_proxy_type: str | Unset = UNSET
        if not isinstance(self.internet_proxy_type, Unset):
            internet_proxy_type = self.internet_proxy_type.value

        internet_proxy_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.internet_proxy_settings, Unset):
            internet_proxy_settings = self.internet_proxy_settings.to_dict()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        host_name = self.host_name

        fqdn = self.fqdn

        description = self.description

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        threads_number: int | None | Unset
        if isinstance(self.threads_number, Unset):
            threads_number = UNSET
        else:
            threads_number = self.threads_number

        enable_network_throttling: bool | None | Unset
        if isinstance(self.enable_network_throttling, Unset):
            enable_network_throttling = UNSET
        else:
            enable_network_throttling = self.enable_network_throttling

        throttling_value: int | None | Unset
        if isinstance(self.throttling_value, Unset):
            throttling_value = UNSET
        else:
            throttling_value = self.throttling_value

        throttling_unit: str | Unset = UNSET
        if not isinstance(self.throttling_unit, Unset):
            throttling_unit = self.throttling_unit.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if use_internet_proxy is not UNSET:
            field_dict["useInternetProxy"] = use_internet_proxy
        if internet_proxy_type is not UNSET:
            field_dict["internetProxyType"] = internet_proxy_type
        if internet_proxy_settings is not UNSET:
            field_dict["internetProxySettings"] = internet_proxy_settings
        if id is not UNSET:
            field_dict["id"] = id
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if fqdn is not UNSET:
            field_dict["fqdn"] = fqdn
        if description is not UNSET:
            field_dict["description"] = description
        if port is not UNSET:
            field_dict["port"] = port
        if threads_number is not UNSET:
            field_dict["threadsNumber"] = threads_number
        if enable_network_throttling is not UNSET:
            field_dict["enableNetworkThrottling"] = enable_network_throttling
        if throttling_value is not UNSET:
            field_dict["throttlingValue"] = throttling_value
        if throttling_unit is not UNSET:
            field_dict["throttlingUnit"] = throttling_unit
        if status is not UNSET:
            field_dict["status"] = status
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_internet_proxy_settings import RESTInternetProxySettings
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTProxyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTProxyType(_type_)

        def _parse_use_internet_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_internet_proxy = _parse_use_internet_proxy(d.pop("useInternetProxy", UNSET))

        _internet_proxy_type = d.pop("internetProxyType", UNSET)
        internet_proxy_type: RESTProxyInternetProxyType | Unset
        if isinstance(_internet_proxy_type, Unset):
            internet_proxy_type = UNSET
        else:
            internet_proxy_type = RESTProxyInternetProxyType(_internet_proxy_type)

        _internet_proxy_settings = d.pop("internetProxySettings", UNSET)
        internet_proxy_settings: RESTInternetProxySettings | Unset
        if isinstance(_internet_proxy_settings, Unset):
            internet_proxy_settings = UNSET
        else:
            internet_proxy_settings = RESTInternetProxySettings.from_dict(_internet_proxy_settings)

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        host_name = d.pop("hostName", UNSET)

        fqdn = d.pop("fqdn", UNSET)

        description = d.pop("description", UNSET)

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_threads_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        threads_number = _parse_threads_number(d.pop("threadsNumber", UNSET))

        def _parse_enable_network_throttling(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_network_throttling = _parse_enable_network_throttling(d.pop("enableNetworkThrottling", UNSET))

        def _parse_throttling_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        throttling_value = _parse_throttling_value(d.pop("throttlingValue", UNSET))

        _throttling_unit = d.pop("throttlingUnit", UNSET)
        throttling_unit: RESTProxyThrottlingUnit | Unset
        if isinstance(_throttling_unit, Unset):
            throttling_unit = UNSET
        else:
            throttling_unit = RESTProxyThrottlingUnit(_throttling_unit)

        _status = d.pop("status", UNSET)
        status: RESTProxyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTProxyStatus(_status)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_proxy = cls(
            type_=type_,
            use_internet_proxy=use_internet_proxy,
            internet_proxy_type=internet_proxy_type,
            internet_proxy_settings=internet_proxy_settings,
            id=id,
            host_name=host_name,
            fqdn=fqdn,
            description=description,
            port=port,
            threads_number=threads_number,
            enable_network_throttling=enable_network_throttling,
            throttling_value=throttling_value,
            throttling_unit=throttling_unit,
            status=status,
            field_links=field_links,
        )

        rest_proxy.additional_properties = d
        return rest_proxy

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
