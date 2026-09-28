from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_one_drive_folder import RESTOneDriveFolder


T = TypeVar("T", bound="RESTSaveOneDriveFoldersOptions")


@_attrs_define
class RESTSaveOneDriveFoldersOptions:
    """
    Attributes:
        folders (list[RESTOneDriveFolder] | Unset): Specifies IDs of the OneDrive folders that you want to save. For
            more information on how to get such IDs, see [Get OneDrive
            Folders](OneDriveFolder#operation/OneDriveFolder_Get).
    """

    folders: list[RESTOneDriveFolder] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()
                folders.append(folders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if folders is not UNSET:
            field_dict["folders"] = folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_one_drive_folder import RESTOneDriveFolder

        d = dict(src_dict)
        _folders = d.pop("folders", UNSET)
        folders: list[RESTOneDriveFolder] | Unset = UNSET
        if _folders is not UNSET:
            folders = []
            for folders_item_data in _folders:
                folders_item = RESTOneDriveFolder.from_dict(folders_item_data)

                folders.append(folders_item)

        rest_save_one_drive_folders_options = cls(
            folders=folders,
        )

        rest_save_one_drive_folders_options.additional_properties = d
        return rest_save_one_drive_folders_options

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
