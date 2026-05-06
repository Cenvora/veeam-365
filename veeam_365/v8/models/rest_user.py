from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_user_location_type import RESTUserLocationType
from ..models.rest_user_type import RESTUserType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
  from ..models.rest_office_license import RESTOfficeLicense





T = TypeVar("T", bound="RESTUser")



@_attrs_define
class RESTUser:
    """ 
        Attributes:
            id (str | Unset): Organization user ID.
            e_tag (int | None | Unset): Version number that Veeam Backup for Microsoft 365 assigns if the organization user
                was modified.
            on_premises_sid (str | Unset): ID of the organization user in the on-premises organization.
            display_name (str | Unset): Display name of the organization user.
            name (str | Unset): Email address of the organization user.
            type_ (RESTUserType | Unset): Type of the organization user.
            location_type (RESTUserLocationType | Unset): Microsoft 365 organization deployment type.
            office (str | Unset): Office location in the place of business of the organization user.
            assigned_licenses (list[RESTOfficeLicense] | None | Unset): Array of licenses assigned to the organization user.
            msid (None | Unset | UUID): ID of the organization user assigned by Microsoft.
            data_location (None | str | Unset): Data location of the organization user.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
     """

    id: str | Unset = UNSET
    e_tag: int | None | Unset = UNSET
    on_premises_sid: str | Unset = UNSET
    display_name: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: RESTUserType | Unset = UNSET
    location_type: RESTUserLocationType | Unset = UNSET
    office: str | Unset = UNSET
    assigned_licenses: list[RESTOfficeLicense] | None | Unset = UNSET
    msid: None | Unset | UUID = UNSET
    data_location: None | str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_office_license import RESTOfficeLicense
        id = self.id

        e_tag: int | None | Unset
        if isinstance(self.e_tag, Unset):
            e_tag = UNSET
        else:
            e_tag = self.e_tag

        on_premises_sid = self.on_premises_sid

        display_name = self.display_name

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value


        office = self.office

        assigned_licenses: list[dict[str, Any]] | None | Unset
        if isinstance(self.assigned_licenses, Unset):
            assigned_licenses = UNSET
        elif isinstance(self.assigned_licenses, list):
            assigned_licenses = []
            for assigned_licenses_type_0_item_data in self.assigned_licenses:
                assigned_licenses_type_0_item = assigned_licenses_type_0_item_data.to_dict()
                assigned_licenses.append(assigned_licenses_type_0_item)


        else:
            assigned_licenses = self.assigned_licenses

        msid: None | str | Unset
        if isinstance(self.msid, Unset):
            msid = UNSET
        elif isinstance(self.msid, UUID):
            msid = str(self.msid)
        else:
            msid = self.msid

        data_location: None | str | Unset
        if isinstance(self.data_location, Unset):
            data_location = UNSET
        else:
            data_location = self.data_location

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag
        if on_premises_sid is not UNSET:
            field_dict["onPremisesSid"] = on_premises_sid
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if location_type is not UNSET:
            field_dict["locationType"] = location_type
        if office is not UNSET:
            field_dict["office"] = office
        if assigned_licenses is not UNSET:
            field_dict["assignedLicenses"] = assigned_licenses
        if msid is not UNSET:
            field_dict["msid"] = msid
        if data_location is not UNSET:
            field_dict["dataLocation"] = data_location
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_office_license import RESTOfficeLicense
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_e_tag(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        e_tag = _parse_e_tag(d.pop("eTag", UNSET))


        on_premises_sid = d.pop("onPremisesSid", UNSET)

        display_name = d.pop("displayName", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTUserType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RESTUserType(_type_)




        _location_type = d.pop("locationType", UNSET)
        location_type: RESTUserLocationType | Unset
        if isinstance(_location_type,  Unset):
            location_type = UNSET
        else:
            location_type = RESTUserLocationType(_location_type)




        office = d.pop("office", UNSET)

        def _parse_assigned_licenses(data: object) -> list[RESTOfficeLicense] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_licenses_type_0 = []
                _assigned_licenses_type_0 = data
                for assigned_licenses_type_0_item_data in (_assigned_licenses_type_0):
                    assigned_licenses_type_0_item = RESTOfficeLicense.from_dict(assigned_licenses_type_0_item_data)



                    assigned_licenses_type_0.append(assigned_licenses_type_0_item)

                return assigned_licenses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RESTOfficeLicense] | None | Unset, data)

        assigned_licenses = _parse_assigned_licenses(d.pop("assignedLicenses", UNSET))


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


        def _parse_data_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_location = _parse_data_location(d.pop("dataLocation", UNSET))


        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        rest_user = cls(
            id=id,
            e_tag=e_tag,
            on_premises_sid=on_premises_sid,
            display_name=display_name,
            name=name,
            type_=type_,
            location_type=location_type,
            office=office,
            assigned_licenses=assigned_licenses,
            msid=msid,
            data_location=data_location,
            field_links=field_links,
        )


        rest_user.additional_properties = d
        return rest_user

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
