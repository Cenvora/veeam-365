from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_share_point_attachment import RESTSharePointAttachment





T = TypeVar("T", bound="RESTSendAttachmentsAsMsgOptions")



@_attrs_define
class RESTSendAttachmentsAsMsgOptions:
    """ 
        Attributes:
            attachments (list[RESTSharePointAttachment] | Unset): Specifies IDs of the SharePoint item attachments that you
                want to send. For more information on how to get such IDs, see [Get SharePoint
                Attachments](#/SharePointAttachment/SharePointAttachment_Get).
            from_ (str | Unset): Specifies the email address from which the attachments will be sent.
            to (str | Unset): Specifies the email address to which the attachments will be sent.
            subject (str | Unset): Specifies the subject of the email message used for sending the attachments.
            text (str | Unset): Specifies the body of the email message used for sending the attachments.
     """

    attachments: list[RESTSharePointAttachment] | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    subject: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_share_point_attachment import RESTSharePointAttachment
        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        from_ = self.from_

        to = self.to

        subject = self.subject

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_share_point_attachment import RESTSharePointAttachment
        d = dict(src_dict)
        _attachments = d.pop("attachments", UNSET)
        attachments: list[RESTSharePointAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = RESTSharePointAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        rest_send_attachments_as_msg_options = cls(
            attachments=attachments,
            from_=from_,
            to=to,
            subject=subject,
            text=text,
        )


        rest_send_attachments_as_msg_options.additional_properties = d
        return rest_send_attachments_as_msg_options

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
