from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_one_drive_folder import RESTOneDriveFolder


T = TypeVar("T", bound="RESTSendFoldersAsMsgOptions")


@_attrs_define
class RESTSendFoldersAsMsgOptions:
    """
    Attributes:
        skip_item_checks (bool | Unset):
        folders (list[RESTOneDriveFolder] | Unset):
        from_ (str | Unset):
        to (str | Unset):
        subject (str | Unset):
        text (str | Unset):
    """

    skip_item_checks: bool | Unset = UNSET
    folders: list[RESTOneDriveFolder] | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    subject: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        field_dict.update({})
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
        from ..models.rest_one_drive_folder import RESTOneDriveFolder

        d = dict(src_dict)
        skip_item_checks = d.pop("skipItemChecks", UNSET)

        _folders = d.pop("folders", UNSET)
        folders: list[RESTOneDriveFolder] | Unset = UNSET
        if _folders is not UNSET:
            folders = []
            for folders_item_data in _folders:
                folders_item = RESTOneDriveFolder.from_dict(folders_item_data)

                folders.append(folders_item)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        rest_send_folders_as_msg_options = cls(
            skip_item_checks=skip_item_checks,
            folders=folders,
            from_=from_,
            to=to,
            subject=subject,
            text=text,
        )

        rest_send_folders_as_msg_options.additional_properties = d
        return rest_send_folders_as_msg_options

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
