from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_share_point_folder_type import RESTSharePointFolderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_item_composed_links import RESTItemComposedLinks


T = TypeVar("T", bound="RESTItemComposed")


@_attrs_define
class RESTItemComposed:
    """
    Attributes:
        id (str):
        name (str):
        created_by (str):
        creation_time (datetime.datetime):
        modified_by (str):
        modification_time (datetime.datetime):
        size_bytes (int | Unset):
        inherited_permissions (bool | Unset):
        version (str | Unset):
        version_id (int | None | Unset):
        field_links (RESTItemComposedLinks | Unset):
        type_ (RESTSharePointFolderType | Unset):
        title (str | Unset):
    """

    id: str
    name: str
    created_by: str
    creation_time: datetime.datetime
    modified_by: str
    modification_time: datetime.datetime
    size_bytes: int | Unset = UNSET
    inherited_permissions: bool | Unset = UNSET
    version: str | Unset = UNSET
    version_id: int | None | Unset = UNSET
    field_links: RESTItemComposedLinks | Unset = UNSET
    type_: RESTSharePointFolderType | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_by = self.created_by

        creation_time = self.creation_time.isoformat()

        modified_by = self.modified_by

        modification_time = self.modification_time.isoformat()

        size_bytes = self.size_bytes

        inherited_permissions = self.inherited_permissions

        version = self.version

        version_id: int | None | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        else:
            version_id = self.version_id

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        title = self.title

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
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if inherited_permissions is not UNSET:
            field_dict["inheritedPermissions"] = inherited_permissions
        if version is not UNSET:
            field_dict["version"] = version
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_item_composed_links import RESTItemComposedLinks

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        created_by = d.pop("createdBy")

        creation_time = isoparse(d.pop("creationTime"))

        modified_by = d.pop("modifiedBy")

        modification_time = isoparse(d.pop("modificationTime"))

        size_bytes = d.pop("sizeBytes", UNSET)

        inherited_permissions = d.pop("inheritedPermissions", UNSET)

        version = d.pop("version", UNSET)

        def _parse_version_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version_id = _parse_version_id(d.pop("versionId", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: RESTItemComposedLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTItemComposedLinks.from_dict(_field_links)

        _type_ = d.pop("type", UNSET)
        type_: RESTSharePointFolderType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTSharePointFolderType(_type_)

        title = d.pop("title", UNSET)

        rest_item_composed = cls(
            id=id,
            name=name,
            created_by=created_by,
            creation_time=creation_time,
            modified_by=modified_by,
            modification_time=modification_time,
            size_bytes=size_bytes,
            inherited_permissions=inherited_permissions,
            version=version,
            version_id=version_id,
            field_links=field_links,
            type_=type_,
            title=title,
        )

        rest_item_composed.additional_properties = d
        return rest_item_composed

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
