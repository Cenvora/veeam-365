from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_operator_explore_options_type import RESTOperatorExploreOptionsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_rbac_item_composed import RESTRbacItemComposed


T = TypeVar("T", bound="RESTOperatorExploreOptions")


@_attrs_define
class RESTOperatorExploreOptions:
    """
    Attributes:
        date_time (datetime.datetime | None | Unset):
        type_ (RESTOperatorExploreOptionsType | Unset):
        show_deleted (bool | None | Unset):
        show_all_versions (bool | None | Unset):
        scope (RESTRbacItemComposed | Unset):
        reason (str | Unset):
    """

    date_time: datetime.datetime | None | Unset = UNSET
    type_: RESTOperatorExploreOptionsType | Unset = UNSET
    show_deleted: bool | None | Unset = UNSET
    show_all_versions: bool | None | Unset = UNSET
    scope: RESTRbacItemComposed | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_time: None | str | Unset
        if isinstance(self.date_time, Unset):
            date_time = UNSET
        elif isinstance(self.date_time, datetime.datetime):
            date_time = self.date_time.isoformat()
        else:
            date_time = self.date_time

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        show_deleted: bool | None | Unset
        if isinstance(self.show_deleted, Unset):
            show_deleted = UNSET
        else:
            show_deleted = self.show_deleted

        show_all_versions: bool | None | Unset
        if isinstance(self.show_all_versions, Unset):
            show_all_versions = UNSET
        else:
            show_all_versions = self.show_all_versions

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if type_ is not UNSET:
            field_dict["type"] = type_
        if show_deleted is not UNSET:
            field_dict["showDeleted"] = show_deleted
        if show_all_versions is not UNSET:
            field_dict["showAllVersions"] = show_all_versions
        if scope is not UNSET:
            field_dict["scope"] = scope
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_rbac_item_composed import RESTRbacItemComposed

        d = dict(src_dict)

        def _parse_date_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_time_type_0 = isoparse(data)

                return date_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_time = _parse_date_time(d.pop("dateTime", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: RESTOperatorExploreOptionsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTOperatorExploreOptionsType(_type_)

        def _parse_show_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_deleted = _parse_show_deleted(d.pop("showDeleted", UNSET))

        def _parse_show_all_versions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_all_versions = _parse_show_all_versions(d.pop("showAllVersions", UNSET))

        _scope = d.pop("scope", UNSET)
        scope: RESTRbacItemComposed | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RESTRbacItemComposed.from_dict(_scope)

        reason = d.pop("reason", UNSET)

        rest_operator_explore_options = cls(
            date_time=date_time,
            type_=type_,
            show_deleted=show_deleted,
            show_all_versions=show_all_versions,
            scope=scope,
            reason=reason,
        )

        rest_operator_explore_options.additional_properties = d
        return rest_operator_explore_options

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
