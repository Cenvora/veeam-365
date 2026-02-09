from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_restore_point_user_account_type import RESTRestorePointUserAccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTRestorePointUser")


@_attrs_define
class RESTRestorePointUser:
    """
    Attributes:
        is_mailbox_backed_up (bool | Unset): Defines whether the user mailbox was backed-up.
        is_one_drive_backed_up (bool | Unset): Defines whether the user OneDrive was backed-up.
        is_archive_backed_up (bool | Unset): Defines whether the archived user mailbox was backed-up.
        is_personal_site_backed_up (bool | Unset): Defines whether the user personal site was backed-up.
        account_type (RESTRestorePointUserAccountType | Unset): Type of the user account.
        archive_name (str | Unset): Name of the user archive.
        id (str | Unset): User ID.
        account_id (str | Unset): User account ID.
        display_name (str | Unset): Display name of the backed-up user.
        email (str | Unset): User email.
        one_drive_url (list[str] | Unset): Array of URLs for the backed-up Microsoft OneDrive components.
        personal_site_url (list[str] | Unset): Array of URLs for the backed-up personal sites.
        organization_id (None | Unset | UUID): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
        backed_up_organization_id (str | Unset): ID of the backed-up organization in the backup.
        field_links (RESTLinkHALDictionary | Unset):
    """

    is_mailbox_backed_up: bool | Unset = UNSET
    is_one_drive_backed_up: bool | Unset = UNSET
    is_archive_backed_up: bool | Unset = UNSET
    is_personal_site_backed_up: bool | Unset = UNSET
    account_type: RESTRestorePointUserAccountType | Unset = UNSET
    archive_name: str | Unset = UNSET
    id: str | Unset = UNSET
    account_id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    one_drive_url: list[str] | Unset = UNSET
    personal_site_url: list[str] | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    backed_up_organization_id: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_mailbox_backed_up = self.is_mailbox_backed_up

        is_one_drive_backed_up = self.is_one_drive_backed_up

        is_archive_backed_up = self.is_archive_backed_up

        is_personal_site_backed_up = self.is_personal_site_backed_up

        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        archive_name = self.archive_name

        id = self.id

        account_id = self.account_id

        display_name = self.display_name

        email = self.email

        one_drive_url: list[str] | Unset = UNSET
        if not isinstance(self.one_drive_url, Unset):
            one_drive_url = self.one_drive_url

        personal_site_url: list[str] | Unset = UNSET
        if not isinstance(self.personal_site_url, Unset):
            personal_site_url = self.personal_site_url

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        backed_up_organization_id = self.backed_up_organization_id

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if id is not UNSET:
            field_dict["id"] = id
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
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if backed_up_organization_id is not UNSET:
            field_dict["backedUpOrganizationId"] = backed_up_organization_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        is_mailbox_backed_up = d.pop("isMailboxBackedUp", UNSET)

        is_one_drive_backed_up = d.pop("isOneDriveBackedUp", UNSET)

        is_archive_backed_up = d.pop("isArchiveBackedUp", UNSET)

        is_personal_site_backed_up = d.pop("isPersonalSiteBackedUp", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: RESTRestorePointUserAccountType | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = RESTRestorePointUserAccountType(_account_type)

        archive_name = d.pop("archiveName", UNSET)

        id = d.pop("id", UNSET)

        account_id = d.pop("accountId", UNSET)

        display_name = d.pop("displayName", UNSET)

        email = d.pop("email", UNSET)

        one_drive_url = cast(list[str], d.pop("oneDriveUrl", UNSET))

        personal_site_url = cast(list[str], d.pop("personalSiteUrl", UNSET))

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organizationId", UNSET))

        backed_up_organization_id = d.pop("backedUpOrganizationId", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_restore_point_user = cls(
            is_mailbox_backed_up=is_mailbox_backed_up,
            is_one_drive_backed_up=is_one_drive_backed_up,
            is_archive_backed_up=is_archive_backed_up,
            is_personal_site_backed_up=is_personal_site_backed_up,
            account_type=account_type,
            archive_name=archive_name,
            id=id,
            account_id=account_id,
            display_name=display_name,
            email=email,
            one_drive_url=one_drive_url,
            personal_site_url=personal_site_url,
            organization_id=organization_id,
            backed_up_organization_id=backed_up_organization_id,
            field_links=field_links,
        )

        rest_restore_point_user.additional_properties = d
        return rest_restore_point_user

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
