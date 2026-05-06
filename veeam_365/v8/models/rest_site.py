from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary





T = TypeVar("T", bound="RESTSite")



@_attrs_define
class RESTSite:
    """ 
        Attributes:
            id (str): ID of the organization site.
            url (str): Path to the organization site.
            is_cloud (bool): Defines whether this organization site is located in cloud.
            is_personal (bool): Defines whether this organization site is personal.
            title (str): Title of the organization site.
            e_tag (int | None | Unset): Version number that Veeam Backup for Microsoft 365 assigns if the organization site
                was modified.
            parent_url (str | Unset): Path for the parent object.
            name (str | Unset): Name of the organization site.
            is_available (bool | Unset): Defines whether the organization site is available for backup and restore.
            site_collection_error (str | Unset): Error occurred when processing site collections.
            msid (None | str | Unset): ID of the organization site assigned by Microsoft.
            data_location (None | str | Unset): Data location of the organization site.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
     """

    id: str
    url: str
    is_cloud: bool
    is_personal: bool
    title: str
    e_tag: int | None | Unset = UNSET
    parent_url: str | Unset = UNSET
    name: str | Unset = UNSET
    is_available: bool | Unset = UNSET
    site_collection_error: str | Unset = UNSET
    msid: None | str | Unset = UNSET
    data_location: None | str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        id = self.id

        url = self.url

        is_cloud = self.is_cloud

        is_personal = self.is_personal

        title = self.title

        e_tag: int | None | Unset
        if isinstance(self.e_tag, Unset):
            e_tag = UNSET
        else:
            e_tag = self.e_tag

        parent_url = self.parent_url

        name = self.name

        is_available = self.is_available

        site_collection_error = self.site_collection_error

        msid: None | str | Unset
        if isinstance(self.msid, Unset):
            msid = UNSET
        else:
            msid = self.msid

        data_location: None | str | Unset
        if isinstance(self.data_location, Unset):
            data_location = UNSET
        else:
            data_location = self.data_location

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "url": url,
            "isCloud": is_cloud,
            "isPersonal": is_personal,
            "title": title,
        })
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag
        if parent_url is not UNSET:
            field_dict["parentUrl"] = parent_url
        if name is not UNSET:
            field_dict["name"] = name
        if is_available is not UNSET:
            field_dict["isAvailable"] = is_available
        if site_collection_error is not UNSET:
            field_dict["siteCollectionError"] = site_collection_error
        if msid is not UNSET:
            field_dict["msid"] = msid
        if data_location is not UNSET:
            field_dict["dataLocation"] = data_location
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

        def _parse_e_tag(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        e_tag = _parse_e_tag(d.pop("eTag", UNSET))


        parent_url = d.pop("parentUrl", UNSET)

        name = d.pop("name", UNSET)

        is_available = d.pop("isAvailable", UNSET)

        site_collection_error = d.pop("siteCollectionError", UNSET)

        def _parse_msid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        msid = _parse_msid(d.pop("msid", UNSET))


        def _parse_data_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_location = _parse_data_location(d.pop("dataLocation", UNSET))


        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        rest_site = cls(
            id=id,
            url=url,
            is_cloud=is_cloud,
            is_personal=is_personal,
            title=title,
            e_tag=e_tag,
            parent_url=parent_url,
            name=name,
            is_available=is_available,
            site_collection_error=site_collection_error,
            msid=msid,
            data_location=data_location,
            field_links=field_links,
        )


        rest_site.additional_properties = d
        return rest_site

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
