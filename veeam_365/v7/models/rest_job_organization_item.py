from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_job_backup_item_type import RESTJobBackupItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_job_organization_item_links_type_0 import RESTJobOrganizationItemLinksType0


T = TypeVar("T", bound="RESTJobOrganizationItem")


@_attrs_define
class RESTJobOrganizationItem:
    """
    Attributes:
        type_ (RESTJobBackupItemType | Unset): Type of the backup item.
        mailbox (bool | None | Unset): Defines whether this backup job will include/exclude the *Mail* processing
            option.
        one_drive (bool | None | Unset): Defines whether this backup job will include/exclude the *OneDrive* processing
            option.
        archive_mailbox (bool | None | Unset): Defines whether this backup job will include/exclude the *Archive*
            processing option.
        sites (bool | None | Unset): Defines whether this backup job will include/exclude the *Sites* processing option.
        teams (bool | None | Unset): Defines whether this backup job will include/exclude the *Teams* processing option.
        teams_chats (bool | None | Unset): Defines whether this job will back up team chats.
        id (None | str | Unset): Backup item ID.
        field_links (None | RESTJobOrganizationItemLinksType0 | Unset):
    """

    type_: RESTJobBackupItemType | Unset = UNSET
    mailbox: bool | None | Unset = UNSET
    one_drive: bool | None | Unset = UNSET
    archive_mailbox: bool | None | Unset = UNSET
    sites: bool | None | Unset = UNSET
    teams: bool | None | Unset = UNSET
    teams_chats: bool | None | Unset = UNSET
    id: None | str | Unset = UNSET
    field_links: None | RESTJobOrganizationItemLinksType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_job_organization_item_links_type_0 import RESTJobOrganizationItemLinksType0

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        mailbox: bool | None | Unset
        if isinstance(self.mailbox, Unset):
            mailbox = UNSET
        else:
            mailbox = self.mailbox

        one_drive: bool | None | Unset
        if isinstance(self.one_drive, Unset):
            one_drive = UNSET
        else:
            one_drive = self.one_drive

        archive_mailbox: bool | None | Unset
        if isinstance(self.archive_mailbox, Unset):
            archive_mailbox = UNSET
        else:
            archive_mailbox = self.archive_mailbox

        sites: bool | None | Unset
        if isinstance(self.sites, Unset):
            sites = UNSET
        else:
            sites = self.sites

        teams: bool | None | Unset
        if isinstance(self.teams, Unset):
            teams = UNSET
        else:
            teams = self.teams

        teams_chats: bool | None | Unset
        if isinstance(self.teams_chats, Unset):
            teams_chats = UNSET
        else:
            teams_chats = self.teams_chats

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, RESTJobOrganizationItemLinksType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mailbox is not UNSET:
            field_dict["mailbox"] = mailbox
        if one_drive is not UNSET:
            field_dict["oneDrive"] = one_drive
        if archive_mailbox is not UNSET:
            field_dict["archiveMailbox"] = archive_mailbox
        if sites is not UNSET:
            field_dict["sites"] = sites
        if teams is not UNSET:
            field_dict["teams"] = teams
        if teams_chats is not UNSET:
            field_dict["teamsChats"] = teams_chats
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_job_organization_item_links_type_0 import RESTJobOrganizationItemLinksType0

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTJobBackupItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTJobBackupItemType(_type_)

        def _parse_mailbox(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mailbox = _parse_mailbox(d.pop("mailbox", UNSET))

        def _parse_one_drive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        one_drive = _parse_one_drive(d.pop("oneDrive", UNSET))

        def _parse_archive_mailbox(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        archive_mailbox = _parse_archive_mailbox(d.pop("archiveMailbox", UNSET))

        def _parse_sites(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sites = _parse_sites(d.pop("sites", UNSET))

        def _parse_teams(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        teams = _parse_teams(d.pop("teams", UNSET))

        def _parse_teams_chats(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        teams_chats = _parse_teams_chats(d.pop("teamsChats", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_field_links(data: object) -> None | RESTJobOrganizationItemLinksType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_links_type_0 = RESTJobOrganizationItemLinksType0.from_dict(data)

                return field_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTJobOrganizationItemLinksType0 | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        rest_job_organization_item = cls(
            type_=type_,
            mailbox=mailbox,
            one_drive=one_drive,
            archive_mailbox=archive_mailbox,
            sites=sites,
            teams=teams,
            teams_chats=teams_chats,
            id=id,
            field_links=field_links,
        )

        rest_job_organization_item.additional_properties = d
        return rest_job_organization_item

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
