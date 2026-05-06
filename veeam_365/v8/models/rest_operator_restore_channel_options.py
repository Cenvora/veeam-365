from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RESTOperatorRestoreChannelOptions")



@_attrs_define
class RESTOperatorRestoreChannelOptions:
    """ 
        Attributes:
            restore_changed_items (bool | None): Defines whether to restore channel items that have been modified in the
                original location since the time when the backup was created.
            restore_missing_items (bool | None): Defines whether to restore channel items that are missed in the original
                location.
            restore_members (bool | None | Unset): Defines whether to restore members of the restored channel along with
                their roles.
            reason (str | Unset): Specifies a reason for the restore operation.
     """

    restore_changed_items: bool | None
    restore_missing_items: bool | None
    restore_members: bool | None | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        restore_changed_items: bool | None
        restore_changed_items = self.restore_changed_items

        restore_missing_items: bool | None
        restore_missing_items = self.restore_missing_items

        restore_members: bool | None | Unset
        if isinstance(self.restore_members, Unset):
            restore_members = UNSET
        else:
            restore_members = self.restore_members

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "restoreChangedItems": restore_changed_items,
            "restoreMissingItems": restore_missing_items,
        })
        if restore_members is not UNSET:
            field_dict["restoreMembers"] = restore_members
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_restore_changed_items(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        restore_changed_items = _parse_restore_changed_items(d.pop("restoreChangedItems"))


        def _parse_restore_missing_items(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        restore_missing_items = _parse_restore_missing_items(d.pop("restoreMissingItems"))


        def _parse_restore_members(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restore_members = _parse_restore_members(d.pop("restoreMembers", UNSET))


        reason = d.pop("reason", UNSET)

        rest_operator_restore_channel_options = cls(
            restore_changed_items=restore_changed_items,
            restore_missing_items=restore_missing_items,
            restore_members=restore_members,
            reason=reason,
        )


        rest_operator_restore_channel_options.additional_properties = d
        return rest_operator_restore_channel_options

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
