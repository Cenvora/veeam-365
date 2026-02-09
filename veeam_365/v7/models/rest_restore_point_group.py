from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTRestorePointGroup")


@_attrs_define
class RESTRestorePointGroup:
    """
    Attributes:
        is_mailbox_backed_up (bool | Unset): Defines whether the group mailbox was backed-up.
        is_site_backed_up (bool | Unset): Defines whether the group site was backed-up.
        id (str | Unset): Group ID.
        account_id (str | Unset): Group account ID.
        display_name (str | Unset): Display name of the backed-up group.
        email (str | Unset): Group email.
        group_site_url (list[str] | Unset): Group site path.
        organization_id (None | Unset | UUID): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
        backed_up_organization_id (str | Unset): ID of the backed-up organization in the backup.
        field_links (RESTLinkHALDictionary | Unset):
    """

    is_mailbox_backed_up: bool | Unset = UNSET
    is_site_backed_up: bool | Unset = UNSET
    id: str | Unset = UNSET
    account_id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    group_site_url: list[str] | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    backed_up_organization_id: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_mailbox_backed_up = self.is_mailbox_backed_up

        is_site_backed_up = self.is_site_backed_up

        id = self.id

        account_id = self.account_id

        display_name = self.display_name

        email = self.email

        group_site_url: list[str] | Unset = UNSET
        if not isinstance(self.group_site_url, Unset):
            group_site_url = self.group_site_url

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
        if is_site_backed_up is not UNSET:
            field_dict["isSiteBackedUp"] = is_site_backed_up
        if id is not UNSET:
            field_dict["id"] = id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if group_site_url is not UNSET:
            field_dict["groupSiteUrl"] = group_site_url
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

        is_site_backed_up = d.pop("isSiteBackedUp", UNSET)

        id = d.pop("id", UNSET)

        account_id = d.pop("accountId", UNSET)

        display_name = d.pop("displayName", UNSET)

        email = d.pop("email", UNSET)

        group_site_url = cast(list[str], d.pop("groupSiteUrl", UNSET))

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

        rest_restore_point_group = cls(
            is_mailbox_backed_up=is_mailbox_backed_up,
            is_site_backed_up=is_site_backed_up,
            id=id,
            account_id=account_id,
            display_name=display_name,
            email=email,
            group_site_url=group_site_url,
            organization_id=organization_id,
            backed_up_organization_id=backed_up_organization_id,
            field_links=field_links,
        )

        rest_restore_point_group.additional_properties = d
        return rest_restore_point_group

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
