from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_proxy_from_client_internet_proxy_type import RESTProxyFromClientInternetProxyType
from ..models.rest_proxy_from_client_throttling_unit import RESTProxyFromClientThrottlingUnit
from ..models.rest_proxy_operating_system import RESTProxyOperatingSystem
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_internet_proxy_settings_from_client import RESTInternetProxySettingsFromClient
  from ..models.rest_ssh_settings_from_client import RESTSshSettingsFromClient





T = TypeVar("T", bound="RESTProxyFromClient")



@_attrs_define
class RESTProxyFromClient:
    """ 
        Attributes:
            use_domain_network (bool | None | Unset): Defines the type of the backup proxy server to add. The following
                values are available: <ul> <li>*true* - domain backup proxy, that is, a backup proxy server that resides in the
                same domain as the Veeam Backup for Microsoft 365 server or in a trusted domain.</li> <li>*false* - workgroup
                backup proxy, that is, a backup proxy server that resides in a workgroup.</li> </ul> If you omit this property,
                a workgroup backup proxy will be added.
            use_internet_proxy (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 will use an internet
                proxy server to process backup and backup copy jobs.
            internet_proxy_type (RESTProxyFromClientInternetProxyType | Unset): Specifies the type of the internet proxy
                server. The following types are available: <ul> <li>*FromManagementServer* - the internet proxy server uses
                connection settings from the Veeam Backup for Microsoft 365 server.</li> <li>*Custom* - the internet proxy
                server uses connection settings configured on the Veeam Backup for Microsoft 365 proxy.</li> </ul>

                **Note**: The `useInternetProxy` property value must be set to *true*.
            internet_proxy_settings (RESTInternetProxySettingsFromClient | Unset):
            operating_system (RESTProxyOperatingSystem | Unset): Type of the operating system that the backup proxy server
                runs.
            ssh_settings (RESTSshSettingsFromClient | Unset): Specifies credentials to access the Linux-based backup proxy
                server.
            id (None | Unset | UUID): Specifies the ID of the backup proxy server. Example:
                00000000-0000-0000-0000-000000000000.
            host_name (str | Unset): Specifies the DNS name or IP address of the backup proxy server.
            description (str | Unset): Specifies a description of the backup proxy server.
            port (int | None | Unset): Specifies the port number to connect to the backup proxy server. The default port is
                *9193*.
            username (str | Unset): Specifies the user name to access the backup proxy server.
            password (str | Unset): Specifies a password.
            service_account_name (None | str | Unset): Specifies the service account to run *Veeam Backup for Microsoft 365
                Proxy Service*.
            service_account_password (str | Unset): Specifies a password.
            create_service_account (bool | Unset): Defines whether Veeam Backup for Microsoft 365 will create the service
                account.
            enable_network_throttling (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 will limit the
                network bandwidth for performance optimization. Use the `throttlingValue` property to set the network throttling
                value.
            throttling_value (int | None | Unset): Specifies the network bandwidth limit value.

                **Note**: The `enableNetworkThrottling` property value must be set to true. Otherwise, the network bandwidth
                limit value will not be applied.
            throttling_unit (RESTProxyFromClientThrottlingUnit | Unset): Specifies the measuring unit for the network
                bandwidth limit.

                **Note**: The `enableNetworkThrottling` property value must be set to *true*.
            attach_used_proxy (bool | None | Unset): Adds a backup proxy server that is already managed by another Veeam
                Backup for Microsoft 365 server. Defines whether Veeam Backup for Microsoft 365 will take ownership of the
                backup proxy server and add it to the backup infrastructure.
     """

    use_domain_network: bool | None | Unset = UNSET
    use_internet_proxy: bool | None | Unset = UNSET
    internet_proxy_type: RESTProxyFromClientInternetProxyType | Unset = UNSET
    internet_proxy_settings: RESTInternetProxySettingsFromClient | Unset = UNSET
    operating_system: RESTProxyOperatingSystem | Unset = UNSET
    ssh_settings: RESTSshSettingsFromClient | Unset = UNSET
    id: None | Unset | UUID = UNSET
    host_name: str | Unset = UNSET
    description: str | Unset = UNSET
    port: int | None | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    service_account_name: None | str | Unset = UNSET
    service_account_password: str | Unset = UNSET
    create_service_account: bool | Unset = UNSET
    enable_network_throttling: bool | None | Unset = UNSET
    throttling_value: int | None | Unset = UNSET
    throttling_unit: RESTProxyFromClientThrottlingUnit | Unset = UNSET
    attach_used_proxy: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_internet_proxy_settings_from_client import RESTInternetProxySettingsFromClient
        from ..models.rest_ssh_settings_from_client import RESTSshSettingsFromClient
        use_domain_network: bool | None | Unset
        if isinstance(self.use_domain_network, Unset):
            use_domain_network = UNSET
        else:
            use_domain_network = self.use_domain_network

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

        operating_system: str | Unset = UNSET
        if not isinstance(self.operating_system, Unset):
            operating_system = self.operating_system.value


        ssh_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssh_settings, Unset):
            ssh_settings = self.ssh_settings.to_dict()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        host_name = self.host_name

        description = self.description

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        username = self.username

        password = self.password

        service_account_name: None | str | Unset
        if isinstance(self.service_account_name, Unset):
            service_account_name = UNSET
        else:
            service_account_name = self.service_account_name

        service_account_password = self.service_account_password

        create_service_account = self.create_service_account

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


        attach_used_proxy: bool | None | Unset
        if isinstance(self.attach_used_proxy, Unset):
            attach_used_proxy = UNSET
        else:
            attach_used_proxy = self.attach_used_proxy


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if use_domain_network is not UNSET:
            field_dict["useDomainNetwork"] = use_domain_network
        if use_internet_proxy is not UNSET:
            field_dict["useInternetProxy"] = use_internet_proxy
        if internet_proxy_type is not UNSET:
            field_dict["internetProxyType"] = internet_proxy_type
        if internet_proxy_settings is not UNSET:
            field_dict["internetProxySettings"] = internet_proxy_settings
        if operating_system is not UNSET:
            field_dict["operatingSystem"] = operating_system
        if ssh_settings is not UNSET:
            field_dict["sshSettings"] = ssh_settings
        if id is not UNSET:
            field_dict["id"] = id
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if description is not UNSET:
            field_dict["description"] = description
        if port is not UNSET:
            field_dict["port"] = port
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if service_account_name is not UNSET:
            field_dict["serviceAccountName"] = service_account_name
        if service_account_password is not UNSET:
            field_dict["serviceAccountPassword"] = service_account_password
        if create_service_account is not UNSET:
            field_dict["createServiceAccount"] = create_service_account
        if enable_network_throttling is not UNSET:
            field_dict["enableNetworkThrottling"] = enable_network_throttling
        if throttling_value is not UNSET:
            field_dict["throttlingValue"] = throttling_value
        if throttling_unit is not UNSET:
            field_dict["throttlingUnit"] = throttling_unit
        if attach_used_proxy is not UNSET:
            field_dict["attachUsedProxy"] = attach_used_proxy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_internet_proxy_settings_from_client import RESTInternetProxySettingsFromClient
        from ..models.rest_ssh_settings_from_client import RESTSshSettingsFromClient
        d = dict(src_dict)
        def _parse_use_domain_network(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_domain_network = _parse_use_domain_network(d.pop("useDomainNetwork", UNSET))


        def _parse_use_internet_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_internet_proxy = _parse_use_internet_proxy(d.pop("useInternetProxy", UNSET))


        _internet_proxy_type = d.pop("internetProxyType", UNSET)
        internet_proxy_type: RESTProxyFromClientInternetProxyType | Unset
        if isinstance(_internet_proxy_type,  Unset):
            internet_proxy_type = UNSET
        else:
            internet_proxy_type = RESTProxyFromClientInternetProxyType(_internet_proxy_type)




        _internet_proxy_settings = d.pop("internetProxySettings", UNSET)
        internet_proxy_settings: RESTInternetProxySettingsFromClient | Unset
        if isinstance(_internet_proxy_settings,  Unset):
            internet_proxy_settings = UNSET
        else:
            internet_proxy_settings = RESTInternetProxySettingsFromClient.from_dict(_internet_proxy_settings)




        _operating_system = d.pop("operatingSystem", UNSET)
        operating_system: RESTProxyOperatingSystem | Unset
        if isinstance(_operating_system,  Unset):
            operating_system = UNSET
        else:
            operating_system = RESTProxyOperatingSystem(_operating_system)




        _ssh_settings = d.pop("sshSettings", UNSET)
        ssh_settings: RESTSshSettingsFromClient | Unset
        if isinstance(_ssh_settings,  Unset):
            ssh_settings = UNSET
        else:
            ssh_settings = RESTSshSettingsFromClient.from_dict(_ssh_settings)




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

        description = d.pop("description", UNSET)

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))


        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        def _parse_service_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_account_name = _parse_service_account_name(d.pop("serviceAccountName", UNSET))


        service_account_password = d.pop("serviceAccountPassword", UNSET)

        create_service_account = d.pop("createServiceAccount", UNSET)

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
        throttling_unit: RESTProxyFromClientThrottlingUnit | Unset
        if isinstance(_throttling_unit,  Unset):
            throttling_unit = UNSET
        else:
            throttling_unit = RESTProxyFromClientThrottlingUnit(_throttling_unit)




        def _parse_attach_used_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        attach_used_proxy = _parse_attach_used_proxy(d.pop("attachUsedProxy", UNSET))


        rest_proxy_from_client = cls(
            use_domain_network=use_domain_network,
            use_internet_proxy=use_internet_proxy,
            internet_proxy_type=internet_proxy_type,
            internet_proxy_settings=internet_proxy_settings,
            operating_system=operating_system,
            ssh_settings=ssh_settings,
            id=id,
            host_name=host_name,
            description=description,
            port=port,
            username=username,
            password=password,
            service_account_name=service_account_name,
            service_account_password=service_account_password,
            create_service_account=create_service_account,
            enable_network_throttling=enable_network_throttling,
            throttling_value=throttling_value,
            throttling_unit=throttling_unit,
            attach_used_proxy=attach_used_proxy,
        )


        rest_proxy_from_client.additional_properties = d
        return rest_proxy_from_client

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
