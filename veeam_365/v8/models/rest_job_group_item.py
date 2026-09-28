from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_job_backup_item_type import RESTJobBackupItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_group import RESTGroup
    from ..models.rest_job_group_item_links_type_0 import RESTJobGroupItemLinksType0


T = TypeVar("T", bound="RESTJobGroupItem")


@_attrs_define
class RESTJobGroupItem:
    """
    Attributes:
        type_ (RESTJobBackupItemType | Unset): Type of the backup item.
        group (RESTGroup | Unset):
        members (bool | None | Unset): Defines whether this backup job will include/exclude the *Members* processing
            option.
        member_mailbox (bool | None | Unset): Defines whether this backup job will include/exclude the *Mail* processing
            option.
        member_archive_mailbox (bool | None | Unset): Defines whether this backup job will include/exclude the *Archive*
            processing option.
        member_onedrive (bool | None | Unset): Defines whether this backup job will include/exclude the *OneDrive*
            processing option.
        member_site (bool | None | Unset): Defines whether this backup job will include/exclude the *Site* processing
            option.
        mailbox (bool | None | Unset): Defines whether this job will back up a group mailbox.
        group_site (bool | None | Unset): Defines whether this job will back up a group site.
        id (None | str | Unset): Backup item ID.
        field_links (None | RESTJobGroupItemLinksType0 | Unset):
    """

    type_: RESTJobBackupItemType | Unset = UNSET
    group: RESTGroup | Unset = UNSET
    members: bool | None | Unset = UNSET
    member_mailbox: bool | None | Unset = UNSET
    member_archive_mailbox: bool | None | Unset = UNSET
    member_onedrive: bool | None | Unset = UNSET
    member_site: bool | None | Unset = UNSET
    mailbox: bool | None | Unset = UNSET
    group_site: bool | None | Unset = UNSET
    id: None | str | Unset = UNSET
    field_links: None | RESTJobGroupItemLinksType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_job_group_item_links_type_0 import RESTJobGroupItemLinksType0

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        members: bool | None | Unset
        if isinstance(self.members, Unset):
            members = UNSET
        else:
            members = self.members

        member_mailbox: bool | None | Unset
        if isinstance(self.member_mailbox, Unset):
            member_mailbox = UNSET
        else:
            member_mailbox = self.member_mailbox

        member_archive_mailbox: bool | None | Unset
        if isinstance(self.member_archive_mailbox, Unset):
            member_archive_mailbox = UNSET
        else:
            member_archive_mailbox = self.member_archive_mailbox

        member_onedrive: bool | None | Unset
        if isinstance(self.member_onedrive, Unset):
            member_onedrive = UNSET
        else:
            member_onedrive = self.member_onedrive

        member_site: bool | None | Unset
        if isinstance(self.member_site, Unset):
            member_site = UNSET
        else:
            member_site = self.member_site

        mailbox: bool | None | Unset
        if isinstance(self.mailbox, Unset):
            mailbox = UNSET
        else:
            mailbox = self.mailbox

        group_site: bool | None | Unset
        if isinstance(self.group_site, Unset):
            group_site = UNSET
        else:
            group_site = self.group_site

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, RESTJobGroupItemLinksType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if group is not UNSET:
            field_dict["group"] = group
        if members is not UNSET:
            field_dict["members"] = members
        if member_mailbox is not UNSET:
            field_dict["memberMailbox"] = member_mailbox
        if member_archive_mailbox is not UNSET:
            field_dict["memberArchiveMailbox"] = member_archive_mailbox
        if member_onedrive is not UNSET:
            field_dict["memberOnedrive"] = member_onedrive
        if member_site is not UNSET:
            field_dict["memberSite"] = member_site
        if mailbox is not UNSET:
            field_dict["mailbox"] = mailbox
        if group_site is not UNSET:
            field_dict["groupSite"] = group_site
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_group import RESTGroup
        from ..models.rest_job_group_item_links_type_0 import RESTJobGroupItemLinksType0

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTJobBackupItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTJobBackupItemType(_type_)

        _group = d.pop("group", UNSET)
        group: RESTGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = RESTGroup.from_dict(_group)

        def _parse_members(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        members = _parse_members(d.pop("members", UNSET))

        def _parse_member_mailbox(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        member_mailbox = _parse_member_mailbox(d.pop("memberMailbox", UNSET))

        def _parse_member_archive_mailbox(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        member_archive_mailbox = _parse_member_archive_mailbox(d.pop("memberArchiveMailbox", UNSET))

        def _parse_member_onedrive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        member_onedrive = _parse_member_onedrive(d.pop("memberOnedrive", UNSET))

        def _parse_member_site(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        member_site = _parse_member_site(d.pop("memberSite", UNSET))

        def _parse_mailbox(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mailbox = _parse_mailbox(d.pop("mailbox", UNSET))

        def _parse_group_site(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        group_site = _parse_group_site(d.pop("groupSite", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_field_links(data: object) -> None | RESTJobGroupItemLinksType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_links_type_0 = RESTJobGroupItemLinksType0.from_dict(data)

                return field_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTJobGroupItemLinksType0 | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        rest_job_group_item = cls(
            type_=type_,
            group=group,
            members=members,
            member_mailbox=member_mailbox,
            member_archive_mailbox=member_archive_mailbox,
            member_onedrive=member_onedrive,
            member_site=member_site,
            mailbox=mailbox,
            group_site=group_site,
            id=id,
            field_links=field_links,
        )

        rest_job_group_item.additional_properties = d
        return rest_job_group_item

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
