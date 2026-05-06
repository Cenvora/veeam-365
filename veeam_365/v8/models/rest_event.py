from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_event_job_type import RESTEventJobType
from ..models.rest_event_type import RESTEventType
from ..models.rest_job_session_update_event_status import RESTJobSessionUpdateEventStatus
from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="RESTEvent")



@_attrs_define
class RESTEvent:
    """ 
        Attributes:
            event_type (RESTEventType): Type of the event.
            id (str | Unset): Restore session ID.
            e_tag (int | Unset): Version number that Veeam Backup for Microsoft 365 assigns if the restore session was
                modified.
            organization_id (UUID | Unset): Backed-up organization ID.
            job_type (RESTEventJobType | Unset): Type of a job for which the event was created.
            policy_id (str | Unset): Microsoft 365 Backup Storage policy ID.
            job_id (str | Unset): ID of the backup or backup copy job.
            status (RESTJobSessionUpdateEventStatus | Unset): Status of the job session.
            objects_etag (int | Unset): Version number that Veeam Backup for Microsoft 365 assigns if objects included to
                the restore point were modified.
     """

    event_type: RESTEventType
    id: str | Unset = UNSET
    e_tag: int | Unset = UNSET
    organization_id: UUID | Unset = UNSET
    job_type: RESTEventJobType | Unset = UNSET
    policy_id: str | Unset = UNSET
    job_id: str | Unset = UNSET
    status: RESTJobSessionUpdateEventStatus | Unset = UNSET
    objects_etag: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        id = self.id

        e_tag = self.e_tag

        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        job_type: str | Unset = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value


        policy_id = self.policy_id

        job_id = self.job_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        objects_etag = self.objects_etag


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "eventType": event_type,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if policy_id is not UNSET:
            field_dict["policyId"] = policy_id
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if status is not UNSET:
            field_dict["status"] = status
        if objects_etag is not UNSET:
            field_dict["objectsEtag"] = objects_etag

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = RESTEventType(d.pop("eventType"))




        id = d.pop("id", UNSET)

        e_tag = d.pop("eTag", UNSET)

        _organization_id = d.pop("organizationId", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id,  Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)




        _job_type = d.pop("jobType", UNSET)
        job_type: RESTEventJobType | Unset
        if isinstance(_job_type,  Unset):
            job_type = UNSET
        else:
            job_type = RESTEventJobType(_job_type)




        policy_id = d.pop("policyId", UNSET)

        job_id = d.pop("jobId", UNSET)

        _status = d.pop("status", UNSET)
        status: RESTJobSessionUpdateEventStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = RESTJobSessionUpdateEventStatus(_status)




        objects_etag = d.pop("objectsEtag", UNSET)

        rest_event = cls(
            event_type=event_type,
            id=id,
            e_tag=e_tag,
            organization_id=organization_id,
            job_type=job_type,
            policy_id=policy_id,
            job_id=job_id,
            status=status,
            objects_etag=objects_etag,
        )


        rest_event.additional_properties = d
        return rest_event

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
