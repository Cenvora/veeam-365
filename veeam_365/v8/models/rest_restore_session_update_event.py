from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_event_type import RESTEventType

T = TypeVar("T", bound="RESTRestoreSessionUpdateEvent")


@_attrs_define
class RESTRestoreSessionUpdateEvent:
    """
    Attributes:
        event_type (RESTEventType): Type of the event.
        id (str): Restore session ID.
        e_tag (int): Version number that Veeam Backup for Microsoft 365 assigns if the restore session was modified.
    """

    event_type: RESTEventType
    id: str
    e_tag: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        id = self.id

        e_tag = self.e_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "id": id,
                "eTag": e_tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = RESTEventType(d.pop("eventType"))

        id = d.pop("id")

        e_tag = d.pop("eTag")

        rest_restore_session_update_event = cls(
            event_type=event_type,
            id=id,
            e_tag=e_tag,
        )

        rest_restore_session_update_event.additional_properties = d
        return rest_restore_session_update_event

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
