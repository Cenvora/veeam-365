from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="RESTTenantInformation")



@_attrs_define
class RESTTenantInformation:
    """ 
        Attributes:
            msid (UUID | Unset): ID of the organization assigned by Microsoft. Example:
                00000000-0000-0000-0000-000000000000.
            multiple_data_locations_enabled (bool | Unset): Defines whether the Multi-Geo tenants are available for the
                Microsoft organization.
            primary_location (None | str | Unset): Primary geographic location for the Microsoft organization.
            enable_location_protection (bool | Unset): Defines whether protection of geographic locations is enabled for the
                organization.
            protect_invalid_locations (bool | Unset): Defines whether protection of objects with invalid geographic location
                is enabled.
            protect_empty_locations (bool | Unset): Defines whether protection of objects with empty geographic location is
                enabled.
            protected_locations (list[str] | None | Unset): Array of geographic locations that must be protected.
     """

    msid: UUID | Unset = UNSET
    multiple_data_locations_enabled: bool | Unset = UNSET
    primary_location: None | str | Unset = UNSET
    enable_location_protection: bool | Unset = UNSET
    protect_invalid_locations: bool | Unset = UNSET
    protect_empty_locations: bool | Unset = UNSET
    protected_locations: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        msid: str | Unset = UNSET
        if not isinstance(self.msid, Unset):
            msid = str(self.msid)

        multiple_data_locations_enabled = self.multiple_data_locations_enabled

        primary_location: None | str | Unset
        if isinstance(self.primary_location, Unset):
            primary_location = UNSET
        else:
            primary_location = self.primary_location

        enable_location_protection = self.enable_location_protection

        protect_invalid_locations = self.protect_invalid_locations

        protect_empty_locations = self.protect_empty_locations

        protected_locations: list[str] | None | Unset
        if isinstance(self.protected_locations, Unset):
            protected_locations = UNSET
        elif isinstance(self.protected_locations, list):
            protected_locations = self.protected_locations


        else:
            protected_locations = self.protected_locations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if msid is not UNSET:
            field_dict["msid"] = msid
        if multiple_data_locations_enabled is not UNSET:
            field_dict["multipleDataLocationsEnabled"] = multiple_data_locations_enabled
        if primary_location is not UNSET:
            field_dict["primaryLocation"] = primary_location
        if enable_location_protection is not UNSET:
            field_dict["enableLocationProtection"] = enable_location_protection
        if protect_invalid_locations is not UNSET:
            field_dict["protectInvalidLocations"] = protect_invalid_locations
        if protect_empty_locations is not UNSET:
            field_dict["protectEmptyLocations"] = protect_empty_locations
        if protected_locations is not UNSET:
            field_dict["protectedLocations"] = protected_locations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _msid = d.pop("msid", UNSET)
        msid: UUID | Unset
        if isinstance(_msid,  Unset):
            msid = UNSET
        else:
            msid = UUID(_msid)




        multiple_data_locations_enabled = d.pop("multipleDataLocationsEnabled", UNSET)

        def _parse_primary_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_location = _parse_primary_location(d.pop("primaryLocation", UNSET))


        enable_location_protection = d.pop("enableLocationProtection", UNSET)

        protect_invalid_locations = d.pop("protectInvalidLocations", UNSET)

        protect_empty_locations = d.pop("protectEmptyLocations", UNSET)

        def _parse_protected_locations(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protected_locations_type_0 = cast(list[str], data)

                return protected_locations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        protected_locations = _parse_protected_locations(d.pop("protectedLocations", UNSET))


        rest_tenant_information = cls(
            msid=msid,
            multiple_data_locations_enabled=multiple_data_locations_enabled,
            primary_location=primary_location,
            enable_location_protection=enable_location_protection,
            protect_invalid_locations=protect_invalid_locations,
            protect_empty_locations=protect_empty_locations,
            protected_locations=protected_locations,
        )


        rest_tenant_information.additional_properties = d
        return rest_tenant_information

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
