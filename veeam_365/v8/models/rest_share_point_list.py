from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_share_point_list_links import RESTSharePointListLinks


T = TypeVar("T", bound="RESTSharePointList")


@_attrs_define
class RESTSharePointList:
    """
    Attributes:
        id (str | Unset): ID of the SharePoint list.
        name (str | Unset): Name of the SharePoint list.
        url (str | Unset): Path to the SharePoint list.
        description (str | Unset): Description of the SharePoint list.
        creation_time (datetime.datetime | Unset): Date and time when the SharePoint list was created.
        site_id (str | Unset): ID of the SharePoint site.
        field_links (RESTSharePointListLinks | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    description: str | Unset = UNSET
    creation_time: datetime.datetime | Unset = UNSET
    site_id: str | Unset = UNSET
    field_links: RESTSharePointListLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        url = self.url

        description = self.description

        creation_time: str | Unset = UNSET
        if not isinstance(self.creation_time, Unset):
            creation_time = self.creation_time.isoformat()

        site_id = self.site_id

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_share_point_list_links import RESTSharePointListLinks

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        description = d.pop("description", UNSET)

        _creation_time = d.pop("creationTime", UNSET)
        creation_time: datetime.datetime | Unset
        if isinstance(_creation_time, Unset):
            creation_time = UNSET
        else:
            creation_time = isoparse(_creation_time)

        site_id = d.pop("siteId", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTSharePointListLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTSharePointListLinks.from_dict(_field_links)

        rest_share_point_list = cls(
            id=id,
            name=name,
            url=url,
            description=description,
            creation_time=creation_time,
            site_id=site_id,
            field_links=field_links,
        )

        rest_share_point_list.additional_properties = d
        return rest_share_point_list

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
