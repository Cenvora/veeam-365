from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_teams_node_type import RESTTeamsNodeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_teams_node_links import RESTTeamsNodeLinks


T = TypeVar("T", bound="RESTTeamsNode")


@_attrs_define
class RESTTeamsNode:
    """
    Attributes:
        display_name (str | Unset): Display name of the teams item.
        type_ (RESTTeamsNodeType | Unset): Type of the teams item.
        field_links (RESTTeamsNodeLinks | Unset):
    """

    display_name: str | Unset = UNSET
    type_: RESTTeamsNodeType | Unset = UNSET
    field_links: RESTTeamsNodeLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_node_links import RESTTeamsNodeLinks

        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTTeamsNodeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTTeamsNodeType(_type_)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTTeamsNodeLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTTeamsNodeLinks.from_dict(_field_links)

        rest_teams_node = cls(
            display_name=display_name,
            type_=type_,
            field_links=field_links,
        )

        rest_teams_node.additional_properties = d
        return rest_teams_node

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
