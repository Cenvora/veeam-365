from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_exchange_item_importance import RESTExchangeItemImportance
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.rest_attachment import RESTAttachment
  from ..models.rest_exchange_message_item_actions import RESTExchangeMessageItemActions
  from ..models.rest_exchange_message_item_links import RESTExchangeMessageItemLinks





T = TypeVar("T", bound="RESTExchangeMessageItem")



@_attrs_define
class RESTExchangeMessageItem:
    """ 
        Attributes:
            mailbox_id (UUID | Unset): ID of the organization mailbox.
            from_ (str | Unset): Sender email address.
            cc (str | Unset): Recipient email address in carbon copy.
            bcc (str | Unset): Recipient address in blind carbon copy.
            to (str | Unset): Recipient email address.
            sent (datetime.datetime | Unset): Date and time when the message was sent.
            received (datetime.datetime | Unset): Date and time when the message was received.
            reminder (bool | Unset): Defines whether the message was sent with the reminder.
            attachments (list[RESTAttachment] | Unset): Array of attachment items for the message.
            subject (str | Unset): Message subject.
            item_class (str | Unset): Exchange item class.
            importance (RESTExchangeItemImportance | Unset): Message importance.
            field_links (RESTExchangeMessageItemLinks | Unset):
            field_actions (RESTExchangeMessageItemActions | Unset):
            id (str | Unset): Exchange item ID.
     """

    mailbox_id: UUID | Unset = UNSET
    from_: str | Unset = UNSET
    cc: str | Unset = UNSET
    bcc: str | Unset = UNSET
    to: str | Unset = UNSET
    sent: datetime.datetime | Unset = UNSET
    received: datetime.datetime | Unset = UNSET
    reminder: bool | Unset = UNSET
    attachments: list[RESTAttachment] | Unset = UNSET
    subject: str | Unset = UNSET
    item_class: str | Unset = UNSET
    importance: RESTExchangeItemImportance | Unset = UNSET
    field_links: RESTExchangeMessageItemLinks | Unset = UNSET
    field_actions: RESTExchangeMessageItemActions | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_attachment import RESTAttachment
        from ..models.rest_exchange_message_item_actions import RESTExchangeMessageItemActions
        from ..models.rest_exchange_message_item_links import RESTExchangeMessageItemLinks
        mailbox_id: str | Unset = UNSET
        if not isinstance(self.mailbox_id, Unset):
            mailbox_id = str(self.mailbox_id)

        from_ = self.from_

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

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        subject = self.subject

        item_class = self.item_class

        importance: str | Unset = UNSET
        if not isinstance(self.importance, Unset):
            importance = self.importance.value


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
        if from_ is not UNSET:
            field_dict["from"] = from_
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
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if subject is not UNSET:
            field_dict["subject"] = subject
        if item_class is not UNSET:
            field_dict["itemClass"] = item_class
        if importance is not UNSET:
            field_dict["importance"] = importance
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_attachment import RESTAttachment
        from ..models.rest_exchange_message_item_actions import RESTExchangeMessageItemActions
        from ..models.rest_exchange_message_item_links import RESTExchangeMessageItemLinks
        d = dict(src_dict)
        _mailbox_id = d.pop("mailboxId", UNSET)
        mailbox_id: UUID | Unset
        if isinstance(_mailbox_id,  Unset):
            mailbox_id = UNSET
        else:
            mailbox_id = UUID(_mailbox_id)




        from_ = d.pop("from", UNSET)

        cc = d.pop("cc", UNSET)

        bcc = d.pop("bcc", UNSET)

        to = d.pop("to", UNSET)

        _sent = d.pop("sent", UNSET)
        sent: datetime.datetime | Unset
        if isinstance(_sent,  Unset):
            sent = UNSET
        else:
            sent = isoparse(_sent)




        _received = d.pop("received", UNSET)
        received: datetime.datetime | Unset
        if isinstance(_received,  Unset):
            received = UNSET
        else:
            received = isoparse(_received)




        reminder = d.pop("reminder", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[RESTAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = RESTAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        subject = d.pop("subject", UNSET)

        item_class = d.pop("itemClass", UNSET)

        _importance = d.pop("importance", UNSET)
        importance: RESTExchangeItemImportance | Unset
        if isinstance(_importance,  Unset):
            importance = UNSET
        else:
            importance = RESTExchangeItemImportance(_importance)




        _field_links = d.pop("_links", UNSET)
        field_links: RESTExchangeMessageItemLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTExchangeMessageItemLinks.from_dict(_field_links)




        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTExchangeMessageItemActions | Unset
        if isinstance(_field_actions,  Unset):
            field_actions = UNSET
        else:
            field_actions = RESTExchangeMessageItemActions.from_dict(_field_actions)




        id = d.pop("id", UNSET)

        rest_exchange_message_item = cls(
            mailbox_id=mailbox_id,
            from_=from_,
            cc=cc,
            bcc=bcc,
            to=to,
            sent=sent,
            received=received,
            reminder=reminder,
            attachments=attachments,
            subject=subject,
            item_class=item_class,
            importance=importance,
            field_links=field_links,
            field_actions=field_actions,
            id=id,
        )


        rest_exchange_message_item.additional_properties = d
        return rest_exchange_message_item

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
