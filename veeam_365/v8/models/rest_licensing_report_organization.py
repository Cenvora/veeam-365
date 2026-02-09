from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTLicensingReportOrganization")


@_attrs_define
class RESTLicensingReportOrganization:
    """
    Attributes:
        organization_id (UUID | Unset): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
        backed_up_organization_id (str | Unset): ID of the backed-up Microsoft organization in the backup.
        organization_name (str | Unset): Name of the Microsoft organization whose license usage statistics is included
            in the report.
        initial_count (int | Unset): Number of objects that consume the license within the time period covered by the
            report.
        initial_points (float | Unset): Number of licensing points that consume the license within the time period
            covered by the report.
        reported_count (int | Unset): Number of objects consuming the license that you report to Veeam.
        reported_points (float | Unset): Number of licensing points consuming the license that you report to Veeam.
        new_count (int | Unset): Number of objects that were activated within the time period covered by the report.
        new_points (float | Unset): Number of licensing points that were activated within the time period covered by the
            report.
        removed_count (int | Unset): Number of objects removed from the report.
        removed_points (float | Unset): Number of licensing points removed from the report.
        removal_reason (str | Unset): Reason for removal of objects from the report.
    """

    organization_id: UUID | Unset = UNSET
    backed_up_organization_id: str | Unset = UNSET
    organization_name: str | Unset = UNSET
    initial_count: int | Unset = UNSET
    initial_points: float | Unset = UNSET
    reported_count: int | Unset = UNSET
    reported_points: float | Unset = UNSET
    new_count: int | Unset = UNSET
    new_points: float | Unset = UNSET
    removed_count: int | Unset = UNSET
    removed_points: float | Unset = UNSET
    removal_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        backed_up_organization_id = self.backed_up_organization_id

        organization_name = self.organization_name

        initial_count = self.initial_count

        initial_points = self.initial_points

        reported_count = self.reported_count

        reported_points = self.reported_points

        new_count = self.new_count

        new_points = self.new_points

        removed_count = self.removed_count

        removed_points = self.removed_points

        removal_reason = self.removal_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if backed_up_organization_id is not UNSET:
            field_dict["backedUpOrganizationId"] = backed_up_organization_id
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if initial_count is not UNSET:
            field_dict["initialCount"] = initial_count
        if initial_points is not UNSET:
            field_dict["initialPoints"] = initial_points
        if reported_count is not UNSET:
            field_dict["reportedCount"] = reported_count
        if reported_points is not UNSET:
            field_dict["reportedPoints"] = reported_points
        if new_count is not UNSET:
            field_dict["newCount"] = new_count
        if new_points is not UNSET:
            field_dict["newPoints"] = new_points
        if removed_count is not UNSET:
            field_dict["removedCount"] = removed_count
        if removed_points is not UNSET:
            field_dict["removedPoints"] = removed_points
        if removal_reason is not UNSET:
            field_dict["removalReason"] = removal_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _organization_id = d.pop("organizationId", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        backed_up_organization_id = d.pop("backedUpOrganizationId", UNSET)

        organization_name = d.pop("organizationName", UNSET)

        initial_count = d.pop("initialCount", UNSET)

        initial_points = d.pop("initialPoints", UNSET)

        reported_count = d.pop("reportedCount", UNSET)

        reported_points = d.pop("reportedPoints", UNSET)

        new_count = d.pop("newCount", UNSET)

        new_points = d.pop("newPoints", UNSET)

        removed_count = d.pop("removedCount", UNSET)

        removed_points = d.pop("removedPoints", UNSET)

        removal_reason = d.pop("removalReason", UNSET)

        rest_licensing_report_organization = cls(
            organization_id=organization_id,
            backed_up_organization_id=backed_up_organization_id,
            organization_name=organization_name,
            initial_count=initial_count,
            initial_points=initial_points,
            reported_count=reported_count,
            reported_points=reported_points,
            new_count=new_count,
            new_points=new_points,
            removed_count=removed_count,
            removed_points=removed_points,
            removal_reason=removal_reason,
        )

        rest_licensing_report_organization.additional_properties = d
        return rest_licensing_report_organization

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
