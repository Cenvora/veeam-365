from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_job_backup_item_type import RESTJobBackupItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_job_personal_sites_item_links import RESTJobPersonalSitesItemLinks


T = TypeVar("T", bound="RESTJobPersonalSitesItem")


@_attrs_define
class RESTJobPersonalSitesItem:
    """
    Attributes:
        type_ (RESTJobBackupItemType | Unset):
        id (str | Unset):
        field_links (RESTJobPersonalSitesItemLinks | Unset):
    """

    type_: RESTJobBackupItemType | Unset = UNSET
    id: str | Unset = UNSET
    field_links: RESTJobPersonalSitesItemLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_job_personal_sites_item_links import RESTJobPersonalSitesItemLinks

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTJobBackupItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTJobBackupItemType(_type_)

        id = d.pop("id", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTJobPersonalSitesItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTJobPersonalSitesItemLinks.from_dict(_field_links)

        rest_job_personal_sites_item = cls(
            type_=type_,
            id=id,
            field_links=field_links,
        )

        rest_job_personal_sites_item.additional_properties = d
        return rest_job_personal_sites_item

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
