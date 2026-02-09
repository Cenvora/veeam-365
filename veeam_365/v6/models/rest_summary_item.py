from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_summary_item_type import RESTSummaryItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTSummaryItem")


@_attrs_define
class RESTSummaryItem:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        title (str | Unset):
        type_ (RESTSummaryItemType | Unset):
        warnings (list[str] | Unset):
        error (str | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: RESTSummaryItemType | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        title = self.title

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTSummaryItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTSummaryItemType(_type_)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        error = d.pop("error", UNSET)

        rest_summary_item = cls(
            id=id,
            name=name,
            title=title,
            type_=type_,
            warnings=warnings,
            error=error,
        )

        rest_summary_item.additional_properties = d
        return rest_summary_item

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
