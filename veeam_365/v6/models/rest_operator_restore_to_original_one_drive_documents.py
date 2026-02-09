from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_operator_restore_to_original_one_drive_documents_document_action import (
    RESTOperatorRestoreToOriginalOneDriveDocumentsDocumentAction,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_restore_one_drive_document_config import RESTRestoreOneDriveDocumentConfig


T = TypeVar("T", bound="RESTOperatorRestoreToOriginalOneDriveDocuments")


@_attrs_define
class RESTOperatorRestoreToOriginalOneDriveDocuments:
    """
    Attributes:
        document_action (RESTOperatorRestoreToOriginalOneDriveDocumentsDocumentAction):
        documents_restore_configs (list[RESTRestoreOneDriveDocumentConfig]):
        reason (str | Unset):
    """

    document_action: RESTOperatorRestoreToOriginalOneDriveDocumentsDocumentAction
    documents_restore_configs: list[RESTRestoreOneDriveDocumentConfig]
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_action = self.document_action.value

        documents_restore_configs = []
        for documents_restore_configs_item_data in self.documents_restore_configs:
            documents_restore_configs_item = documents_restore_configs_item_data.to_dict()
            documents_restore_configs.append(documents_restore_configs_item)

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentAction": document_action,
                "documentsRestoreConfigs": documents_restore_configs,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_restore_one_drive_document_config import RESTRestoreOneDriveDocumentConfig

        d = dict(src_dict)
        document_action = RESTOperatorRestoreToOriginalOneDriveDocumentsDocumentAction(d.pop("documentAction"))

        documents_restore_configs = []
        _documents_restore_configs = d.pop("documentsRestoreConfigs")
        for documents_restore_configs_item_data in _documents_restore_configs:
            documents_restore_configs_item = RESTRestoreOneDriveDocumentConfig.from_dict(
                documents_restore_configs_item_data
            )

            documents_restore_configs.append(documents_restore_configs_item)

        reason = d.pop("reason", UNSET)

        rest_operator_restore_to_original_one_drive_documents = cls(
            document_action=document_action,
            documents_restore_configs=documents_restore_configs,
            reason=reason,
        )

        rest_operator_restore_to_original_one_drive_documents.additional_properties = d
        return rest_operator_restore_to_original_one_drive_documents

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
