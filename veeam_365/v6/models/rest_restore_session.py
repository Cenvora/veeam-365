from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_restore_session_result import RESTRestoreSessionResult
from ..models.rest_restore_session_state import RESTRestoreSessionState
from ..models.rest_restore_session_type import RESTRestoreSessionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTRestoreSession")


@_attrs_define
class RESTRestoreSession:
    """
    Attributes:
        id (UUID):  Example: 00000000-0000-0000-0000-000000000000.
        type_ (RESTRestoreSessionType):
        creation_time (datetime.datetime):
        state (RESTRestoreSessionState):
        result (RESTRestoreSessionResult):
        name (str | Unset):
        organization (str | Unset):
        end_time (datetime.datetime | None | Unset):
        initiated_by (str | Unset):
        details (str | Unset):
        scope_name (str | Unset):
        client_host (str | Unset):
        reason (str | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: UUID
    type_: RESTRestoreSessionType
    creation_time: datetime.datetime
    state: RESTRestoreSessionState
    result: RESTRestoreSessionResult
    name: str | Unset = UNSET
    organization: str | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    initiated_by: str | Unset = UNSET
    details: str | Unset = UNSET
    scope_name: str | Unset = UNSET
    client_host: str | Unset = UNSET
    reason: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_.value

        creation_time = self.creation_time.isoformat()

        state = self.state.value

        result = self.result.value

        name = self.name

        organization = self.organization

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        initiated_by = self.initiated_by

        details = self.details

        scope_name = self.scope_name

        client_host = self.client_host

        reason = self.reason

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "creationTime": creation_time,
                "state": state,
                "result": result,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if initiated_by is not UNSET:
            field_dict["initiatedBy"] = initiated_by
        if details is not UNSET:
            field_dict["details"] = details
        if scope_name is not UNSET:
            field_dict["scopeName"] = scope_name
        if client_host is not UNSET:
            field_dict["clientHost"] = client_host
        if reason is not UNSET:
            field_dict["reason"] = reason
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = RESTRestoreSessionType(d.pop("type"))

        creation_time = isoparse(d.pop("creationTime"))

        state = RESTRestoreSessionState(d.pop("state"))

        result = RESTRestoreSessionResult(d.pop("result"))

        name = d.pop("name", UNSET)

        organization = d.pop("organization", UNSET)

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        initiated_by = d.pop("initiatedBy", UNSET)

        details = d.pop("details", UNSET)

        scope_name = d.pop("scopeName", UNSET)

        client_host = d.pop("clientHost", UNSET)

        reason = d.pop("reason", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_restore_session = cls(
            id=id,
            type_=type_,
            creation_time=creation_time,
            state=state,
            result=result,
            name=name,
            organization=organization,
            end_time=end_time,
            initiated_by=initiated_by,
            details=details,
            scope_name=scope_name,
            client_host=client_host,
            reason=reason,
            field_links=field_links,
        )

        rest_restore_session.additional_properties = d
        return rest_restore_session

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
