from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_organization_last_sync_state_result import RESTOrganizationLastSyncStateResult
from ..models.rest_organization_last_sync_state_type import RESTOrganizationLastSyncStateType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="RESTOrganizationLastSyncState")



@_attrs_define
class RESTOrganizationLastSyncState:
    """ 
        Attributes:
            type_ (RESTOrganizationLastSyncStateType | Unset): Type of the synchronization.
            result (RESTOrganizationLastSyncStateResult | Unset): Result of the synchronization.
            start_time (datetime.datetime | Unset): Date and time when the synchronization was started.
            end_time (datetime.datetime | Unset): Date and time when the synchronization ended.
            error (None | str | Unset): Error occurred during the synchronization operation.
     """

    type_: RESTOrganizationLastSyncStateType | Unset = UNSET
    result: RESTOrganizationLastSyncStateResult | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value


        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if result is not UNSET:
            field_dict["result"] = result
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTOrganizationLastSyncStateType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RESTOrganizationLastSyncStateType(_type_)




        _result = d.pop("result", UNSET)
        result: RESTOrganizationLastSyncStateResult | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = RESTOrganizationLastSyncStateResult(_result)




        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time,  Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)




        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time,  Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)




        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        rest_organization_last_sync_state = cls(
            type_=type_,
            result=result,
            start_time=start_time,
            end_time=end_time,
            error=error,
        )


        rest_organization_last_sync_state.additional_properties = d
        return rest_organization_last_sync_state

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
