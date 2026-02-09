from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_organization_sync_state_status import RESTOrganizationSyncStateStatus
from ..models.rest_organization_sync_state_type import RESTOrganizationSyncStateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTOrganizationSyncState")


@_attrs_define
class RESTOrganizationSyncState:
    """
    Attributes:
        type_ (RESTOrganizationSyncStateType | Unset): Type of the synchronization.
        status (RESTOrganizationSyncStateStatus | Unset): Status of the synchronization.
        last_sync_time (datetime.datetime | None | Unset): Date and time when the synchronization operation was
            performed for the last time.
        error (None | str | Unset): Error occurred during the synchronization operation.
        field_links (RESTLinkHALDictionary | Unset):
    """

    type_: RESTOrganizationSyncStateType | Unset = UNSET
    status: RESTOrganizationSyncStateStatus | Unset = UNSET
    last_sync_time: datetime.datetime | None | Unset = UNSET
    error: None | str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        last_sync_time: None | str | Unset
        if isinstance(self.last_sync_time, Unset):
            last_sync_time = UNSET
        elif isinstance(self.last_sync_time, datetime.datetime):
            last_sync_time = self.last_sync_time.isoformat()
        else:
            last_sync_time = self.last_sync_time

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if last_sync_time is not UNSET:
            field_dict["lastSyncTime"] = last_sync_time
        if error is not UNSET:
            field_dict["error"] = error
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTOrganizationSyncStateType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTOrganizationSyncStateType(_type_)

        _status = d.pop("status", UNSET)
        status: RESTOrganizationSyncStateStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTOrganizationSyncStateStatus(_status)

        def _parse_last_sync_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_sync_time_type_0 = isoparse(data)

                return last_sync_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_sync_time = _parse_last_sync_time(d.pop("lastSyncTime", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_organization_sync_state = cls(
            type_=type_,
            status=status,
            last_sync_time=last_sync_time,
            error=error,
            field_links=field_links,
        )

        rest_organization_sync_state.additional_properties = d
        return rest_organization_sync_state

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
