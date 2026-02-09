from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTOffice365ConnectionSettingsType0")


@_attrs_define
class RESTOffice365ConnectionSettingsType0:
    """
    Attributes:
        use_application_only_auth (bool | None | Unset): Defines whether to use Microsoft Entra application
            authentication.

            **Note**: If set to *false*, enables basic authentication. Since [Microsoft deprecated basic authentication and
            legacy authentication protocols](https://techcommunity.microsoft.com/t5/exchange-team-blog/basic-authentication-
            deprecation-in-exchange-online-september/ba-p/3609437), adding Microsoft organizations using these
            authentication methods will be deprecated in future versions of Veeam Backup for Microsoft 365. Use the *modern
            app-only* authentication method instead.
        office_organization_name (str | Unset): Specifies the name of a SharePoint Online organization.
        share_point_save_all_web_parts (bool | None | Unset): Defines whether to change export mode for SharePoint Web
            Parts to back up a customized content of SharePoint Online sites. For more information, see the [Adding
            Organizations with Modern App-Only
            Authentication](https://helpcenter.veeam.com/docs/vbo365/guide/adding_o365_organizations_sd.html?ver=80) section
            of the Veeam Backup for Microsoft 365 User Guide.
        account (str | Unset): Specifies the account name of an Exchange Online organization.
        password (str | Unset): Specifies a password.
        grant_admin_access (bool | None | Unset): Defines whether to grant administrative permissions.
        use_mfa (bool | None | Unset): Defines whether to use multi-factor authentication (MFA).
        use_custom_veeam_aad_application (bool | None | Unset): Defines whether to use a custom Microsoft Entra
            application that is automatically configured by Veeam Backup for Microsoft 365.
        application_id (None | Unset | UUID): Specifies the identification number of the Microsoft Entra application.
            Example: 00000000-0000-0000-0000-000000000000.
        application_secret (str | Unset): Specifies a password.
        application_certificate (str | Unset): Specifies the Base64 string of an SSL certificate that you want to use to
            access the Microsoft Entra application.
        application_certificate_password (str | Unset): Specifies a password.
        application_certificate_thumbprint (str | Unset): Specifies an application certificate thumbprint for connecting
            to Microsoft Entra.
    """

    use_application_only_auth: bool | None | Unset = UNSET
    office_organization_name: str | Unset = UNSET
    share_point_save_all_web_parts: bool | None | Unset = UNSET
    account: str | Unset = UNSET
    password: str | Unset = UNSET
    grant_admin_access: bool | None | Unset = UNSET
    use_mfa: bool | None | Unset = UNSET
    use_custom_veeam_aad_application: bool | None | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_secret: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate_thumbprint: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_application_only_auth: bool | None | Unset
        if isinstance(self.use_application_only_auth, Unset):
            use_application_only_auth = UNSET
        else:
            use_application_only_auth = self.use_application_only_auth

        office_organization_name = self.office_organization_name

        share_point_save_all_web_parts: bool | None | Unset
        if isinstance(self.share_point_save_all_web_parts, Unset):
            share_point_save_all_web_parts = UNSET
        else:
            share_point_save_all_web_parts = self.share_point_save_all_web_parts

        account = self.account

        password = self.password

        grant_admin_access: bool | None | Unset
        if isinstance(self.grant_admin_access, Unset):
            grant_admin_access = UNSET
        else:
            grant_admin_access = self.grant_admin_access

        use_mfa: bool | None | Unset
        if isinstance(self.use_mfa, Unset):
            use_mfa = UNSET
        else:
            use_mfa = self.use_mfa

        use_custom_veeam_aad_application: bool | None | Unset
        if isinstance(self.use_custom_veeam_aad_application, Unset):
            use_custom_veeam_aad_application = UNSET
        else:
            use_custom_veeam_aad_application = self.use_custom_veeam_aad_application

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        elif isinstance(self.application_id, UUID):
            application_id = str(self.application_id)
        else:
            application_id = self.application_id

        application_secret = self.application_secret

        application_certificate = self.application_certificate

        application_certificate_password = self.application_certificate_password

        application_certificate_thumbprint = self.application_certificate_thumbprint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if use_application_only_auth is not UNSET:
            field_dict["useApplicationOnlyAuth"] = use_application_only_auth
        if office_organization_name is not UNSET:
            field_dict["officeOrganizationName"] = office_organization_name
        if share_point_save_all_web_parts is not UNSET:
            field_dict["sharePointSaveAllWebParts"] = share_point_save_all_web_parts
        if account is not UNSET:
            field_dict["account"] = account
        if password is not UNSET:
            field_dict["password"] = password
        if grant_admin_access is not UNSET:
            field_dict["grantAdminAccess"] = grant_admin_access
        if use_mfa is not UNSET:
            field_dict["useMfa"] = use_mfa
        if use_custom_veeam_aad_application is not UNSET:
            field_dict["useCustomVeeamAADApplication"] = use_custom_veeam_aad_application
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_secret is not UNSET:
            field_dict["applicationSecret"] = application_secret
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if application_certificate_thumbprint is not UNSET:
            field_dict["applicationCertificateThumbprint"] = application_certificate_thumbprint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_use_application_only_auth(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_application_only_auth = _parse_use_application_only_auth(d.pop("useApplicationOnlyAuth", UNSET))

        office_organization_name = d.pop("officeOrganizationName", UNSET)

        def _parse_share_point_save_all_web_parts(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        share_point_save_all_web_parts = _parse_share_point_save_all_web_parts(
            d.pop("sharePointSaveAllWebParts", UNSET)
        )

        account = d.pop("account", UNSET)

        password = d.pop("password", UNSET)

        def _parse_grant_admin_access(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grant_admin_access = _parse_grant_admin_access(d.pop("grantAdminAccess", UNSET))

        def _parse_use_mfa(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_mfa = _parse_use_mfa(d.pop("useMfa", UNSET))

        def _parse_use_custom_veeam_aad_application(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_custom_veeam_aad_application = _parse_use_custom_veeam_aad_application(
            d.pop("useCustomVeeamAADApplication", UNSET)
        )

        def _parse_application_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_id_type_0 = UUID(data)

                return application_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        application_id = _parse_application_id(d.pop("applicationId", UNSET))

        application_secret = d.pop("applicationSecret", UNSET)

        application_certificate = d.pop("applicationCertificate", UNSET)

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        application_certificate_thumbprint = d.pop("applicationCertificateThumbprint", UNSET)

        rest_office_365_connection_settings_type_0 = cls(
            use_application_only_auth=use_application_only_auth,
            office_organization_name=office_organization_name,
            share_point_save_all_web_parts=share_point_save_all_web_parts,
            account=account,
            password=password,
            grant_admin_access=grant_admin_access,
            use_mfa=use_mfa,
            use_custom_veeam_aad_application=use_custom_veeam_aad_application,
            application_id=application_id,
            application_secret=application_secret,
            application_certificate=application_certificate,
            application_certificate_password=application_certificate_password,
            application_certificate_thumbprint=application_certificate_thumbprint,
        )

        rest_office_365_connection_settings_type_0.additional_properties = d
        return rest_office_365_connection_settings_type_0

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
