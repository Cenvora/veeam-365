from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_job_backup_item_type import RESTJobBackupItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_group import RESTGroup
    from ..models.rest_job_item_composed_links_type_0 import RESTJobItemComposedLinksType0
    from ..models.rest_job_site import RESTJobSite
    from ..models.rest_team import RESTTeam
    from ..models.rest_user import RESTUser


T = TypeVar("T", bound="RESTJobItemComposed")


@_attrs_define
class RESTJobItemComposed:
    """
    Attributes:
        type_ (RESTJobBackupItemType | Unset): Type of the backup item.
        folders (list[str] | Unset): Array of OneDrive folders included in/excluded from the backup job.

            **Note**: This property applies to all OneDrives in an organization. Only specified folders will be processed
            for each OneDrive.
        id (None | str | Unset): Backup item ID.

            **Note**: This complex ID comprises the combination of the unchangeable identificator of an object type in Veeam
            Backup for Microsoft 365 and ID of a particular object. Unchangeable identificators have different values
            depending on an object type. You can use the following values to recognize objects of a particular type in the
            response: <ul> <li>*2b38d840-8098-4614-b369-ebce33f9b2c7* - for organization users.</li>
            <li>*9592732d-22d8-426a-8167-d9635158e945* - for organization groups.</li>
            <li>*e1fa728c-4150-4724-ab3b-5deda33db0cf* - for organization sites.</li>
            <li>*c37da450-6c4b-48c4-87e2-cc557ef5d897* - for organizations.</li> <li>*9a01bcb3-d2de-4271-96bb-95611ddc70b3*
            - for personal sites.</li> <li>*7f07820e-9e77-4beb-92a3-b31f30bc192c* - for OneDrive folders.</li>
            <li>*7B985334-BC0E-4791-B30C-D03A1FECC840* - for teams.</li> </ul>
        field_links (None | RESTJobItemComposedLinksType0 | Unset):
        mailbox (bool | None | Unset): Defines whether this backup job will include/exclude the *Mail* processing
            option.
        one_drive (bool | None | Unset): Defines whether this backup job will include/exclude the *OneDrive* processing
            option.
        archive_mailbox (bool | None | Unset): Defines whether this backup job will include/exclude the *Archive*
            processing option.
        sites (bool | None | Unset): Defines whether this backup job will include/exclude the *Sites* processing option.
        teams (bool | None | Unset): Defines whether this backup job will include/exclude the *Teams* processing option.
        teams_chats (bool | None | Unset): Defines whether this job will back up team chats.
        site (RESTJobSite | Unset):
        team (RESTTeam | Unset):
        user (RESTUser | Unset):
        personal_site (bool | None | Unset): Defines whether this backup job will include/exclude the *Site* processing
            option.
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
        group_site (bool | None | Unset): Defines whether this job will back up a group site.
    """

    type_: RESTJobBackupItemType | Unset = UNSET
    folders: list[str] | Unset = UNSET
    id: None | str | Unset = UNSET
    field_links: None | RESTJobItemComposedLinksType0 | Unset = UNSET
    mailbox: bool | None | Unset = UNSET
    one_drive: bool | None | Unset = UNSET
    archive_mailbox: bool | None | Unset = UNSET
    sites: bool | None | Unset = UNSET
    teams: bool | None | Unset = UNSET
    teams_chats: bool | None | Unset = UNSET
    site: RESTJobSite | Unset = UNSET
    team: RESTTeam | Unset = UNSET
    user: RESTUser | Unset = UNSET
    personal_site: bool | None | Unset = UNSET
    group: RESTGroup | Unset = UNSET
    members: bool | None | Unset = UNSET
    member_mailbox: bool | None | Unset = UNSET
    member_archive_mailbox: bool | None | Unset = UNSET
    member_onedrive: bool | None | Unset = UNSET
    member_site: bool | None | Unset = UNSET
    group_site: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_job_item_composed_links_type_0 import RESTJobItemComposedLinksType0

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        folders: list[str] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = self.folders

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, RESTJobItemComposedLinksType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

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

        site: dict[str, Any] | Unset = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        team: dict[str, Any] | Unset = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        personal_site: bool | None | Unset
        if isinstance(self.personal_site, Unset):
            personal_site = UNSET
        else:
            personal_site = self.personal_site

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

        group_site: bool | None | Unset
        if isinstance(self.group_site, Unset):
            group_site = UNSET
        else:
            group_site = self.group_site

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if folders is not UNSET:
            field_dict["folders"] = folders
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links
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
        if site is not UNSET:
            field_dict["site"] = site
        if team is not UNSET:
            field_dict["team"] = team
        if user is not UNSET:
            field_dict["user"] = user
        if personal_site is not UNSET:
            field_dict["personalSite"] = personal_site
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
        if group_site is not UNSET:
            field_dict["groupSite"] = group_site

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_group import RESTGroup
        from ..models.rest_job_item_composed_links_type_0 import RESTJobItemComposedLinksType0
        from ..models.rest_job_site import RESTJobSite
        from ..models.rest_team import RESTTeam
        from ..models.rest_user import RESTUser

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTJobBackupItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTJobBackupItemType(_type_)

        folders = cast(list[str], d.pop("folders", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_field_links(data: object) -> None | RESTJobItemComposedLinksType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_links_type_0 = RESTJobItemComposedLinksType0.from_dict(data)

                return field_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTJobItemComposedLinksType0 | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

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

        _site = d.pop("site", UNSET)
        site: RESTJobSite | Unset
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = RESTJobSite.from_dict(_site)

        _team = d.pop("team", UNSET)
        team: RESTTeam | Unset
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = RESTTeam.from_dict(_team)

        _user = d.pop("user", UNSET)
        user: RESTUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RESTUser.from_dict(_user)

        def _parse_personal_site(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        personal_site = _parse_personal_site(d.pop("personalSite", UNSET))

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

        def _parse_group_site(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        group_site = _parse_group_site(d.pop("groupSite", UNSET))

        rest_job_item_composed = cls(
            type_=type_,
            folders=folders,
            id=id,
            field_links=field_links,
            mailbox=mailbox,
            one_drive=one_drive,
            archive_mailbox=archive_mailbox,
            sites=sites,
            teams=teams,
            teams_chats=teams_chats,
            site=site,
            team=team,
            user=user,
            personal_site=personal_site,
            group=group,
            members=members,
            member_mailbox=member_mailbox,
            member_archive_mailbox=member_archive_mailbox,
            member_onedrive=member_onedrive,
            member_site=member_site,
            group_site=group_site,
        )

        rest_job_item_composed.additional_properties = d
        return rest_job_item_composed

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
