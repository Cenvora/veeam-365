from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.azure_storage_endpoint import AzureStorageEndpoint
from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTDeviceCodeInfoRequest")



@_attrs_define
class RESTDeviceCodeInfoRequest:
    """ 
        Attributes:
            azure_environment (AzureStorageEndpoint | Unset): Specifies a Microsoft Entra region.
            azure_tenant_id (str | Unset): Specifies the Microsoft 365 organization ID in Microsoft Entra.
     """

    azure_environment: AzureStorageEndpoint | Unset = UNSET
    azure_tenant_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        azure_environment: str | Unset = UNSET
        if not isinstance(self.azure_environment, Unset):
            azure_environment = self.azure_environment.value


        azure_tenant_id = self.azure_tenant_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if azure_environment is not UNSET:
            field_dict["azureEnvironment"] = azure_environment
        if azure_tenant_id is not UNSET:
            field_dict["azureTenantId"] = azure_tenant_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _azure_environment = d.pop("azureEnvironment", UNSET)
        azure_environment: AzureStorageEndpoint | Unset
        if isinstance(_azure_environment,  Unset):
            azure_environment = UNSET
        else:
            azure_environment = AzureStorageEndpoint(_azure_environment)




        azure_tenant_id = d.pop("azureTenantId", UNSET)

        rest_device_code_info_request = cls(
            azure_environment=azure_environment,
            azure_tenant_id=azure_tenant_id,
        )


        rest_device_code_info_request.additional_properties = d
        return rest_device_code_info_request

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
