from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_contact_group_item_actions import RESTContactGroupItemActions
    from ..models.rest_contact_group_item_links import RESTContactGroupItemLinks


T = TypeVar("T", bound="RESTContactGroupItem")


@_attrs_define
class RESTContactGroupItem:
    """
    Attributes:
        name (str | Unset):
        item_class (str | Unset):
        field_links (RESTContactGroupItemLinks | Unset):
        field_actions (RESTContactGroupItemActions | Unset):
        id (str | Unset):
    """

    name: str | Unset = UNSET
    item_class: str | Unset = UNSET
    field_links: RESTContactGroupItemLinks | Unset = UNSET
    field_actions: RESTContactGroupItemActions | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        item_class = self.item_class

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if item_class is not UNSET:
            field_dict["itemClass"] = item_class
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_contact_group_item_actions import RESTContactGroupItemActions
        from ..models.rest_contact_group_item_links import RESTContactGroupItemLinks

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        item_class = d.pop("itemClass", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTContactGroupItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTContactGroupItemLinks.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTContactGroupItemActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTContactGroupItemActions.from_dict(_field_actions)

        id = d.pop("id", UNSET)

        rest_contact_group_item = cls(
            name=name,
            item_class=item_class,
            field_links=field_links,
            field_actions=field_actions,
            id=id,
        )

        rest_contact_group_item.additional_properties = d
        return rest_contact_group_item

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
