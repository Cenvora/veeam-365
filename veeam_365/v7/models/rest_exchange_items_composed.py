from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_exchange_item_importance import RESTExchangeItemImportance
from ..models.rest_task_item_status import RESTTaskItemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_attachment import RESTAttachment
    from ..models.rest_exchange_items_composed_actions import RESTExchangeItemsComposedActions
    from ..models.rest_exchange_items_composed_links import RESTExchangeItemsComposedLinks


T = TypeVar("T", bound="RESTExchangeItemsComposed")


@_attrs_define
class RESTExchangeItemsComposed:
    """
    Attributes:
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
        field_links (RESTExchangeItemsComposedLinks | Unset):
        field_actions (RESTExchangeItemsComposedActions | Unset):
        id (str | Unset): Exchange item ID.
        name (str | Unset): Name of the contact group.
        address (str | Unset): Contact address.
        business_phone (str | Unset): Business phone number of the contact.
        company (str | Unset): Company of the contact.
        display_as (str | Unset): Contact alias.
        email (str | Unset): Contact email.
        fax (str | Unset): Fax number of the contact.
        file_as (str | Unset): Name of the file.
        full_name (str | Unset): Contact full name.
        home_phone (str | Unset): Home phone number of the contact.
        im_address (str | Unset): Instant messenger address.
        job_title (str | Unset): Contact job title.
        mobile (str | Unset): Contact mobile.
        web_page (str | Unset): Contact webpage.
        from_ (str | Unset): Name of the discussion author.
        posted_on (datetime.datetime | Unset): Date and time when the discussion was started.
        importance (RESTExchangeItemImportance | Unset): Message importance.
        cc (str | Unset): Recipient email address in carbon copy.
        bcc (str | Unset): Recipient address in blind carbon copy.
        to (str | Unset): Recipient email address.
        sent (datetime.datetime | Unset): Date and time when the message was sent.
        received (datetime.datetime | Unset): Date and time when the message was received.
        reminder (bool | Unset): Defines whether the message was sent with the reminder.
        duration (int | Unset): Duration of the journal entry in hours.
        entry_type (str | Unset): Type of the journal entry.
        date (datetime.datetime | Unset): Date when the note was created.
        status (RESTTaskItemStatus | Unset): Task status.
        percent_complete (float | Unset): Task progress.
        start_date (datetime.datetime | Unset): Date and time when the task was started.
        due_date (datetime.datetime | Unset): Date and time when the task must be completed.
        owner (str | Unset): Task owner.
    """

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
    field_links: RESTExchangeItemsComposedLinks | Unset = UNSET
    field_actions: RESTExchangeItemsComposedActions | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    address: str | Unset = UNSET
    business_phone: str | Unset = UNSET
    company: str | Unset = UNSET
    display_as: str | Unset = UNSET
    email: str | Unset = UNSET
    fax: str | Unset = UNSET
    file_as: str | Unset = UNSET
    full_name: str | Unset = UNSET
    home_phone: str | Unset = UNSET
    im_address: str | Unset = UNSET
    job_title: str | Unset = UNSET
    mobile: str | Unset = UNSET
    web_page: str | Unset = UNSET
    from_: str | Unset = UNSET
    posted_on: datetime.datetime | Unset = UNSET
    importance: RESTExchangeItemImportance | Unset = UNSET
    cc: str | Unset = UNSET
    bcc: str | Unset = UNSET
    to: str | Unset = UNSET
    sent: datetime.datetime | Unset = UNSET
    received: datetime.datetime | Unset = UNSET
    reminder: bool | Unset = UNSET
    duration: int | Unset = UNSET
    entry_type: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    status: RESTTaskItemStatus | Unset = UNSET
    percent_complete: float | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    due_date: datetime.datetime | Unset = UNSET
    owner: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        name = self.name

        address = self.address

        business_phone = self.business_phone

        company = self.company

        display_as = self.display_as

        email = self.email

        fax = self.fax

        file_as = self.file_as

        full_name = self.full_name

        home_phone = self.home_phone

        im_address = self.im_address

        job_title = self.job_title

        mobile = self.mobile

        web_page = self.web_page

        from_ = self.from_

        posted_on: str | Unset = UNSET
        if not isinstance(self.posted_on, Unset):
            posted_on = self.posted_on.isoformat()

        importance: str | Unset = UNSET
        if not isinstance(self.importance, Unset):
            importance = self.importance.value

        cc = self.cc

        bcc = self.bcc

        to = self.to

        sent: str | Unset = UNSET
        if not isinstance(self.sent, Unset):
            sent = self.sent.isoformat()

        received: str | Unset = UNSET
        if not isinstance(self.received, Unset):
            received = self.received.isoformat()

        reminder = self.reminder

        duration = self.duration

        entry_type = self.entry_type

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        percent_complete = self.percent_complete

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        due_date: str | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        owner = self.owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if business_phone is not UNSET:
            field_dict["businessPhone"] = business_phone
        if company is not UNSET:
            field_dict["company"] = company
        if display_as is not UNSET:
            field_dict["displayAs"] = display_as
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if file_as is not UNSET:
            field_dict["fileAs"] = file_as
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if home_phone is not UNSET:
            field_dict["homePhone"] = home_phone
        if im_address is not UNSET:
            field_dict["imAddress"] = im_address
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if web_page is not UNSET:
            field_dict["webPage"] = web_page
        if from_ is not UNSET:
            field_dict["from"] = from_
        if posted_on is not UNSET:
            field_dict["postedOn"] = posted_on
        if importance is not UNSET:
            field_dict["importance"] = importance
        if cc is not UNSET:
            field_dict["cc"] = cc
        if bcc is not UNSET:
            field_dict["bcc"] = bcc
        if to is not UNSET:
            field_dict["to"] = to
        if sent is not UNSET:
            field_dict["sent"] = sent
        if received is not UNSET:
            field_dict["received"] = received
        if reminder is not UNSET:
            field_dict["reminder"] = reminder
        if duration is not UNSET:
            field_dict["duration"] = duration
        if entry_type is not UNSET:
            field_dict["entryType"] = entry_type
        if date is not UNSET:
            field_dict["date"] = date
        if status is not UNSET:
            field_dict["status"] = status
        if percent_complete is not UNSET:
            field_dict["percentComplete"] = percent_complete
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_attachment import RESTAttachment
        from ..models.rest_exchange_items_composed_actions import RESTExchangeItemsComposedActions
        from ..models.rest_exchange_items_composed_links import RESTExchangeItemsComposedLinks

        d = dict(src_dict)
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
        field_links: RESTExchangeItemsComposedLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTExchangeItemsComposedLinks.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTExchangeItemsComposedActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTExchangeItemsComposedActions.from_dict(_field_actions)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        business_phone = d.pop("businessPhone", UNSET)

        company = d.pop("company", UNSET)

        display_as = d.pop("displayAs", UNSET)

        email = d.pop("email", UNSET)

        fax = d.pop("fax", UNSET)

        file_as = d.pop("fileAs", UNSET)

        full_name = d.pop("fullName", UNSET)

        home_phone = d.pop("homePhone", UNSET)

        im_address = d.pop("imAddress", UNSET)

        job_title = d.pop("jobTitle", UNSET)

        mobile = d.pop("mobile", UNSET)

        web_page = d.pop("webPage", UNSET)

        from_ = d.pop("from", UNSET)

        _posted_on = d.pop("postedOn", UNSET)
        posted_on: datetime.datetime | Unset
        if isinstance(_posted_on, Unset):
            posted_on = UNSET
        else:
            posted_on = isoparse(_posted_on)

        _importance = d.pop("importance", UNSET)
        importance: RESTExchangeItemImportance | Unset
        if isinstance(_importance, Unset):
            importance = UNSET
        else:
            importance = RESTExchangeItemImportance(_importance)

        cc = d.pop("cc", UNSET)

        bcc = d.pop("bcc", UNSET)

        to = d.pop("to", UNSET)

        _sent = d.pop("sent", UNSET)
        sent: datetime.datetime | Unset
        if isinstance(_sent, Unset):
            sent = UNSET
        else:
            sent = isoparse(_sent)

        _received = d.pop("received", UNSET)
        received: datetime.datetime | Unset
        if isinstance(_received, Unset):
            received = UNSET
        else:
            received = isoparse(_received)

        reminder = d.pop("reminder", UNSET)

        duration = d.pop("duration", UNSET)

        entry_type = d.pop("entryType", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _status = d.pop("status", UNSET)
        status: RESTTaskItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTTaskItemStatus(_status)

        percent_complete = d.pop("percentComplete", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _due_date = d.pop("dueDate", UNSET)
        due_date: datetime.datetime | Unset
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        owner = d.pop("owner", UNSET)

        rest_exchange_items_composed = cls(
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
            name=name,
            address=address,
            business_phone=business_phone,
            company=company,
            display_as=display_as,
            email=email,
            fax=fax,
            file_as=file_as,
            full_name=full_name,
            home_phone=home_phone,
            im_address=im_address,
            job_title=job_title,
            mobile=mobile,
            web_page=web_page,
            from_=from_,
            posted_on=posted_on,
            importance=importance,
            cc=cc,
            bcc=bcc,
            to=to,
            sent=sent,
            received=received,
            reminder=reminder,
            duration=duration,
            entry_type=entry_type,
            date=date,
            status=status,
            percent_complete=percent_complete,
            start_date=start_date,
            due_date=due_date,
            owner=owner,
        )

        rest_exchange_items_composed.additional_properties = d
        return rest_exchange_items_composed

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
