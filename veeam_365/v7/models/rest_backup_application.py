from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTBackupApplication")


@_attrs_define
class RESTBackupApplication:
    """
    Attributes:
        application_id (UUID | Unset): ID of the application in Microsoft Azure. Example:
            00000000-0000-0000-0000-000000000000.
        display_name (str | Unset): Name of the backup application.
        certificate_thumbprint (str | Unset): Thumbprint of the used certificate.
    """

    application_id: UUID | Unset = UNSET
    display_name: str | Unset = UNSET
    certificate_thumbprint: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id: str | Unset = UNSET
        if not isinstance(self.application_id, Unset):
            application_id = str(self.application_id)

        display_name = self.display_name

        certificate_thumbprint = self.certificate_thumbprint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if certificate_thumbprint is not UNSET:
            field_dict["certificateThumbprint"] = certificate_thumbprint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _application_id = d.pop("applicationId", UNSET)
        application_id: UUID | Unset
        if isinstance(_application_id, Unset):
            application_id = UNSET
        else:
            application_id = UUID(_application_id)

        display_name = d.pop("displayName", UNSET)

        certificate_thumbprint = d.pop("certificateThumbprint", UNSET)

        rest_backup_application = cls(
            application_id=application_id,
            display_name=display_name,
            certificate_thumbprint=certificate_thumbprint,
        )

        rest_backup_application.additional_properties = d
        return rest_backup_application

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
