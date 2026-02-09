from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_license_status import RESTLicenseStatus
from ..models.rest_license_type import RESTLicenseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTLicense")


@_attrs_define
class RESTLicense:
    """
    Attributes:
        license_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        email (str | Unset):
        status (RESTLicenseStatus | Unset):
        expiration_date (datetime.datetime | None | Unset):
        type_ (RESTLicenseType | Unset):
        licensed_to (str | Unset):
        contact_person (str | Unset):
        total_number (int | Unset):
        used_number (int | Unset):
        new_number (int | Unset):
        support_id (str | Unset):
        support_expiration_date (datetime.datetime | None | Unset):
    """

    license_id: None | Unset | UUID = UNSET
    email: str | Unset = UNSET
    status: RESTLicenseStatus | Unset = UNSET
    expiration_date: datetime.datetime | None | Unset = UNSET
    type_: RESTLicenseType | Unset = UNSET
    licensed_to: str | Unset = UNSET
    contact_person: str | Unset = UNSET
    total_number: int | Unset = UNSET
    used_number: int | Unset = UNSET
    new_number: int | Unset = UNSET
    support_id: str | Unset = UNSET
    support_expiration_date: datetime.datetime | None | Unset = UNSET
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

        expiration_date: None | str | Unset
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.datetime):
            expiration_date = self.expiration_date.isoformat()
        else:
            expiration_date = self.expiration_date

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        licensed_to = self.licensed_to

        contact_person = self.contact_person

        total_number = self.total_number

        used_number = self.used_number

        new_number = self.new_number

        support_id = self.support_id

        support_expiration_date: None | str | Unset
        if isinstance(self.support_expiration_date, Unset):
            support_expiration_date = UNSET
        elif isinstance(self.support_expiration_date, datetime.datetime):
            support_expiration_date = self.support_expiration_date.isoformat()
        else:
            support_expiration_date = self.support_expiration_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if license_id is not UNSET:
            field_dict["licenseID"] = license_id
        if email is not UNSET:
            field_dict["email"] = email
        if status is not UNSET:
            field_dict["status"] = status
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if type_ is not UNSET:
            field_dict["type"] = type_
        if licensed_to is not UNSET:
            field_dict["licensedTo"] = licensed_to
        if contact_person is not UNSET:
            field_dict["contactPerson"] = contact_person
        if total_number is not UNSET:
            field_dict["totalNumber"] = total_number
        if used_number is not UNSET:
            field_dict["usedNumber"] = used_number
        if new_number is not UNSET:
            field_dict["newNumber"] = new_number
        if support_id is not UNSET:
            field_dict["supportID"] = support_id
        if support_expiration_date is not UNSET:
            field_dict["supportExpirationDate"] = support_expiration_date

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
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTLicenseStatus(_status)

        def _parse_expiration_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_type_0 = isoparse(data)

                return expiration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_date = _parse_expiration_date(d.pop("expirationDate", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: RESTLicenseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTLicenseType(_type_)

        licensed_to = d.pop("licensedTo", UNSET)

        contact_person = d.pop("contactPerson", UNSET)

        total_number = d.pop("totalNumber", UNSET)

        used_number = d.pop("usedNumber", UNSET)

        new_number = d.pop("newNumber", UNSET)

        support_id = d.pop("supportID", UNSET)

        def _parse_support_expiration_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                support_expiration_date_type_0 = isoparse(data)

                return support_expiration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        support_expiration_date = _parse_support_expiration_date(d.pop("supportExpirationDate", UNSET))

        rest_license = cls(
            license_id=license_id,
            email=email,
            status=status,
            expiration_date=expiration_date,
            type_=type_,
            licensed_to=licensed_to,
            contact_person=contact_person,
            total_number=total_number,
            used_number=used_number,
            new_number=new_number,
            support_id=support_id,
            support_expiration_date=support_expiration_date,
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
