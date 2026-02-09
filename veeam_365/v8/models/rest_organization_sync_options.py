from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_organization_sync_options_type import RESTOrganizationSyncOptionsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTOrganizationSyncOptions")


@_attrs_define
class RESTOrganizationSyncOptions:
    """
    Attributes:
        type_ (RESTOrganizationSyncOptionsType | Unset): Specifies the synchronization type. The following values are
            available: <ul> <li>*Full* - all objects in the Microsoft organization will be synchronized with the
            organization cache database.</li> <li>*Incremental* - only new and modified objects in the Microsoft
            organization will be synchronized with the organization cache database.</li> </ul>
    """

    type_: RESTOrganizationSyncOptionsType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTOrganizationSyncOptionsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTOrganizationSyncOptionsType(_type_)

        rest_organization_sync_options = cls(
            type_=type_,
        )

        rest_organization_sync_options.additional_properties = d
        return rest_organization_sync_options

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
