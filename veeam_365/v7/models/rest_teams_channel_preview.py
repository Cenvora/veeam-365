from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_teams_channel_preview_links import RESTTeamsChannelPreviewLinks


T = TypeVar("T", bound="RESTTeamsChannelPreview")


@_attrs_define
class RESTTeamsChannelPreview:
    """
    Attributes:
        id (str): ID of the backed-up channel.
        display_name (str | Unset): Display name of the backed-up channel.
        field_links (RESTTeamsChannelPreviewLinks | Unset):
    """

    id: str
    display_name: str | Unset = UNSET
    field_links: RESTTeamsChannelPreviewLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_channel_preview_links import RESTTeamsChannelPreviewLinks

        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("displayName", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTTeamsChannelPreviewLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTTeamsChannelPreviewLinks.from_dict(_field_links)

        rest_teams_channel_preview = cls(
            id=id,
            display_name=display_name,
            field_links=field_links,
        )

        rest_teams_channel_preview.additional_properties = d
        return rest_teams_channel_preview

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
