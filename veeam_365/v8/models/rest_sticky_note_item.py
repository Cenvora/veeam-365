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
    from ..models.rest_sticky_note_item_actions import RESTStickyNoteItemActions
    from ..models.rest_sticky_note_item_links import RESTStickyNoteItemLinks


T = TypeVar("T", bound="RESTStickyNoteItem")


@_attrs_define
class RESTStickyNoteItem:
    """
    Attributes:
        mailbox_id (UUID | Unset): ID of the organization mailbox.
        subject (str | Unset): Note subject.
        date (datetime.datetime | Unset): Date when the note was created.
        item_class (str | Unset): Exchange item class.
        field_links (RESTStickyNoteItemLinks | Unset):
        field_actions (RESTStickyNoteItemActions | Unset):
        id (str | Unset): Exchange item ID.
    """

    mailbox_id: UUID | Unset = UNSET
    subject: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    item_class: str | Unset = UNSET
    field_links: RESTStickyNoteItemLinks | Unset = UNSET
    field_actions: RESTStickyNoteItemActions | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mailbox_id: str | Unset = UNSET
        if not isinstance(self.mailbox_id, Unset):
            mailbox_id = str(self.mailbox_id)

        subject = self.subject

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

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
        if subject is not UNSET:
            field_dict["subject"] = subject
        if date is not UNSET:
            field_dict["date"] = date
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
        from ..models.rest_sticky_note_item_actions import RESTStickyNoteItemActions
        from ..models.rest_sticky_note_item_links import RESTStickyNoteItemLinks

        d = dict(src_dict)
        _mailbox_id = d.pop("mailboxId", UNSET)
        mailbox_id: UUID | Unset
        if isinstance(_mailbox_id, Unset):
            mailbox_id = UNSET
        else:
            mailbox_id = UUID(_mailbox_id)

        subject = d.pop("subject", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        item_class = d.pop("itemClass", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTStickyNoteItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTStickyNoteItemLinks.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTStickyNoteItemActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTStickyNoteItemActions.from_dict(_field_actions)

        id = d.pop("id", UNSET)

        rest_sticky_note_item = cls(
            mailbox_id=mailbox_id,
            subject=subject,
            date=date,
            item_class=item_class,
            field_links=field_links,
            field_actions=field_actions,
            id=id,
        )

        rest_sticky_note_item.additional_properties = d
        return rest_sticky_note_item

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
