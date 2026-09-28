from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_licensing_organization_removed_objects import RESTLicensingOrganizationRemovedObjects


T = TypeVar("T", bound="RESTLicensingApproveReportOptions")


@_attrs_define
class RESTLicensingApproveReportOptions:
    """
    Attributes:
        removed_objects (list[RESTLicensingOrganizationRemovedObjects] | Unset): Specifies the information about objects
            removed from the report for each organization added to Veeam Backup for Microsoft 365.
    """

    removed_objects: list[RESTLicensingOrganizationRemovedObjects] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        removed_objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.removed_objects, Unset):
            removed_objects = []
            for removed_objects_item_data in self.removed_objects:
                removed_objects_item = removed_objects_item_data.to_dict()
                removed_objects.append(removed_objects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if removed_objects is not UNSET:
            field_dict["removedObjects"] = removed_objects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_licensing_organization_removed_objects import RESTLicensingOrganizationRemovedObjects

        d = dict(src_dict)
        _removed_objects = d.pop("removedObjects", UNSET)
        removed_objects: list[RESTLicensingOrganizationRemovedObjects] | Unset = UNSET
        if _removed_objects is not UNSET:
            removed_objects = []
            for removed_objects_item_data in _removed_objects:
                removed_objects_item = RESTLicensingOrganizationRemovedObjects.from_dict(removed_objects_item_data)

                removed_objects.append(removed_objects_item)

        rest_licensing_approve_report_options = cls(
            removed_objects=removed_objects,
        )

        rest_licensing_approve_report_options.additional_properties = d
        return rest_licensing_approve_report_options

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
