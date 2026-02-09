from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_exchange_item_string_id import RESTExchangeItemStringId


T = TypeVar("T", bound="RESTSendToDifferentAddressOptions")


@_attrs_define
class RESTSendToDifferentAddressOptions:
    """
    Attributes:
        items (list[RESTExchangeItemStringId] | Unset):
        from_ (str | Unset):
        to (str | Unset):
        subject (str | Unset):
        text (str | Unset):
    """

    items: list[RESTExchangeItemStringId] | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    subject: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        from_ = self.from_

        to = self.to

        subject = self.subject

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text

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

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        rest_send_to_different_address_options = cls(
            items=items,
            from_=from_,
            to=to,
            subject=subject,
            text=text,
        )

        rest_send_to_different_address_options.additional_properties = d
        return rest_send_to_different_address_options

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
