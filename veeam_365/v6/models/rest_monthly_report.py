from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_report_organization import RESTReportOrganization
    from ..models.rest_report_parameters import RESTReportParameters
    from ..models.rest_report_summary import RESTReportSummary


T = TypeVar("T", bound="RESTMonthlyReport")


@_attrs_define
class RESTMonthlyReport:
    """
    Attributes:
        report_parameters (RESTReportParameters | Unset):
        report_summary (RESTReportSummary | Unset):
        organizations (list[RESTReportOrganization] | Unset):
    """

    report_parameters: RESTReportParameters | Unset = UNSET
    report_summary: RESTReportSummary | Unset = UNSET
    organizations: list[RESTReportOrganization] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.report_parameters, Unset):
            report_parameters = self.report_parameters.to_dict()

        report_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.report_summary, Unset):
            report_summary = self.report_summary.to_dict()

        organizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if report_parameters is not UNSET:
            field_dict["reportParameters"] = report_parameters
        if report_summary is not UNSET:
            field_dict["reportSummary"] = report_summary
        if organizations is not UNSET:
            field_dict["organizations"] = organizations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_report_organization import RESTReportOrganization
        from ..models.rest_report_parameters import RESTReportParameters
        from ..models.rest_report_summary import RESTReportSummary

        d = dict(src_dict)
        _report_parameters = d.pop("reportParameters", UNSET)
        report_parameters: RESTReportParameters | Unset
        if isinstance(_report_parameters, Unset):
            report_parameters = UNSET
        else:
            report_parameters = RESTReportParameters.from_dict(_report_parameters)

        _report_summary = d.pop("reportSummary", UNSET)
        report_summary: RESTReportSummary | Unset
        if isinstance(_report_summary, Unset):
            report_summary = UNSET
        else:
            report_summary = RESTReportSummary.from_dict(_report_summary)

        _organizations = d.pop("organizations", UNSET)
        organizations: list[RESTReportOrganization] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:
                organizations_item = RESTReportOrganization.from_dict(organizations_item_data)

                organizations.append(organizations_item)

        rest_monthly_report = cls(
            report_parameters=report_parameters,
            report_summary=report_summary,
            organizations=organizations,
        )

        rest_monthly_report.additional_properties = d
        return rest_monthly_report

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
