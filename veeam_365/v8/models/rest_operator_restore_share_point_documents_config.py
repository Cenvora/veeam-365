from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_operator_restore_share_point_documents_config_document_last_version_action import RESTOperatorRestoreSharePointDocumentsConfigDocumentLastVersionAction
from ..models.rest_operator_restore_share_point_documents_config_document_version import RESTOperatorRestoreSharePointDocumentsConfigDocumentVersion
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_restore_share_point_document_config import RESTRestoreSharePointDocumentConfig





T = TypeVar("T", bound="RESTOperatorRestoreSharePointDocumentsConfig")



@_attrs_define
class RESTOperatorRestoreSharePointDocumentsConfig:
    """ 
        Attributes:
            documents_restore_configs (list[RESTRestoreSharePointDocumentConfig]): Specifies settings to restore the
                SharePoint document.
            list_ (str | Unset): Specifies the target SharePoint list.
            restore_permissions (bool | None | Unset): Defines whether the SharePoint documents will be restored with all
                permissions.
            send_shared_links_notification (bool | None | Unset): Defines whether the shared links notifications will be
                sent.
            document_version (RESTOperatorRestoreSharePointDocumentsConfigDocumentVersion | Unset): Specifies what version
                of the SharePoint documents will be restored.
            document_last_version_action (RESTOperatorRestoreSharePointDocumentsConfigDocumentLastVersionAction | Unset):
                Specifies the action that will be performed with the last version of the restored SharePoint document on the
                destination server.
            restore_changed_items (bool | None | Unset): Defines whether to restore the documents that have been modified in
                the original location.
            restore_deleted_items (bool | None | Unset): Defines whether to restore the documents that have been deleted in
                the original location.
            reason (str | Unset): Specifies a reason for the restore operation.
     """

    documents_restore_configs: list[RESTRestoreSharePointDocumentConfig]
    list_: str | Unset = UNSET
    restore_permissions: bool | None | Unset = UNSET
    send_shared_links_notification: bool | None | Unset = UNSET
    document_version: RESTOperatorRestoreSharePointDocumentsConfigDocumentVersion | Unset = UNSET
    document_last_version_action: RESTOperatorRestoreSharePointDocumentsConfigDocumentLastVersionAction | Unset = UNSET
    restore_changed_items: bool | None | Unset = UNSET
    restore_deleted_items: bool | None | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_restore_share_point_document_config import RESTRestoreSharePointDocumentConfig
        documents_restore_configs = []
        for documents_restore_configs_item_data in self.documents_restore_configs:
            documents_restore_configs_item = documents_restore_configs_item_data.to_dict()
            documents_restore_configs.append(documents_restore_configs_item)



        list_ = self.list_

        restore_permissions: bool | None | Unset
        if isinstance(self.restore_permissions, Unset):
            restore_permissions = UNSET
        else:
            restore_permissions = self.restore_permissions

        send_shared_links_notification: bool | None | Unset
        if isinstance(self.send_shared_links_notification, Unset):
            send_shared_links_notification = UNSET
        else:
            send_shared_links_notification = self.send_shared_links_notification

        document_version: str | Unset = UNSET
        if not isinstance(self.document_version, Unset):
            document_version = self.document_version.value


        document_last_version_action: str | Unset = UNSET
        if not isinstance(self.document_last_version_action, Unset):
            document_last_version_action = self.document_last_version_action.value


        restore_changed_items: bool | None | Unset
        if isinstance(self.restore_changed_items, Unset):
            restore_changed_items = UNSET
        else:
            restore_changed_items = self.restore_changed_items

        restore_deleted_items: bool | None | Unset
        if isinstance(self.restore_deleted_items, Unset):
            restore_deleted_items = UNSET
        else:
            restore_deleted_items = self.restore_deleted_items

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "documentsRestoreConfigs": documents_restore_configs,
        })
        if list_ is not UNSET:
            field_dict["list"] = list_
        if restore_permissions is not UNSET:
            field_dict["restorePermissions"] = restore_permissions
        if send_shared_links_notification is not UNSET:
            field_dict["sendSharedLinksNotification"] = send_shared_links_notification
        if document_version is not UNSET:
            field_dict["documentVersion"] = document_version
        if document_last_version_action is not UNSET:
            field_dict["documentLastVersionAction"] = document_last_version_action
        if restore_changed_items is not UNSET:
            field_dict["restoreChangedItems"] = restore_changed_items
        if restore_deleted_items is not UNSET:
            field_dict["restoreDeletedItems"] = restore_deleted_items
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_restore_share_point_document_config import RESTRestoreSharePointDocumentConfig
        d = dict(src_dict)
        documents_restore_configs = []
        _documents_restore_configs = d.pop("documentsRestoreConfigs")
        for documents_restore_configs_item_data in (_documents_restore_configs):
            documents_restore_configs_item = RESTRestoreSharePointDocumentConfig.from_dict(documents_restore_configs_item_data)



            documents_restore_configs.append(documents_restore_configs_item)


        list_ = d.pop("list", UNSET)

        def _parse_restore_permissions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restore_permissions = _parse_restore_permissions(d.pop("restorePermissions", UNSET))


        def _parse_send_shared_links_notification(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        send_shared_links_notification = _parse_send_shared_links_notification(d.pop("sendSharedLinksNotification", UNSET))


        _document_version = d.pop("documentVersion", UNSET)
        document_version: RESTOperatorRestoreSharePointDocumentsConfigDocumentVersion | Unset
        if isinstance(_document_version,  Unset):
            document_version = UNSET
        else:
            document_version = RESTOperatorRestoreSharePointDocumentsConfigDocumentVersion(_document_version)




        _document_last_version_action = d.pop("documentLastVersionAction", UNSET)
        document_last_version_action: RESTOperatorRestoreSharePointDocumentsConfigDocumentLastVersionAction | Unset
        if isinstance(_document_last_version_action,  Unset):
            document_last_version_action = UNSET
        else:
            document_last_version_action = RESTOperatorRestoreSharePointDocumentsConfigDocumentLastVersionAction(_document_last_version_action)




        def _parse_restore_changed_items(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restore_changed_items = _parse_restore_changed_items(d.pop("restoreChangedItems", UNSET))


        def _parse_restore_deleted_items(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restore_deleted_items = _parse_restore_deleted_items(d.pop("restoreDeletedItems", UNSET))


        reason = d.pop("reason", UNSET)

        rest_operator_restore_share_point_documents_config = cls(
            documents_restore_configs=documents_restore_configs,
            list_=list_,
            restore_permissions=restore_permissions,
            send_shared_links_notification=send_shared_links_notification,
            document_version=document_version,
            document_last_version_action=document_last_version_action,
            restore_changed_items=restore_changed_items,
            restore_deleted_items=restore_deleted_items,
            reason=reason,
        )


        rest_operator_restore_share_point_documents_config.additional_properties = d
        return rest_operator_restore_share_point_documents_config

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
