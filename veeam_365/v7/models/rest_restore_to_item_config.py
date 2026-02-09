from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_restore_to_item_config_document_last_version_action import (
    RESTRestoreToItemConfigDocumentLastVersionAction,
)
from ..models.rest_restore_to_item_config_document_version import RESTRestoreToItemConfigDocumentVersion
from ..models.rest_restore_to_item_config_office_region import RESTRestoreToItemConfigOfficeRegion
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTRestoreToItemConfig")


@_attrs_define
class RESTRestoreToItemConfig:
    """
    Attributes:
        list_ (str | Unset): Specifies the target SharePoint list.
        send_shared_links_notification (bool | None | Unset): Defines whether the shared links notifications will be
            sent.
        document_version (RESTRestoreToItemConfigDocumentVersion | Unset): Specifies what version of the SharePoint
            document/item will be restored. To restore a SharePoint document version, specify *Last* as a value for this
            property.
        document_last_version_action (RESTRestoreToItemConfigDocumentLastVersionAction | Unset): Specifies the action
            that will be performed with the last version of the restored SharePoint document on the destination server.
        site_url (str | Unset): Specifies the URL of the target SharePoint site.
        user_code (str | Unset): Specifies the authentication code. For more information on how to get a device code,
            see [Get Device Code](#tag/RestoreSession/operation/RestoreSession_DeviceCodeAction).
            This property is required if you want to use a device code for data restore.
        application_id (None | Unset | UUID): Specifies the ID of the Azure AD application that you want to use for
            restore. Example: 00000000-0000-0000-0000-000000000000.
        application_certificate_password (str | Unset): Specifies a password.
        application_certificate (str | Unset): Specifies the SSL certificate configured for the Azure AD application
            that you want to use for data restore. You must provide the certificate as a Base64 string.
        user_name (str | Unset): Specifies the user name that you want to use for authenticating to the organization.
        user_password (str | Unset): Specifies a password.
        office_region (RESTRestoreToItemConfigOfficeRegion | Unset): Specifies the region of the target Microsoft 365
            organization.
        organization_name (str | Unset): Specifies the name of the target Microsoft 365 organization.
    """

    list_: str | Unset = UNSET
    send_shared_links_notification: bool | None | Unset = UNSET
    document_version: RESTRestoreToItemConfigDocumentVersion | Unset = UNSET
    document_last_version_action: RESTRestoreToItemConfigDocumentLastVersionAction | Unset = UNSET
    site_url: str | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    office_region: RESTRestoreToItemConfigOfficeRegion | Unset = UNSET
    organization_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_ = self.list_

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

        site_url = self.site_url

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
        if list_ is not UNSET:
            field_dict["list"] = list_
        if send_shared_links_notification is not UNSET:
            field_dict["sendSharedLinksNotification"] = send_shared_links_notification
        if document_version is not UNSET:
            field_dict["documentVersion"] = document_version
        if document_last_version_action is not UNSET:
            field_dict["documentLastVersionAction"] = document_last_version_action
        if site_url is not UNSET:
            field_dict["siteURL"] = site_url
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
        d = dict(src_dict)
        list_ = d.pop("list", UNSET)

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
        document_version: RESTRestoreToItemConfigDocumentVersion | Unset
        if isinstance(_document_version, Unset):
            document_version = UNSET
        else:
            document_version = RESTRestoreToItemConfigDocumentVersion(_document_version)

        _document_last_version_action = d.pop("documentLastVersionAction", UNSET)
        document_last_version_action: RESTRestoreToItemConfigDocumentLastVersionAction | Unset
        if isinstance(_document_last_version_action, Unset):
            document_last_version_action = UNSET
        else:
            document_last_version_action = RESTRestoreToItemConfigDocumentLastVersionAction(
                _document_last_version_action
            )

        site_url = d.pop("siteURL", UNSET)

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
        office_region: RESTRestoreToItemConfigOfficeRegion | Unset
        if isinstance(_office_region, Unset):
            office_region = UNSET
        else:
            office_region = RESTRestoreToItemConfigOfficeRegion(_office_region)

        organization_name = d.pop("organizationName", UNSET)

        rest_restore_to_item_config = cls(
            list_=list_,
            send_shared_links_notification=send_shared_links_notification,
            document_version=document_version,
            document_last_version_action=document_last_version_action,
            site_url=site_url,
            user_code=user_code,
            application_id=application_id,
            application_certificate_password=application_certificate_password,
            application_certificate=application_certificate,
            user_name=user_name,
            user_password=user_password,
            office_region=office_region,
            organization_name=organization_name,
        )

        rest_restore_to_item_config.additional_properties = d
        return rest_restore_to_item_config

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
