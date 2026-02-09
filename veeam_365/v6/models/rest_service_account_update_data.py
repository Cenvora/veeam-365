from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTServiceAccountUpdateData")


@_attrs_define
class RESTServiceAccountUpdateData:
    """
    Attributes:
        description (str | Unset):
        application_certificate (str | Unset):
        application_certificate_password (str | Unset):
        application_secret (str | Unset):
        user_code (str | Unset):
        subscription_ids (list[str] | Unset):
    """

    description: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    application_certificate_password: str | Unset = UNSET
    application_secret: str | Unset = UNSET
    user_code: str | Unset = UNSET
    subscription_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        application_certificate = self.application_certificate

        application_certificate_password = self.application_certificate_password

        application_secret = self.application_secret

        user_code = self.user_code

        subscription_ids: list[str] | Unset = UNSET
        if not isinstance(self.subscription_ids, Unset):
            subscription_ids = self.subscription_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if application_secret is not UNSET:
            field_dict["applicationSecret"] = application_secret
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if subscription_ids is not UNSET:
            field_dict["subscriptionIds"] = subscription_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        application_certificate = d.pop("applicationCertificate", UNSET)

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        application_secret = d.pop("applicationSecret", UNSET)

        user_code = d.pop("userCode", UNSET)

        subscription_ids = cast(list[str], d.pop("subscriptionIds", UNSET))

        rest_service_account_update_data = cls(
            description=description,
            application_certificate=application_certificate,
            application_certificate_password=application_certificate_password,
            application_secret=application_secret,
            user_code=user_code,
            subscription_ids=subscription_ids,
        )

        rest_service_account_update_data.additional_properties = d
        return rest_service_account_update_data

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
