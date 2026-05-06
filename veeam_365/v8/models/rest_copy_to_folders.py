from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_copy_to_folders_document_last_version_action import RESTCopyToFoldersDocumentLastVersionAction
from ..models.rest_copy_to_folders_document_version import RESTCopyToFoldersDocumentVersion
from ..models.rest_copy_to_folders_office_region import RESTCopyToFoldersOfficeRegion
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_one_drive import RESTOneDrive
  from ..models.rest_one_drive_folder import RESTOneDriveFolder





T = TypeVar("T", bound="RESTCopyToFolders")



@_attrs_define
class RESTCopyToFolders:
    """ 
        Attributes:
            folders (list[RESTOneDriveFolder] | Unset): Specifies IDs of the OneDrive folders that you want to copy. For
                more information on how to get such IDs, see [Get OneDrive Folders](#/OneDriveFolder/OneDriveFolder_Get).
            changed_items (bool | None | Unset): Defines whether all versions of OneDrive items will be copied.
            deleted_items (bool | None | Unset): Defines whether the deleted OneDrive items will be copied.
            restore_permissions (bool | Unset): Defines whether the OneDrive items will be copied with all permissions.
            send_shared_links_notification (bool | None | Unset): Defines whether the shared links notifications will be
                sent.
            onedrive (RESTOneDrive | Unset):
            folder (str | Unset): Specifies the target folder for the copied OneDrive folders.
            document_version (RESTCopyToFoldersDocumentVersion | Unset): Specifies what version of the OneDrive documents
                will be copied.
            document_last_version_action (RESTCopyToFoldersDocumentLastVersionAction | Unset): Specifies the action that
                will be performed with the last version of the copied OneDrive document on the destination server.
            user_code (str | Unset): Specifies the authentication code. For more information on how to get a device code,
                see [Get Device Code](#/RestoreSession/RestoreSession_DeviceCodeAction).
                This property is required if you want to use a device code for data restore.
            application_id (None | Unset | UUID): Specifies the ID of the Microsoft Entra application that you want to use
                for restore. Example: 00000000-0000-0000-0000-000000000000.
            application_certificate_password (str | Unset): Specifies a password.
            application_certificate (str | Unset): Specifies the TLS certificate configured for the Microsoft Entra
                application that you want to use for data restore. You must provide the certificate as a Base64 string.
            user_name (str | Unset): Specifies the user name that you want to use for authenticating to the organization.
            user_password (str | Unset): Specifies a password.
            office_region (RESTCopyToFoldersOfficeRegion | Unset): Specifies the region of the target Microsoft 365
                organization.
            organization_name (str | Unset): Specifies the name of the target Microsoft 365 organization.
     """

    folders: list[RESTOneDriveFolder] | Unset = UNSET
    changed_items: bool | None | Unset = UNSET
    deleted_items: bool | None | Unset = UNSET
    restore_permissions: bool | Unset = UNSET
    send_shared_links_notification: bool | None | Unset = UNSET
    onedrive: RESTOneDrive | Unset = UNSET
    folder: str | Unset = UNSET
    document_version: RESTCopyToFoldersDocumentVersion | Unset = UNSET
    document_last_version_action: RESTCopyToFoldersDocumentLastVersionAction | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    office_region: RESTCopyToFoldersOfficeRegion | Unset = UNSET
    organization_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_one_drive import RESTOneDrive
        from ..models.rest_one_drive_folder import RESTOneDriveFolder
        folders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()
                folders.append(folders_item)



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

        restore_permissions = self.restore_permissions

        send_shared_links_notification: bool | None | Unset
        if isinstance(self.send_shared_links_notification, Unset):
            send_shared_links_notification = UNSET
        else:
            send_shared_links_notification = self.send_shared_links_notification

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
        field_dict.update({
        })
        if folders is not UNSET:
            field_dict["folders"] = folders
        if changed_items is not UNSET:
            field_dict["changedItems"] = changed_items
        if deleted_items is not UNSET:
            field_dict["deletedItems"] = deleted_items
        if restore_permissions is not UNSET:
            field_dict["restorePermissions"] = restore_permissions
        if send_shared_links_notification is not UNSET:
            field_dict["sendSharedLinksNotification"] = send_shared_links_notification
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
        from ..models.rest_one_drive_folder import RESTOneDriveFolder
        d = dict(src_dict)
        _folders = d.pop("folders", UNSET)
        folders: list[RESTOneDriveFolder] | Unset = UNSET
        if _folders is not UNSET:
            folders = []
            for folders_item_data in _folders:
                folders_item = RESTOneDriveFolder.from_dict(folders_item_data)



                folders.append(folders_item)


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


        restore_permissions = d.pop("restorePermissions", UNSET)

        def _parse_send_shared_links_notification(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        send_shared_links_notification = _parse_send_shared_links_notification(d.pop("sendSharedLinksNotification", UNSET))


        _onedrive = d.pop("onedrive", UNSET)
        onedrive: RESTOneDrive | Unset
        if isinstance(_onedrive,  Unset):
            onedrive = UNSET
        else:
            onedrive = RESTOneDrive.from_dict(_onedrive)




        folder = d.pop("folder", UNSET)

        _document_version = d.pop("documentVersion", UNSET)
        document_version: RESTCopyToFoldersDocumentVersion | Unset
        if isinstance(_document_version,  Unset):
            document_version = UNSET
        else:
            document_version = RESTCopyToFoldersDocumentVersion(_document_version)




        _document_last_version_action = d.pop("documentLastVersionAction", UNSET)
        document_last_version_action: RESTCopyToFoldersDocumentLastVersionAction | Unset
        if isinstance(_document_last_version_action,  Unset):
            document_last_version_action = UNSET
        else:
            document_last_version_action = RESTCopyToFoldersDocumentLastVersionAction(_document_last_version_action)




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
        office_region: RESTCopyToFoldersOfficeRegion | Unset
        if isinstance(_office_region,  Unset):
            office_region = UNSET
        else:
            office_region = RESTCopyToFoldersOfficeRegion(_office_region)




        organization_name = d.pop("organizationName", UNSET)

        rest_copy_to_folders = cls(
            folders=folders,
            changed_items=changed_items,
            deleted_items=deleted_items,
            restore_permissions=restore_permissions,
            send_shared_links_notification=send_shared_links_notification,
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


        rest_copy_to_folders.additional_properties = d
        return rest_copy_to_folders

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
