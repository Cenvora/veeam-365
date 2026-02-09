from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_restore_site_config_document_last_version_action import (
    RESTRestoreSiteConfigDocumentLastVersionAction,
)
from ..models.rest_restore_site_config_document_version import RESTRestoreSiteConfigDocumentVersion
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTRestoreSiteConfig")


@_attrs_define
class RESTRestoreSiteConfig:
    """
    Attributes:
        impersonation_account_name (str | Unset): Specifies a user name of the account that will be used as a SharePoint
            site owner account to restore a SharePoint site.

            **Note**: This property is required if you want to use an application certificate for data restore. Use this
            property only with the `applicationCertificate` property.
        alias (str | Unset): Specifies an alias for the target SharePoint site. If you omit this property, the
            SharePoint site items will be restored to the original location.
        restore_list_views (bool | None | Unset): Defines whether the SharePoint lists will be restored with all list
            views.
        changed_items (bool | None | Unset): Defines whether the SharePoint site will be restored with all modified
            items.
        deleted_items (bool | None | Unset): Defines whether the SharePoint site will be restored with all deleted
            items.
        restore_subsites (bool | None | Unset): Defines whether the SharePoint site will be restored with all subsites.
        restore_master_pages (bool | None | Unset): Defines whether the SharePoint site will be restored with all master
            pages.
        restore_permissions (bool | Unset): Defines whether the SharePoint site will be restored with all permissions.
        send_shared_links_notification (bool | None | Unset): Defines whether the shared links notifications will be
            sent.
        document_version (RESTRestoreSiteConfigDocumentVersion | Unset): Specifies what version of the SharePoint
            documents will be restored.
        document_last_version_action (RESTRestoreSiteConfigDocumentLastVersionAction | Unset): Specifies the action that
            will be performed with the last version of the restored SharePoint document on the destination server.
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
    """

    impersonation_account_name: str | Unset = UNSET
    alias: str | Unset = UNSET
    restore_list_views: bool | None | Unset = UNSET
    changed_items: bool | None | Unset = UNSET
    deleted_items: bool | None | Unset = UNSET
    restore_subsites: bool | None | Unset = UNSET
    restore_master_pages: bool | None | Unset = UNSET
    restore_permissions: bool | Unset = UNSET
    send_shared_links_notification: bool | None | Unset = UNSET
    document_version: RESTRestoreSiteConfigDocumentVersion | Unset = UNSET
    document_last_version_action: RESTRestoreSiteConfigDocumentLastVersionAction | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        impersonation_account_name = self.impersonation_account_name

        alias = self.alias

        restore_list_views: bool | None | Unset
        if isinstance(self.restore_list_views, Unset):
            restore_list_views = UNSET
        else:
            restore_list_views = self.restore_list_views

        changed_items: bool | None | Unset
        if isinstance(self.changed_items, Unset):
            changed_items = UNSET
        else:
            changed_items = self.changed_items

        deleted_items: bool | None | Unset
        if isinstance(self.deleted_items, Unset):
            deleted_items = UNSET
        else:
            deleted_items = self.deleted_items

        restore_subsites: bool | None | Unset
        if isinstance(self.restore_subsites, Unset):
            restore_subsites = UNSET
        else:
            restore_subsites = self.restore_subsites

        restore_master_pages: bool | None | Unset
        if isinstance(self.restore_master_pages, Unset):
            restore_master_pages = UNSET
        else:
            restore_master_pages = self.restore_master_pages

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
        if impersonation_account_name is not UNSET:
            field_dict["impersonationAccountName"] = impersonation_account_name
        if alias is not UNSET:
            field_dict["alias"] = alias
        if restore_list_views is not UNSET:
            field_dict["restoreListViews"] = restore_list_views
        if changed_items is not UNSET:
            field_dict["changedItems"] = changed_items
        if deleted_items is not UNSET:
            field_dict["deletedItems"] = deleted_items
        if restore_subsites is not UNSET:
            field_dict["restoreSubsites"] = restore_subsites
        if restore_master_pages is not UNSET:
            field_dict["restoreMasterPages"] = restore_master_pages
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
        d = dict(src_dict)
        impersonation_account_name = d.pop("impersonationAccountName", UNSET)

        alias = d.pop("alias", UNSET)

        def _parse_restore_list_views(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restore_list_views = _parse_restore_list_views(d.pop("restoreListViews", UNSET))

        def _parse_changed_items(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        changed_items = _parse_changed_items(d.pop("changedItems", UNSET))

        def _parse_deleted_items(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deleted_items = _parse_deleted_items(d.pop("deletedItems", UNSET))

        def _parse_restore_subsites(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restore_subsites = _parse_restore_subsites(d.pop("restoreSubsites", UNSET))

        def _parse_restore_master_pages(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restore_master_pages = _parse_restore_master_pages(d.pop("restoreMasterPages", UNSET))

        restore_permissions = d.pop("restorePermissions", UNSET)

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
        document_version: RESTRestoreSiteConfigDocumentVersion | Unset
        if isinstance(_document_version, Unset):
            document_version = UNSET
        else:
            document_version = RESTRestoreSiteConfigDocumentVersion(_document_version)

        _document_last_version_action = d.pop("documentLastVersionAction", UNSET)
        document_last_version_action: RESTRestoreSiteConfigDocumentLastVersionAction | Unset
        if isinstance(_document_last_version_action, Unset):
            document_last_version_action = UNSET
        else:
            document_last_version_action = RESTRestoreSiteConfigDocumentLastVersionAction(_document_last_version_action)

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

        rest_restore_site_config = cls(
            impersonation_account_name=impersonation_account_name,
            alias=alias,
            restore_list_views=restore_list_views,
            changed_items=changed_items,
            deleted_items=deleted_items,
            restore_subsites=restore_subsites,
            restore_master_pages=restore_master_pages,
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

        rest_restore_site_config.additional_properties = d
        return rest_restore_site_config

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
