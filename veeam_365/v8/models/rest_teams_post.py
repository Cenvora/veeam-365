from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.rest_attach_info import RESTAttachInfo
  from ..models.rest_teams_post_links import RESTTeamsPostLinks





T = TypeVar("T", bound="RESTTeamsPost")



@_attrs_define
class RESTTeamsPost:
    """ 
        Attributes:
            post_id (int | Unset): Post ID.
            change_key (str | Unset): Change key.
            is_important (bool | Unset): Defines whether the post is marked as important.
            author (str | Unset): User name of the author of the post.
            subject (str | Unset): Post subject.
            created_time (datetime.datetime | Unset): Date and time when the post was created.
            last_modified_time (datetime.datetime | Unset): Date and time of the last modification of the post.
            is_deleted (bool | Unset): Defines whether the post is marked as deleted or soft deleted.
            channel_id (str | Unset): Channel ID.
            team_id (UUID | Unset): Team ID.
            parent_id (int | None | Unset): Parent post ID.
            parent_change_key (str | Unset): Parent change key.
            attachments (list[RESTAttachInfo] | Unset): Array of attachment items for the post.
            field_links (RESTTeamsPostLinks | Unset):
     """

    post_id: int | Unset = UNSET
    change_key: str | Unset = UNSET
    is_important: bool | Unset = UNSET
    author: str | Unset = UNSET
    subject: str | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    last_modified_time: datetime.datetime | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    channel_id: str | Unset = UNSET
    team_id: UUID | Unset = UNSET
    parent_id: int | None | Unset = UNSET
    parent_change_key: str | Unset = UNSET
    attachments: list[RESTAttachInfo] | Unset = UNSET
    field_links: RESTTeamsPostLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_attach_info import RESTAttachInfo
        from ..models.rest_teams_post_links import RESTTeamsPostLinks
        post_id = self.post_id

        change_key = self.change_key

        is_important = self.is_important

        author = self.author

        subject = self.subject

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        last_modified_time: str | Unset = UNSET
        if not isinstance(self.last_modified_time, Unset):
            last_modified_time = self.last_modified_time.isoformat()

        is_deleted = self.is_deleted

        channel_id = self.channel_id

        team_id: str | Unset = UNSET
        if not isinstance(self.team_id, Unset):
            team_id = str(self.team_id)

        parent_id: int | None | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_change_key = self.parent_change_key

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
        field_dict.update({
        })
        if post_id is not UNSET:
            field_dict["postId"] = post_id
        if change_key is not UNSET:
            field_dict["changeKey"] = change_key
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
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_change_key is not UNSET:
            field_dict["parentChangeKey"] = parent_change_key
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

        change_key = d.pop("changeKey", UNSET)

        is_important = d.pop("isImportant", UNSET)

        author = d.pop("author", UNSET)

        subject = d.pop("subject", UNSET)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time,  Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)




        _last_modified_time = d.pop("lastModifiedTime", UNSET)
        last_modified_time: datetime.datetime | Unset
        if isinstance(_last_modified_time,  Unset):
            last_modified_time = UNSET
        else:
            last_modified_time = isoparse(_last_modified_time)




        is_deleted = d.pop("isDeleted", UNSET)

        channel_id = d.pop("channelId", UNSET)

        _team_id = d.pop("teamId", UNSET)
        team_id: UUID | Unset
        if isinstance(_team_id,  Unset):
            team_id = UNSET
        else:
            team_id = UUID(_team_id)




        def _parse_parent_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        parent_change_key = d.pop("parentChangeKey", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[RESTAttachInfo] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = RESTAttachInfo.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        _field_links = d.pop("_links", UNSET)
        field_links: RESTTeamsPostLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTTeamsPostLinks.from_dict(_field_links)




        rest_teams_post = cls(
            post_id=post_id,
            change_key=change_key,
            is_important=is_important,
            author=author,
            subject=subject,
            created_time=created_time,
            last_modified_time=last_modified_time,
            is_deleted=is_deleted,
            channel_id=channel_id,
            team_id=team_id,
            parent_id=parent_id,
            parent_change_key=parent_change_key,
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
