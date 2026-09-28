from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.rest_teams_post import RESTTeamsPost


T = TypeVar("T", bound="RESTOperatorStartExportTaskOptions")


@_attrs_define
class RESTOperatorStartExportTaskOptions:
    """
    Attributes:
        posts (list[RESTTeamsPost]): Specifies IDs of the posts that you want to export. The posts must reside in the
            same channel. For more information on how to get such IDs, see [Get
            Posts](TeamsPost#operation/TeamsPost_GetPage).
    """

    posts: list[RESTTeamsPost]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        posts = []
        for posts_item_data in self.posts:
            posts_item = posts_item_data.to_dict()
            posts.append(posts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "posts": posts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_post import RESTTeamsPost

        d = dict(src_dict)
        posts = []
        _posts = d.pop("posts")
        for posts_item_data in _posts:
            posts_item = RESTTeamsPost.from_dict(posts_item_data)

            posts.append(posts_item)

        rest_operator_start_export_task_options = cls(
            posts=posts,
        )

        rest_operator_start_export_task_options.additional_properties = d
        return rest_operator_start_export_task_options

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
