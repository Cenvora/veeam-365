from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_job_session_status import RESTJobSessionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_job_statistics import RESTJobStatistics
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTJobSession")


@_attrs_define
class RESTJobSession:
    """
    Attributes:
        id (UUID | Unset):  Example: 00000000-0000-0000-0000-000000000000.
        details (None | str | Unset):
        creation_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        retry_count (int | Unset):
        progress (int | Unset):
        status (RESTJobSessionStatus | Unset):
        statistics (RESTJobStatistics | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: UUID | Unset = UNSET
    details: None | str | Unset = UNSET
    creation_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    retry_count: int | Unset = UNSET
    progress: int | Unset = UNSET
    status: RESTJobSessionStatus | Unset = UNSET
    statistics: RESTJobStatistics | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        details: None | str | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        creation_time: str | Unset = UNSET
        if not isinstance(self.creation_time, Unset):
            creation_time = self.creation_time.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        retry_count = self.retry_count

        progress = self.progress

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if details is not UNSET:
            field_dict["details"] = details
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if retry_count is not UNSET:
            field_dict["retryCount"] = retry_count
        if progress is not UNSET:
            field_dict["progress"] = progress
        if status is not UNSET:
            field_dict["status"] = status
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_job_statistics import RESTJobStatistics
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        _creation_time = d.pop("creationTime", UNSET)
        creation_time: datetime.datetime | Unset
        if isinstance(_creation_time, Unset):
            creation_time = UNSET
        else:
            creation_time = isoparse(_creation_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        retry_count = d.pop("retryCount", UNSET)

        progress = d.pop("progress", UNSET)

        _status = d.pop("status", UNSET)
        status: RESTJobSessionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTJobSessionStatus(_status)

        _statistics = d.pop("statistics", UNSET)
        statistics: RESTJobStatistics | Unset
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = RESTJobStatistics.from_dict(_statistics)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_job_session = cls(
            id=id,
            details=details,
            creation_time=creation_time,
            end_time=end_time,
            retry_count=retry_count,
            progress=progress,
            status=status,
            statistics=statistics,
            field_links=field_links,
        )

        rest_job_session.additional_properties = d
        return rest_job_session

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
