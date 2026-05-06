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





T = TypeVar("T", bound="RESTOperatorRestoreOptions")



@_attrs_define
class RESTOperatorRestoreOptions:
    """ 
        Attributes:
            changed_items (bool | Unset): Defines whether all versions of mailbox items will be restored.
            deleted_items (bool | Unset): Defines whether the deleted mailbox items will be restored.
            mark_restored_as_unread (bool | Unset): Defines whether the restored mailbox items will be marked as unread.
            folder (str | Unset): Specifies the folder to which you want to restore mailbox items.
            items (list[RESTExchangeItemStringId] | Unset): Specifies IDs of the mailbox items that you want to restore. For
                more information on how to get such IDs, see [Get Mailbox Items](#/ExchangeItem/ExchangeItem_Get).
            reason (str | Unset): Specifies a reason for the restore operation.
     """

    changed_items: bool | Unset = UNSET
    deleted_items: bool | Unset = UNSET
    mark_restored_as_unread: bool | Unset = UNSET
    folder: str | Unset = UNSET
    items: list[RESTExchangeItemStringId] | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_exchange_item_string_id import RESTExchangeItemStringId
        changed_items = self.changed_items

        deleted_items = self.deleted_items

        mark_restored_as_unread = self.mark_restored_as_unread

        folder = self.folder

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if changed_items is not UNSET:
            field_dict["changedItems"] = changed_items
        if deleted_items is not UNSET:
            field_dict["deletedItems"] = deleted_items
        if mark_restored_as_unread is not UNSET:
            field_dict["markRestoredAsUnread"] = mark_restored_as_unread
        if folder is not UNSET:
            field_dict["folder"] = folder
        if items is not UNSET:
            field_dict["items"] = items
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_exchange_item_string_id import RESTExchangeItemStringId
        d = dict(src_dict)
        changed_items = d.pop("changedItems", UNSET)

        deleted_items = d.pop("deletedItems", UNSET)

        mark_restored_as_unread = d.pop("markRestoredAsUnread", UNSET)

        folder = d.pop("folder", UNSET)

        _items = d.pop("items", UNSET)
        items: list[RESTExchangeItemStringId] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RESTExchangeItemStringId.from_dict(items_item_data)



                items.append(items_item)


        reason = d.pop("reason", UNSET)

        rest_operator_restore_options = cls(
            changed_items=changed_items,
            deleted_items=deleted_items,
            mark_restored_as_unread=mark_restored_as_unread,
            folder=folder,
            items=items,
            reason=reason,
        )


        rest_operator_restore_options.additional_properties = d
        return rest_operator_restore_options

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
