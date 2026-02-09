from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTApplicationFromClient")


@_attrs_define
class RESTApplicationFromClient:
    """
    Attributes:
        display_name (str | Unset): Specifies the Azure AD application name.
            If you create more than one application, all created applications will have the same name. Each application will
            have a unique identification number.
        user_code (str | Unset): Specifies the device code. For more information on how to get a device code, see [Get
            Device
            Code](#tag/OrganizationBackupApplications/operation/OrganizationBackupApplications_OrganizationDeviceCode).
            To sign in to Microsoft Azure, open the Microsoft authentication portal and specify this device code.
        count (int | None | Unset): Defines the number of applications to create.
        application_certificate_password (str | Unset): Specifies a password.
        application_certificate (str | Unset): Specifies the Base64 string of an SSL certificate that you want to use to
            access the Azure AD application.
    """

    display_name: str | Unset = UNSET
    user_code: str | Unset = UNSET
    count: int | None | Unset = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        user_code = self.user_code

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        application_certificate_password = self.application_certificate_password

        application_certificate = self.application_certificate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if count is not UNSET:
            field_dict["count"] = count
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        user_code = d.pop("userCode", UNSET)

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        application_certificate = d.pop("applicationCertificate", UNSET)

        rest_application_from_client = cls(
            display_name=display_name,
            user_code=user_code,
            count=count,
            application_certificate_password=application_certificate_password,
            application_certificate=application_certificate,
        )

        rest_application_from_client.additional_properties = d
        return rest_application_from_client

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
