from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_job_session_job_type import RESTJobSessionJobType
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
        id (UUID | Unset): Job session ID. Example: 00000000-0000-0000-0000-000000000000.
        repository_id (UUID | Unset): Backup repository ID. Example: 00000000-0000-0000-0000-000000000000.
        main_session_id (UUID | Unset): Job session ID. Example: 00000000-0000-0000-0000-000000000000.
        details (None | str | Unset): Job session details.
        creation_time (datetime.datetime | Unset): Date and time when the job session was created.
        end_time (datetime.datetime | None | Unset): Date and time when the latest job session ended.
        retry_count (int | Unset): Order number of the job session retry.
        job_will_be_retried (bool | None | Unset): Defines whether the job session will be restarted.
        progress (int | Unset): Number of processed objects during the job session.
        job_type (RESTJobSessionJobType | Unset): Type of the job session.
        status (RESTJobSessionStatus | Unset): Status of the backup or backup copy job.
        statistics (RESTJobStatistics | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: UUID | Unset = UNSET
    repository_id: UUID | Unset = UNSET
    main_session_id: UUID | Unset = UNSET
    details: None | str | Unset = UNSET
    creation_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    retry_count: int | Unset = UNSET
    job_will_be_retried: bool | None | Unset = UNSET
    progress: int | Unset = UNSET
    job_type: RESTJobSessionJobType | Unset = UNSET
    status: RESTJobSessionStatus | Unset = UNSET
    statistics: RESTJobStatistics | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        repository_id: str | Unset = UNSET
        if not isinstance(self.repository_id, Unset):
            repository_id = str(self.repository_id)

        main_session_id: str | Unset = UNSET
        if not isinstance(self.main_session_id, Unset):
            main_session_id = str(self.main_session_id)

        details: None | str | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        creation_time: str | Unset = UNSET
        if not isinstance(self.creation_time, Unset):
            creation_time = self.creation_time.isoformat()

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        retry_count = self.retry_count

        job_will_be_retried: bool | None | Unset
        if isinstance(self.job_will_be_retried, Unset):
            job_will_be_retried = UNSET
        else:
            job_will_be_retried = self.job_will_be_retried

        progress = self.progress

        job_type: str | Unset = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value

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
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if main_session_id is not UNSET:
            field_dict["mainSessionId"] = main_session_id
        if details is not UNSET:
            field_dict["details"] = details
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if retry_count is not UNSET:
            field_dict["retryCount"] = retry_count
        if job_will_be_retried is not UNSET:
            field_dict["jobWillBeRetried"] = job_will_be_retried
        if progress is not UNSET:
            field_dict["progress"] = progress
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
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

        _repository_id = d.pop("repositoryId", UNSET)
        repository_id: UUID | Unset
        if isinstance(_repository_id, Unset):
            repository_id = UNSET
        else:
            repository_id = UUID(_repository_id)

        _main_session_id = d.pop("mainSessionId", UNSET)
        main_session_id: UUID | Unset
        if isinstance(_main_session_id, Unset):
            main_session_id = UNSET
        else:
            main_session_id = UUID(_main_session_id)

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

        retry_count = d.pop("retryCount", UNSET)

        def _parse_job_will_be_retried(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        job_will_be_retried = _parse_job_will_be_retried(d.pop("jobWillBeRetried", UNSET))

        progress = d.pop("progress", UNSET)

        _job_type = d.pop("jobType", UNSET)
        job_type: RESTJobSessionJobType | Unset
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = RESTJobSessionJobType(_job_type)

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
            repository_id=repository_id,
            main_session_id=main_session_id,
            details=details,
            creation_time=creation_time,
            end_time=end_time,
            retry_count=retry_count,
            job_will_be_retried=job_will_be_retried,
            progress=progress,
            job_type=job_type,
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
