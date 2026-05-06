from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTSendAsMsgOptionsV6")



@_attrs_define
class RESTSendAsMsgOptionsV6:
    """ 
        Attributes:
            skip_item_checks (bool | Unset): Defines whether Veeam Backup for Microsoft 365 does not check items and skips
                those items that cannot be sent.
            from_ (str | Unset): Specifies the email address from which the attachments will be sent.
            to (str | Unset): Specifies the email address to which the attachments will be sent.
            subject (str | Unset): Specifies the subject of the email message used for sending the attachments.
            text (str | Unset): Specifies the body of the email message used for sending the attachments.
     """

    skip_item_checks: bool | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    subject: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        skip_item_checks = self.skip_item_checks

        from_ = self.from_

        to = self.to

        subject = self.subject

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if skip_item_checks is not UNSET:
            field_dict["skipItemChecks"] = skip_item_checks
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
        d = dict(src_dict)
        skip_item_checks = d.pop("skipItemChecks", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        rest_send_as_msg_options_v6 = cls(
            skip_item_checks=skip_item_checks,
            from_=from_,
            to=to,
            subject=subject,
            text=text,
        )


        rest_send_as_msg_options_v6.additional_properties = d
        return rest_send_as_msg_options_v6

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
