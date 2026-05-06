from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_share_point_folder import RESTSharePointFolder





T = TypeVar("T", bound="RESTSharePointSendFoldersAsMsgOptions")



@_attrs_define
class RESTSharePointSendFoldersAsMsgOptions:
    """ 
        Attributes:
            skip_item_checks (bool | Unset): Defines whether Veeam Backup for Microsoft 365 does not check items and skips
                those items that cannot be sent.
            folders (list[RESTSharePointFolder] | Unset): Specifies IDs of the SharePoint folders that you want to send. For
                more information on how to get such IDs, see [Get SharePoint Folders](#/SharePointFolder/SharePointFolder_Get).
            from_ (str | Unset): Specifies the email address from which the attachments will be sent.
            to (str | Unset): Specifies the email address to which the attachments will be sent.
            subject (str | Unset): Specifies the subject of the email message used for sending the attachments.
            text (str | Unset): Specifies the body of the email message used for sending the attachments.
     """

    skip_item_checks: bool | Unset = UNSET
    folders: list[RESTSharePointFolder] | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    subject: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_share_point_folder import RESTSharePointFolder
        skip_item_checks = self.skip_item_checks

        folders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()
                folders.append(folders_item)



        from_ = self.from_

        to = self.to

        subject = self.subject

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if skip_item_checks is not UNSET:
            field_dict["skipItemChecks"] = skip_item_checks
        if folders is not UNSET:
            field_dict["folders"] = folders
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_share_point_folder import RESTSharePointFolder
        d = dict(src_dict)
        skip_item_checks = d.pop("skipItemChecks", UNSET)

        _folders = d.pop("folders", UNSET)
        folders: list[RESTSharePointFolder] | Unset = UNSET
        if _folders is not UNSET:
            folders = []
            for folders_item_data in _folders:
                folders_item = RESTSharePointFolder.from_dict(folders_item_data)



                folders.append(folders_item)


        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        rest_share_point_send_folders_as_msg_options = cls(
            skip_item_checks=skip_item_checks,
            folders=folders,
            from_=from_,
            to=to,
            subject=subject,
            text=text,
        )


        rest_share_point_send_folders_as_msg_options.additional_properties = d
        return rest_share_point_send_folders_as_msg_options

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
