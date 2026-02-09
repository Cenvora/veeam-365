from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_restore_to_original_documents_document_action import RESTRestoreToOriginalDocumentsDocumentAction
from ..models.rest_restore_to_original_documents_office_region import RESTRestoreToOriginalDocumentsOfficeRegion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_one_drive_document import RESTOneDriveDocument


T = TypeVar("T", bound="RESTRestoreToOriginalDocuments")


@_attrs_define
class RESTRestoreToOriginalDocuments:
    """
    Attributes:
        documents (list[RESTOneDriveDocument] | Unset): Specifies IDs of the OneDrive documents that you want to
            restore. For more information on how to get such IDs, see [Get OneDrive
            Documents](OneDriveDocument#operation/OneDriveDocument_Get).
        document_action (RESTRestoreToOriginalDocumentsDocumentAction | Unset): Specifies the action that will be
            performed in case the restore destination contains the restored documents.
        user_code (str | Unset): Specifies the authentication code. For more information on how to get a device code,
            see [Get Device Code](RestoreSession#operation/RestoreSession_DeviceCodeAction).
            This property is required if you want to use a device code for data restore.
        application_id (None | Unset | UUID): Specifies the ID of the Microsoft Entra application that you want to use
            for restore. Example: 00000000-0000-0000-0000-000000000000.
        application_certificate_password (str | Unset): Specifies a password.
        application_certificate (str | Unset): Specifies the SSL certificate configured for the Microsoft Entra
            application that you want to use for data restore. You must provide the certificate as a Base64 string.
        user_name (str | Unset): Specifies the user name that you want to use for authenticating to the organization.
        user_password (str | Unset): Specifies a password.
        office_region (RESTRestoreToOriginalDocumentsOfficeRegion | Unset): Specifies the region of the target Microsoft
            365 organization.
        organization_name (str | Unset): Specifies the name of the target Microsoft 365 organization.
    """

    documents: list[RESTOneDriveDocument] | Unset = UNSET
    document_action: RESTRestoreToOriginalDocumentsDocumentAction | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    office_region: RESTRestoreToOriginalDocumentsOfficeRegion | Unset = UNSET
    organization_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        document_action: str | Unset = UNSET
        if not isinstance(self.document_action, Unset):
            document_action = self.document_action.value

        user_code = self.user_code

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        elif isinstance(self.application_id, UUID):
            application_id = str(self.application_id)
        else:
            application_id = self.application_id

        application_certificate_password = self.application_certificate_password

        application_certificate = self.application_certificate

        user_name = self.user_name

        user_password = self.user_password

        office_region: str | Unset = UNSET
        if not isinstance(self.office_region, Unset):
            office_region = self.office_region.value

        organization_name = self.organization_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if documents is not UNSET:
            field_dict["documents"] = documents
        if document_action is not UNSET:
            field_dict["documentAction"] = document_action
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_password is not UNSET:
            field_dict["userPassword"] = user_password
        if office_region is not UNSET:
            field_dict["officeRegion"] = office_region
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_one_drive_document import RESTOneDriveDocument

        d = dict(src_dict)
        _documents = d.pop("documents", UNSET)
        documents: list[RESTOneDriveDocument] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = RESTOneDriveDocument.from_dict(documents_item_data)

                documents.append(documents_item)

        _document_action = d.pop("documentAction", UNSET)
        document_action: RESTRestoreToOriginalDocumentsDocumentAction | Unset
        if isinstance(_document_action, Unset):
            document_action = UNSET
        else:
            document_action = RESTRestoreToOriginalDocumentsDocumentAction(_document_action)

        user_code = d.pop("userCode", UNSET)

        def _parse_application_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_id_type_0 = UUID(data)

                return application_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        application_id = _parse_application_id(d.pop("applicationId", UNSET))

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        application_certificate = d.pop("applicationCertificate", UNSET)

        user_name = d.pop("userName", UNSET)

        user_password = d.pop("userPassword", UNSET)

        _office_region = d.pop("officeRegion", UNSET)
        office_region: RESTRestoreToOriginalDocumentsOfficeRegion | Unset
        if isinstance(_office_region, Unset):
            office_region = UNSET
        else:
            office_region = RESTRestoreToOriginalDocumentsOfficeRegion(_office_region)

        organization_name = d.pop("organizationName", UNSET)

        rest_restore_to_original_documents = cls(
            documents=documents,
            document_action=document_action,
            user_code=user_code,
            application_id=application_id,
            application_certificate_password=application_certificate_password,
            application_certificate=application_certificate,
            user_name=user_name,
            user_password=user_password,
            office_region=office_region,
            organization_name=organization_name,
        )

        rest_restore_to_original_documents.additional_properties = d
        return rest_restore_to_original_documents

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
