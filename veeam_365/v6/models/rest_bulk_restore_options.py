from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_exchange_mailbox import RESTExchangeMailbox


T = TypeVar("T", bound="RestBulkRestoreOptions")


@_attrs_define
class RestBulkRestoreOptions:
    """
    Attributes:
        cas_server (str | Unset):
        mailboxes (list[RESTExchangeMailbox] | Unset):
        changed_items (bool | None | Unset):
        deleted_items (bool | None | Unset):
        mark_restored_as_unread (bool | None | Unset):
        skip_unresolved (bool | None | Unset):
        exclude_drafts (bool | None | Unset):
        exclude_deleted_items (bool | None | Unset):
        exclude_in_place_hold_items (bool | None | Unset):
        exclude_litigation_hold_items (bool | None | Unset):
        office_365_user_name (str | Unset):
        user_code (str | Unset):
        application_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        application_certificate_password (str | Unset):
        application_certificate (str | Unset):
        impersonation_account_name (str | Unset):
        office_365_user_password (str | Unset):
        domain_name (str | Unset):
        on_premises_user_name (str | Unset):
        on_premises_user_password (str | Unset):
        recent_item_restore_period (int | None | Unset):
    """

    cas_server: str | Unset = UNSET
    mailboxes: list[RESTExchangeMailbox] | Unset = UNSET
    changed_items: bool | None | Unset = UNSET
    deleted_items: bool | None | Unset = UNSET
    mark_restored_as_unread: bool | None | Unset = UNSET
    skip_unresolved: bool | None | Unset = UNSET
    exclude_drafts: bool | None | Unset = UNSET
    exclude_deleted_items: bool | None | Unset = UNSET
    exclude_in_place_hold_items: bool | None | Unset = UNSET
    exclude_litigation_hold_items: bool | None | Unset = UNSET
    office_365_user_name: str | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    impersonation_account_name: str | Unset = UNSET
    office_365_user_password: str | Unset = UNSET
    domain_name: str | Unset = UNSET
    on_premises_user_name: str | Unset = UNSET
    on_premises_user_password: str | Unset = UNSET
    recent_item_restore_period: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cas_server = self.cas_server

        mailboxes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mailboxes, Unset):
            mailboxes = []
            for mailboxes_item_data in self.mailboxes:
                mailboxes_item = mailboxes_item_data.to_dict()
                mailboxes.append(mailboxes_item)

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

        skip_unresolved: bool | None | Unset
        if isinstance(self.skip_unresolved, Unset):
            skip_unresolved = UNSET
        else:
            skip_unresolved = self.skip_unresolved

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

        office_365_user_name = self.office_365_user_name

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

        office_365_user_password = self.office_365_user_password

        domain_name = self.domain_name

        on_premises_user_name = self.on_premises_user_name

        on_premises_user_password = self.on_premises_user_password

        recent_item_restore_period: int | None | Unset
        if isinstance(self.recent_item_restore_period, Unset):
            recent_item_restore_period = UNSET
        else:
            recent_item_restore_period = self.recent_item_restore_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cas_server is not UNSET:
            field_dict["casServer"] = cas_server
        if mailboxes is not UNSET:
            field_dict["mailboxes"] = mailboxes
        if changed_items is not UNSET:
            field_dict["changedItems"] = changed_items
        if deleted_items is not UNSET:
            field_dict["deletedItems"] = deleted_items
        if mark_restored_as_unread is not UNSET:
            field_dict["markRestoredAsUnread"] = mark_restored_as_unread
        if skip_unresolved is not UNSET:
            field_dict["skipUnresolved"] = skip_unresolved
        if exclude_drafts is not UNSET:
            field_dict["excludeDrafts"] = exclude_drafts
        if exclude_deleted_items is not UNSET:
            field_dict["excludeDeletedItems"] = exclude_deleted_items
        if exclude_in_place_hold_items is not UNSET:
            field_dict["excludeInPlaceHoldItems"] = exclude_in_place_hold_items
        if exclude_litigation_hold_items is not UNSET:
            field_dict["excludeLitigationHoldItems"] = exclude_litigation_hold_items
        if office_365_user_name is not UNSET:
            field_dict["office365UserName"] = office_365_user_name
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
        if office_365_user_password is not UNSET:
            field_dict["office365UserPassword"] = office_365_user_password
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name
        if on_premises_user_name is not UNSET:
            field_dict["onPremisesUserName"] = on_premises_user_name
        if on_premises_user_password is not UNSET:
            field_dict["onPremisesUserPassword"] = on_premises_user_password
        if recent_item_restore_period is not UNSET:
            field_dict["recentItemRestorePeriod"] = recent_item_restore_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_exchange_mailbox import RESTExchangeMailbox

        d = dict(src_dict)
        cas_server = d.pop("casServer", UNSET)

        _mailboxes = d.pop("mailboxes", UNSET)
        mailboxes: list[RESTExchangeMailbox] | Unset = UNSET
        if _mailboxes is not UNSET:
            mailboxes = []
            for mailboxes_item_data in _mailboxes:
                mailboxes_item = RESTExchangeMailbox.from_dict(mailboxes_item_data)

                mailboxes.append(mailboxes_item)

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

        def _parse_skip_unresolved(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_unresolved = _parse_skip_unresolved(d.pop("skipUnresolved", UNSET))

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

        office_365_user_name = d.pop("office365UserName", UNSET)

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

        office_365_user_password = d.pop("office365UserPassword", UNSET)

        domain_name = d.pop("domainName", UNSET)

        on_premises_user_name = d.pop("onPremisesUserName", UNSET)

        on_premises_user_password = d.pop("onPremisesUserPassword", UNSET)

        def _parse_recent_item_restore_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        recent_item_restore_period = _parse_recent_item_restore_period(d.pop("recentItemRestorePeriod", UNSET))

        rest_bulk_restore_options = cls(
            cas_server=cas_server,
            mailboxes=mailboxes,
            changed_items=changed_items,
            deleted_items=deleted_items,
            mark_restored_as_unread=mark_restored_as_unread,
            skip_unresolved=skip_unresolved,
            exclude_drafts=exclude_drafts,
            exclude_deleted_items=exclude_deleted_items,
            exclude_in_place_hold_items=exclude_in_place_hold_items,
            exclude_litigation_hold_items=exclude_litigation_hold_items,
            office_365_user_name=office_365_user_name,
            user_code=user_code,
            application_id=application_id,
            application_certificate_password=application_certificate_password,
            application_certificate=application_certificate,
            impersonation_account_name=impersonation_account_name,
            office_365_user_password=office_365_user_password,
            domain_name=domain_name,
            on_premises_user_name=on_premises_user_name,
            on_premises_user_password=on_premises_user_password,
            recent_item_restore_period=recent_item_restore_period,
        )

        rest_bulk_restore_options.additional_properties = d
        return rest_bulk_restore_options

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
