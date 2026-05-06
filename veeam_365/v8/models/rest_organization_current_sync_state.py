from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_organization_current_sync_state_status import RESTOrganizationCurrentSyncStateStatus
from ..models.rest_organization_current_sync_state_type import RESTOrganizationCurrentSyncStateType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="RESTOrganizationCurrentSyncState")



@_attrs_define
class RESTOrganizationCurrentSyncState:
    """ 
        Attributes:
            type_ (RESTOrganizationCurrentSyncStateType | Unset): Type of the synchronization.
            scheduled_time (datetime.datetime | None | Unset): Date and time when the synchronization was scheduled.
            start_time (datetime.datetime | None | Unset): Date and time when the synchronization was started.
            status (RESTOrganizationCurrentSyncStateStatus | Unset): Status of the synchronization.
     """

    type_: RESTOrganizationCurrentSyncStateType | Unset = UNSET
    scheduled_time: datetime.datetime | None | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    status: RESTOrganizationCurrentSyncStateStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        scheduled_time: None | str | Unset
        if isinstance(self.scheduled_time, Unset):
            scheduled_time = UNSET
        elif isinstance(self.scheduled_time, datetime.datetime):
            scheduled_time = self.scheduled_time.isoformat()
        else:
            scheduled_time = self.scheduled_time

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if scheduled_time is not UNSET:
            field_dict["scheduledTime"] = scheduled_time
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTOrganizationCurrentSyncStateType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RESTOrganizationCurrentSyncStateType(_type_)




        def _parse_scheduled_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_time_type_0 = isoparse(data)



                return scheduled_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_time = _parse_scheduled_time(d.pop("scheduledTime", UNSET))


        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)



                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))


        _status = d.pop("status", UNSET)
        status: RESTOrganizationCurrentSyncStateStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = RESTOrganizationCurrentSyncStateStatus(_status)




        rest_organization_current_sync_state = cls(
            type_=type_,
            scheduled_time=scheduled_time,
            start_time=start_time,
            status=status,
        )


        rest_organization_current_sync_state.additional_properties = d
        return rest_organization_current_sync_state

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
