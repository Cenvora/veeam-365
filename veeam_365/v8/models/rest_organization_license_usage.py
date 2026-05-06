from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="RESTOrganizationLicenseUsage")



@_attrs_define
class RESTOrganizationLicenseUsage:
    """ 
        Attributes:
            organization_id (None | Unset | UUID): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
            backed_up_organization_id (str | Unset): ID of the backed-up Microsoft organization in the backup.
            organization_name (str | Unset): Name of the Microsoft organization whose license usage statistics is included
                in the report.
            used_objects_count (int | Unset): Number of objects that have licenses assigned.
            used_points (float | Unset): Number of licensing points that have licenses assigned.
            new_objects_count (int | Unset): Number of objects that were activated within the time period covered by the
                report.
            new_points (float | Unset): Number of licensing points that were activated within the time period covered by the
                report.
     """

    organization_id: None | Unset | UUID = UNSET
    backed_up_organization_id: str | Unset = UNSET
    organization_name: str | Unset = UNSET
    used_objects_count: int | Unset = UNSET
    used_points: float | Unset = UNSET
    new_objects_count: int | Unset = UNSET
    new_points: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        backed_up_organization_id = self.backed_up_organization_id

        organization_name = self.organization_name

        used_objects_count = self.used_objects_count

        used_points = self.used_points

        new_objects_count = self.new_objects_count

        new_points = self.new_points


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if backed_up_organization_id is not UNSET:
            field_dict["backedUpOrganizationId"] = backed_up_organization_id
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if used_objects_count is not UNSET:
            field_dict["usedObjectsCount"] = used_objects_count
        if used_points is not UNSET:
            field_dict["usedPoints"] = used_points
        if new_objects_count is not UNSET:
            field_dict["newObjectsCount"] = new_objects_count
        if new_points is not UNSET:
            field_dict["newPoints"] = new_points

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        organization_name = d.pop("organizationName", UNSET)

        used_objects_count = d.pop("usedObjectsCount", UNSET)

        used_points = d.pop("usedPoints", UNSET)

        new_objects_count = d.pop("newObjectsCount", UNSET)

        new_points = d.pop("newPoints", UNSET)

        rest_organization_license_usage = cls(
            organization_id=organization_id,
            backed_up_organization_id=backed_up_organization_id,
            organization_name=organization_name,
            used_objects_count=used_objects_count,
            used_points=used_points,
            new_objects_count=new_objects_count,
            new_points=new_points,
        )


        rest_organization_license_usage.additional_properties = d
        return rest_organization_license_usage

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
