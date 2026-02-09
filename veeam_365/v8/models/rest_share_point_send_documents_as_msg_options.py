from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_share_point_document import RESTSharePointDocument


T = TypeVar("T", bound="RESTSharePointSendDocumentsAsMsgOptions")


@_attrs_define
class RESTSharePointSendDocumentsAsMsgOptions:
    """
    Attributes:
        skip_item_checks (bool | Unset): Defines whether Veeam Backup for Microsoft 365 does not check items and skips
            those items that cannot be sent.
        documents (list[RESTSharePointDocument] | Unset): Specifies IDs of the SharePoint documents that you want to
            send. For more information on how to get such IDs, see [Get SharePoint
            Documents](SharePointDocument#operation/SharePointDocument_Get).
        from_ (str | Unset): Specifies the email address from which the attachments will be sent.
        to (str | Unset): Specifies the email address to which the attachments will be sent.
        subject (str | Unset): Specifies the subject of the email message used for sending the attachments.
        text (str | Unset): Specifies the body of the email message used for sending the attachments.
    """

    skip_item_checks: bool | Unset = UNSET
    documents: list[RESTSharePointDocument] | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    subject: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skip_item_checks = self.skip_item_checks

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        from_ = self.from_

        to = self.to

        subject = self.subject

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if skip_item_checks is not UNSET:
            field_dict["skipItemChecks"] = skip_item_checks
        if documents is not UNSET:
            field_dict["documents"] = documents
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
        from ..models.rest_share_point_document import RESTSharePointDocument

        d = dict(src_dict)
        skip_item_checks = d.pop("skipItemChecks", UNSET)

        _documents = d.pop("documents", UNSET)
        documents: list[RESTSharePointDocument] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = RESTSharePointDocument.from_dict(documents_item_data)

                documents.append(documents_item)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        rest_share_point_send_documents_as_msg_options = cls(
            skip_item_checks=skip_item_checks,
            documents=documents,
            from_=from_,
            to=to,
            subject=subject,
            text=text,
        )

        rest_share_point_send_documents_as_msg_options.additional_properties = d
        return rest_share_point_send_documents_as_msg_options

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
