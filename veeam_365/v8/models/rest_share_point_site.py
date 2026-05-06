from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_share_point_site_links import RESTSharePointSiteLinks





T = TypeVar("T", bound="RESTSharePointSite")



@_attrs_define
class RESTSharePointSite:
    """ 
        Attributes:
            id (str | Unset): ID of the backed-up SharePoint site.
            name (str | Unset): Name of the backed-up SharePoint site.
            url (str | Unset): Path to the backed-up SharePoint site.
            field_links (RESTSharePointSiteLinks | Unset):
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    field_links: RESTSharePointSiteLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_share_point_site_links import RESTSharePointSiteLinks
        id = self.id

        name = self.name

        url = self.url

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_share_point_site_links import RESTSharePointSiteLinks
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTSharePointSiteLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTSharePointSiteLinks.from_dict(_field_links)




        rest_share_point_site = cls(
            id=id,
            name=name,
            url=url,
            field_links=field_links,
        )


        rest_share_point_site.additional_properties = d
        return rest_share_point_site

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
