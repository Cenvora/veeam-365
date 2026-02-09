from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_exchange_folder_category import RESTExchangeFolderCategory
from ..models.rest_exchange_folder_type import RESTExchangeFolderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_exchange_folder_actions import RESTExchangeFolderActions
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTExchangeFolder")


@_attrs_define
class RESTExchangeFolder:
    """
    Attributes:
        name (str | Unset):
        type_ (RESTExchangeFolderType | Unset):
        category (RESTExchangeFolderCategory | Unset):
        description (str | Unset):
        field_links (RESTLinkHALDictionary | Unset):
        field_actions (RESTExchangeFolderActions | Unset):
        id (str | Unset):
    """

    name: str | Unset = UNSET
    type_: RESTExchangeFolderType | Unset = UNSET
    category: RESTExchangeFolderCategory | Unset = UNSET
    description: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTExchangeFolderActions | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        description = self.description

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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_exchange_folder_actions import RESTExchangeFolderActions
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTExchangeFolderType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTExchangeFolderType(_type_)

        _category = d.pop("category", UNSET)
        category: RESTExchangeFolderCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = RESTExchangeFolderCategory(_category)

        description = d.pop("description", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTExchangeFolderActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTExchangeFolderActions.from_dict(_field_actions)

        id = d.pop("id", UNSET)

        rest_exchange_folder = cls(
            name=name,
            type_=type_,
            category=category,
            description=description,
            field_links=field_links,
            field_actions=field_actions,
            id=id,
        )

        rest_exchange_folder.additional_properties = d
        return rest_exchange_folder

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
