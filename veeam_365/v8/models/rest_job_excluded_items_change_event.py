from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_event_type import RESTEventType






T = TypeVar("T", bound="RESTJobExcludedItemsChangeEvent")



@_attrs_define
class RESTJobExcludedItemsChangeEvent:
    """ 
        Attributes:
            event_type (RESTEventType): Type of the event.
            job_id (str): Backup job ID.
     """

    event_type: RESTEventType
    job_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        job_id = self.job_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "eventType": event_type,
            "jobId": job_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = RESTEventType(d.pop("eventType"))




        job_id = d.pop("jobId")

        rest_job_excluded_items_change_event = cls(
            event_type=event_type,
            job_id=job_id,
        )


        rest_job_excluded_items_change_event.additional_properties = d
        return rest_job_excluded_items_change_event

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
