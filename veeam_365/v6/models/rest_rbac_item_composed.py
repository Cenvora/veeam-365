from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_rbac_item_type import RESTRbacItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_rbac_group import RESTRbacGroup
    from ..models.rest_rbac_item_composed_links import RESTRbacItemComposedLinks
    from ..models.rest_rbac_site import RESTRbacSite
    from ..models.rest_rbac_user import RESTRbacUser


T = TypeVar("T", bound="RESTRbacItemComposed")


@_attrs_define
class RESTRbacItemComposed:
    """
    Attributes:
        type_ (RESTRbacItemType | Unset):
        user (RESTRbacUser | Unset):
        id (str | Unset):
        field_links (RESTRbacItemComposedLinks | Unset):
        site (RESTRbacSite | Unset):
        group (RESTRbacGroup | Unset):
    """

    type_: RESTRbacItemType | Unset = UNSET
    user: RESTRbacUser | Unset = UNSET
    id: str | Unset = UNSET
    field_links: RESTRbacItemComposedLinks | Unset = UNSET
    site: RESTRbacSite | Unset = UNSET
    group: RESTRbacGroup | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        id = self.id

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        site: dict[str, Any] | Unset = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user is not UNSET:
            field_dict["user"] = user
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if site is not UNSET:
            field_dict["site"] = site
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_rbac_group import RESTRbacGroup
        from ..models.rest_rbac_item_composed_links import RESTRbacItemComposedLinks
        from ..models.rest_rbac_site import RESTRbacSite
        from ..models.rest_rbac_user import RESTRbacUser

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTRbacItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTRbacItemType(_type_)

        _user = d.pop("user", UNSET)
        user: RESTRbacUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RESTRbacUser.from_dict(_user)

        id = d.pop("id", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTRbacItemComposedLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTRbacItemComposedLinks.from_dict(_field_links)

        _site = d.pop("site", UNSET)
        site: RESTRbacSite | Unset
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = RESTRbacSite.from_dict(_site)

        _group = d.pop("group", UNSET)
        group: RESTRbacGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = RESTRbacGroup.from_dict(_group)

        rest_rbac_item_composed = cls(
            type_=type_,
            user=user,
            id=id,
            field_links=field_links,
            site=site,
            group=group,
        )

        rest_rbac_item_composed.additional_properties = d
        return rest_rbac_item_composed

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
