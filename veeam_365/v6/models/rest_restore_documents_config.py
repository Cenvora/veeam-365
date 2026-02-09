from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_restore_documents_config_document_last_version_action import (
    RESTRestoreDocumentsConfigDocumentLastVersionAction,
)
from ..models.rest_restore_documents_config_document_version import RESTRestoreDocumentsConfigDocumentVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_share_point_document import RESTSharePointDocument


T = TypeVar("T", bound="RESTRestoreDocumentsConfig")


@_attrs_define
class RESTRestoreDocumentsConfig:
    """
    Attributes:
        documents (list[RESTSharePointDocument] | Unset):
        list_ (str | Unset):
        restore_permissions (bool | None | Unset):
        send_shared_links_notification (bool | None | Unset):
        document_version (RESTRestoreDocumentsConfigDocumentVersion | Unset):
        document_last_version_action (RESTRestoreDocumentsConfigDocumentLastVersionAction | Unset):
        user_code (str | Unset):
        application_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        application_certificate_password (str | Unset):
        application_certificate (str | Unset):
        user_name (str | Unset):
        user_password (str | Unset):
    """

    documents: list[RESTSharePointDocument] | Unset = UNSET
    list_: str | Unset = UNSET
    restore_permissions: bool | None | Unset = UNSET
    send_shared_links_notification: bool | None | Unset = UNSET
    document_version: RESTRestoreDocumentsConfigDocumentVersion | Unset = UNSET
    document_last_version_action: RESTRestoreDocumentsConfigDocumentLastVersionAction | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        list_ = self.list_

        restore_permissions: bool | None | Unset
        if isinstance(self.restore_permissions, Unset):
            restore_permissions = UNSET
        else:
            restore_permissions = self.restore_permissions

        send_shared_links_notification: bool | None | Unset
        if isinstance(self.send_shared_links_notification, Unset):
            send_shared_links_notification = UNSET
        else:
            send_shared_links_notification = self.send_shared_links_notification

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if documents is not UNSET:
            field_dict["documents"] = documents
        if list_ is not UNSET:
            field_dict["list"] = list_
        if restore_permissions is not UNSET:
            field_dict["restorePermissions"] = restore_permissions
        if send_shared_links_notification is not UNSET:
            field_dict["sendSharedLinksNotification"] = send_shared_links_notification
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_share_point_document import RESTSharePointDocument

        d = dict(src_dict)
        _documents = d.pop("documents", UNSET)
        documents: list[RESTSharePointDocument] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = RESTSharePointDocument.from_dict(documents_item_data)

                documents.append(documents_item)

        list_ = d.pop("list", UNSET)

        def _parse_restore_permissions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restore_permissions = _parse_restore_permissions(d.pop("restorePermissions", UNSET))

        def _parse_send_shared_links_notification(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        send_shared_links_notification = _parse_send_shared_links_notification(
            d.pop("sendSharedLinksNotification", UNSET)
        )

        _document_version = d.pop("documentVersion", UNSET)
        document_version: RESTRestoreDocumentsConfigDocumentVersion | Unset
        if isinstance(_document_version, Unset):
            document_version = UNSET
        else:
            document_version = RESTRestoreDocumentsConfigDocumentVersion(_document_version)

        _document_last_version_action = d.pop("documentLastVersionAction", UNSET)
        document_last_version_action: RESTRestoreDocumentsConfigDocumentLastVersionAction | Unset
        if isinstance(_document_last_version_action, Unset):
            document_last_version_action = UNSET
        else:
            document_last_version_action = RESTRestoreDocumentsConfigDocumentLastVersionAction(
                _document_last_version_action
            )

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

        rest_restore_documents_config = cls(
            documents=documents,
            list_=list_,
            restore_permissions=restore_permissions,
            send_shared_links_notification=send_shared_links_notification,
            document_version=document_version,
            document_last_version_action=document_last_version_action,
            user_code=user_code,
            application_id=application_id,
            application_certificate_password=application_certificate_password,
            application_certificate=application_certificate,
            user_name=user_name,
            user_password=user_password,
        )

        rest_restore_documents_config.additional_properties = d
        return rest_restore_documents_config

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
