from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_restore_share_point_item_config_document_version import (
    RESTRestoreSharePointItemConfigDocumentVersion,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_share_point_item import RESTSharePointItem


T = TypeVar("T", bound="RESTRestoreSharePointItemConfig")


@_attrs_define
class RESTRestoreSharePointItemConfig:
    """
    Attributes:
        item (RESTSharePointItem):
        document_version (RESTRestoreSharePointItemConfigDocumentVersion | Unset):
    """

    item: RESTSharePointItem
    document_version: RESTRestoreSharePointItemConfigDocumentVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item = self.item.to_dict()

        document_version: str | Unset = UNSET
        if not isinstance(self.document_version, Unset):
            document_version = self.document_version.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item": item,
            }
        )
        if document_version is not UNSET:
            field_dict["documentVersion"] = document_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_share_point_item import RESTSharePointItem

        d = dict(src_dict)
        item = RESTSharePointItem.from_dict(d.pop("item"))

        _document_version = d.pop("documentVersion", UNSET)
        document_version: RESTRestoreSharePointItemConfigDocumentVersion | Unset
        if isinstance(_document_version, Unset):
            document_version = UNSET
        else:
            document_version = RESTRestoreSharePointItemConfigDocumentVersion(_document_version)

        rest_restore_share_point_item_config = cls(
            item=item,
            document_version=document_version,
        )

        rest_restore_share_point_item_config.additional_properties = d
        return rest_restore_share_point_item_config

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
