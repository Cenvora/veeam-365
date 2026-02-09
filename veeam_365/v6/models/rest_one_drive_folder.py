from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_one_drive_folder_links import RESTOneDriveFolderLinks


T = TypeVar("T", bound="RESTOneDriveFolder")


@_attrs_define
class RESTOneDriveFolder:
    """
    Attributes:
        id (str):
        name (str):
        created_by (str):
        creation_time (datetime.datetime):
        modified_by (str):
        modification_time (datetime.datetime):
        version (str | Unset):
        version_id (int | None | Unset):
        field_links (RESTOneDriveFolderLinks | Unset):
    """

    id: str
    name: str
    created_by: str
    creation_time: datetime.datetime
    modified_by: str
    modification_time: datetime.datetime
    version: str | Unset = UNSET
    version_id: int | None | Unset = UNSET
    field_links: RESTOneDriveFolderLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_by = self.created_by

        creation_time = self.creation_time.isoformat()

        modified_by = self.modified_by

        modification_time = self.modification_time.isoformat()

        version = self.version

        version_id: int | None | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        else:
            version_id = self.version_id

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "createdBy": created_by,
                "creationTime": creation_time,
                "modifiedBy": modified_by,
                "modificationTime": modification_time,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_one_drive_folder_links import RESTOneDriveFolderLinks

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        created_by = d.pop("createdBy")

        creation_time = isoparse(d.pop("creationTime"))

        modified_by = d.pop("modifiedBy")

        modification_time = isoparse(d.pop("modificationTime"))

        version = d.pop("version", UNSET)

        def _parse_version_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version_id = _parse_version_id(d.pop("versionId", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: RESTOneDriveFolderLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTOneDriveFolderLinks.from_dict(_field_links)

        rest_one_drive_folder = cls(
            id=id,
            name=name,
            created_by=created_by,
            creation_time=creation_time,
            modified_by=modified_by,
            modification_time=modification_time,
            version=version,
            version_id=version_id,
            field_links=field_links,
        )

        rest_one_drive_folder.additional_properties = d
        return rest_one_drive_folder

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
