from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_teams_post import RESTTeamsPost


T = TypeVar("T", bound="RESTExportOptions")


@_attrs_define
class RESTExportOptions:
    """
    Attributes:
        posts (list[RESTTeamsPost] | Unset): Specifies IDs of the posts that you want to export. The posts must reside
            in the same channel. For more information on how to get such IDs, see [Get
            Posts](TeamsPost#operation/TeamsPost_GetPage).

            **Note**: You do not need to use this property if you use the `channelId` property to specify a channel whose
            posts to export.
        channel_id (str | Unset): Specifies the ID of the channel whose posts you want to export. For more information
            on how to get this parameter, see [Get Team Channels](TeamsChannel#operation/TeamsChannel_Get).

            **Note**: If you specify this property, you can use the `from` and `to` properties to specify a time period for
            which you want to export posts. You do not need to use this property if you use the `posts` property to specify
            what posts to export.
        from_ (datetime.datetime | None | Unset): Specifies the point in time that defines the start of the period for
            which you want to export posts.
        to (datetime.datetime | None | Unset): Specifies the point in time that defines the end of the period for which
            you want to export posts.
    """

    posts: list[RESTTeamsPost] | Unset = UNSET
    channel_id: str | Unset = UNSET
    from_: datetime.datetime | None | Unset = UNSET
    to: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        posts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.posts, Unset):
            posts = []
            for posts_item_data in self.posts:
                posts_item = posts_item_data.to_dict()
                posts.append(posts_item)

        channel_id = self.channel_id

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        elif isinstance(self.from_, datetime.datetime):
            from_ = self.from_.isoformat()
        else:
            from_ = self.from_

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, datetime.datetime):
            to = self.to.isoformat()
        else:
            to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posts is not UNSET:
            field_dict["posts"] = posts
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_post import RESTTeamsPost

        d = dict(src_dict)
        _posts = d.pop("posts", UNSET)
        posts: list[RESTTeamsPost] | Unset = UNSET
        if _posts is not UNSET:
            posts = []
            for posts_item_data in _posts:
                posts_item = RESTTeamsPost.from_dict(posts_item_data)

                posts.append(posts_item)

        channel_id = d.pop("channelId", UNSET)

        def _parse_from_(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_type_0 = isoparse(data)

                return from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_type_0 = isoparse(data)

                return to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        to = _parse_to(d.pop("to", UNSET))

        rest_export_options = cls(
            posts=posts,
            channel_id=channel_id,
            from_=from_,
            to=to,
        )

        rest_export_options.additional_properties = d
        return rest_export_options

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
