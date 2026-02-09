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


T = TypeVar("T", bound="RESTOperatorRestorePostsOptions")


@_attrs_define
class RESTOperatorRestorePostsOptions:
    """
    Attributes:
        channel_id (str): Specifies the ID of the channel whose posts you want to restore using Restore Portal. For more
            information on how to get this parameter, see [Get Team Channels](#tag/TeamsChannel/operation/TeamsChannel_Get).

            **Note**: If you specify this property, you can use the `from` and `to` properties to specify a time period for
            which you want to restore posts. You do not need to use this property if you use the `posts` property to specify
            what posts to restore.
        from_ (datetime.datetime | None | Unset): Specifies the point in time that defines the start of the period for
            which you want to restore posts.
        to (datetime.datetime | None | Unset): Specifies the point in time that defines the end of the period for which
            you want to restore posts.
        posts (list[RESTTeamsPost] | None | Unset): Specifies IDs of posts that you want to restore. The posts must
            reside in the same channel. For more information on how to get such IDs, see [Get
            Posts](#tag/TeamsPost/operation/TeamsPost_GetPage).

            **Note**: You do not need to use this property if you use the `channelId` property to specify a channel whose
            posts to restore.
        reason (str | Unset): Specifies a reason for the restore operation.
    """

    channel_id: str
    from_: datetime.datetime | None | Unset = UNSET
    to: datetime.datetime | None | Unset = UNSET
    posts: list[RESTTeamsPost] | None | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        posts: list[dict[str, Any]] | None | Unset
        if isinstance(self.posts, Unset):
            posts = UNSET
        elif isinstance(self.posts, list):
            posts = []
            for posts_type_0_item_data in self.posts:
                posts_type_0_item = posts_type_0_item_data.to_dict()
                posts.append(posts_type_0_item)

        else:
            posts = self.posts

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if posts is not UNSET:
            field_dict["posts"] = posts
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_post import RESTTeamsPost

        d = dict(src_dict)
        channel_id = d.pop("channelId")

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

        def _parse_posts(data: object) -> list[RESTTeamsPost] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                posts_type_0 = []
                _posts_type_0 = data
                for posts_type_0_item_data in _posts_type_0:
                    posts_type_0_item = RESTTeamsPost.from_dict(posts_type_0_item_data)

                    posts_type_0.append(posts_type_0_item)

                return posts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RESTTeamsPost] | None | Unset, data)

        posts = _parse_posts(d.pop("posts", UNSET))

        reason = d.pop("reason", UNSET)

        rest_operator_restore_posts_options = cls(
            channel_id=channel_id,
            from_=from_,
            to=to,
            posts=posts,
            reason=reason,
        )

        rest_operator_restore_posts_options.additional_properties = d
        return rest_operator_restore_posts_options

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
