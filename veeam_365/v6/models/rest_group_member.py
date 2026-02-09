from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_group_member_type import RESTGroupMemberType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTGroupMember")


@_attrs_define
class RESTGroupMember:
    """
    Attributes:
        group_id (str | Unset):
        name (str | Unset):
        login (str | Unset):
        type_ (RESTGroupMemberType | Unset):
        is_cloud (bool | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    group_id: str | Unset = UNSET
    name: str | Unset = UNSET
    login: str | Unset = UNSET
    type_: RESTGroupMemberType | Unset = UNSET
    is_cloud: bool | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        name = self.name

        login = self.login

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        is_cloud = self.is_cloud

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if login is not UNSET:
            field_dict["login"] = login
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_cloud is not UNSET:
            field_dict["isCloud"] = is_cloud
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        group_id = d.pop("groupId", UNSET)

        name = d.pop("name", UNSET)

        login = d.pop("login", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTGroupMemberType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTGroupMemberType(_type_)

        is_cloud = d.pop("isCloud", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_group_member = cls(
            group_id=group_id,
            name=name,
            login=login,
            type_=type_,
            is_cloud=is_cloud,
            field_links=field_links,
        )

        rest_group_member.additional_properties = d
        return rest_group_member

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
