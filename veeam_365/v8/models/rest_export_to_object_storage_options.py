from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_storage_endpoint import AzureStorageEndpoint
from ..models.rest_export_object_storage_type import RESTExportObjectStorageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTExportToObjectStorageOptions")


@_attrs_define
class RESTExportToObjectStorageOptions:
    """
    Attributes:
        container_name (str): Specifies an Azure Blob Storage container name.
        object_storage_type (RESTExportObjectStorageType): Specifies the object storage repository type to perform the
            operation.
        credential_id (UUID | Unset): Specifies an Azure cloud account ID.
        prefix (str | Unset): Specifies an Azure Blob Storage path prefix.
        region_type (AzureStorageEndpoint | Unset): Specifies a Microsoft Entra region.
    """

    container_name: str
    object_storage_type: RESTExportObjectStorageType
    credential_id: UUID | Unset = UNSET
    prefix: str | Unset = UNSET
    region_type: AzureStorageEndpoint | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_name = self.container_name

        object_storage_type = self.object_storage_type.value

        credential_id: str | Unset = UNSET
        if not isinstance(self.credential_id, Unset):
            credential_id = str(self.credential_id)

        prefix = self.prefix

        region_type: str | Unset = UNSET
        if not isinstance(self.region_type, Unset):
            region_type = self.region_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containerName": container_name,
                "objectStorageType": object_storage_type,
            }
        )
        if credential_id is not UNSET:
            field_dict["credentialId"] = credential_id
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if region_type is not UNSET:
            field_dict["regionType"] = region_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        container_name = d.pop("containerName")

        object_storage_type = RESTExportObjectStorageType(d.pop("objectStorageType"))

        _credential_id = d.pop("credentialId", UNSET)
        credential_id: UUID | Unset
        if isinstance(_credential_id, Unset):
            credential_id = UNSET
        else:
            credential_id = UUID(_credential_id)

        prefix = d.pop("prefix", UNSET)

        _region_type = d.pop("regionType", UNSET)
        region_type: AzureStorageEndpoint | Unset
        if isinstance(_region_type, Unset):
            region_type = UNSET
        else:
            region_type = AzureStorageEndpoint(_region_type)

        rest_export_to_object_storage_options = cls(
            container_name=container_name,
            object_storage_type=object_storage_type,
            credential_id=credential_id,
            prefix=prefix,
            region_type=region_type,
        )

        rest_export_to_object_storage_options.additional_properties = d
        return rest_export_to_object_storage_options

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
