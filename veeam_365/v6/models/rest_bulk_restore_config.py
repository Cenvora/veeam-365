from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_bulk_restore_config_document_action import RESTBulkRestoreConfigDocumentAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_one_drive import RESTOneDrive


T = TypeVar("T", bound="RESTBulkRestoreConfig")


@_attrs_define
class RESTBulkRestoreConfig:
    """
    Attributes:
        document_action (RESTBulkRestoreConfigDocumentAction | Unset):
        skip_unresolved (bool | None | Unset):
        one_drives (list[RESTOneDrive] | Unset):
        office_username (str | Unset):
        user_code (str | Unset):
        application_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        application_certificate_password (str | Unset):
        application_certificate (str | Unset):
        office_userpassword (str | Unset):
        onpremises_username (str | Unset):
        onpremises_userpassword (str | Unset):
    """

    document_action: RESTBulkRestoreConfigDocumentAction | Unset = UNSET
    skip_unresolved: bool | None | Unset = UNSET
    one_drives: list[RESTOneDrive] | Unset = UNSET
    office_username: str | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    office_userpassword: str | Unset = UNSET
    onpremises_username: str | Unset = UNSET
    onpremises_userpassword: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_action: str | Unset = UNSET
        if not isinstance(self.document_action, Unset):
            document_action = self.document_action.value

        skip_unresolved: bool | None | Unset
        if isinstance(self.skip_unresolved, Unset):
            skip_unresolved = UNSET
        else:
            skip_unresolved = self.skip_unresolved

        one_drives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.one_drives, Unset):
            one_drives = []
            for one_drives_item_data in self.one_drives:
                one_drives_item = one_drives_item_data.to_dict()
                one_drives.append(one_drives_item)

        office_username = self.office_username

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

        office_userpassword = self.office_userpassword

        onpremises_username = self.onpremises_username

        onpremises_userpassword = self.onpremises_userpassword

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_action is not UNSET:
            field_dict["documentAction"] = document_action
        if skip_unresolved is not UNSET:
            field_dict["skipUnresolved"] = skip_unresolved
        if one_drives is not UNSET:
            field_dict["oneDrives"] = one_drives
        if office_username is not UNSET:
            field_dict["officeUsername"] = office_username
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if office_userpassword is not UNSET:
            field_dict["officeUserpassword"] = office_userpassword
        if onpremises_username is not UNSET:
            field_dict["onpremisesUsername"] = onpremises_username
        if onpremises_userpassword is not UNSET:
            field_dict["onpremisesUserpassword"] = onpremises_userpassword

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_one_drive import RESTOneDrive

        d = dict(src_dict)
        _document_action = d.pop("documentAction", UNSET)
        document_action: RESTBulkRestoreConfigDocumentAction | Unset
        if isinstance(_document_action, Unset):
            document_action = UNSET
        else:
            document_action = RESTBulkRestoreConfigDocumentAction(_document_action)

        def _parse_skip_unresolved(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_unresolved = _parse_skip_unresolved(d.pop("skipUnresolved", UNSET))

        _one_drives = d.pop("oneDrives", UNSET)
        one_drives: list[RESTOneDrive] | Unset = UNSET
        if _one_drives is not UNSET:
            one_drives = []
            for one_drives_item_data in _one_drives:
                one_drives_item = RESTOneDrive.from_dict(one_drives_item_data)

                one_drives.append(one_drives_item)

        office_username = d.pop("officeUsername", UNSET)

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

        office_userpassword = d.pop("officeUserpassword", UNSET)

        onpremises_username = d.pop("onpremisesUsername", UNSET)

        onpremises_userpassword = d.pop("onpremisesUserpassword", UNSET)

        rest_bulk_restore_config = cls(
            document_action=document_action,
            skip_unresolved=skip_unresolved,
            one_drives=one_drives,
            office_username=office_username,
            user_code=user_code,
            application_id=application_id,
            application_certificate_password=application_certificate_password,
            application_certificate=application_certificate,
            office_userpassword=office_userpassword,
            onpremises_username=onpremises_username,
            onpremises_userpassword=onpremises_userpassword,
        )

        rest_bulk_restore_config.additional_properties = d
        return rest_bulk_restore_config

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
