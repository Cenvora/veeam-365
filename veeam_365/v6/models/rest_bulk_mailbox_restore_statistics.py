from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_bulk_mailbox_restore_statistics_status import RESTBulkMailboxRestoreStatisticsStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_common_restore_statistics import RESTCommonRestoreStatistics
    from ..models.rest_exchange_mailbox import RESTExchangeMailbox


T = TypeVar("T", bound="RESTBulkMailboxRestoreStatistics")


@_attrs_define
class RESTBulkMailboxRestoreStatistics:
    """
    Attributes:
        mailbox (RESTExchangeMailbox | Unset):
        status (RESTBulkMailboxRestoreStatisticsStatus | Unset):
        error (str | Unset):
        details (RESTCommonRestoreStatistics | Unset):
    """

    mailbox: RESTExchangeMailbox | Unset = UNSET
    status: RESTBulkMailboxRestoreStatisticsStatus | Unset = UNSET
    error: str | Unset = UNSET
    details: RESTCommonRestoreStatistics | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mailbox: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mailbox, Unset):
            mailbox = self.mailbox.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        error = self.error

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mailbox is not UNSET:
            field_dict["mailbox"] = mailbox
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_common_restore_statistics import RESTCommonRestoreStatistics
        from ..models.rest_exchange_mailbox import RESTExchangeMailbox

        d = dict(src_dict)
        _mailbox = d.pop("mailbox", UNSET)
        mailbox: RESTExchangeMailbox | Unset
        if isinstance(_mailbox, Unset):
            mailbox = UNSET
        else:
            mailbox = RESTExchangeMailbox.from_dict(_mailbox)

        _status = d.pop("status", UNSET)
        status: RESTBulkMailboxRestoreStatisticsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTBulkMailboxRestoreStatisticsStatus(_status)

        error = d.pop("error", UNSET)

        _details = d.pop("details", UNSET)
        details: RESTCommonRestoreStatistics | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = RESTCommonRestoreStatistics.from_dict(_details)

        rest_bulk_mailbox_restore_statistics = cls(
            mailbox=mailbox,
            status=status,
            error=error,
            details=details,
        )

        rest_bulk_mailbox_restore_statistics.additional_properties = d
        return rest_bulk_mailbox_restore_statistics

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
