from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_channel_entity_file_type import RESTChannelEntityFileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_attach_info import RESTAttachInfo
    from ..models.rest_channel_entity_links import RESTChannelEntityLinks


T = TypeVar("T", bound="RESTChannelEntity")


@_attrs_define
class RESTChannelEntity:
    """
    Attributes:
        id (UUID | Unset):  Example: 00000000-0000-0000-0000-000000000000.
        name (str | Unset):
        size_bytes (int | Unset):
        version (int | Unset):
        modified (datetime.datetime | Unset):
        modified_by (str | Unset):
        file_type (RESTChannelEntityFileType | Unset):
        field_links (RESTChannelEntityLinks | Unset):
        post_id (int | Unset):
        is_important (bool | Unset):
        author (str | Unset):
        subject (str | Unset):
        created_time (datetime.datetime | Unset):
        last_modified_time (datetime.datetime | Unset):
        attachments (list[RESTAttachInfo] | Unset):
        display_name (str | Unset):
        content_url (str | Unset):
        type_ (str | Unset):
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    version: int | Unset = UNSET
    modified: datetime.datetime | Unset = UNSET
    modified_by: str | Unset = UNSET
    file_type: RESTChannelEntityFileType | Unset = UNSET
    field_links: RESTChannelEntityLinks | Unset = UNSET
    post_id: int | Unset = UNSET
    is_important: bool | Unset = UNSET
    author: str | Unset = UNSET
    subject: str | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    last_modified_time: datetime.datetime | Unset = UNSET
    attachments: list[RESTAttachInfo] | Unset = UNSET
    display_name: str | Unset = UNSET
    content_url: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        size_bytes = self.size_bytes

        version = self.version

        modified: str | Unset = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        modified_by = self.modified_by

        file_type: str | Unset = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        post_id = self.post_id

        is_important = self.is_important

        author = self.author

        subject = self.subject

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        last_modified_time: str | Unset = UNSET
        if not isinstance(self.last_modified_time, Unset):
            last_modified_time = self.last_modified_time.isoformat()

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        display_name = self.display_name

        content_url = self.content_url

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if version is not UNSET:
            field_dict["version"] = version
        if modified is not UNSET:
            field_dict["modified"] = modified
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if post_id is not UNSET:
            field_dict["postId"] = post_id
        if is_important is not UNSET:
            field_dict["isImportant"] = is_important
        if author is not UNSET:
            field_dict["author"] = author
        if subject is not UNSET:
            field_dict["subject"] = subject
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if last_modified_time is not UNSET:
            field_dict["lastModifiedTime"] = last_modified_time
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if content_url is not UNSET:
            field_dict["contentUrl"] = content_url
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_attach_info import RESTAttachInfo
        from ..models.rest_channel_entity_links import RESTChannelEntityLinks

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        size_bytes = d.pop("sizeBytes", UNSET)

        version = d.pop("version", UNSET)

        _modified = d.pop("modified", UNSET)
        modified: datetime.datetime | Unset
        if isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        modified_by = d.pop("modifiedBy", UNSET)

        _file_type = d.pop("fileType", UNSET)
        file_type: RESTChannelEntityFileType | Unset
        if isinstance(_file_type, Unset):
            file_type = UNSET
        else:
            file_type = RESTChannelEntityFileType(_file_type)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTChannelEntityLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTChannelEntityLinks.from_dict(_field_links)

        post_id = d.pop("postId", UNSET)

        is_important = d.pop("isImportant", UNSET)

        author = d.pop("author", UNSET)

        subject = d.pop("subject", UNSET)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)

        _last_modified_time = d.pop("lastModifiedTime", UNSET)
        last_modified_time: datetime.datetime | Unset
        if isinstance(_last_modified_time, Unset):
            last_modified_time = UNSET
        else:
            last_modified_time = isoparse(_last_modified_time)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[RESTAttachInfo] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = RESTAttachInfo.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        display_name = d.pop("displayName", UNSET)

        content_url = d.pop("contentUrl", UNSET)

        type_ = d.pop("type", UNSET)

        rest_channel_entity = cls(
            id=id,
            name=name,
            size_bytes=size_bytes,
            version=version,
            modified=modified,
            modified_by=modified_by,
            file_type=file_type,
            field_links=field_links,
            post_id=post_id,
            is_important=is_important,
            author=author,
            subject=subject,
            created_time=created_time,
            last_modified_time=last_modified_time,
            attachments=attachments,
            display_name=display_name,
            content_url=content_url,
            type_=type_,
        )

        rest_channel_entity.additional_properties = d
        return rest_channel_entity

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
