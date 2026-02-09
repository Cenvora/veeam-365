from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_azure_resource_group import RESTAzureResourceGroup
    from ..models.rest_azure_subnet import RESTAzureSubnet
    from ..models.rest_azure_virtual_machine_size import RESTAzureVirtualMachineSize
    from ..models.rest_azure_virtual_network import RESTAzureVirtualNetwork


T = TypeVar("T", bound="RESTAzureArchiverAppliance")


@_attrs_define
class RESTAzureArchiverAppliance:
    """
    Attributes:
        virtual_machine_size (RESTAzureVirtualMachineSize | Unset):
        resource_group (RESTAzureResourceGroup | Unset):
        virtual_network (RESTAzureVirtualNetwork | Unset):
        subnet (RESTAzureSubnet | Unset):
        region (str | Unset):
        appliance_port (int | None | Unset):
    """

    virtual_machine_size: RESTAzureVirtualMachineSize | Unset = UNSET
    resource_group: RESTAzureResourceGroup | Unset = UNSET
    virtual_network: RESTAzureVirtualNetwork | Unset = UNSET
    subnet: RESTAzureSubnet | Unset = UNSET
    region: str | Unset = UNSET
    appliance_port: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_machine_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.virtual_machine_size, Unset):
            virtual_machine_size = self.virtual_machine_size.to_dict()

        resource_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_group, Unset):
            resource_group = self.resource_group.to_dict()

        virtual_network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.virtual_network, Unset):
            virtual_network = self.virtual_network.to_dict()

        subnet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subnet, Unset):
            subnet = self.subnet.to_dict()

        region = self.region

        appliance_port: int | None | Unset
        if isinstance(self.appliance_port, Unset):
            appliance_port = UNSET
        else:
            appliance_port = self.appliance_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtual_machine_size is not UNSET:
            field_dict["virtualMachineSize"] = virtual_machine_size
        if resource_group is not UNSET:
            field_dict["resourceGroup"] = resource_group
        if virtual_network is not UNSET:
            field_dict["virtualNetwork"] = virtual_network
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if region is not UNSET:
            field_dict["region"] = region
        if appliance_port is not UNSET:
            field_dict["appliancePort"] = appliance_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_azure_resource_group import RESTAzureResourceGroup
        from ..models.rest_azure_subnet import RESTAzureSubnet
        from ..models.rest_azure_virtual_machine_size import RESTAzureVirtualMachineSize
        from ..models.rest_azure_virtual_network import RESTAzureVirtualNetwork

        d = dict(src_dict)
        _virtual_machine_size = d.pop("virtualMachineSize", UNSET)
        virtual_machine_size: RESTAzureVirtualMachineSize | Unset
        if isinstance(_virtual_machine_size, Unset):
            virtual_machine_size = UNSET
        else:
            virtual_machine_size = RESTAzureVirtualMachineSize.from_dict(_virtual_machine_size)

        _resource_group = d.pop("resourceGroup", UNSET)
        resource_group: RESTAzureResourceGroup | Unset
        if isinstance(_resource_group, Unset):
            resource_group = UNSET
        else:
            resource_group = RESTAzureResourceGroup.from_dict(_resource_group)

        _virtual_network = d.pop("virtualNetwork", UNSET)
        virtual_network: RESTAzureVirtualNetwork | Unset
        if isinstance(_virtual_network, Unset):
            virtual_network = UNSET
        else:
            virtual_network = RESTAzureVirtualNetwork.from_dict(_virtual_network)

        _subnet = d.pop("subnet", UNSET)
        subnet: RESTAzureSubnet | Unset
        if isinstance(_subnet, Unset):
            subnet = UNSET
        else:
            subnet = RESTAzureSubnet.from_dict(_subnet)

        region = d.pop("region", UNSET)

        def _parse_appliance_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        appliance_port = _parse_appliance_port(d.pop("appliancePort", UNSET))

        rest_azure_archiver_appliance = cls(
            virtual_machine_size=virtual_machine_size,
            resource_group=resource_group,
            virtual_network=virtual_network,
            subnet=subnet,
            region=region,
            appliance_port=appliance_port,
        )

        rest_azure_archiver_appliance.additional_properties = d
        return rest_azure_archiver_appliance

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
