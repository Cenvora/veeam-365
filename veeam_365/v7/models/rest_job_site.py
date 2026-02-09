from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTJobSite")


@_attrs_define
class RESTJobSite:
    """
    Attributes:
        id (str): ID of the organization site.
        url (str): Path to the organization site.
        is_cloud (bool): Defines whether this organization site is located in cloud.
        is_personal (bool): Defines whether the organization site is personal.
        title (str): Title of the organization site.
        parent_url (str | Unset): Path for the parent object.
        name (str | Unset): Name of the organization site.
        site_collection_error (str | Unset): Error occurred when processing site collections.
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: str
    url: str
    is_cloud: bool
    is_personal: bool
    title: str
    parent_url: str | Unset = UNSET
    name: str | Unset = UNSET
    site_collection_error: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        is_cloud = self.is_cloud

        is_personal = self.is_personal

        title = self.title

        parent_url = self.parent_url

        name = self.name

        site_collection_error = self.site_collection_error

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "isCloud": is_cloud,
                "isPersonal": is_personal,
                "title": title,
            }
        )
        if parent_url is not UNSET:
            field_dict["parentUrl"] = parent_url
        if name is not UNSET:
            field_dict["name"] = name
        if site_collection_error is not UNSET:
            field_dict["siteCollectionError"] = site_collection_error
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        is_cloud = d.pop("isCloud")

        is_personal = d.pop("isPersonal")

        title = d.pop("title")

        parent_url = d.pop("parentUrl", UNSET)

        name = d.pop("name", UNSET)

        site_collection_error = d.pop("siteCollectionError", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_job_site = cls(
            id=id,
            url=url,
            is_cloud=is_cloud,
            is_personal=is_personal,
            title=title,
            parent_url=parent_url,
            name=name,
            site_collection_error=site_collection_error,
            field_links=field_links,
        )

        rest_job_site.additional_properties = d
        return rest_job_site

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
