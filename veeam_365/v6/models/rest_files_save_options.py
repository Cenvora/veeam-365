from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_teams_file import RESTTeamsFile


T = TypeVar("T", bound="RESTFilesSaveOptions")


@_attrs_define
class RESTFilesSaveOptions:
    """
    Attributes:
        channel_id (str | Unset):
        files (list[RESTTeamsFile] | Unset):
    """

    channel_id: str | Unset = UNSET
    files: list[RESTTeamsFile] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_file import RESTTeamsFile

        d = dict(src_dict)
        channel_id = d.pop("channelId", UNSET)

        _files = d.pop("files", UNSET)
        files: list[RESTTeamsFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = RESTTeamsFile.from_dict(files_item_data)

                files.append(files_item)

        rest_files_save_options = cls(
            channel_id=channel_id,
            files=files,
        )

        rest_files_save_options.additional_properties = d
        return rest_files_save_options

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
