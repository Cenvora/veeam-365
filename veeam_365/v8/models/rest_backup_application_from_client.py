from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_application import RESTApplication





T = TypeVar("T", bound="RESTBackupApplicationFromClient")



@_attrs_define
class RESTBackupApplicationFromClient:
    """ 
        Attributes:
            application (RESTApplication | Unset):
            application_certificate_password (str | Unset): Specifies a password.
            application_certificate (str | Unset): Specifies the Base64 string of a TLS certificate that you want to use to
                access the Microsoft Entra application.
     """

    application: RESTApplication | Unset = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_application import RESTApplication
        application: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application, Unset):
            application = self.application.to_dict()

        application_certificate_password = self.application_certificate_password

        application_certificate = self.application_certificate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if application is not UNSET:
            field_dict["application"] = application
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_application import RESTApplication
        d = dict(src_dict)
        _application = d.pop("application", UNSET)
        application: RESTApplication | Unset
        if isinstance(_application,  Unset):
            application = UNSET
        else:
            application = RESTApplication.from_dict(_application)




        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        application_certificate = d.pop("applicationCertificate", UNSET)

        rest_backup_application_from_client = cls(
            application=application,
            application_certificate_password=application_certificate_password,
            application_certificate=application_certificate,
        )


        rest_backup_application_from_client.additional_properties = d
        return rest_backup_application_from_client

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
