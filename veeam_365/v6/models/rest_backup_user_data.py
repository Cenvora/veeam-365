from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_backup_user_account_type import RESTBackupUserAccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTBackupUserData")


@_attrs_define
class RESTBackupUserData:
    """
    Attributes:
        id (str):
        organization_id (str):
        mailbox_backed_up_time (datetime.datetime | None | Unset):
        archive_backed_up_time (datetime.datetime | None | Unset):
        one_drive_backed_up_time (datetime.datetime | None | Unset):
        personal_site_backed_up_time (datetime.datetime | None | Unset):
        is_mailbox_backed_up (bool | Unset):
        is_one_drive_backed_up (bool | Unset):
        is_archive_backed_up (bool | Unset):
        is_personal_site_backed_up (bool | Unset):
        account_type (RESTBackupUserAccountType | Unset):
        archive_name (str | Unset):
        account_id (str | Unset):
        display_name (str | Unset):
        email (str | Unset):
        one_drive_url (list[str] | Unset):
        personal_site_url (list[str] | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: str
    organization_id: str
    mailbox_backed_up_time: datetime.datetime | None | Unset = UNSET
    archive_backed_up_time: datetime.datetime | None | Unset = UNSET
    one_drive_backed_up_time: datetime.datetime | None | Unset = UNSET
    personal_site_backed_up_time: datetime.datetime | None | Unset = UNSET
    is_mailbox_backed_up: bool | Unset = UNSET
    is_one_drive_backed_up: bool | Unset = UNSET
    is_archive_backed_up: bool | Unset = UNSET
    is_personal_site_backed_up: bool | Unset = UNSET
    account_type: RESTBackupUserAccountType | Unset = UNSET
    archive_name: str | Unset = UNSET
    account_id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    one_drive_url: list[str] | Unset = UNSET
    personal_site_url: list[str] | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization_id = self.organization_id

        mailbox_backed_up_time: None | str | Unset
        if isinstance(self.mailbox_backed_up_time, Unset):
            mailbox_backed_up_time = UNSET
        elif isinstance(self.mailbox_backed_up_time, datetime.datetime):
            mailbox_backed_up_time = self.mailbox_backed_up_time.isoformat()
        else:
            mailbox_backed_up_time = self.mailbox_backed_up_time

        archive_backed_up_time: None | str | Unset
        if isinstance(self.archive_backed_up_time, Unset):
            archive_backed_up_time = UNSET
        elif isinstance(self.archive_backed_up_time, datetime.datetime):
            archive_backed_up_time = self.archive_backed_up_time.isoformat()
        else:
            archive_backed_up_time = self.archive_backed_up_time

        one_drive_backed_up_time: None | str | Unset
        if isinstance(self.one_drive_backed_up_time, Unset):
            one_drive_backed_up_time = UNSET
        elif isinstance(self.one_drive_backed_up_time, datetime.datetime):
            one_drive_backed_up_time = self.one_drive_backed_up_time.isoformat()
        else:
            one_drive_backed_up_time = self.one_drive_backed_up_time

        personal_site_backed_up_time: None | str | Unset
        if isinstance(self.personal_site_backed_up_time, Unset):
            personal_site_backed_up_time = UNSET
        elif isinstance(self.personal_site_backed_up_time, datetime.datetime):
            personal_site_backed_up_time = self.personal_site_backed_up_time.isoformat()
        else:
            personal_site_backed_up_time = self.personal_site_backed_up_time

        is_mailbox_backed_up = self.is_mailbox_backed_up

        is_one_drive_backed_up = self.is_one_drive_backed_up

        is_archive_backed_up = self.is_archive_backed_up

        is_personal_site_backed_up = self.is_personal_site_backed_up

        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        archive_name = self.archive_name

        account_id = self.account_id

        display_name = self.display_name

        email = self.email

        one_drive_url: list[str] | Unset = UNSET
        if not isinstance(self.one_drive_url, Unset):
            one_drive_url = self.one_drive_url

        personal_site_url: list[str] | Unset = UNSET
        if not isinstance(self.personal_site_url, Unset):
            personal_site_url = self.personal_site_url

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
        if mailbox_backed_up_time is not UNSET:
            field_dict["mailboxBackedUpTime"] = mailbox_backed_up_time
        if archive_backed_up_time is not UNSET:
            field_dict["archiveBackedUpTime"] = archive_backed_up_time
        if one_drive_backed_up_time is not UNSET:
            field_dict["oneDriveBackedUpTime"] = one_drive_backed_up_time
        if personal_site_backed_up_time is not UNSET:
            field_dict["personalSiteBackedUpTime"] = personal_site_backed_up_time
        if is_mailbox_backed_up is not UNSET:
            field_dict["isMailboxBackedUp"] = is_mailbox_backed_up
        if is_one_drive_backed_up is not UNSET:
            field_dict["isOneDriveBackedUp"] = is_one_drive_backed_up
        if is_archive_backed_up is not UNSET:
            field_dict["isArchiveBackedUp"] = is_archive_backed_up
        if is_personal_site_backed_up is not UNSET:
            field_dict["isPersonalSiteBackedUp"] = is_personal_site_backed_up
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if archive_name is not UNSET:
            field_dict["archiveName"] = archive_name
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if one_drive_url is not UNSET:
            field_dict["oneDriveUrl"] = one_drive_url
        if personal_site_url is not UNSET:
            field_dict["personalSiteUrl"] = personal_site_url
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        id = d.pop("id")

        organization_id = d.pop("organizationId")

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

        def _parse_archive_backed_up_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archive_backed_up_time_type_0 = isoparse(data)

                return archive_backed_up_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        archive_backed_up_time = _parse_archive_backed_up_time(d.pop("archiveBackedUpTime", UNSET))

        def _parse_one_drive_backed_up_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                one_drive_backed_up_time_type_0 = isoparse(data)

                return one_drive_backed_up_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        one_drive_backed_up_time = _parse_one_drive_backed_up_time(d.pop("oneDriveBackedUpTime", UNSET))

        def _parse_personal_site_backed_up_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                personal_site_backed_up_time_type_0 = isoparse(data)

                return personal_site_backed_up_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        personal_site_backed_up_time = _parse_personal_site_backed_up_time(d.pop("personalSiteBackedUpTime", UNSET))

        is_mailbox_backed_up = d.pop("isMailboxBackedUp", UNSET)

        is_one_drive_backed_up = d.pop("isOneDriveBackedUp", UNSET)

        is_archive_backed_up = d.pop("isArchiveBackedUp", UNSET)

        is_personal_site_backed_up = d.pop("isPersonalSiteBackedUp", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: RESTBackupUserAccountType | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = RESTBackupUserAccountType(_account_type)

        archive_name = d.pop("archiveName", UNSET)

        account_id = d.pop("accountId", UNSET)

        display_name = d.pop("displayName", UNSET)

        email = d.pop("email", UNSET)

        one_drive_url = cast(list[str], d.pop("oneDriveUrl", UNSET))

        personal_site_url = cast(list[str], d.pop("personalSiteUrl", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_backup_user_data = cls(
            id=id,
            organization_id=organization_id,
            mailbox_backed_up_time=mailbox_backed_up_time,
            archive_backed_up_time=archive_backed_up_time,
            one_drive_backed_up_time=one_drive_backed_up_time,
            personal_site_backed_up_time=personal_site_backed_up_time,
            is_mailbox_backed_up=is_mailbox_backed_up,
            is_one_drive_backed_up=is_one_drive_backed_up,
            is_archive_backed_up=is_archive_backed_up,
            is_personal_site_backed_up=is_personal_site_backed_up,
            account_type=account_type,
            archive_name=archive_name,
            account_id=account_id,
            display_name=display_name,
            email=email,
            one_drive_url=one_drive_url,
            personal_site_url=personal_site_url,
            field_links=field_links,
        )

        rest_backup_user_data.additional_properties = d
        return rest_backup_user_data

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
