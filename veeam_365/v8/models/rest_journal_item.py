from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.rest_journal_item_actions import RESTJournalItemActions
  from ..models.rest_journal_item_links import RESTJournalItemLinks





T = TypeVar("T", bound="RESTJournalItem")



@_attrs_define
class RESTJournalItem:
    """ 
        Attributes:
            mailbox_id (UUID | Unset): ID of the organization mailbox.
            start_time (datetime.datetime | Unset): Date and time when the task was started.
            duration (int | Unset): Duration of the journal entry in hours.
            entry_type (str | Unset): Type of the journal entry.
            company (str | Unset): Company.
            subject (str | Unset): Task subject.
            item_class (str | Unset): Exchange item class.
            field_links (RESTJournalItemLinks | Unset):
            field_actions (RESTJournalItemActions | Unset):
            id (str | Unset): Exchange item ID.
     """

    mailbox_id: UUID | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    duration: int | Unset = UNSET
    entry_type: str | Unset = UNSET
    company: str | Unset = UNSET
    subject: str | Unset = UNSET
    item_class: str | Unset = UNSET
    field_links: RESTJournalItemLinks | Unset = UNSET
    field_actions: RESTJournalItemActions | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_journal_item_actions import RESTJournalItemActions
        from ..models.rest_journal_item_links import RESTJournalItemLinks
        mailbox_id: str | Unset = UNSET
        if not isinstance(self.mailbox_id, Unset):
            mailbox_id = str(self.mailbox_id)

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        duration = self.duration

        entry_type = self.entry_type

        company = self.company

        subject = self.subject

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
        field_dict.update({
        })
        if mailbox_id is not UNSET:
            field_dict["mailboxId"] = mailbox_id
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if entry_type is not UNSET:
            field_dict["entryType"] = entry_type
        if company is not UNSET:
            field_dict["company"] = company
        if subject is not UNSET:
            field_dict["subject"] = subject
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
        from ..models.rest_journal_item_actions import RESTJournalItemActions
        from ..models.rest_journal_item_links import RESTJournalItemLinks
        d = dict(src_dict)
        _mailbox_id = d.pop("mailboxId", UNSET)
        mailbox_id: UUID | Unset
        if isinstance(_mailbox_id,  Unset):
            mailbox_id = UNSET
        else:
            mailbox_id = UUID(_mailbox_id)




        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time,  Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)




        duration = d.pop("duration", UNSET)

        entry_type = d.pop("entryType", UNSET)

        company = d.pop("company", UNSET)

        subject = d.pop("subject", UNSET)

        item_class = d.pop("itemClass", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTJournalItemLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTJournalItemLinks.from_dict(_field_links)




        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTJournalItemActions | Unset
        if isinstance(_field_actions,  Unset):
            field_actions = UNSET
        else:
            field_actions = RESTJournalItemActions.from_dict(_field_actions)




        id = d.pop("id", UNSET)

        rest_journal_item = cls(
            mailbox_id=mailbox_id,
            start_time=start_time,
            duration=duration,
            entry_type=entry_type,
            company=company,
            subject=subject,
            item_class=item_class,
            field_links=field_links,
            field_actions=field_actions,
            id=id,
        )


        rest_journal_item.additional_properties = d
        return rest_journal_item

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
