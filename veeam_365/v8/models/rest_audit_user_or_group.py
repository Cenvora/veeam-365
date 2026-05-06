from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_audit_user_or_group_type import RESTAuditUserOrGroupType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_group import RESTGroup
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
  from ..models.rest_user import RESTUser





T = TypeVar("T", bound="RESTAuditUserOrGroup")



@_attrs_define
class RESTAuditUserOrGroup:
    """ 
        Attributes:
            id (str | Unset): ID of the audit item.
            type_ (RESTAuditUserOrGroupType | Unset): Type of the audit item.
            group (RESTGroup | Unset):
            user (RESTUser | Unset):
            field_links (RESTLinkHALDictionary | Unset): Related resources.
     """

    id: str | Unset = UNSET
    type_: RESTAuditUserOrGroupType | Unset = UNSET
    group: RESTGroup | Unset = UNSET
    user: RESTUser | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_group import RESTGroup
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_user import RESTUser
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if group is not UNSET:
            field_dict["group"] = group
        if user is not UNSET:
            field_dict["user"] = user
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_group import RESTGroup
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_user import RESTUser
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTAuditUserOrGroupType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RESTAuditUserOrGroupType(_type_)




        _group = d.pop("group", UNSET)
        group: RESTGroup | Unset
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = RESTGroup.from_dict(_group)




        _user = d.pop("user", UNSET)
        user: RESTUser | Unset
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = RESTUser.from_dict(_user)




        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        rest_audit_user_or_group = cls(
            id=id,
            type_=type_,
            group=group,
            user=user,
            field_links=field_links,
        )


        rest_audit_user_or_group.additional_properties = d
        return rest_audit_user_or_group

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
