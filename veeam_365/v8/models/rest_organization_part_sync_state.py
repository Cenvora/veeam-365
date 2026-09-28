from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_organization_current_sync_state import RESTOrganizationCurrentSyncState
    from ..models.rest_organization_last_sync_state import RESTOrganizationLastSyncState


T = TypeVar("T", bound="RESTOrganizationPartSyncState")


@_attrs_define
class RESTOrganizationPartSyncState:
    """
    Attributes:
        last_successful_sync_time (datetime.datetime | None | Unset): Date and time of the latest successful
            synchronization.
        last_sync_state (None | RESTOrganizationLastSyncState | Unset): Details of the latest synchronization of the
            organization part.
        current_sync_state (None | RESTOrganizationCurrentSyncState | Unset): Details of the synchronization of the
            organization part that is currently queued or running.
    """

    last_successful_sync_time: datetime.datetime | None | Unset = UNSET
    last_sync_state: None | RESTOrganizationLastSyncState | Unset = UNSET
    current_sync_state: None | RESTOrganizationCurrentSyncState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_organization_current_sync_state import RESTOrganizationCurrentSyncState
        from ..models.rest_organization_last_sync_state import RESTOrganizationLastSyncState

        last_successful_sync_time: None | str | Unset
        if isinstance(self.last_successful_sync_time, Unset):
            last_successful_sync_time = UNSET
        elif isinstance(self.last_successful_sync_time, datetime.datetime):
            last_successful_sync_time = self.last_successful_sync_time.isoformat()
        else:
            last_successful_sync_time = self.last_successful_sync_time

        last_sync_state: dict[str, Any] | None | Unset
        if isinstance(self.last_sync_state, Unset):
            last_sync_state = UNSET
        elif isinstance(self.last_sync_state, RESTOrganizationLastSyncState):
            last_sync_state = self.last_sync_state.to_dict()
        else:
            last_sync_state = self.last_sync_state

        current_sync_state: dict[str, Any] | None | Unset
        if isinstance(self.current_sync_state, Unset):
            current_sync_state = UNSET
        elif isinstance(self.current_sync_state, RESTOrganizationCurrentSyncState):
            current_sync_state = self.current_sync_state.to_dict()
        else:
            current_sync_state = self.current_sync_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_successful_sync_time is not UNSET:
            field_dict["lastSuccessfulSyncTime"] = last_successful_sync_time
        if last_sync_state is not UNSET:
            field_dict["lastSyncState"] = last_sync_state
        if current_sync_state is not UNSET:
            field_dict["currentSyncState"] = current_sync_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_organization_current_sync_state import RESTOrganizationCurrentSyncState
        from ..models.rest_organization_last_sync_state import RESTOrganizationLastSyncState

        d = dict(src_dict)

        def _parse_last_successful_sync_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_successful_sync_time_type_0 = isoparse(data)

                return last_successful_sync_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_successful_sync_time = _parse_last_successful_sync_time(d.pop("lastSuccessfulSyncTime", UNSET))

        def _parse_last_sync_state(data: object) -> None | RESTOrganizationLastSyncState | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_sync_state_type_1 = RESTOrganizationLastSyncState.from_dict(data)

                return last_sync_state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTOrganizationLastSyncState | Unset, data)

        last_sync_state = _parse_last_sync_state(d.pop("lastSyncState", UNSET))

        def _parse_current_sync_state(data: object) -> None | RESTOrganizationCurrentSyncState | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_sync_state_type_1 = RESTOrganizationCurrentSyncState.from_dict(data)

                return current_sync_state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTOrganizationCurrentSyncState | Unset, data)

        current_sync_state = _parse_current_sync_state(d.pop("currentSyncState", UNSET))

        rest_organization_part_sync_state = cls(
            last_successful_sync_time=last_successful_sync_time,
            last_sync_state=last_sync_state,
            current_sync_state=current_sync_state,
        )

        rest_organization_part_sync_state.additional_properties = d
        return rest_organization_part_sync_state

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
