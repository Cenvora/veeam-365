from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_restore_session_event_status import RESTRestoreSessionEventStatus
from ..models.rest_restore_session_event_type import RESTRestoreSessionEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTRestoreSessionEvent")


@_attrs_define
class RESTRestoreSessionEvent:
    """
    Attributes:
        id (UUID): ID of the restore session event. Example: 00000000-0000-0000-0000-000000000000.
        status (RESTRestoreSessionEventStatus): Status of the restore session.
        start_time (datetime.datetime): Date and time when the restore session event was started.
        message (str): Message of the restore session event.
        order (int): Order number of the restore session event.
        item_name (str | Unset): Name of the restored item.
        item_type (str | Unset): Type of the restored item.
        item_size_bytes (int | Unset): Size of the restored item in *Bytes*.
        source (str | Unset): Source path of the restored item.
        target (str | Unset): Target path for the item restore.
        type_ (RESTRestoreSessionEventType | Unset): Type of the restore session event.
        end_time (datetime.datetime | None | Unset): Date and time when the restore session event ended.
        duration (str | Unset): Duration of the restore session.
        title (str | Unset): Title of the restore session event.
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: UUID
    status: RESTRestoreSessionEventStatus
    start_time: datetime.datetime
    message: str
    order: int
    item_name: str | Unset = UNSET
    item_type: str | Unset = UNSET
    item_size_bytes: int | Unset = UNSET
    source: str | Unset = UNSET
    target: str | Unset = UNSET
    type_: RESTRestoreSessionEventType | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    duration: str | Unset = UNSET
    title: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        start_time = self.start_time.isoformat()

        message = self.message

        order = self.order

        item_name = self.item_name

        item_type = self.item_type

        item_size_bytes = self.item_size_bytes

        source = self.source

        target = self.target

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        duration = self.duration

        title = self.title

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "startTime": start_time,
                "message": message,
                "order": order,
            }
        )
        if item_name is not UNSET:
            field_dict["itemName"] = item_name
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if item_size_bytes is not UNSET:
            field_dict["itemSizeBytes"] = item_size_bytes
        if source is not UNSET:
            field_dict["source"] = source
        if target is not UNSET:
            field_dict["target"] = target
        if type_ is not UNSET:
            field_dict["type"] = type_
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if title is not UNSET:
            field_dict["title"] = title
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = RESTRestoreSessionEventStatus(d.pop("status"))

        start_time = isoparse(d.pop("startTime"))

        message = d.pop("message")

        order = d.pop("order")

        item_name = d.pop("itemName", UNSET)

        item_type = d.pop("itemType", UNSET)

        item_size_bytes = d.pop("itemSizeBytes", UNSET)

        source = d.pop("source", UNSET)

        target = d.pop("target", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTRestoreSessionEventType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTRestoreSessionEventType(_type_)

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

        duration = d.pop("duration", UNSET)

        title = d.pop("title", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_restore_session_event = cls(
            id=id,
            status=status,
            start_time=start_time,
            message=message,
            order=order,
            item_name=item_name,
            item_type=item_type,
            item_size_bytes=item_size_bytes,
            source=source,
            target=target,
            type_=type_,
            end_time=end_time,
            duration=duration,
            title=title,
            field_links=field_links,
        )

        rest_restore_session_event.additional_properties = d
        return rest_restore_session_event

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
