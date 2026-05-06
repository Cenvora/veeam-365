from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_report_parameters_report_status import RESTReportParametersReportStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.rest_monthly_report_interval import RESTMonthlyReportInterval





T = TypeVar("T", bound="RESTReportParameters")



@_attrs_define
class RESTReportParameters:
    """ 
        Attributes:
            report_id (int | Unset): ID of the report.
            report_status (RESTReportParametersReportStatus | Unset): Status of the report. The following values are
                available: <ul> <li>*Draft* - the report was not sent to Veeam.</li> <li>*Approved* - the report was sent to
                Veeam.</li> </ul>
            company_name (str | Unset): Name of the company to which the license was issued.
            license_expiration_date (datetime.datetime | Unset): Date and time when the license expires.
            license_id (UUID | Unset): ID of the installed license. Example: 00000000-0000-0000-0000-000000000000.
            support_id (str | Unset): Support ID of the installed license.
            report_generation_date (datetime.datetime | Unset): Date and time when the report was generated.
            reporting_interval (RESTMonthlyReportInterval | Unset):
     """

    report_id: int | Unset = UNSET
    report_status: RESTReportParametersReportStatus | Unset = UNSET
    company_name: str | Unset = UNSET
    license_expiration_date: datetime.datetime | Unset = UNSET
    license_id: UUID | Unset = UNSET
    support_id: str | Unset = UNSET
    report_generation_date: datetime.datetime | Unset = UNSET
    reporting_interval: RESTMonthlyReportInterval | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_monthly_report_interval import RESTMonthlyReportInterval
        report_id = self.report_id

        report_status: str | Unset = UNSET
        if not isinstance(self.report_status, Unset):
            report_status = self.report_status.value


        company_name = self.company_name

        license_expiration_date: str | Unset = UNSET
        if not isinstance(self.license_expiration_date, Unset):
            license_expiration_date = self.license_expiration_date.isoformat()

        license_id: str | Unset = UNSET
        if not isinstance(self.license_id, Unset):
            license_id = str(self.license_id)

        support_id = self.support_id

        report_generation_date: str | Unset = UNSET
        if not isinstance(self.report_generation_date, Unset):
            report_generation_date = self.report_generation_date.isoformat()

        reporting_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reporting_interval, Unset):
            reporting_interval = self.reporting_interval.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if report_id is not UNSET:
            field_dict["reportID"] = report_id
        if report_status is not UNSET:
            field_dict["reportStatus"] = report_status
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if license_expiration_date is not UNSET:
            field_dict["licenseExpirationDate"] = license_expiration_date
        if license_id is not UNSET:
            field_dict["licenseID"] = license_id
        if support_id is not UNSET:
            field_dict["supportID"] = support_id
        if report_generation_date is not UNSET:
            field_dict["reportGenerationDate"] = report_generation_date
        if reporting_interval is not UNSET:
            field_dict["reportingInterval"] = reporting_interval

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_monthly_report_interval import RESTMonthlyReportInterval
        d = dict(src_dict)
        report_id = d.pop("reportID", UNSET)

        _report_status = d.pop("reportStatus", UNSET)
        report_status: RESTReportParametersReportStatus | Unset
        if isinstance(_report_status,  Unset):
            report_status = UNSET
        else:
            report_status = RESTReportParametersReportStatus(_report_status)




        company_name = d.pop("companyName", UNSET)

        _license_expiration_date = d.pop("licenseExpirationDate", UNSET)
        license_expiration_date: datetime.datetime | Unset
        if isinstance(_license_expiration_date,  Unset):
            license_expiration_date = UNSET
        else:
            license_expiration_date = isoparse(_license_expiration_date)




        _license_id = d.pop("licenseID", UNSET)
        license_id: UUID | Unset
        if isinstance(_license_id,  Unset):
            license_id = UNSET
        else:
            license_id = UUID(_license_id)




        support_id = d.pop("supportID", UNSET)

        _report_generation_date = d.pop("reportGenerationDate", UNSET)
        report_generation_date: datetime.datetime | Unset
        if isinstance(_report_generation_date,  Unset):
            report_generation_date = UNSET
        else:
            report_generation_date = isoparse(_report_generation_date)




        _reporting_interval = d.pop("reportingInterval", UNSET)
        reporting_interval: RESTMonthlyReportInterval | Unset
        if isinstance(_reporting_interval,  Unset):
            reporting_interval = UNSET
        else:
            reporting_interval = RESTMonthlyReportInterval.from_dict(_reporting_interval)




        rest_report_parameters = cls(
            report_id=report_id,
            report_status=report_status,
            company_name=company_name,
            license_expiration_date=license_expiration_date,
            license_id=license_id,
            support_id=support_id,
            report_generation_date=report_generation_date,
            reporting_interval=reporting_interval,
        )


        rest_report_parameters.additional_properties = d
        return rest_report_parameters

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
