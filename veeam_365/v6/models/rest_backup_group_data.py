from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTBackupGroupData")


@_attrs_define
class RESTBackupGroupData:
    """
    Attributes:
        id (str):
        organization_id (str):
        is_mailbox_backed_up (bool | Unset):
        is_site_backed_up (bool | Unset):
        mailbox_backed_up_time (datetime.datetime | None | Unset):
        site_backed_up_time (datetime.datetime | None | Unset):
        account_id (str | Unset):
        display_name (str | Unset):
        email (str | Unset):
        group_site_url (list[str] | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: str
    organization_id: str
    is_mailbox_backed_up: bool | Unset = UNSET
    is_site_backed_up: bool | Unset = UNSET
    mailbox_backed_up_time: datetime.datetime | None | Unset = UNSET
    site_backed_up_time: datetime.datetime | None | Unset = UNSET
    account_id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    group_site_url: list[str] | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization_id = self.organization_id

        is_mailbox_backed_up = self.is_mailbox_backed_up

        is_site_backed_up = self.is_site_backed_up

        mailbox_backed_up_time: None | str | Unset
        if isinstance(self.mailbox_backed_up_time, Unset):
            mailbox_backed_up_time = UNSET
        elif isinstance(self.mailbox_backed_up_time, datetime.datetime):
            mailbox_backed_up_time = self.mailbox_backed_up_time.isoformat()
        else:
            mailbox_backed_up_time = self.mailbox_backed_up_time

        site_backed_up_time: None | str | Unset
        if isinstance(self.site_backed_up_time, Unset):
            site_backed_up_time = UNSET
        elif isinstance(self.site_backed_up_time, datetime.datetime):
            site_backed_up_time = self.site_backed_up_time.isoformat()
        else:
            site_backed_up_time = self.site_backed_up_time

        account_id = self.account_id

        display_name = self.display_name

        email = self.email

        group_site_url: list[str] | Unset = UNSET
        if not isinstance(self.group_site_url, Unset):
            group_site_url = self.group_site_url

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organizationId": organization_id,
            }
        )
        if is_mailbox_backed_up is not UNSET:
            field_dict["isMailboxBackedUp"] = is_mailbox_backed_up
        if is_site_backed_up is not UNSET:
            field_dict["isSiteBackedUp"] = is_site_backed_up
        if mailbox_backed_up_time is not UNSET:
            field_dict["mailboxBackedUpTime"] = mailbox_backed_up_time
        if site_backed_up_time is not UNSET:
            field_dict["siteBackedUpTime"] = site_backed_up_time
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if group_site_url is not UNSET:
            field_dict["groupSiteUrl"] = group_site_url
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        id = d.pop("id")

        organization_id = d.pop("organizationId")

        is_mailbox_backed_up = d.pop("isMailboxBackedUp", UNSET)

        is_site_backed_up = d.pop("isSiteBackedUp", UNSET)

        def _parse_mailbox_backed_up_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mailbox_backed_up_time_type_0 = isoparse(data)

                return mailbox_backed_up_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        mailbox_backed_up_time = _parse_mailbox_backed_up_time(d.pop("mailboxBackedUpTime", UNSET))

        def _parse_site_backed_up_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                site_backed_up_time_type_0 = isoparse(data)

                return site_backed_up_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        site_backed_up_time = _parse_site_backed_up_time(d.pop("siteBackedUpTime", UNSET))

        account_id = d.pop("accountId", UNSET)

        display_name = d.pop("displayName", UNSET)

        email = d.pop("email", UNSET)

        group_site_url = cast(list[str], d.pop("groupSiteUrl", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_backup_group_data = cls(
            id=id,
            organization_id=organization_id,
            is_mailbox_backed_up=is_mailbox_backed_up,
            is_site_backed_up=is_site_backed_up,
            mailbox_backed_up_time=mailbox_backed_up_time,
            site_backed_up_time=site_backed_up_time,
            account_id=account_id,
            display_name=display_name,
            email=email,
            group_site_url=group_site_url,
            field_links=field_links,
        )

        rest_backup_group_data.additional_properties = d
        return rest_backup_group_data

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
