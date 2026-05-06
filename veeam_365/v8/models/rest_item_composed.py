from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_share_point_folder_type import RESTSharePointFolderType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.rest_item_composed_links import RESTItemComposedLinks





T = TypeVar("T", bound="RESTItemComposed")



@_attrs_define
class RESTItemComposed:
    """ 
        Attributes:
            id (str): ID of the backed-up OneDrive document.
            name (str): Name of the backed-up OneDrive document.
            created_by (str): User who created the document.
            creation_time (datetime.datetime): Date and time when the document was created.
            modified_by (str): User who performed the last modification to the document.
            modification_time (datetime.datetime): Date and time when the document was modified.
            one_drive_id (str | Unset): OneDrive ID.
            size_bytes (int | Unset): Size of the backed-up OneDrive document.
            inherited_permissions (bool | Unset): Defines whether the permission settings of an element will be passed on to
                the subordinates of that element.
            version (str | Unset): Version of the OneDrive document.
            version_id (int | None | Unset): ID of the OneDrive document version.
            is_folder (bool | Unset): Defines whether the item is a folder.
            field_links (RESTItemComposedLinks | Unset):
            site_id (str | Unset): ID of the SharePoint site.
            type_ (RESTSharePointFolderType | Unset): Type of the backed-up SharePoint folder.
            title (str | Unset): Title of the backed-up SharePoint item.
     """

    id: str
    name: str
    created_by: str
    creation_time: datetime.datetime
    modified_by: str
    modification_time: datetime.datetime
    one_drive_id: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    inherited_permissions: bool | Unset = UNSET
    version: str | Unset = UNSET
    version_id: int | None | Unset = UNSET
    is_folder: bool | Unset = UNSET
    field_links: RESTItemComposedLinks | Unset = UNSET
    site_id: str | Unset = UNSET
    type_: RESTSharePointFolderType | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_item_composed_links import RESTItemComposedLinks
        id = self.id

        name = self.name

        created_by = self.created_by

        creation_time = self.creation_time.isoformat()

        modified_by = self.modified_by

        modification_time = self.modification_time.isoformat()

        one_drive_id = self.one_drive_id

        size_bytes = self.size_bytes

        inherited_permissions = self.inherited_permissions

        version = self.version

        version_id: int | None | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        else:
            version_id = self.version_id

        is_folder = self.is_folder

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        site_id = self.site_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "createdBy": created_by,
            "creationTime": creation_time,
            "modifiedBy": modified_by,
            "modificationTime": modification_time,
        })
        if one_drive_id is not UNSET:
            field_dict["oneDriveId"] = one_drive_id
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if inherited_permissions is not UNSET:
            field_dict["inheritedPermissions"] = inherited_permissions
        if version is not UNSET:
            field_dict["version"] = version
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if is_folder is not UNSET:
            field_dict["isFolder"] = is_folder
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
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




        one_drive_id = d.pop("oneDriveId", UNSET)

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


        is_folder = d.pop("isFolder", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTItemComposedLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTItemComposedLinks.from_dict(_field_links)




        site_id = d.pop("siteId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTSharePointFolderType | Unset
        if isinstance(_type_,  Unset):
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
            one_drive_id=one_drive_id,
            size_bytes=size_bytes,
            inherited_permissions=inherited_permissions,
            version=version,
            version_id=version_id,
            is_folder=is_folder,
            field_links=field_links,
            site_id=site_id,
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
