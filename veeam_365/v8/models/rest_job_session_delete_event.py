from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_event_job_type import RESTEventJobType
from ..models.rest_event_type import RESTEventType

T = TypeVar("T", bound="RESTJobSessionDeleteEvent")


@_attrs_define
class RESTJobSessionDeleteEvent:
    """
    Attributes:
        event_type (RESTEventType): Type of the event.
        id (str): Job session ID.
        job_type (RESTEventJobType): Type of a job for which the event was created.
    """

    event_type: RESTEventType
    id: str
    job_type: RESTEventJobType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        id = self.id

        job_type = self.job_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "id": id,
                "jobType": job_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = RESTEventType(d.pop("eventType"))

        id = d.pop("id")

        job_type = RESTEventJobType(d.pop("jobType"))

        rest_job_session_delete_event = cls(
            event_type=event_type,
            id=id,
            job_type=job_type,
        )

        rest_job_session_delete_event.additional_properties = d
        return rest_job_session_delete_event

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
