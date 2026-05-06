from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_backup_item_type import RESTBackupItemType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary





T = TypeVar("T", bound="RESTBackupTeamData")



@_attrs_define
class RESTBackupTeamData:
    """ 
        Attributes:
            id (str): Team ID.
            item_type (RESTBackupItemType): Type of the backup item.
            repository_id (UUID): Backup repository ID.
            backed_up_organization_id (str): ID of the backed-up organization in the backup.
            display_name (str | Unset): Display name of the backed-up or archived team.
            backed_up_time (datetime.datetime | None | Unset): Date and time when the team was backed up.
            organization_id (None | Unset | UUID): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
            msid (None | Unset | UUID): ID of the organization assigned by Microsoft. Example:
                00000000-0000-0000-0000-000000000000.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
     """

    id: str
    item_type: RESTBackupItemType
    repository_id: UUID
    backed_up_organization_id: str
    display_name: str | Unset = UNSET
    backed_up_time: datetime.datetime | None | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    msid: None | Unset | UUID = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        id = self.id

        item_type = self.item_type.value

        repository_id = str(self.repository_id)

        backed_up_organization_id = self.backed_up_organization_id

        display_name = self.display_name

        backed_up_time: None | str | Unset
        if isinstance(self.backed_up_time, Unset):
            backed_up_time = UNSET
        elif isinstance(self.backed_up_time, datetime.datetime):
            backed_up_time = self.backed_up_time.isoformat()
        else:
            backed_up_time = self.backed_up_time

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        msid: None | str | Unset
        if isinstance(self.msid, Unset):
            msid = UNSET
        elif isinstance(self.msid, UUID):
            msid = str(self.msid)
        else:
            msid = self.msid

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "itemType": item_type,
            "repositoryId": repository_id,
            "backedUpOrganizationId": backed_up_organization_id,
        })
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if backed_up_time is not UNSET:
            field_dict["backedUpTime"] = backed_up_time
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if msid is not UNSET:
            field_dict["msid"] = msid
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        d = dict(src_dict)
        id = d.pop("id")

        item_type = RESTBackupItemType(d.pop("itemType"))




        repository_id = UUID(d.pop("repositoryId"))




        backed_up_organization_id = d.pop("backedUpOrganizationId")

        display_name = d.pop("displayName", UNSET)

        def _parse_backed_up_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backed_up_time_type_0 = isoparse(data)



                return backed_up_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        backed_up_time = _parse_backed_up_time(d.pop("backedUpTime", UNSET))


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


        def _parse_msid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                msid_type_0 = UUID(data)



                return msid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        msid = _parse_msid(d.pop("msid", UNSET))


        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        rest_backup_team_data = cls(
            id=id,
            item_type=item_type,
            repository_id=repository_id,
            backed_up_organization_id=backed_up_organization_id,
            display_name=display_name,
            backed_up_time=backed_up_time,
            organization_id=organization_id,
            msid=msid,
            field_links=field_links,
        )


        rest_backup_team_data.additional_properties = d
        return rest_backup_team_data

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
