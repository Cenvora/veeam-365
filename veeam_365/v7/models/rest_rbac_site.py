from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTRbacSite")


@_attrs_define
class RESTRbacSite:
    """
    Attributes:
        id (str): ID of the organization site.
        url (None | str): Path to the organization site.
        title (str): Title of the organization site.
        is_cloud (bool | None): Defines whether this organization site is located in cloud.
        is_personal (bool | None): Defines whether the organization site is personal.
        parent_url (str | Unset): Path for the parent object.
    """

    id: str
    url: None | str
    title: str
    is_cloud: bool | None
    is_personal: bool | None
    parent_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url: None | str
        url = self.url

        title = self.title

        is_cloud: bool | None
        is_cloud = self.is_cloud

        is_personal: bool | None
        is_personal = self.is_personal

        parent_url = self.parent_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "title": title,
                "isCloud": is_cloud,
                "isPersonal": is_personal,
            }
        )
        if parent_url is not UNSET:
            field_dict["parentUrl"] = parent_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        title = d.pop("title")

        def _parse_is_cloud(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_cloud = _parse_is_cloud(d.pop("isCloud"))

        def _parse_is_personal(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_personal = _parse_is_personal(d.pop("isPersonal"))

        parent_url = d.pop("parentUrl", UNSET)

        rest_rbac_site = cls(
            id=id,
            url=url,
            title=title,
            is_cloud=is_cloud,
            is_personal=is_personal,
            parent_url=parent_url,
        )

        rest_rbac_site.additional_properties = d
        return rest_rbac_site

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
