from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTSaveOneDriveDocumentOptions")


@_attrs_define
class RESTSaveOneDriveDocumentOptions:
    """
    Attributes:
        as_zip (bool | None | Unset):
    """

    as_zip: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_zip: bool | None | Unset
        if isinstance(self.as_zip, Unset):
            as_zip = UNSET
        else:
            as_zip = self.as_zip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_zip is not UNSET:
            field_dict["asZip"] = as_zip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_as_zip(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        as_zip = _parse_as_zip(d.pop("asZip", UNSET))

        rest_save_one_drive_document_options = cls(
            as_zip=as_zip,
        )

        rest_save_one_drive_document_options.additional_properties = d
        return rest_save_one_drive_document_options

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
