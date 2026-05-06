from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_protected_user_account_type import RESTProtectedUserAccountType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_protected_mailbox import RESTProtectedMailbox
  from ..models.rest_protected_one_drive import RESTProtectedOneDrive
  from ..models.rest_protected_site import RESTProtectedSite





T = TypeVar("T", bound="RESTProtectedUser")



@_attrs_define
class RESTProtectedUser:
    """ 
        Attributes:
            id (str | Unset): User ID.
            msid (None | str | Unset): ID of the protected user assigned by Microsoft.
            display_name (str | Unset): Display name of the backed-up user.
            account_type (RESTProtectedUserAccountType | Unset): Type of the user account.
            organization_id (None | Unset | UUID): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
            backed_up_organization_id (str | Unset): ID of the backed-up organization in the backup.
            mailboxes (list[RESTProtectedMailbox] | Unset): Array of protected mailboxes.
            one_drives (list[RESTProtectedOneDrive] | Unset): Array of protected OneDrives.
            sites (list[RESTProtectedSite] | Unset): Array of protected SharePoint sites.
            e_tag (int | Unset): Version number that Veeam Backup for Microsoft 365 assigns if the protected user was
                modified.
     """

    id: str | Unset = UNSET
    msid: None | str | Unset = UNSET
    display_name: str | Unset = UNSET
    account_type: RESTProtectedUserAccountType | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    backed_up_organization_id: str | Unset = UNSET
    mailboxes: list[RESTProtectedMailbox] | Unset = UNSET
    one_drives: list[RESTProtectedOneDrive] | Unset = UNSET
    sites: list[RESTProtectedSite] | Unset = UNSET
    e_tag: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_protected_mailbox import RESTProtectedMailbox
        from ..models.rest_protected_one_drive import RESTProtectedOneDrive
        from ..models.rest_protected_site import RESTProtectedSite
        id = self.id

        msid: None | str | Unset
        if isinstance(self.msid, Unset):
            msid = UNSET
        else:
            msid = self.msid

        display_name = self.display_name

        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value


        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        backed_up_organization_id = self.backed_up_organization_id

        mailboxes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mailboxes, Unset):
            mailboxes = []
            for mailboxes_item_data in self.mailboxes:
                mailboxes_item = mailboxes_item_data.to_dict()
                mailboxes.append(mailboxes_item)



        one_drives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.one_drives, Unset):
            one_drives = []
            for one_drives_item_data in self.one_drives:
                one_drives_item = one_drives_item_data.to_dict()
                one_drives.append(one_drives_item)



        sites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)



        e_tag = self.e_tag


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if msid is not UNSET:
            field_dict["msid"] = msid
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if backed_up_organization_id is not UNSET:
            field_dict["backedUpOrganizationId"] = backed_up_organization_id
        if mailboxes is not UNSET:
            field_dict["mailboxes"] = mailboxes
        if one_drives is not UNSET:
            field_dict["oneDrives"] = one_drives
        if sites is not UNSET:
            field_dict["sites"] = sites
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_protected_mailbox import RESTProtectedMailbox
        from ..models.rest_protected_one_drive import RESTProtectedOneDrive
        from ..models.rest_protected_site import RESTProtectedSite
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_msid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        msid = _parse_msid(d.pop("msid", UNSET))


        display_name = d.pop("displayName", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: RESTProtectedUserAccountType | Unset
        if isinstance(_account_type,  Unset):
            account_type = UNSET
        else:
            account_type = RESTProtectedUserAccountType(_account_type)




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

        _mailboxes = d.pop("mailboxes", UNSET)
        mailboxes: list[RESTProtectedMailbox] | Unset = UNSET
        if _mailboxes is not UNSET:
            mailboxes = []
            for mailboxes_item_data in _mailboxes:
                mailboxes_item = RESTProtectedMailbox.from_dict(mailboxes_item_data)



                mailboxes.append(mailboxes_item)


        _one_drives = d.pop("oneDrives", UNSET)
        one_drives: list[RESTProtectedOneDrive] | Unset = UNSET
        if _one_drives is not UNSET:
            one_drives = []
            for one_drives_item_data in _one_drives:
                one_drives_item = RESTProtectedOneDrive.from_dict(one_drives_item_data)



                one_drives.append(one_drives_item)


        _sites = d.pop("sites", UNSET)
        sites: list[RESTProtectedSite] | Unset = UNSET
        if _sites is not UNSET:
            sites = []
            for sites_item_data in _sites:
                sites_item = RESTProtectedSite.from_dict(sites_item_data)



                sites.append(sites_item)


        e_tag = d.pop("eTag", UNSET)

        rest_protected_user = cls(
            id=id,
            msid=msid,
            display_name=display_name,
            account_type=account_type,
            organization_id=organization_id,
            backed_up_organization_id=backed_up_organization_id,
            mailboxes=mailboxes,
            one_drives=one_drives,
            sites=sites,
            e_tag=e_tag,
        )


        rest_protected_user.additional_properties = d
        return rest_protected_user

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
