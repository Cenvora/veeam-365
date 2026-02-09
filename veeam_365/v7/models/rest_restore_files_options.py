from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_restore_files_options_file_version import RESTRestoreFilesOptionsFileVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_teams_file import RESTTeamsFile


T = TypeVar("T", bound="RESTRestoreFilesOptions")


@_attrs_define
class RESTRestoreFilesOptions:
    """
    Attributes:
        restore_changed_items (bool | None): Defines whether to restore files that have been modified in the original
            location since the time when the backup was created.
        restore_missing_items (bool | None): Defines whether to restore files that are missed in the original location.
        file_version (RESTRestoreFilesOptionsFileVersion): Specifies what version of files will be restored.
        channel_id (str | Unset): Specifies the ID of the channel whose files you want to restore. Veeam Explorer for
            Microsoft Teams will restore all files of this channel. For more information on how to get this parameter, see
            [Get Team Channels](#tag/TeamsChannel/operation/TeamsChannel_Get).

            **Note**: You do not need to use this property if you use the `files` property to specify what files to restore.
        files (list[RESTTeamsFile] | Unset): Specifies IDs of files that you want to restore. The files must reside in
            the same channel. For more information on how to get such IDs, see [Get
            Files](#tag/TeamsFile/operation/TeamsFile_GetPage).

            **Note**: You do not need to use this property if you use the `channelId` property to specify a channel whose
            files to restore.
        user_code (str | Unset): Specifies the authentication code. For more information on how to get a device code,
            see [Get Device Code](#tag/RestoreSession/operation/RestoreSession_DeviceCodeAction).
            This property is required if you want to use a device code for data restore.
        application_id (None | Unset | UUID): Specifies the ID of the Azure AD application that you want to use for
            restore. Example: 00000000-0000-0000-0000-000000000000.
        application_certificate (str | Unset): Specifies the SSL certificate configured for the Azure AD application
            that you want to use for data restore. You must provide the certificate as a Base64 string.
        application_certificate_password (str | Unset): Specifies a password.
        user_name (str | Unset): Specifies the user name that you want to use for authenticating to the organization.
        user_password (str | Unset): Specifies a password.
    """

    restore_changed_items: bool | None
    restore_missing_items: bool | None
    file_version: RESTRestoreFilesOptionsFileVersion
    channel_id: str | Unset = UNSET
    files: list[RESTTeamsFile] | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate: str | Unset = UNSET
    application_certificate_password: str | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_changed_items: bool | None
        restore_changed_items = self.restore_changed_items

        restore_missing_items: bool | None
        restore_missing_items = self.restore_missing_items

        file_version = self.file_version.value

        channel_id = self.channel_id

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        user_code = self.user_code

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        elif isinstance(self.application_id, UUID):
            application_id = str(self.application_id)
        else:
            application_id = self.application_id

        application_certificate = self.application_certificate

        application_certificate_password = self.application_certificate_password

        user_name = self.user_name

        user_password = self.user_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restoreChangedItems": restore_changed_items,
                "restoreMissingItems": restore_missing_items,
                "fileVersion": file_version,
            }
        )
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if files is not UNSET:
            field_dict["files"] = files
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_password is not UNSET:
            field_dict["userPassword"] = user_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_file import RESTTeamsFile

        d = dict(src_dict)

        def _parse_restore_changed_items(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        restore_changed_items = _parse_restore_changed_items(d.pop("restoreChangedItems"))

        def _parse_restore_missing_items(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        restore_missing_items = _parse_restore_missing_items(d.pop("restoreMissingItems"))

        file_version = RESTRestoreFilesOptionsFileVersion(d.pop("fileVersion"))

        channel_id = d.pop("channelId", UNSET)

        _files = d.pop("files", UNSET)
        files: list[RESTTeamsFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = RESTTeamsFile.from_dict(files_item_data)

                files.append(files_item)

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

        application_certificate = d.pop("applicationCertificate", UNSET)

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        user_name = d.pop("userName", UNSET)

        user_password = d.pop("userPassword", UNSET)

        rest_restore_files_options = cls(
            restore_changed_items=restore_changed_items,
            restore_missing_items=restore_missing_items,
            file_version=file_version,
            channel_id=channel_id,
            files=files,
            user_code=user_code,
            application_id=application_id,
            application_certificate=application_certificate,
            application_certificate_password=application_certificate_password,
            user_name=user_name,
            user_password=user_password,
        )

        rest_restore_files_options.additional_properties = d
        return rest_restore_files_options

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
