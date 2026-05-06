from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTAzureVirtualMachineSize")



@_attrs_define
class RESTAzureVirtualMachineSize:
    """ 
        Attributes:
            name (str | Unset): Name of the Azure archiver appliance.
            cores_count (str | Unset): Number of processor cores.
            memory_mb (int | Unset): Auxiliary virtual machine memory.
            os_disk_size_mb (int | Unset): Size of the operating system partition.
            resource_disk_size_mb (int | Unset): Size of the resource partition.
     """

    name: str | Unset = UNSET
    cores_count: str | Unset = UNSET
    memory_mb: int | Unset = UNSET
    os_disk_size_mb: int | Unset = UNSET
    resource_disk_size_mb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        cores_count = self.cores_count

        memory_mb = self.memory_mb

        os_disk_size_mb = self.os_disk_size_mb

        resource_disk_size_mb = self.resource_disk_size_mb


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if cores_count is not UNSET:
            field_dict["coresCount"] = cores_count
        if memory_mb is not UNSET:
            field_dict["memoryMB"] = memory_mb
        if os_disk_size_mb is not UNSET:
            field_dict["osDiskSizeMB"] = os_disk_size_mb
        if resource_disk_size_mb is not UNSET:
            field_dict["resourceDiskSizeMB"] = resource_disk_size_mb

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        cores_count = d.pop("coresCount", UNSET)

        memory_mb = d.pop("memoryMB", UNSET)

        os_disk_size_mb = d.pop("osDiskSizeMB", UNSET)

        resource_disk_size_mb = d.pop("resourceDiskSizeMB", UNSET)

        rest_azure_virtual_machine_size = cls(
            name=name,
            cores_count=cores_count,
            memory_mb=memory_mb,
            os_disk_size_mb=os_disk_size_mb,
            resource_disk_size_mb=resource_disk_size_mb,
        )


        rest_azure_virtual_machine_size.additional_properties = d
        return rest_azure_virtual_machine_size

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
