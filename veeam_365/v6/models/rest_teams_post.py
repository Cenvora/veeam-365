from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_attach_info import RESTAttachInfo
    from ..models.rest_teams_post_links import RESTTeamsPostLinks


T = TypeVar("T", bound="RESTTeamsPost")


@_attrs_define
class RESTTeamsPost:
    """
    Attributes:
        post_id (int | Unset):
        is_important (bool | Unset):
        author (str | Unset):
        subject (str | Unset):
        created_time (datetime.datetime | Unset):
        last_modified_time (datetime.datetime | Unset):
        attachments (list[RESTAttachInfo] | Unset):
        field_links (RESTTeamsPostLinks | Unset):
    """

    post_id: int | Unset = UNSET
    is_important: bool | Unset = UNSET
    author: str | Unset = UNSET
    subject: str | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    last_modified_time: datetime.datetime | Unset = UNSET
    attachments: list[RESTAttachInfo] | Unset = UNSET
    field_links: RESTTeamsPostLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_attach_info import RESTAttachInfo
        from ..models.rest_teams_post_links import RESTTeamsPostLinks

        d = dict(src_dict)
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

        _field_links = d.pop("_links", UNSET)
        field_links: RESTTeamsPostLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTTeamsPostLinks.from_dict(_field_links)

        rest_teams_post = cls(
            post_id=post_id,
            is_important=is_important,
            author=author,
            subject=subject,
            created_time=created_time,
            last_modified_time=last_modified_time,
            attachments=attachments,
            field_links=field_links,
        )

        rest_teams_post.additional_properties = d
        return rest_teams_post

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
