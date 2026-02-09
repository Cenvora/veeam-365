from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_item_restore_details_type import RESTItemRestoreDetailsType
from ..models.rest_restore_item_type import RESTRestoreItemType
from ..models.rest_restore_status import RESTRestoreStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTItemRestoreDetailsComposed")


@_attrs_define
class RESTItemRestoreDetailsComposed:
    r"""
    Attributes:
        item_restore_details_type (RESTItemRestoreDetailsType): Type of the restore operation performed with the object.
        id (str | Unset): ID of the object.
        title (str | Unset): Title of the restored item.
        error (str | Unset): Error that occurred during the item restore.
        name (str | Unset): Name of the restored item.
        item_type (RESTRestoreItemType | Unset): Type of the restored item.
        status (RESTRestoreStatus | Unset): Status of the restored item.
        path (str | Unset): Path to the restored item.
        warnings (list[str] | Unset): Array of warnings appeared during the restore operation.
        mailbox_email (str | Unset): Email address of the organization mailbox.
        mailbox_is_archive (bool | Unset): Defines whether the mailbox is of the *Archive* type.
        mailbox_is_public (bool | Unset): Defines whether the mailbox is public.
        created_mailbox_items_count (int | Unset): Number of missed items restored from the backup.
        merged_mailbox_items_count (int | Unset): Number of changed items restored from the backup.
        failed_mailbox_items_count (int | Unset): Number of items for which the restore operation failed.
        skipped_mailbox_items_count (int | Unset): Number of items that were not changed or missed in the original
            location. Such items are skipped during the restore operation.
        cannot_continue_mailbox_error (str | Unset): Error that occurred during the restore operation.
        child_items (list[RESTItemRestoreDetailsComposed] | Unset): \[If available\] Statistics for child items
            processed during the restore operation.
        one_drive_web_id (UUID | Unset): OneDrive ID. Example: 00000000-0000-0000-0000-000000000000.
        one_drive_site_id (UUID | Unset): Site collection ID. Example: 00000000-0000-0000-0000-000000000000.
        one_drive_url (str | Unset): OneDrive path.
    """

    item_restore_details_type: RESTItemRestoreDetailsType
    id: str | Unset = UNSET
    title: str | Unset = UNSET
    error: str | Unset = UNSET
    name: str | Unset = UNSET
    item_type: RESTRestoreItemType | Unset = UNSET
    status: RESTRestoreStatus | Unset = UNSET
    path: str | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    mailbox_email: str | Unset = UNSET
    mailbox_is_archive: bool | Unset = UNSET
    mailbox_is_public: bool | Unset = UNSET
    created_mailbox_items_count: int | Unset = UNSET
    merged_mailbox_items_count: int | Unset = UNSET
    failed_mailbox_items_count: int | Unset = UNSET
    skipped_mailbox_items_count: int | Unset = UNSET
    cannot_continue_mailbox_error: str | Unset = UNSET
    child_items: list[RESTItemRestoreDetailsComposed] | Unset = UNSET
    one_drive_web_id: UUID | Unset = UNSET
    one_drive_site_id: UUID | Unset = UNSET
    one_drive_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_restore_details_type = self.item_restore_details_type.value

        id = self.id

        title = self.title

        error = self.error

        name = self.name

        item_type: str | Unset = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        path = self.path

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        mailbox_email = self.mailbox_email

        mailbox_is_archive = self.mailbox_is_archive

        mailbox_is_public = self.mailbox_is_public

        created_mailbox_items_count = self.created_mailbox_items_count

        merged_mailbox_items_count = self.merged_mailbox_items_count

        failed_mailbox_items_count = self.failed_mailbox_items_count

        skipped_mailbox_items_count = self.skipped_mailbox_items_count

        cannot_continue_mailbox_error = self.cannot_continue_mailbox_error

        child_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.child_items, Unset):
            child_items = []
            for child_items_item_data in self.child_items:
                child_items_item = child_items_item_data.to_dict()
                child_items.append(child_items_item)

        one_drive_web_id: str | Unset = UNSET
        if not isinstance(self.one_drive_web_id, Unset):
            one_drive_web_id = str(self.one_drive_web_id)

        one_drive_site_id: str | Unset = UNSET
        if not isinstance(self.one_drive_site_id, Unset):
            one_drive_site_id = str(self.one_drive_site_id)

        one_drive_url = self.one_drive_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemRestoreDetailsType": item_restore_details_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if error is not UNSET:
            field_dict["error"] = error
        if name is not UNSET:
            field_dict["name"] = name
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if status is not UNSET:
            field_dict["status"] = status
        if path is not UNSET:
            field_dict["path"] = path
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if mailbox_email is not UNSET:
            field_dict["mailboxEmail"] = mailbox_email
        if mailbox_is_archive is not UNSET:
            field_dict["mailboxIsArchive"] = mailbox_is_archive
        if mailbox_is_public is not UNSET:
            field_dict["mailboxIsPublic"] = mailbox_is_public
        if created_mailbox_items_count is not UNSET:
            field_dict["createdMailboxItemsCount"] = created_mailbox_items_count
        if merged_mailbox_items_count is not UNSET:
            field_dict["mergedMailboxItemsCount"] = merged_mailbox_items_count
        if failed_mailbox_items_count is not UNSET:
            field_dict["failedMailboxItemsCount"] = failed_mailbox_items_count
        if skipped_mailbox_items_count is not UNSET:
            field_dict["skippedMailboxItemsCount"] = skipped_mailbox_items_count
        if cannot_continue_mailbox_error is not UNSET:
            field_dict["cannotContinueMailboxError"] = cannot_continue_mailbox_error
        if child_items is not UNSET:
            field_dict["childItems"] = child_items
        if one_drive_web_id is not UNSET:
            field_dict["oneDriveWebId"] = one_drive_web_id
        if one_drive_site_id is not UNSET:
            field_dict["oneDriveSiteId"] = one_drive_site_id
        if one_drive_url is not UNSET:
            field_dict["oneDriveUrl"] = one_drive_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_restore_details_type = RESTItemRestoreDetailsType(d.pop("itemRestoreDetailsType"))

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        error = d.pop("error", UNSET)

        name = d.pop("name", UNSET)

        _item_type = d.pop("itemType", UNSET)
        item_type: RESTRestoreItemType | Unset
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = RESTRestoreItemType(_item_type)

        _status = d.pop("status", UNSET)
        status: RESTRestoreStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTRestoreStatus(_status)

        path = d.pop("path", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        mailbox_email = d.pop("mailboxEmail", UNSET)

        mailbox_is_archive = d.pop("mailboxIsArchive", UNSET)

        mailbox_is_public = d.pop("mailboxIsPublic", UNSET)

        created_mailbox_items_count = d.pop("createdMailboxItemsCount", UNSET)

        merged_mailbox_items_count = d.pop("mergedMailboxItemsCount", UNSET)

        failed_mailbox_items_count = d.pop("failedMailboxItemsCount", UNSET)

        skipped_mailbox_items_count = d.pop("skippedMailboxItemsCount", UNSET)

        cannot_continue_mailbox_error = d.pop("cannotContinueMailboxError", UNSET)

        _child_items = d.pop("childItems", UNSET)
        child_items: list[RESTItemRestoreDetailsComposed] | Unset = UNSET
        if _child_items is not UNSET:
            child_items = []
            for child_items_item_data in _child_items:
                child_items_item = RESTItemRestoreDetailsComposed.from_dict(child_items_item_data)

                child_items.append(child_items_item)

        _one_drive_web_id = d.pop("oneDriveWebId", UNSET)
        one_drive_web_id: UUID | Unset
        if isinstance(_one_drive_web_id, Unset):
            one_drive_web_id = UNSET
        else:
            one_drive_web_id = UUID(_one_drive_web_id)

        _one_drive_site_id = d.pop("oneDriveSiteId", UNSET)
        one_drive_site_id: UUID | Unset
        if isinstance(_one_drive_site_id, Unset):
            one_drive_site_id = UNSET
        else:
            one_drive_site_id = UUID(_one_drive_site_id)

        one_drive_url = d.pop("oneDriveUrl", UNSET)

        rest_item_restore_details_composed = cls(
            item_restore_details_type=item_restore_details_type,
            id=id,
            title=title,
            error=error,
            name=name,
            item_type=item_type,
            status=status,
            path=path,
            warnings=warnings,
            mailbox_email=mailbox_email,
            mailbox_is_archive=mailbox_is_archive,
            mailbox_is_public=mailbox_is_public,
            created_mailbox_items_count=created_mailbox_items_count,
            merged_mailbox_items_count=merged_mailbox_items_count,
            failed_mailbox_items_count=failed_mailbox_items_count,
            skipped_mailbox_items_count=skipped_mailbox_items_count,
            cannot_continue_mailbox_error=cannot_continue_mailbox_error,
            child_items=child_items,
            one_drive_web_id=one_drive_web_id,
            one_drive_site_id=one_drive_site_id,
            one_drive_url=one_drive_url,
        )

        rest_item_restore_details_composed.additional_properties = d
        return rest_item_restore_details_composed

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
