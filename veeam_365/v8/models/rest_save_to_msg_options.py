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





T = TypeVar("T", bound="RESTSaveToMsgOptions")



@_attrs_define
class RESTSaveToMsgOptions:
    """ 
        Attributes:
            items (list[RESTExchangeItemStringId] | Unset): Specifies IDs of the mailbox items that you want to save. For
                more information on how to get such IDs, see [Get Mailbox Items](#/ExchangeItem/ExchangeItem_Get).
     """

    items: list[RESTExchangeItemStringId] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_exchange_item_string_id import RESTExchangeItemStringId
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items

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


        rest_save_to_msg_options = cls(
            items=items,
        )


        rest_save_to_msg_options.additional_properties = d
        return rest_save_to_msg_options

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
