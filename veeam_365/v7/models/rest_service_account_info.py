from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.azure_storage_endpoint import AzureStorageEndpoint
from ..models.rest_cloud_service_account_type import RESTCloudServiceAccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTServiceAccountInfo")


@_attrs_define
class RESTServiceAccountInfo:
    """
    Attributes:
        id (UUID | Unset): Microsoft Azure service account ID.
        type_ (RESTCloudServiceAccountType | Unset): Type of Microsoft Azure service account.
        display_name (str | Unset): Name of Azure AD application associated with Microsoft Azure service account.
        description (str | Unset): Description of Microsoft Azure service account.
        application_id (UUID | Unset): Azure AD application ID.
        application_certificate_thumbprint (str | Unset): Application certificate thumbprint for connecting to Microsoft
            Azure.
        azure_environment (AzureStorageEndpoint | Unset): Specifies a Microsoft Azure region.
        azure_tenant_id (str | Unset): Microsoft 365 organization ID in Microsoft Azure.
        last_modified (datetime.datetime | Unset): Date and time of the last modification of Microsoft Azure service
            account.
    """

    id: UUID | Unset = UNSET
    type_: RESTCloudServiceAccountType | Unset = UNSET
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    application_id: UUID | Unset = UNSET
    application_certificate_thumbprint: str | Unset = UNSET
    azure_environment: AzureStorageEndpoint | Unset = UNSET
    azure_tenant_id: str | Unset = UNSET
    last_modified: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        display_name = self.display_name

        description = self.description

        application_id: str | Unset = UNSET
        if not isinstance(self.application_id, Unset):
            application_id = str(self.application_id)

        application_certificate_thumbprint = self.application_certificate_thumbprint

        azure_environment: str | Unset = UNSET
        if not isinstance(self.azure_environment, Unset):
            azure_environment = self.azure_environment.value

        azure_tenant_id = self.azure_tenant_id

        last_modified: str | Unset = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_certificate_thumbprint is not UNSET:
            field_dict["applicationCertificateThumbprint"] = application_certificate_thumbprint
        if azure_environment is not UNSET:
            field_dict["azureEnvironment"] = azure_environment
        if azure_tenant_id is not UNSET:
            field_dict["azureTenantId"] = azure_tenant_id
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _type_ = d.pop("type", UNSET)
        type_: RESTCloudServiceAccountType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTCloudServiceAccountType(_type_)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        _application_id = d.pop("applicationId", UNSET)
        application_id: UUID | Unset
        if isinstance(_application_id, Unset):
            application_id = UNSET
        else:
            application_id = UUID(_application_id)

        application_certificate_thumbprint = d.pop("applicationCertificateThumbprint", UNSET)

        _azure_environment = d.pop("azureEnvironment", UNSET)
        azure_environment: AzureStorageEndpoint | Unset
        if isinstance(_azure_environment, Unset):
            azure_environment = UNSET
        else:
            azure_environment = AzureStorageEndpoint(_azure_environment)

        azure_tenant_id = d.pop("azureTenantId", UNSET)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: datetime.datetime | Unset
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        rest_service_account_info = cls(
            id=id,
            type_=type_,
            display_name=display_name,
            description=description,
            application_id=application_id,
            application_certificate_thumbprint=application_certificate_thumbprint,
            azure_environment=azure_environment,
            azure_tenant_id=azure_tenant_id,
            last_modified=last_modified,
        )

        rest_service_account_info.additional_properties = d
        return rest_service_account_info

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
