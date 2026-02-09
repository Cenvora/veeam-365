from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_appointment_item_actions import RESTAppointmentItemActions
    from ..models.rest_appointment_item_links import RESTAppointmentItemLinks
    from ..models.rest_attachment import RESTAttachment


T = TypeVar("T", bound="RESTAppointmentItem")


@_attrs_define
class RESTAppointmentItem:
    """
    Attributes:
        mailbox_id (UUID | Unset): ID of the organization mailbox.
        attachments (list[RESTAttachment] | Unset): Array of attachment items for the appointment.
        organizer (str | Unset): Appointment organizer.
        attendees (str | Unset): Appointment attendees.
        start_time (datetime.datetime | Unset): Date and time when the appointment starts.
        end_time (datetime.datetime | Unset): Date and time when the appointment finishes.
        location (str | Unset): Location where the appointment is held.
        subject (str | Unset): Appointment subject.
        recurrence_pattern_format (str | Unset): Recurrence format.
        recurring (bool | Unset): Defines whether the appointment is recurring.
        item_class (str | Unset): Exchange item class.
        field_links (RESTAppointmentItemLinks | Unset):
        field_actions (RESTAppointmentItemActions | Unset):
        id (str | Unset): Exchange item ID.
    """

    mailbox_id: UUID | Unset = UNSET
    attachments: list[RESTAttachment] | Unset = UNSET
    organizer: str | Unset = UNSET
    attendees: str | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    location: str | Unset = UNSET
    subject: str | Unset = UNSET
    recurrence_pattern_format: str | Unset = UNSET
    recurring: bool | Unset = UNSET
    item_class: str | Unset = UNSET
    field_links: RESTAppointmentItemLinks | Unset = UNSET
    field_actions: RESTAppointmentItemActions | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mailbox_id: str | Unset = UNSET
        if not isinstance(self.mailbox_id, Unset):
            mailbox_id = str(self.mailbox_id)

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        organizer = self.organizer

        attendees = self.attendees

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        location = self.location

        subject = self.subject

        recurrence_pattern_format = self.recurrence_pattern_format

        recurring = self.recurring

        item_class = self.item_class

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mailbox_id is not UNSET:
            field_dict["mailboxId"] = mailbox_id
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if organizer is not UNSET:
            field_dict["organizer"] = organizer
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if location is not UNSET:
            field_dict["location"] = location
        if subject is not UNSET:
            field_dict["subject"] = subject
        if recurrence_pattern_format is not UNSET:
            field_dict["recurrencePatternFormat"] = recurrence_pattern_format
        if recurring is not UNSET:
            field_dict["recurring"] = recurring
        if item_class is not UNSET:
            field_dict["itemClass"] = item_class
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_appointment_item_actions import RESTAppointmentItemActions
        from ..models.rest_appointment_item_links import RESTAppointmentItemLinks
        from ..models.rest_attachment import RESTAttachment

        d = dict(src_dict)
        _mailbox_id = d.pop("mailboxId", UNSET)
        mailbox_id: UUID | Unset
        if isinstance(_mailbox_id, Unset):
            mailbox_id = UNSET
        else:
            mailbox_id = UUID(_mailbox_id)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[RESTAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = RESTAttachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        organizer = d.pop("organizer", UNSET)

        attendees = d.pop("attendees", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        location = d.pop("location", UNSET)

        subject = d.pop("subject", UNSET)

        recurrence_pattern_format = d.pop("recurrencePatternFormat", UNSET)

        recurring = d.pop("recurring", UNSET)

        item_class = d.pop("itemClass", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTAppointmentItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTAppointmentItemLinks.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTAppointmentItemActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTAppointmentItemActions.from_dict(_field_actions)

        id = d.pop("id", UNSET)

        rest_appointment_item = cls(
            mailbox_id=mailbox_id,
            attachments=attachments,
            organizer=organizer,
            attendees=attendees,
            start_time=start_time,
            end_time=end_time,
            location=location,
            subject=subject,
            recurrence_pattern_format=recurrence_pattern_format,
            recurring=recurring,
            item_class=item_class,
            field_links=field_links,
            field_actions=field_actions,
            id=id,
        )

        rest_appointment_item.additional_properties = d
        return rest_appointment_item

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
