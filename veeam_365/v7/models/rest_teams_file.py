from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_teams_file_file_type import RESTTeamsFileFileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_teams_file_links import RESTTeamsFileLinks


T = TypeVar("T", bound="RESTTeamsFile")


@_attrs_define
class RESTTeamsFile:
    """
    Attributes:
        id (UUID): File ID. Example: 00000000-0000-0000-0000-000000000000.
        name (str | Unset): Name of the file.
        size_bytes (int | Unset): File size.
        version (int | Unset): Version of the file in the backup.
        ui_version (str | Unset): Version of the file.
        modified (datetime.datetime | Unset): Date and time of the last modification of the file.
        modified_by (str | Unset): Name of the user who performed the last modification of the file.
        channel_id (str | Unset): Channel ID.
        file_type (RESTTeamsFileFileType | Unset): Type of the Microsoft Teams item.
        field_links (RESTTeamsFileLinks | Unset):
    """

    id: UUID
    name: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    version: int | Unset = UNSET
    ui_version: str | Unset = UNSET
    modified: datetime.datetime | Unset = UNSET
    modified_by: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    file_type: RESTTeamsFileFileType | Unset = UNSET
    field_links: RESTTeamsFileLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        size_bytes = self.size_bytes

        version = self.version

        ui_version = self.ui_version

        modified: str | Unset = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        modified_by = self.modified_by

        channel_id = self.channel_id

        file_type: str | Unset = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if version is not UNSET:
            field_dict["version"] = version
        if ui_version is not UNSET:
            field_dict["uiVersion"] = ui_version
        if modified is not UNSET:
            field_dict["modified"] = modified
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_file_links import RESTTeamsFileLinks

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name", UNSET)

        size_bytes = d.pop("sizeBytes", UNSET)

        version = d.pop("version", UNSET)

        ui_version = d.pop("uiVersion", UNSET)

        _modified = d.pop("modified", UNSET)
        modified: datetime.datetime | Unset
        if isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        modified_by = d.pop("modifiedBy", UNSET)

        channel_id = d.pop("channelId", UNSET)

        _file_type = d.pop("fileType", UNSET)
        file_type: RESTTeamsFileFileType | Unset
        if isinstance(_file_type, Unset):
            file_type = UNSET
        else:
            file_type = RESTTeamsFileFileType(_file_type)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTTeamsFileLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTTeamsFileLinks.from_dict(_field_links)

        rest_teams_file = cls(
            id=id,
            name=name,
            size_bytes=size_bytes,
            version=version,
            ui_version=ui_version,
            modified=modified,
            modified_by=modified_by,
            channel_id=channel_id,
            file_type=file_type,
            field_links=field_links,
        )

        rest_teams_file.additional_properties = d
        return rest_teams_file

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
