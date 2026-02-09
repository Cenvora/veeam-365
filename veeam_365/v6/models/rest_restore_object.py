from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_restore_object_type import RESTRestoreObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTRestoreObject")


@_attrs_define
class RESTRestoreObject:
    """
    Attributes:
        id (UUID | Unset):  Example: 00000000-0000-0000-0000-000000000000.
        path (str | Unset):
        title (str | Unset):
        type_ (RESTRestoreObjectType | Unset):
        warnings (list[str] | Unset):
        error (str | Unset):
    """

    id: UUID | Unset = UNSET
    path: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: RESTRestoreObjectType | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        path = self.path

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
        if path is not UNSET:
            field_dict["path"] = path
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
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        path = d.pop("path", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTRestoreObjectType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTRestoreObjectType(_type_)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        error = d.pop("error", UNSET)

        rest_restore_object = cls(
            id=id,
            path=path,
            title=title,
            type_=type_,
            warnings=warnings,
            error=error,
        )

        rest_restore_object.additional_properties = d
        return rest_restore_object

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
