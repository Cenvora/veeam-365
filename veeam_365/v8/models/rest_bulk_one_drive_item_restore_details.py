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
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_item_restore_details_composed import RESTItemRestoreDetailsComposed





T = TypeVar("T", bound="RESTBulkOneDriveItemRestoreDetails")



@_attrs_define
class RESTBulkOneDriveItemRestoreDetails:
    r""" 
        Attributes:
            id (str): ID of the object.
            item_restore_details_type (RESTItemRestoreDetailsType): Type of the restore operation performed with the object.
            name (str): Name of the restored item.
            item_type (RESTRestoreItemType): Type of the restored item.
            status (RESTRestoreStatus): Status of the restored item.
            child_items (list[RESTItemRestoreDetailsComposed]): \[If available\] Statistics for child items processed during
                the restore operation.
            one_drive_web_id (UUID): OneDrive ID. Example: 00000000-0000-0000-0000-000000000000.
            one_drive_site_id (UUID): Site collection ID. Example: 00000000-0000-0000-0000-000000000000.
            one_drive_url (str): OneDrive path.
            title (str | Unset): Title of the restored item.
            error (str | Unset): Error that occurred during the item restore.
            warnings (list[str] | Unset): Array of warnings appeared during the restore operation.
     """

    id: str
    item_restore_details_type: RESTItemRestoreDetailsType
    name: str
    item_type: RESTRestoreItemType
    status: RESTRestoreStatus
    child_items: list[RESTItemRestoreDetailsComposed]
    one_drive_web_id: UUID
    one_drive_site_id: UUID
    one_drive_url: str
    title: str | Unset = UNSET
    error: str | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_item_restore_details_composed import RESTItemRestoreDetailsComposed
        id = self.id

        item_restore_details_type = self.item_restore_details_type.value

        name = self.name

        item_type = self.item_type.value

        status = self.status.value

        child_items = []
        for child_items_item_data in self.child_items:
            child_items_item = child_items_item_data.to_dict()
            child_items.append(child_items_item)



        one_drive_web_id = str(self.one_drive_web_id)

        one_drive_site_id = str(self.one_drive_site_id)

        one_drive_url = self.one_drive_url

        title = self.title

        error = self.error

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "itemRestoreDetailsType": item_restore_details_type,
            "name": name,
            "itemType": item_type,
            "status": status,
            "childItems": child_items,
            "oneDriveWebId": one_drive_web_id,
            "oneDriveSiteId": one_drive_site_id,
            "oneDriveUrl": one_drive_url,
        })
        if title is not UNSET:
            field_dict["title"] = title
        if error is not UNSET:
            field_dict["error"] = error
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_item_restore_details_composed import RESTItemRestoreDetailsComposed
        d = dict(src_dict)
        id = d.pop("id")

        item_restore_details_type = RESTItemRestoreDetailsType(d.pop("itemRestoreDetailsType"))




        name = d.pop("name")

        item_type = RESTRestoreItemType(d.pop("itemType"))




        status = RESTRestoreStatus(d.pop("status"))




        child_items = []
        _child_items = d.pop("childItems")
        for child_items_item_data in (_child_items):
            child_items_item = RESTItemRestoreDetailsComposed.from_dict(child_items_item_data)



            child_items.append(child_items_item)


        one_drive_web_id = UUID(d.pop("oneDriveWebId"))




        one_drive_site_id = UUID(d.pop("oneDriveSiteId"))




        one_drive_url = d.pop("oneDriveUrl")

        title = d.pop("title", UNSET)

        error = d.pop("error", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))


        rest_bulk_one_drive_item_restore_details = cls(
            id=id,
            item_restore_details_type=item_restore_details_type,
            name=name,
            item_type=item_type,
            status=status,
            child_items=child_items,
            one_drive_web_id=one_drive_web_id,
            one_drive_site_id=one_drive_site_id,
            one_drive_url=one_drive_url,
            title=title,
            error=error,
            warnings=warnings,
        )


        rest_bulk_one_drive_item_restore_details.additional_properties = d
        return rest_bulk_one_drive_item_restore_details

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
