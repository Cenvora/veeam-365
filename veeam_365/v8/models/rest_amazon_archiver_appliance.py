from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_amazon_security_group import RESTAmazonSecurityGroup
    from ..models.rest_amazon_subnet import RESTAmazonSubnet
    from ..models.rest_amazon_vpc import RESTAmazonVpc


T = TypeVar("T", bound="RESTAmazonArchiverAppliance")


@_attrs_define
class RESTAmazonArchiverAppliance:
    """
    Attributes:
        instance_type_name (str | Unset): Instance type.
        virtual_private_cloud (RESTAmazonVpc | Unset):
        subnet (RESTAmazonSubnet | Unset):
        security_group (RESTAmazonSecurityGroup | Unset):
        ip_ranges (None | str | Unset): Range of IPv4 addresses for the security group. Example:
            24.48.96.192/32,16.24.0.0/24.
        appliance_port (int | None | Unset): Port number to route requests between the Amazon archiver appliance and
            Veeam Backup for Microsoft 365 backup infrastructure components.
    """

    instance_type_name: str | Unset = UNSET
    virtual_private_cloud: RESTAmazonVpc | Unset = UNSET
    subnet: RESTAmazonSubnet | Unset = UNSET
    security_group: RESTAmazonSecurityGroup | Unset = UNSET
    ip_ranges: None | str | Unset = UNSET
    appliance_port: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_type_name = self.instance_type_name

        virtual_private_cloud: dict[str, Any] | Unset = UNSET
        if not isinstance(self.virtual_private_cloud, Unset):
            virtual_private_cloud = self.virtual_private_cloud.to_dict()

        subnet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subnet, Unset):
            subnet = self.subnet.to_dict()

        security_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.security_group, Unset):
            security_group = self.security_group.to_dict()

        ip_ranges: None | str | Unset
        if isinstance(self.ip_ranges, Unset):
            ip_ranges = UNSET
        else:
            ip_ranges = self.ip_ranges

        appliance_port: int | None | Unset
        if isinstance(self.appliance_port, Unset):
            appliance_port = UNSET
        else:
            appliance_port = self.appliance_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_type_name is not UNSET:
            field_dict["instanceTypeName"] = instance_type_name
        if virtual_private_cloud is not UNSET:
            field_dict["virtualPrivateCloud"] = virtual_private_cloud
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if security_group is not UNSET:
            field_dict["securityGroup"] = security_group
        if ip_ranges is not UNSET:
            field_dict["ipRanges"] = ip_ranges
        if appliance_port is not UNSET:
            field_dict["appliancePort"] = appliance_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_amazon_security_group import RESTAmazonSecurityGroup
        from ..models.rest_amazon_subnet import RESTAmazonSubnet
        from ..models.rest_amazon_vpc import RESTAmazonVpc

        d = dict(src_dict)
        instance_type_name = d.pop("instanceTypeName", UNSET)

        _virtual_private_cloud = d.pop("virtualPrivateCloud", UNSET)
        virtual_private_cloud: RESTAmazonVpc | Unset
        if isinstance(_virtual_private_cloud, Unset):
            virtual_private_cloud = UNSET
        else:
            virtual_private_cloud = RESTAmazonVpc.from_dict(_virtual_private_cloud)

        _subnet = d.pop("subnet", UNSET)
        subnet: RESTAmazonSubnet | Unset
        if isinstance(_subnet, Unset):
            subnet = UNSET
        else:
            subnet = RESTAmazonSubnet.from_dict(_subnet)

        _security_group = d.pop("securityGroup", UNSET)
        security_group: RESTAmazonSecurityGroup | Unset
        if isinstance(_security_group, Unset):
            security_group = UNSET
        else:
            security_group = RESTAmazonSecurityGroup.from_dict(_security_group)

        def _parse_ip_ranges(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_ranges = _parse_ip_ranges(d.pop("ipRanges", UNSET))

        def _parse_appliance_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        appliance_port = _parse_appliance_port(d.pop("appliancePort", UNSET))

        rest_amazon_archiver_appliance = cls(
            instance_type_name=instance_type_name,
            virtual_private_cloud=virtual_private_cloud,
            subnet=subnet,
            security_group=security_group,
            ip_ranges=ip_ranges,
            appliance_port=appliance_port,
        )

        rest_amazon_archiver_appliance.additional_properties = d
        return rest_amazon_archiver_appliance

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
