from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_job_backup_item_type import RESTJobBackupItemType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_job_user_item_links_type_0 import RESTJobUserItemLinksType0
  from ..models.rest_user import RESTUser





T = TypeVar("T", bound="RESTJobUserItem")



@_attrs_define
class RESTJobUserItem:
    """ 
        Attributes:
            type_ (RESTJobBackupItemType | Unset): Type of the backup item.
            user (RESTUser | Unset):
            mailbox (bool | None | Unset): Defines whether this backup job will include/exclude the *Mail* processing
                option.
            one_drive (bool | None | Unset): Defines whether this backup job will include/exclude the *OneDrive* processing
                option.
            archive_mailbox (bool | None | Unset): Defines whether this backup job will include/exclude the *Archive*
                processing option.
            personal_site (bool | None | Unset): Defines whether this backup job will include/exclude the *Site* processing
                option.
            id (None | str | Unset): Backup item ID.
            field_links (None | RESTJobUserItemLinksType0 | Unset):
     """

    type_: RESTJobBackupItemType | Unset = UNSET
    user: RESTUser | Unset = UNSET
    mailbox: bool | None | Unset = UNSET
    one_drive: bool | None | Unset = UNSET
    archive_mailbox: bool | None | Unset = UNSET
    personal_site: bool | None | Unset = UNSET
    id: None | str | Unset = UNSET
    field_links: None | RESTJobUserItemLinksType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_job_user_item_links_type_0 import RESTJobUserItemLinksType0
        from ..models.rest_user import RESTUser
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

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

        personal_site: bool | None | Unset
        if isinstance(self.personal_site, Unset):
            personal_site = UNSET
        else:
            personal_site = self.personal_site

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, RESTJobUserItemLinksType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user is not UNSET:
            field_dict["user"] = user
        if mailbox is not UNSET:
            field_dict["mailbox"] = mailbox
        if one_drive is not UNSET:
            field_dict["oneDrive"] = one_drive
        if archive_mailbox is not UNSET:
            field_dict["archiveMailbox"] = archive_mailbox
        if personal_site is not UNSET:
            field_dict["personalSite"] = personal_site
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_job_user_item_links_type_0 import RESTJobUserItemLinksType0
        from ..models.rest_user import RESTUser
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTJobBackupItemType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RESTJobBackupItemType(_type_)




        _user = d.pop("user", UNSET)
        user: RESTUser | Unset
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = RESTUser.from_dict(_user)




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


        def _parse_personal_site(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        personal_site = _parse_personal_site(d.pop("personalSite", UNSET))


        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_field_links(data: object) -> None | RESTJobUserItemLinksType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_links_type_0 = RESTJobUserItemLinksType0.from_dict(data)



                return field_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTJobUserItemLinksType0 | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))


        rest_job_user_item = cls(
            type_=type_,
            user=user,
            mailbox=mailbox,
            one_drive=one_drive,
            archive_mailbox=archive_mailbox,
            personal_site=personal_site,
            id=id,
            field_links=field_links,
        )


        rest_job_user_item.additional_properties = d
        return rest_job_user_item

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
