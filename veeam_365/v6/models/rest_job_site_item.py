from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_job_backup_item_type import RESTJobBackupItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_job_site import RESTJobSite
    from ..models.rest_job_site_item_links import RESTJobSiteItemLinks


T = TypeVar("T", bound="RESTJobSiteItem")


@_attrs_define
class RESTJobSiteItem:
    """
    Attributes:
        type_ (RESTJobBackupItemType | Unset):
        site (RESTJobSite | Unset):
        id (str | Unset):
        field_links (RESTJobSiteItemLinks | Unset):
    """

    type_: RESTJobBackupItemType | Unset = UNSET
    site: RESTJobSite | Unset = UNSET
    id: str | Unset = UNSET
    field_links: RESTJobSiteItemLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        site: dict[str, Any] | Unset = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        id = self.id

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if site is not UNSET:
            field_dict["site"] = site
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_job_site import RESTJobSite
        from ..models.rest_job_site_item_links import RESTJobSiteItemLinks

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTJobBackupItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTJobBackupItemType(_type_)

        _site = d.pop("site", UNSET)
        site: RESTJobSite | Unset
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = RESTJobSite.from_dict(_site)

        id = d.pop("id", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTJobSiteItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTJobSiteItemLinks.from_dict(_field_links)

        rest_job_site_item = cls(
            type_=type_,
            site=site,
            id=id,
            field_links=field_links,
        )

        rest_job_site_item.additional_properties = d
        return rest_job_site_item

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
