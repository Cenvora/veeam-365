from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_share_point_attachment_links import RESTSharePointAttachmentLinks


T = TypeVar("T", bound="RESTSharePointAttachment")


@_attrs_define
class RESTSharePointAttachment:
    """
    Attributes:
        size_bytes (int | Unset): Size of the SharePoint item attachment in *Bytes*.
        id (str | Unset): ID of the backed-up SharePoint item attachment.
        name (str | Unset): Name of the backed-up SharePoint item attachment.
        url (str | Unset): Path to the SharePoint item attachment.
        site_id (str | Unset): ID of the SharePoint site.
        item_id (str | Unset): ID of the SharePoint item.
        field_links (RESTSharePointAttachmentLinks | Unset):
    """

    size_bytes: int | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    site_id: str | Unset = UNSET
    item_id: str | Unset = UNSET
    field_links: RESTSharePointAttachmentLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size_bytes = self.size_bytes

        id = self.id

        name = self.name

        url = self.url

        site_id = self.site_id

        item_id = self.item_id

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_share_point_attachment_links import RESTSharePointAttachmentLinks

        d = dict(src_dict)
        size_bytes = d.pop("sizeBytes", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        site_id = d.pop("siteId", UNSET)

        item_id = d.pop("itemId", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTSharePointAttachmentLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTSharePointAttachmentLinks.from_dict(_field_links)

        rest_share_point_attachment = cls(
            size_bytes=size_bytes,
            id=id,
            name=name,
            url=url,
            site_id=site_id,
            item_id=item_id,
            field_links=field_links,
        )

        rest_share_point_attachment.additional_properties = d
        return rest_share_point_attachment

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
