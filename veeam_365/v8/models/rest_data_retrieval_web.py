from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_data_retrieval_web_links import RESTDataRetrievalWebLinks





T = TypeVar("T", bound="RESTDataRetrievalWeb")



@_attrs_define
class RESTDataRetrievalWeb:
    """ 
        Attributes:
            site_id (UUID | Unset): Site collection ID. Example: 00000000-0000-0000-0000-000000000000.
            web_id (UUID | Unset): SharePoint site ID. Example: 00000000-0000-0000-0000-000000000000.
            title (str | Unset): SharePoint site title.
            url (str | Unset): SharePoint site path.
            field_links (RESTDataRetrievalWebLinks | Unset):
     """

    site_id: UUID | Unset = UNSET
    web_id: UUID | Unset = UNSET
    title: str | Unset = UNSET
    url: str | Unset = UNSET
    field_links: RESTDataRetrievalWebLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_data_retrieval_web_links import RESTDataRetrievalWebLinks
        site_id: str | Unset = UNSET
        if not isinstance(self.site_id, Unset):
            site_id = str(self.site_id)

        web_id: str | Unset = UNSET
        if not isinstance(self.web_id, Unset):
            web_id = str(self.web_id)

        title = self.title

        url = self.url

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if site_id is not UNSET:
            field_dict["SiteId"] = site_id
        if web_id is not UNSET:
            field_dict["WebId"] = web_id
        if title is not UNSET:
            field_dict["Title"] = title
        if url is not UNSET:
            field_dict["Url"] = url
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_data_retrieval_web_links import RESTDataRetrievalWebLinks
        d = dict(src_dict)
        _site_id = d.pop("SiteId", UNSET)
        site_id: UUID | Unset
        if isinstance(_site_id,  Unset):
            site_id = UNSET
        else:
            site_id = UUID(_site_id)




        _web_id = d.pop("WebId", UNSET)
        web_id: UUID | Unset
        if isinstance(_web_id,  Unset):
            web_id = UNSET
        else:
            web_id = UUID(_web_id)




        title = d.pop("Title", UNSET)

        url = d.pop("Url", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTDataRetrievalWebLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTDataRetrievalWebLinks.from_dict(_field_links)




        rest_data_retrieval_web = cls(
            site_id=site_id,
            web_id=web_id,
            title=title,
            url=url,
            field_links=field_links,
        )


        rest_data_retrieval_web.additional_properties = d
        return rest_data_retrieval_web

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
