from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="RESTLicensingOrganizationRemovedObjects")



@_attrs_define
class RESTLicensingOrganizationRemovedObjects:
    """ 
        Attributes:
            organization_id (UUID | Unset): Specifies the identification number of the Microsoft 365 organization.
            backed_up_organization_id (str | Unset): Specifies the identification number of the backed-up Microsoft
                organization in the backup.
            platform_id (UUID | Unset): Specifies the identification number of the licensing platform.
            type_id (int | Unset): Specifies the identification number of the license usage counter type.
            removed_count (int | Unset): Specifies the number of organization objects removed from the report.
            removal_reason (str | Unset): Specifies the reason for removal of objects from the report.
     """

    organization_id: UUID | Unset = UNSET
    backed_up_organization_id: str | Unset = UNSET
    platform_id: UUID | Unset = UNSET
    type_id: int | Unset = UNSET
    removed_count: int | Unset = UNSET
    removal_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        backed_up_organization_id = self.backed_up_organization_id

        platform_id: str | Unset = UNSET
        if not isinstance(self.platform_id, Unset):
            platform_id = str(self.platform_id)

        type_id = self.type_id

        removed_count = self.removed_count

        removal_reason = self.removal_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if backed_up_organization_id is not UNSET:
            field_dict["backedUpOrganizationId"] = backed_up_organization_id
        if platform_id is not UNSET:
            field_dict["platformId"] = platform_id
        if type_id is not UNSET:
            field_dict["typeId"] = type_id
        if removed_count is not UNSET:
            field_dict["removedCount"] = removed_count
        if removal_reason is not UNSET:
            field_dict["removalReason"] = removal_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _organization_id = d.pop("organizationId", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id,  Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)




        backed_up_organization_id = d.pop("backedUpOrganizationId", UNSET)

        _platform_id = d.pop("platformId", UNSET)
        platform_id: UUID | Unset
        if isinstance(_platform_id,  Unset):
            platform_id = UNSET
        else:
            platform_id = UUID(_platform_id)




        type_id = d.pop("typeId", UNSET)

        removed_count = d.pop("removedCount", UNSET)

        removal_reason = d.pop("removalReason", UNSET)

        rest_licensing_organization_removed_objects = cls(
            organization_id=organization_id,
            backed_up_organization_id=backed_up_organization_id,
            platform_id=platform_id,
            type_id=type_id,
            removed_count=removed_count,
            removal_reason=removal_reason,
        )


        rest_licensing_organization_removed_objects.additional_properties = d
        return rest_licensing_organization_removed_objects

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
