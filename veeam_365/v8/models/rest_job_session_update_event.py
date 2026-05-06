from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_event_job_type import RESTEventJobType
from ..models.rest_event_type import RESTEventType
from ..models.rest_job_session_update_event_status import RESTJobSessionUpdateEventStatus






T = TypeVar("T", bound="RESTJobSessionUpdateEvent")



@_attrs_define
class RESTJobSessionUpdateEvent:
    """ 
        Attributes:
            event_type (RESTEventType): Type of the event.
            id (str): Job session ID.
            e_tag (int): Version number that Veeam Backup for Microsoft 365 assigns if the job session was modified.
            job_id (str): ID of the backup or backup copy job.
            status (RESTJobSessionUpdateEventStatus): Status of the job session.
            job_type (RESTEventJobType): Type of a job for which the event was created.
     """

    event_type: RESTEventType
    id: str
    e_tag: int
    job_id: str
    status: RESTJobSessionUpdateEventStatus
    job_type: RESTEventJobType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        id = self.id

        e_tag = self.e_tag

        job_id = self.job_id

        status = self.status.value

        job_type = self.job_type.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "eventType": event_type,
            "id": id,
            "eTag": e_tag,
            "jobId": job_id,
            "status": status,
            "jobType": job_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = RESTEventType(d.pop("eventType"))




        id = d.pop("id")

        e_tag = d.pop("eTag")

        job_id = d.pop("jobId")

        status = RESTJobSessionUpdateEventStatus(d.pop("status"))




        job_type = RESTEventJobType(d.pop("jobType"))




        rest_job_session_update_event = cls(
            event_type=event_type,
            id=id,
            e_tag=e_tag,
            job_id=job_id,
            status=status,
            job_type=job_type,
        )


        rest_job_session_update_event.additional_properties = d
        return rest_job_session_update_event

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
