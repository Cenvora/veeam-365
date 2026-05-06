from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_licensing_report_organization import RESTLicensingReportOrganization
  from ..models.rest_licensing_report_summary import RESTLicensingReportSummary





T = TypeVar("T", bound="RESTLicensingReportPlatformType")



@_attrs_define
class RESTLicensingReportPlatformType:
    """ 
        Attributes:
            platform_id (UUID | Unset): ID of the licensing platform.
            type_id (int | Unset): ID of the license usage counter type.
            summary (RESTLicensingReportSummary | Unset):
            organizations (list[RESTLicensingReportOrganization] | Unset): Information about license consumption for each
                organization added to Veeam Backup for Microsoft 365.
     """

    platform_id: UUID | Unset = UNSET
    type_id: int | Unset = UNSET
    summary: RESTLicensingReportSummary | Unset = UNSET
    organizations: list[RESTLicensingReportOrganization] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_licensing_report_organization import RESTLicensingReportOrganization
        from ..models.rest_licensing_report_summary import RESTLicensingReportSummary
        platform_id: str | Unset = UNSET
        if not isinstance(self.platform_id, Unset):
            platform_id = str(self.platform_id)

        type_id = self.type_id

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        organizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if platform_id is not UNSET:
            field_dict["platformId"] = platform_id
        if type_id is not UNSET:
            field_dict["typeId"] = type_id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if organizations is not UNSET:
            field_dict["organizations"] = organizations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_licensing_report_organization import RESTLicensingReportOrganization
        from ..models.rest_licensing_report_summary import RESTLicensingReportSummary
        d = dict(src_dict)
        _platform_id = d.pop("platformId", UNSET)
        platform_id: UUID | Unset
        if isinstance(_platform_id,  Unset):
            platform_id = UNSET
        else:
            platform_id = UUID(_platform_id)




        type_id = d.pop("typeId", UNSET)

        _summary = d.pop("summary", UNSET)
        summary: RESTLicensingReportSummary | Unset
        if isinstance(_summary,  Unset):
            summary = UNSET
        else:
            summary = RESTLicensingReportSummary.from_dict(_summary)




        _organizations = d.pop("organizations", UNSET)
        organizations: list[RESTLicensingReportOrganization] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:
                organizations_item = RESTLicensingReportOrganization.from_dict(organizations_item_data)



                organizations.append(organizations_item)


        rest_licensing_report_platform_type = cls(
            platform_id=platform_id,
            type_id=type_id,
            summary=summary,
            organizations=organizations,
        )


        rest_licensing_report_platform_type.additional_properties = d
        return rest_licensing_report_platform_type

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
