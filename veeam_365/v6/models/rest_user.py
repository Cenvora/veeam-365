from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_user_location_type import RESTUserLocationType
from ..models.rest_user_type import RESTUserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTUser")


@_attrs_define
class RESTUser:
    """
    Attributes:
        id (str | Unset):
        display_name (str | Unset):
        name (str | Unset):
        type_ (RESTUserType | Unset):
        location_type (RESTUserLocationType | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: RESTUserType | Unset = UNSET
    location_type: RESTUserLocationType | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if location_type is not UNSET:
            field_dict["locationType"] = location_type
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTUserType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTUserType(_type_)

        _location_type = d.pop("locationType", UNSET)
        location_type: RESTUserLocationType | Unset
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = RESTUserLocationType(_location_type)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_user = cls(
            id=id,
            display_name=display_name,
            name=name,
            type_=type_,
            location_type=location_type,
            field_links=field_links,
        )

        rest_user.additional_properties = d
        return rest_user

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
