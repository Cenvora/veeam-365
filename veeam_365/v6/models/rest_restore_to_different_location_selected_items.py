from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_restore_to_different_location_selected_items_office_region import (
    RESTRestoreToDifferentLocationSelectedItemsOfficeRegion,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_exchange_item_string_id import RESTExchangeItemStringId


T = TypeVar("T", bound="RESTRestoreToDifferentLocationSelectedItems")


@_attrs_define
class RESTRestoreToDifferentLocationSelectedItems:
    """
    Attributes:
        changed_items (bool | None | Unset):
        deleted_items (bool | None | Unset):
        mark_restored_as_unread (bool | None | Unset):
        exclude_drafts (bool | None | Unset):
        exclude_deleted_items (bool | None | Unset):
        exclude_in_place_hold_items (bool | None | Unset):
        exclude_litigation_hold_items (bool | None | Unset):
        mailbox (str | Unset):
        cas_server (str | Unset):
        folder (str | Unset):
        office_region (RESTRestoreToDifferentLocationSelectedItemsOfficeRegion | Unset):
        office_organization_name (str | Unset):
        user_name (str | Unset):
        user_password (str | Unset):
        user_code (str | Unset):
        application_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        application_certificate_password (str | Unset):
        application_certificate (str | Unset):
        impersonation_account_name (str | Unset):
        items (list[RESTExchangeItemStringId] | Unset):
    """

    changed_items: bool | None | Unset = UNSET
    deleted_items: bool | None | Unset = UNSET
    mark_restored_as_unread: bool | None | Unset = UNSET
    exclude_drafts: bool | None | Unset = UNSET
    exclude_deleted_items: bool | None | Unset = UNSET
    exclude_in_place_hold_items: bool | None | Unset = UNSET
    exclude_litigation_hold_items: bool | None | Unset = UNSET
    mailbox: str | Unset = UNSET
    cas_server: str | Unset = UNSET
    folder: str | Unset = UNSET
    office_region: RESTRestoreToDifferentLocationSelectedItemsOfficeRegion | Unset = UNSET
    office_organization_name: str | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    impersonation_account_name: str | Unset = UNSET
    items: list[RESTExchangeItemStringId] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed_items: bool | None | Unset
        if isinstance(self.changed_items, Unset):
            changed_items = UNSET
        else:
            changed_items = self.changed_items

        deleted_items: bool | None | Unset
        if isinstance(self.deleted_items, Unset):
            deleted_items = UNSET
        else:
            deleted_items = self.deleted_items

        mark_restored_as_unread: bool | None | Unset
        if isinstance(self.mark_restored_as_unread, Unset):
            mark_restored_as_unread = UNSET
        else:
            mark_restored_as_unread = self.mark_restored_as_unread

        exclude_drafts: bool | None | Unset
        if isinstance(self.exclude_drafts, Unset):
            exclude_drafts = UNSET
        else:
            exclude_drafts = self.exclude_drafts

        exclude_deleted_items: bool | None | Unset
        if isinstance(self.exclude_deleted_items, Unset):
            exclude_deleted_items = UNSET
        else:
            exclude_deleted_items = self.exclude_deleted_items

        exclude_in_place_hold_items: bool | None | Unset
        if isinstance(self.exclude_in_place_hold_items, Unset):
            exclude_in_place_hold_items = UNSET
        else:
            exclude_in_place_hold_items = self.exclude_in_place_hold_items

        exclude_litigation_hold_items: bool | None | Unset
        if isinstance(self.exclude_litigation_hold_items, Unset):
            exclude_litigation_hold_items = UNSET
        else:
            exclude_litigation_hold_items = self.exclude_litigation_hold_items

        mailbox = self.mailbox

        cas_server = self.cas_server

        folder = self.folder

        office_region: str | Unset = UNSET
        if not isinstance(self.office_region, Unset):
            office_region = self.office_region.value

        office_organization_name = self.office_organization_name

        user_name = self.user_name

        user_password = self.user_password

        user_code = self.user_code

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        elif isinstance(self.application_id, UUID):
            application_id = str(self.application_id)
        else:
            application_id = self.application_id

        application_certificate_password = self.application_certificate_password

        application_certificate = self.application_certificate

        impersonation_account_name = self.impersonation_account_name

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changed_items is not UNSET:
            field_dict["changedItems"] = changed_items
        if deleted_items is not UNSET:
            field_dict["deletedItems"] = deleted_items
        if mark_restored_as_unread is not UNSET:
            field_dict["markRestoredAsUnread"] = mark_restored_as_unread
        if exclude_drafts is not UNSET:
            field_dict["excludeDrafts"] = exclude_drafts
        if exclude_deleted_items is not UNSET:
            field_dict["excludeDeletedItems"] = exclude_deleted_items
        if exclude_in_place_hold_items is not UNSET:
            field_dict["excludeInPlaceHoldItems"] = exclude_in_place_hold_items
        if exclude_litigation_hold_items is not UNSET:
            field_dict["excludeLitigationHoldItems"] = exclude_litigation_hold_items
        if mailbox is not UNSET:
            field_dict["mailbox"] = mailbox
        if cas_server is not UNSET:
            field_dict["casServer"] = cas_server
        if folder is not UNSET:
            field_dict["folder"] = folder
        if office_region is not UNSET:
            field_dict["officeRegion"] = office_region
        if office_organization_name is not UNSET:
            field_dict["officeOrganizationName"] = office_organization_name
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_password is not UNSET:
            field_dict["userPassword"] = user_password
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if impersonation_account_name is not UNSET:
            field_dict["impersonationAccountName"] = impersonation_account_name
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_exchange_item_string_id import RESTExchangeItemStringId

        d = dict(src_dict)

        def _parse_changed_items(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        changed_items = _parse_changed_items(d.pop("changedItems", UNSET))

        def _parse_deleted_items(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deleted_items = _parse_deleted_items(d.pop("deletedItems", UNSET))

        def _parse_mark_restored_as_unread(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mark_restored_as_unread = _parse_mark_restored_as_unread(d.pop("markRestoredAsUnread", UNSET))

        def _parse_exclude_drafts(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exclude_drafts = _parse_exclude_drafts(d.pop("excludeDrafts", UNSET))

        def _parse_exclude_deleted_items(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exclude_deleted_items = _parse_exclude_deleted_items(d.pop("excludeDeletedItems", UNSET))

        def _parse_exclude_in_place_hold_items(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exclude_in_place_hold_items = _parse_exclude_in_place_hold_items(d.pop("excludeInPlaceHoldItems", UNSET))

        def _parse_exclude_litigation_hold_items(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exclude_litigation_hold_items = _parse_exclude_litigation_hold_items(d.pop("excludeLitigationHoldItems", UNSET))

        mailbox = d.pop("mailbox", UNSET)

        cas_server = d.pop("casServer", UNSET)

        folder = d.pop("folder", UNSET)

        _office_region = d.pop("officeRegion", UNSET)
        office_region: RESTRestoreToDifferentLocationSelectedItemsOfficeRegion | Unset
        if isinstance(_office_region, Unset):
            office_region = UNSET
        else:
            office_region = RESTRestoreToDifferentLocationSelectedItemsOfficeRegion(_office_region)

        office_organization_name = d.pop("officeOrganizationName", UNSET)

        user_name = d.pop("userName", UNSET)

        user_password = d.pop("userPassword", UNSET)

        user_code = d.pop("userCode", UNSET)

        def _parse_application_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_id_type_0 = UUID(data)

                return application_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        application_id = _parse_application_id(d.pop("applicationId", UNSET))

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        application_certificate = d.pop("applicationCertificate", UNSET)

        impersonation_account_name = d.pop("impersonationAccountName", UNSET)

        _items = d.pop("items", UNSET)
        items: list[RESTExchangeItemStringId] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RESTExchangeItemStringId.from_dict(items_item_data)

                items.append(items_item)

        rest_restore_to_different_location_selected_items = cls(
            changed_items=changed_items,
            deleted_items=deleted_items,
            mark_restored_as_unread=mark_restored_as_unread,
            exclude_drafts=exclude_drafts,
            exclude_deleted_items=exclude_deleted_items,
            exclude_in_place_hold_items=exclude_in_place_hold_items,
            exclude_litigation_hold_items=exclude_litigation_hold_items,
            mailbox=mailbox,
            cas_server=cas_server,
            folder=folder,
            office_region=office_region,
            office_organization_name=office_organization_name,
            user_name=user_name,
            user_password=user_password,
            user_code=user_code,
            application_id=application_id,
            application_certificate_password=application_certificate_password,
            application_certificate=application_certificate,
            impersonation_account_name=impersonation_account_name,
            items=items,
        )

        rest_restore_to_different_location_selected_items.additional_properties = d
        return rest_restore_to_different_location_selected_items

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
