from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.azure_storage_endpoint import AzureStorageEndpoint
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTServiceAccountCreationData")


@_attrs_define
class RESTServiceAccountCreationData:
    """
    Attributes:
        application_name (str | Unset): Specifies a name of the Microsoft Entra application associated with Microsoft
            Azure service account.
        description (str | Unset): Specifies a description of Microsoft Azure service account.
        application_id (UUID | Unset): Specifies the ID of the Microsoft Entra application.
        azure_environment (AzureStorageEndpoint | Unset): Specifies a Microsoft Entra region.
        azure_tenant_id (str | Unset): Specifies the identification number of a Microsoft 365 organization in Microsoft
            Entra.
        application_certificate (str | Unset): Specifies the Base64 string of an SSL certificate that you want to use to
            access the Microsoft Entra application.
        application_certificate_password (str | Unset): Specifies a password.
        application_secret (str | Unset): Specifies an application secret for connecting to Microsoft Entra.
        user_code (str | Unset): Specifies the code that you must copy and then specify on Microsoft Identity platform.
        subscription_ids (list[str] | Unset): Specifies an array of subscriptions associated with a user account that
            was used to sign in to Microsoft Entra. For more information on how to get these parameters, see [Get
            Subscriptions](AzureServiceAccounts#operation/AzureServiceAccounts_GetSubscriptions).
    """

    application_name: str | Unset = UNSET
    description: str | Unset = UNSET
    application_id: UUID | Unset = UNSET
    azure_environment: AzureStorageEndpoint | Unset = UNSET
    azure_tenant_id: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    application_certificate_password: str | Unset = UNSET
    application_secret: str | Unset = UNSET
    user_code: str | Unset = UNSET
    subscription_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_name = self.application_name

        description = self.description

        application_id: str | Unset = UNSET
        if not isinstance(self.application_id, Unset):
            application_id = str(self.application_id)

        azure_environment: str | Unset = UNSET
        if not isinstance(self.azure_environment, Unset):
            azure_environment = self.azure_environment.value

        azure_tenant_id = self.azure_tenant_id

        application_certificate = self.application_certificate

        application_certificate_password = self.application_certificate_password

        application_secret = self.application_secret

        user_code = self.user_code

        subscription_ids: list[str] | Unset = UNSET
        if not isinstance(self.subscription_ids, Unset):
            subscription_ids = self.subscription_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if description is not UNSET:
            field_dict["description"] = description
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if azure_environment is not UNSET:
            field_dict["azureEnvironment"] = azure_environment
        if azure_tenant_id is not UNSET:
            field_dict["azureTenantId"] = azure_tenant_id
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if application_secret is not UNSET:
            field_dict["applicationSecret"] = application_secret
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if subscription_ids is not UNSET:
            field_dict["subscriptionIds"] = subscription_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_name = d.pop("applicationName", UNSET)

        description = d.pop("description", UNSET)

        _application_id = d.pop("applicationId", UNSET)
        application_id: UUID | Unset
        if isinstance(_application_id, Unset):
            application_id = UNSET
        else:
            application_id = UUID(_application_id)

        _azure_environment = d.pop("azureEnvironment", UNSET)
        azure_environment: AzureStorageEndpoint | Unset
        if isinstance(_azure_environment, Unset):
            azure_environment = UNSET
        else:
            azure_environment = AzureStorageEndpoint(_azure_environment)

        azure_tenant_id = d.pop("azureTenantId", UNSET)

        application_certificate = d.pop("applicationCertificate", UNSET)

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        application_secret = d.pop("applicationSecret", UNSET)

        user_code = d.pop("userCode", UNSET)

        subscription_ids = cast(list[str], d.pop("subscriptionIds", UNSET))

        rest_service_account_creation_data = cls(
            application_name=application_name,
            description=description,
            application_id=application_id,
            azure_environment=azure_environment,
            azure_tenant_id=azure_tenant_id,
            application_certificate=application_certificate,
            application_certificate_password=application_certificate_password,
            application_secret=application_secret,
            user_code=user_code,
            subscription_ids=subscription_ids,
        )

        rest_service_account_creation_data.additional_properties = d
        return rest_service_account_creation_data

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
