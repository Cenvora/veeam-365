from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_license_status import RESTLicenseStatus
from ..models.rest_license_type import RESTLicenseType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="RESTLicense")



@_attrs_define
class RESTLicense:
    """ 
        Attributes:
            license_id (None | Unset | UUID): ID of the installed license. Example: 00000000-0000-0000-0000-000000000000.
            email (str | Unset): Email of a user to which the license was issued.
            status (RESTLicenseStatus | Unset): Status of the installed license.
            license_expires (datetime.datetime | None | Unset): Date and time when the license expires.
            grace_period_expires (datetime.datetime | None | Unset): Date and time when a grace period expires. A grace
                period is granted after the expiration of license for purpose of renewal.
            type_ (RESTLicenseType | Unset): Type of the license. For more information about license types, see the
                [Licensing and License Types](https://helpcenter.veeam.com/docs/vbo365/guide/vbo_licensing.html?ver=80) section
                of the Veeam Backup for Microsoft 365 User Guide.
            package (str | Unset): Specifies information if Veeam Service Provider Console or Veeam One is allowed to
                monitor the Veeam Backup for Microsoft 365 server.
            licensed_to (str | Unset): Company to which the license was issued.
            total_number (int | Unset): Total number of units within the license.
            used_number (int | Unset): Number of units consumed by objects.
            new_number (int | Unset): Number of users with the *new user* status.
            support_id (str | Unset): Support ID of the installed license.
     """

    license_id: None | Unset | UUID = UNSET
    email: str | Unset = UNSET
    status: RESTLicenseStatus | Unset = UNSET
    license_expires: datetime.datetime | None | Unset = UNSET
    grace_period_expires: datetime.datetime | None | Unset = UNSET
    type_: RESTLicenseType | Unset = UNSET
    package: str | Unset = UNSET
    licensed_to: str | Unset = UNSET
    total_number: int | Unset = UNSET
    used_number: int | Unset = UNSET
    new_number: int | Unset = UNSET
    support_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        license_id: None | str | Unset
        if isinstance(self.license_id, Unset):
            license_id = UNSET
        elif isinstance(self.license_id, UUID):
            license_id = str(self.license_id)
        else:
            license_id = self.license_id

        email = self.email

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        license_expires: None | str | Unset
        if isinstance(self.license_expires, Unset):
            license_expires = UNSET
        elif isinstance(self.license_expires, datetime.datetime):
            license_expires = self.license_expires.isoformat()
        else:
            license_expires = self.license_expires

        grace_period_expires: None | str | Unset
        if isinstance(self.grace_period_expires, Unset):
            grace_period_expires = UNSET
        elif isinstance(self.grace_period_expires, datetime.datetime):
            grace_period_expires = self.grace_period_expires.isoformat()
        else:
            grace_period_expires = self.grace_period_expires

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        package = self.package

        licensed_to = self.licensed_to

        total_number = self.total_number

        used_number = self.used_number

        new_number = self.new_number

        support_id = self.support_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if license_id is not UNSET:
            field_dict["licenseID"] = license_id
        if email is not UNSET:
            field_dict["email"] = email
        if status is not UNSET:
            field_dict["status"] = status
        if license_expires is not UNSET:
            field_dict["licenseExpires"] = license_expires
        if grace_period_expires is not UNSET:
            field_dict["gracePeriodExpires"] = grace_period_expires
        if type_ is not UNSET:
            field_dict["type"] = type_
        if package is not UNSET:
            field_dict["package"] = package
        if licensed_to is not UNSET:
            field_dict["licensedTo"] = licensed_to
        if total_number is not UNSET:
            field_dict["totalNumber"] = total_number
        if used_number is not UNSET:
            field_dict["usedNumber"] = used_number
        if new_number is not UNSET:
            field_dict["newNumber"] = new_number
        if support_id is not UNSET:
            field_dict["supportID"] = support_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_license_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                license_id_type_0 = UUID(data)



                return license_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        license_id = _parse_license_id(d.pop("licenseID", UNSET))


        email = d.pop("email", UNSET)

        _status = d.pop("status", UNSET)
        status: RESTLicenseStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = RESTLicenseStatus(_status)




        def _parse_license_expires(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                license_expires_type_0 = isoparse(data)



                return license_expires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        license_expires = _parse_license_expires(d.pop("licenseExpires", UNSET))


        def _parse_grace_period_expires(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                grace_period_expires_type_0 = isoparse(data)



                return grace_period_expires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        grace_period_expires = _parse_grace_period_expires(d.pop("gracePeriodExpires", UNSET))


        _type_ = d.pop("type", UNSET)
        type_: RESTLicenseType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RESTLicenseType(_type_)




        package = d.pop("package", UNSET)

        licensed_to = d.pop("licensedTo", UNSET)

        total_number = d.pop("totalNumber", UNSET)

        used_number = d.pop("usedNumber", UNSET)

        new_number = d.pop("newNumber", UNSET)

        support_id = d.pop("supportID", UNSET)

        rest_license = cls(
            license_id=license_id,
            email=email,
            status=status,
            license_expires=license_expires,
            grace_period_expires=grace_period_expires,
            type_=type_,
            package=package,
            licensed_to=licensed_to,
            total_number=total_number,
            used_number=used_number,
            new_number=new_number,
            support_id=support_id,
        )


        rest_license.additional_properties = d
        return rest_license

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
