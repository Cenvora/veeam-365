from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_item_restore_details_type import RESTItemRestoreDetailsType
from ..models.rest_restore_item_type import RESTRestoreItemType
from ..models.rest_restore_status import RESTRestoreStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RESTBulkMailboxItemRestoreDetails")



@_attrs_define
class RESTBulkMailboxItemRestoreDetails:
    """ 
        Attributes:
            id (str): ID of the object.
            item_restore_details_type (RESTItemRestoreDetailsType): Type of the restore operation performed with the object.
            name (str): Name of the restored item.
            item_type (RESTRestoreItemType): Type of the restored item.
            status (RESTRestoreStatus): Status of the restored item.
            mailbox_email (str): Email address of the organization mailbox.
            mailbox_is_archive (bool): Defines whether the mailbox is of the *Archive* type.
            mailbox_is_public (bool): Defines whether the mailbox is public.
            created_mailbox_items_count (int): Number of missed items restored from the backup.
            merged_mailbox_items_count (int): Number of changed items restored from the backup.
            failed_mailbox_items_count (int): Number of items for which the restore operation failed.
            skipped_mailbox_items_count (int): Number of items that were not changed or missed in the original location.
                Such items are skipped during the restore operation.
            title (str | Unset): Title of the restored item.
            error (str | Unset): Error that occurred during the item restore.
            warnings (list[str] | Unset): Array of warnings appeared during the restore operation.
            cannot_continue_mailbox_error (str | Unset): Error that occurred during the restore operation.
     """

    id: str
    item_restore_details_type: RESTItemRestoreDetailsType
    name: str
    item_type: RESTRestoreItemType
    status: RESTRestoreStatus
    mailbox_email: str
    mailbox_is_archive: bool
    mailbox_is_public: bool
    created_mailbox_items_count: int
    merged_mailbox_items_count: int
    failed_mailbox_items_count: int
    skipped_mailbox_items_count: int
    title: str | Unset = UNSET
    error: str | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    cannot_continue_mailbox_error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        item_restore_details_type = self.item_restore_details_type.value

        name = self.name

        item_type = self.item_type.value

        status = self.status.value

        mailbox_email = self.mailbox_email

        mailbox_is_archive = self.mailbox_is_archive

        mailbox_is_public = self.mailbox_is_public

        created_mailbox_items_count = self.created_mailbox_items_count

        merged_mailbox_items_count = self.merged_mailbox_items_count

        failed_mailbox_items_count = self.failed_mailbox_items_count

        skipped_mailbox_items_count = self.skipped_mailbox_items_count

        title = self.title

        error = self.error

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings



        cannot_continue_mailbox_error = self.cannot_continue_mailbox_error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "itemRestoreDetailsType": item_restore_details_type,
            "name": name,
            "itemType": item_type,
            "status": status,
            "mailboxEmail": mailbox_email,
            "mailboxIsArchive": mailbox_is_archive,
            "mailboxIsPublic": mailbox_is_public,
            "createdMailboxItemsCount": created_mailbox_items_count,
            "mergedMailboxItemsCount": merged_mailbox_items_count,
            "failedMailboxItemsCount": failed_mailbox_items_count,
            "skippedMailboxItemsCount": skipped_mailbox_items_count,
        })
        if title is not UNSET:
            field_dict["title"] = title
        if error is not UNSET:
            field_dict["error"] = error
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if cannot_continue_mailbox_error is not UNSET:
            field_dict["cannotContinueMailboxError"] = cannot_continue_mailbox_error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        item_restore_details_type = RESTItemRestoreDetailsType(d.pop("itemRestoreDetailsType"))




        name = d.pop("name")

        item_type = RESTRestoreItemType(d.pop("itemType"))




        status = RESTRestoreStatus(d.pop("status"))




        mailbox_email = d.pop("mailboxEmail")

        mailbox_is_archive = d.pop("mailboxIsArchive")

        mailbox_is_public = d.pop("mailboxIsPublic")

        created_mailbox_items_count = d.pop("createdMailboxItemsCount")

        merged_mailbox_items_count = d.pop("mergedMailboxItemsCount")

        failed_mailbox_items_count = d.pop("failedMailboxItemsCount")

        skipped_mailbox_items_count = d.pop("skippedMailboxItemsCount")

        title = d.pop("title", UNSET)

        error = d.pop("error", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))


        cannot_continue_mailbox_error = d.pop("cannotContinueMailboxError", UNSET)

        rest_bulk_mailbox_item_restore_details = cls(
            id=id,
            item_restore_details_type=item_restore_details_type,
            name=name,
            item_type=item_type,
            status=status,
            mailbox_email=mailbox_email,
            mailbox_is_archive=mailbox_is_archive,
            mailbox_is_public=mailbox_is_public,
            created_mailbox_items_count=created_mailbox_items_count,
            merged_mailbox_items_count=merged_mailbox_items_count,
            failed_mailbox_items_count=failed_mailbox_items_count,
            skipped_mailbox_items_count=skipped_mailbox_items_count,
            title=title,
            error=error,
            warnings=warnings,
            cannot_continue_mailbox_error=cannot_continue_mailbox_error,
        )


        rest_bulk_mailbox_item_restore_details.additional_properties = d
        return rest_bulk_mailbox_item_restore_details

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
