from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_storage_endpoint import AzureStorageEndpoint
from ..models.rest_export_object_storage_type import RESTExportObjectStorageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTExportToAzureOptions")


@_attrs_define
class RESTExportToAzureOptions:
    """
    Attributes:
        credential_id (UUID): Specifies an Azure cloud account ID.
        container_name (str): Specifies an Azure Blob Storage container name.
        region_type (AzureStorageEndpoint): Specifies a Microsoft Entra region.
        object_storage_type (RESTExportObjectStorageType): Specifies the object storage repository type to perform the
            operation.
        prefix (str | Unset): Specifies an Azure Blob Storage path prefix.
    """

    credential_id: UUID
    container_name: str
    region_type: AzureStorageEndpoint
    object_storage_type: RESTExportObjectStorageType
    prefix: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential_id = str(self.credential_id)

        container_name = self.container_name

        region_type = self.region_type.value

        object_storage_type = self.object_storage_type.value

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentialId": credential_id,
                "containerName": container_name,
                "regionType": region_type,
                "objectStorageType": object_storage_type,
            }
        )
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential_id = UUID(d.pop("credentialId"))

        container_name = d.pop("containerName")

        region_type = AzureStorageEndpoint(d.pop("regionType"))

        object_storage_type = RESTExportObjectStorageType(d.pop("objectStorageType"))

        prefix = d.pop("prefix", UNSET)

        rest_export_to_azure_options = cls(
            credential_id=credential_id,
            container_name=container_name,
            region_type=region_type,
            object_storage_type=object_storage_type,
            prefix=prefix,
        )

        rest_export_to_azure_options.additional_properties = d
        return rest_export_to_azure_options

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
