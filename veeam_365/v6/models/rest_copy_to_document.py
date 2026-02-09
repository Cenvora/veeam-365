from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_copy_to_document_document_last_version_action import RESTCopyToDocumentDocumentLastVersionAction
from ..models.rest_copy_to_document_document_version import RESTCopyToDocumentDocumentVersion
from ..models.rest_copy_to_document_office_region import RESTCopyToDocumentOfficeRegion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_one_drive import RESTOneDrive


T = TypeVar("T", bound="RESTCopyToDocument")


@_attrs_define
class RESTCopyToDocument:
    """
    Attributes:
        onedrive (RESTOneDrive | Unset):
        folder (str | Unset):
        document_version (RESTCopyToDocumentDocumentVersion | Unset):
        document_last_version_action (RESTCopyToDocumentDocumentLastVersionAction | Unset):
        user_code (str | Unset):
        application_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        application_certificate_password (str | Unset):
        application_certificate (str | Unset):
        user_name (str | Unset):
        user_password (str | Unset):
        office_region (RESTCopyToDocumentOfficeRegion | Unset):
        organization_name (str | Unset):
    """

    onedrive: RESTOneDrive | Unset = UNSET
    folder: str | Unset = UNSET
    document_version: RESTCopyToDocumentDocumentVersion | Unset = UNSET
    document_last_version_action: RESTCopyToDocumentDocumentLastVersionAction | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    office_region: RESTCopyToDocumentOfficeRegion | Unset = UNSET
    organization_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        onedrive: dict[str, Any] | Unset = UNSET
        if not isinstance(self.onedrive, Unset):
            onedrive = self.onedrive.to_dict()

        folder = self.folder

        document_version: str | Unset = UNSET
        if not isinstance(self.document_version, Unset):
            document_version = self.document_version.value

        document_last_version_action: str | Unset = UNSET
        if not isinstance(self.document_last_version_action, Unset):
            document_last_version_action = self.document_last_version_action.value

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
        if onedrive is not UNSET:
            field_dict["onedrive"] = onedrive
        if folder is not UNSET:
            field_dict["folder"] = folder
        if document_version is not UNSET:
            field_dict["documentVersion"] = document_version
        if document_last_version_action is not UNSET:
            field_dict["documentLastVersionAction"] = document_last_version_action
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
        from ..models.rest_one_drive import RESTOneDrive

        d = dict(src_dict)
        _onedrive = d.pop("onedrive", UNSET)
        onedrive: RESTOneDrive | Unset
        if isinstance(_onedrive, Unset):
            onedrive = UNSET
        else:
            onedrive = RESTOneDrive.from_dict(_onedrive)

        folder = d.pop("folder", UNSET)

        _document_version = d.pop("documentVersion", UNSET)
        document_version: RESTCopyToDocumentDocumentVersion | Unset
        if isinstance(_document_version, Unset):
            document_version = UNSET
        else:
            document_version = RESTCopyToDocumentDocumentVersion(_document_version)

        _document_last_version_action = d.pop("documentLastVersionAction", UNSET)
        document_last_version_action: RESTCopyToDocumentDocumentLastVersionAction | Unset
        if isinstance(_document_last_version_action, Unset):
            document_last_version_action = UNSET
        else:
            document_last_version_action = RESTCopyToDocumentDocumentLastVersionAction(_document_last_version_action)

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
        office_region: RESTCopyToDocumentOfficeRegion | Unset
        if isinstance(_office_region, Unset):
            office_region = UNSET
        else:
            office_region = RESTCopyToDocumentOfficeRegion(_office_region)

        organization_name = d.pop("organizationName", UNSET)

        rest_copy_to_document = cls(
            onedrive=onedrive,
            folder=folder,
            document_version=document_version,
            document_last_version_action=document_last_version_action,
            user_code=user_code,
            application_id=application_id,
            application_certificate_password=application_certificate_password,
            application_certificate=application_certificate,
            user_name=user_name,
            user_password=user_password,
            office_region=office_region,
            organization_name=organization_name,
        )

        rest_copy_to_document.additional_properties = d
        return rest_copy_to_document

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
