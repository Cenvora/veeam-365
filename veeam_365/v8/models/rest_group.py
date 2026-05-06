from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_group_location_type import RESTGroupLocationType
from ..models.rest_group_type import RESTGroupType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary





T = TypeVar("T", bound="RESTGroup")



@_attrs_define
class RESTGroup:
    """ 
        Attributes:
            id (str | Unset): Organization group ID.
            e_tag (int | None | Unset): Version number that Veeam Backup for Microsoft 365 assigns if the organization group
                was modified.
            on_premises_sid (None | str | Unset): ID of the organization group in the on-premises organization.
            display_name (str | Unset): Display name of the organization group.
            name (None | str | Unset): Name of the organization group.
            managed_by (None | str | Unset): User who manages the organization group.
            site (None | str | Unset): Site of the organization group.
            type_ (RESTGroupType | Unset): Type of the organization group.
            location_type (RESTGroupLocationType | Unset): Microsoft 365 organization deployment type.
            msid (None | Unset | UUID): ID of the organization group assigned by Microsoft.
            data_location (None | str | Unset): Data location of the organization group.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
     """

    id: str | Unset = UNSET
    e_tag: int | None | Unset = UNSET
    on_premises_sid: None | str | Unset = UNSET
    display_name: str | Unset = UNSET
    name: None | str | Unset = UNSET
    managed_by: None | str | Unset = UNSET
    site: None | str | Unset = UNSET
    type_: RESTGroupType | Unset = UNSET
    location_type: RESTGroupLocationType | Unset = UNSET
    msid: None | Unset | UUID = UNSET
    data_location: None | str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        id = self.id

        e_tag: int | None | Unset
        if isinstance(self.e_tag, Unset):
            e_tag = UNSET
        else:
            e_tag = self.e_tag

        on_premises_sid: None | str | Unset
        if isinstance(self.on_premises_sid, Unset):
            on_premises_sid = UNSET
        else:
            on_premises_sid = self.on_premises_sid

        display_name = self.display_name

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        managed_by: None | str | Unset
        if isinstance(self.managed_by, Unset):
            managed_by = UNSET
        else:
            managed_by = self.managed_by

        site: None | str | Unset
        if isinstance(self.site, Unset):
            site = UNSET
        else:
            site = self.site

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value


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
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by
        if site is not UNSET:
            field_dict["site"] = site
        if type_ is not UNSET:
            field_dict["type"] = type_
        if location_type is not UNSET:
            field_dict["locationType"] = location_type
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
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_e_tag(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        e_tag = _parse_e_tag(d.pop("eTag", UNSET))


        def _parse_on_premises_sid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        on_premises_sid = _parse_on_premises_sid(d.pop("onPremisesSid", UNSET))


        display_name = d.pop("displayName", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_managed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_by = _parse_managed_by(d.pop("managedBy", UNSET))


        def _parse_site(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site = _parse_site(d.pop("site", UNSET))


        _type_ = d.pop("type", UNSET)
        type_: RESTGroupType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RESTGroupType(_type_)




        _location_type = d.pop("locationType", UNSET)
        location_type: RESTGroupLocationType | Unset
        if isinstance(_location_type,  Unset):
            location_type = UNSET
        else:
            location_type = RESTGroupLocationType(_location_type)




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




        rest_group = cls(
            id=id,
            e_tag=e_tag,
            on_premises_sid=on_premises_sid,
            display_name=display_name,
            name=name,
            managed_by=managed_by,
            site=site,
            type_=type_,
            location_type=location_type,
            msid=msid,
            data_location=data_location,
            field_links=field_links,
        )


        rest_group.additional_properties = d
        return rest_group

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
