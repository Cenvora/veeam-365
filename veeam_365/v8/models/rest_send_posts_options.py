from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_teams_post import RESTTeamsPost


T = TypeVar("T", bound="RESTSendPostsOptions")


@_attrs_define
class RESTSendPostsOptions:
    """
    Attributes:
        channel_id (str | Unset): Specifies the ID of the channel whose posts you want to send. Veeam Explorer for
            Microsoft Teams will send all posts of this channel. For more information on how to get this parameter, see [Get
            Team Channels](TeamsChannel#operation/TeamsChannel_Get).

            **Note**: You do not need to use this property if you use the `posts` property to specify what posts to send.
        posts (list[RESTTeamsPost] | Unset): Specifies IDs of the posts that you want to send. The posts must reside in
            the same channel. For more information on how to get such IDs, see [Get
            Posts](TeamsPost#operation/TeamsPost_GetPage).

            **Note**: You do not need to use this property if you use the `channelId` property to specify a channel whose
            posts to send.
        from_ (str | Unset): Specifies the email address from which the attachments will be sent.
        to (str | Unset): Specifies the email address to which the attachments will be sent.
        subject (str | Unset): Specifies the subject of the email message used for sending the attachments.
        text (str | Unset): Specifies the body of the email message used for sending the attachments.
    """

    channel_id: str | Unset = UNSET
    posts: list[RESTTeamsPost] | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    subject: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        posts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.posts, Unset):
            posts = []
            for posts_item_data in self.posts:
                posts_item = posts_item_data.to_dict()
                posts.append(posts_item)

        from_ = self.from_

        to = self.to

        subject = self.subject

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if posts is not UNSET:
            field_dict["posts"] = posts
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_post import RESTTeamsPost

        d = dict(src_dict)
        channel_id = d.pop("channelId", UNSET)

        _posts = d.pop("posts", UNSET)
        posts: list[RESTTeamsPost] | Unset = UNSET
        if _posts is not UNSET:
            posts = []
            for posts_item_data in _posts:
                posts_item = RESTTeamsPost.from_dict(posts_item_data)

                posts.append(posts_item)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        rest_send_posts_options = cls(
            channel_id=channel_id,
            posts=posts,
            from_=from_,
            to=to,
            subject=subject,
            text=text,
        )

        rest_send_posts_options.additional_properties = d
        return rest_send_posts_options

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
