from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_exchange_item_string_id import RESTExchangeItemStringId





T = TypeVar("T", bound="RESTSeveralItemsExportOptions")



@_attrs_define
class RESTSeveralItemsExportOptions:
    """ 
        Attributes:
            items (list[RESTExchangeItemStringId] | Unset): Specifies IDs of the mailbox items that you want to export. For
                more information on how to get such IDs, see [Get Mailbox Items](#/ExchangeItem/ExchangeItem_Get).
            enable_pst_size_limit (bool | None | Unset): Defines whether to set the size limit for the exported PST file. If
                set to true, indicates that you must specify the `pstSizeLimitBytes` property.
            pst_size_limit_bytes (int | None | Unset): Specifies the limit of the exported PST file in *Bytes*. You can
                specify the limit range from 1 GB to 49 GB.
     """

    items: list[RESTExchangeItemStringId] | Unset = UNSET
    enable_pst_size_limit: bool | None | Unset = UNSET
    pst_size_limit_bytes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_exchange_item_string_id import RESTExchangeItemStringId
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



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
        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if enable_pst_size_limit is not UNSET:
            field_dict["enablePstSizeLimit"] = enable_pst_size_limit
        if pst_size_limit_bytes is not UNSET:
            field_dict["pstSizeLimitBytes"] = pst_size_limit_bytes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_exchange_item_string_id import RESTExchangeItemStringId
        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[RESTExchangeItemStringId] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RESTExchangeItemStringId.from_dict(items_item_data)



                items.append(items_item)


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


        rest_several_items_export_options = cls(
            items=items,
            enable_pst_size_limit=enable_pst_size_limit,
            pst_size_limit_bytes=pst_size_limit_bytes,
        )


        rest_several_items_export_options.additional_properties = d
        return rest_several_items_export_options

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
