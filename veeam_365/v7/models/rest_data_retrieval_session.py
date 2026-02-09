from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_data_retrieval_session_status import RESTDataRetrievalSessionStatus
from ..models.rest_data_retrieval_session_type import RESTDataRetrievalSessionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTDataRetrievalSession")


@_attrs_define
class RESTDataRetrievalSession:
    """
    Attributes:
        id (UUID | Unset): Data retrieval session ID. Example: 00000000-0000-0000-0000-000000000000.
        name (str | Unset): Name of the data retrieval session.
        retrieval_id (UUID | Unset): Retrieval job ID. Example: 00000000-0000-0000-0000-000000000000.
        creation_time (datetime.datetime | Unset): Date and time when the data retrieval session was created.
        end_time (datetime.datetime | Unset): Date and time when the latest data retrieval session ended.
        progress (int | Unset): Number of processed objects during the data retrieval session.
        processed_objects (int | Unset): Number of items processed by the retrieval job.
        type_ (RESTDataRetrievalSessionType | Unset): Type of the data retrieval session.
        status (RESTDataRetrievalSessionStatus | Unset): Latest status of the retrieval job.
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    retrieval_id: UUID | Unset = UNSET
    creation_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    progress: int | Unset = UNSET
    processed_objects: int | Unset = UNSET
    type_: RESTDataRetrievalSessionType | Unset = UNSET
    status: RESTDataRetrievalSessionStatus | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        retrieval_id: str | Unset = UNSET
        if not isinstance(self.retrieval_id, Unset):
            retrieval_id = str(self.retrieval_id)

        creation_time: str | Unset = UNSET
        if not isinstance(self.creation_time, Unset):
            creation_time = self.creation_time.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        progress = self.progress

        processed_objects = self.processed_objects

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if retrieval_id is not UNSET:
            field_dict["retrievalId"] = retrieval_id
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if progress is not UNSET:
            field_dict["progress"] = progress
        if processed_objects is not UNSET:
            field_dict["processedObjects"] = processed_objects
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        _retrieval_id = d.pop("retrievalId", UNSET)
        retrieval_id: UUID | Unset
        if isinstance(_retrieval_id, Unset):
            retrieval_id = UNSET
        else:
            retrieval_id = UUID(_retrieval_id)

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

        progress = d.pop("progress", UNSET)

        processed_objects = d.pop("processedObjects", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTDataRetrievalSessionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTDataRetrievalSessionType(_type_)

        _status = d.pop("status", UNSET)
        status: RESTDataRetrievalSessionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTDataRetrievalSessionStatus(_status)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_data_retrieval_session = cls(
            id=id,
            name=name,
            retrieval_id=retrieval_id,
            creation_time=creation_time,
            end_time=end_time,
            progress=progress,
            processed_objects=processed_objects,
            type_=type_,
            status=status,
            field_links=field_links,
        )

        rest_data_retrieval_session.additional_properties = d
        return rest_data_retrieval_session

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
