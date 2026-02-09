from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTRemoveAuditItemsOptions")


@_attrs_define
class RESTRemoveAuditItemsOptions:
    """
    Attributes:
        item_ids (list[str] | Unset): Specifies IDs of audit items that you want to remove. For more information on how
            to get such IDs, see [Get Audit Items](#tag/OrganizationAudit/operation/OrganizationAudit_Get).
    """

    item_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_ids: list[str] | Unset = UNSET
        if not isinstance(self.item_ids, Unset):
            item_ids = self.item_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_ids is not UNSET:
            field_dict["itemIds"] = item_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_ids = cast(list[str], d.pop("itemIds", UNSET))

        rest_remove_audit_items_options = cls(
            item_ids=item_ids,
        )

        rest_remove_audit_items_options.additional_properties = d
        return rest_remove_audit_items_options

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
