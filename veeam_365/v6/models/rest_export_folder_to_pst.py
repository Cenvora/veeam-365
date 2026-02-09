from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTExportFolderToPst")


@_attrs_define
class RESTExportFolderToPst:
    """
    Attributes:
        content_keyword (str | Unset):
        enable_pst_size_limit (bool | None | Unset):
        pst_size_limit_bytes (int | None | Unset):
    """

    content_keyword: str | Unset = UNSET
    enable_pst_size_limit: bool | None | Unset = UNSET
    pst_size_limit_bytes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_keyword = self.content_keyword

        enable_pst_size_limit: bool | None | Unset
        if isinstance(self.enable_pst_size_limit, Unset):
            enable_pst_size_limit = UNSET
        else:
            enable_pst_size_limit = self.enable_pst_size_limit

        pst_size_limit_bytes: int | None | Unset
        if isinstance(self.pst_size_limit_bytes, Unset):
            pst_size_limit_bytes = UNSET
        else:
            pst_size_limit_bytes = self.pst_size_limit_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_keyword is not UNSET:
            field_dict["contentKeyword"] = content_keyword
        if enable_pst_size_limit is not UNSET:
            field_dict["enablePstSizeLimit"] = enable_pst_size_limit
        if pst_size_limit_bytes is not UNSET:
            field_dict["pstSizeLimitBytes"] = pst_size_limit_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_keyword = d.pop("contentKeyword", UNSET)

        def _parse_enable_pst_size_limit(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_pst_size_limit = _parse_enable_pst_size_limit(d.pop("enablePstSizeLimit", UNSET))

        def _parse_pst_size_limit_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pst_size_limit_bytes = _parse_pst_size_limit_bytes(d.pop("pstSizeLimitBytes", UNSET))

        rest_export_folder_to_pst = cls(
            content_keyword=content_keyword,
            enable_pst_size_limit=enable_pst_size_limit,
            pst_size_limit_bytes=pst_size_limit_bytes,
        )

        rest_export_folder_to_pst.additional_properties = d
        return rest_export_folder_to_pst

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
