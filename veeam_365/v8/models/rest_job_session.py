from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_job_session_job_session_config_type import RESTJobSessionJobSessionConfigType
from ..models.rest_job_session_job_type import RESTJobSessionJobType
from ..models.rest_job_session_status import RESTJobSessionStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.rest_job_statistics import RESTJobStatistics
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary





T = TypeVar("T", bound="RESTJobSession")



@_attrs_define
class RESTJobSession:
    """ 
        Attributes:
            id (UUID | Unset): Job session ID. Example: 00000000-0000-0000-0000-000000000000.
            job_id (UUID | Unset): Job ID. Example: 00000000-0000-0000-0000-000000000000.
            repository_id (UUID | Unset): Backup repository ID. Example: 00000000-0000-0000-0000-000000000000.
            main_session_id (UUID | Unset): ID of a main job session that has been finished with an error or warning. This
                property is only available for retry sessions. Example: 00000000-0000-0000-0000-000000000000.
            details (None | str | Unset): Job session details.
            creation_time (datetime.datetime | Unset): Date and time when the job session was created.
            end_time (datetime.datetime | None | Unset): Date and time when the latest job session ended.
            retry_count (int | Unset): Order number of the job session retry.
            job_will_be_retried (bool | None | Unset): Defines whether the job session will be restarted.
            progress (int | Unset): Number of processed objects during the job session.
            job_type (RESTJobSessionJobType | Unset): Type of the job session.
            job_session_config_type (RESTJobSessionJobSessionConfigType | Unset): Type of the job synchronization.
            status (RESTJobSessionStatus | Unset): Status of the backup or backup copy job.
            statistics (RESTJobStatistics | Unset):
            e_tag (int | Unset): Version number that Veeam Backup for Microsoft 365 assigns if the job session was modified.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
            proxy_id (None | Unset | UUID): Backup proxy server ID. Example: 00000000-0000-0000-0000-000000000000.
            proxy_pool_id (None | Unset | UUID): Backup proxy pool ID. Example: 00000000-0000-0000-0000-000000000000.
     """

    id: UUID | Unset = UNSET
    job_id: UUID | Unset = UNSET
    repository_id: UUID | Unset = UNSET
    main_session_id: UUID | Unset = UNSET
    details: None | str | Unset = UNSET
    creation_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    retry_count: int | Unset = UNSET
    job_will_be_retried: bool | None | Unset = UNSET
    progress: int | Unset = UNSET
    job_type: RESTJobSessionJobType | Unset = UNSET
    job_session_config_type: RESTJobSessionJobSessionConfigType | Unset = UNSET
    status: RESTJobSessionStatus | Unset = UNSET
    statistics: RESTJobStatistics | Unset = UNSET
    e_tag: int | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    proxy_id: None | Unset | UUID = UNSET
    proxy_pool_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_job_statistics import RESTJobStatistics
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

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


        job_session_config_type: str | Unset = UNSET
        if not isinstance(self.job_session_config_type, Unset):
            job_session_config_type = self.job_session_config_type.value


        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        e_tag = self.e_tag

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        proxy_id: None | str | Unset
        if isinstance(self.proxy_id, Unset):
            proxy_id = UNSET
        elif isinstance(self.proxy_id, UUID):
            proxy_id = str(self.proxy_id)
        else:
            proxy_id = self.proxy_id

        proxy_pool_id: None | str | Unset
        if isinstance(self.proxy_pool_id, Unset):
            proxy_pool_id = UNSET
        elif isinstance(self.proxy_pool_id, UUID):
            proxy_pool_id = str(self.proxy_pool_id)
        else:
            proxy_pool_id = self.proxy_pool_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
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
        if job_session_config_type is not UNSET:
            field_dict["jobSessionConfigType"] = job_session_config_type
        if status is not UNSET:
            field_dict["status"] = status
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if proxy_id is not UNSET:
            field_dict["proxyId"] = proxy_id
        if proxy_pool_id is not UNSET:
            field_dict["proxyPoolId"] = proxy_pool_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_job_statistics import RESTJobStatistics
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _job_id = d.pop("jobId", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id,  Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)




        _repository_id = d.pop("repositoryId", UNSET)
        repository_id: UUID | Unset
        if isinstance(_repository_id,  Unset):
            repository_id = UNSET
        else:
            repository_id = UUID(_repository_id)




        _main_session_id = d.pop("mainSessionId", UNSET)
        main_session_id: UUID | Unset
        if isinstance(_main_session_id,  Unset):
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
        if isinstance(_creation_time,  Unset):
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
        if isinstance(_job_type,  Unset):
            job_type = UNSET
        else:
            job_type = RESTJobSessionJobType(_job_type)




        _job_session_config_type = d.pop("jobSessionConfigType", UNSET)
        job_session_config_type: RESTJobSessionJobSessionConfigType | Unset
        if isinstance(_job_session_config_type,  Unset):
            job_session_config_type = UNSET
        else:
            job_session_config_type = RESTJobSessionJobSessionConfigType(_job_session_config_type)




        _status = d.pop("status", UNSET)
        status: RESTJobSessionStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = RESTJobSessionStatus(_status)




        _statistics = d.pop("statistics", UNSET)
        statistics: RESTJobStatistics | Unset
        if isinstance(_statistics,  Unset):
            statistics = UNSET
        else:
            statistics = RESTJobStatistics.from_dict(_statistics)




        e_tag = d.pop("eTag", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        def _parse_proxy_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_id_type_0 = UUID(data)



                return proxy_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        proxy_id = _parse_proxy_id(d.pop("proxyId", UNSET))


        def _parse_proxy_pool_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_pool_id_type_0 = UUID(data)



                return proxy_pool_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        proxy_pool_id = _parse_proxy_pool_id(d.pop("proxyPoolId", UNSET))


        rest_job_session = cls(
            id=id,
            job_id=job_id,
            repository_id=repository_id,
            main_session_id=main_session_id,
            details=details,
            creation_time=creation_time,
            end_time=end_time,
            retry_count=retry_count,
            job_will_be_retried=job_will_be_retried,
            progress=progress,
            job_type=job_type,
            job_session_config_type=job_session_config_type,
            status=status,
            statistics=statistics,
            e_tag=e_tag,
            field_links=field_links,
            proxy_id=proxy_id,
            proxy_pool_id=proxy_pool_id,
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
