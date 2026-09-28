from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTRestorePortalSettings")


@_attrs_define
class RESTRestorePortalSettings:
    """
    Attributes:
        application_id (UUID | Unset): ID of the Microsoft Entra application configured to access Restore Portal.
            Example: 00000000-0000-0000-0000-000000000000.
        msal_authority_uri (str | Unset): URL to authenticate to Microsoft 365 and obtain an access token.
        restore_portal_uri (str | Unset): Web address of a machine with the Veeam Backup for Microsoft 365 REST API
            component installed.
        is_enabled (bool | Unset): Defines whether Restore Portal is enabled.
    """

    application_id: UUID | Unset = UNSET
    msal_authority_uri: str | Unset = UNSET
    restore_portal_uri: str | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id: str | Unset = UNSET
        if not isinstance(self.application_id, Unset):
            application_id = str(self.application_id)

        msal_authority_uri = self.msal_authority_uri

        restore_portal_uri = self.restore_portal_uri

        is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if msal_authority_uri is not UNSET:
            field_dict["msalAuthorityUri"] = msal_authority_uri
        if restore_portal_uri is not UNSET:
            field_dict["restorePortalUri"] = restore_portal_uri
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled

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

        msal_authority_uri = d.pop("msalAuthorityUri", UNSET)

        restore_portal_uri = d.pop("restorePortalUri", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        rest_restore_portal_settings = cls(
            application_id=application_id,
            msal_authority_uri=msal_authority_uri,
            restore_portal_uri=restore_portal_uri,
            is_enabled=is_enabled,
        )

        rest_restore_portal_settings.additional_properties = d
        return rest_restore_portal_settings

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
