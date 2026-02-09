from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_authentication_type import RESTAuthenticationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_share_point_smtp_settings_actions import RESTSharePointSmtpSettingsActions
    from ..models.rest_share_point_smtp_settings_links import RESTSharePointSmtpSettingsLinks


T = TypeVar("T", bound="RESTSharePointSmtpSettings")


@_attrs_define
class RESTSharePointSmtpSettings:
    """
    Attributes:
        enable_notification (bool | Unset): Defines whether Veeam Explorer is enabled to send email messages.
        server (str | Unset): DNS name or IP address of the SMTP server for sending email messages.
        port (int | Unset): Port used for connection to the SMTP server.
        from_ (str | Unset): Email address of the notification sender.
        use_authentication (bool | Unset): Defines whether the SMTP server requires authentication.
        use_ssl (bool | Unset): Defines whether Veeam Explorer uses a secure connection to send email messages.
        username (str | Unset): User name of the account used for authentication to the SMTP server.
        authentication_type (RESTAuthenticationType | Unset): Specifies authentication method that Veeam Backup for
            Microsoft 365 and Veeam Explorers use to send emails.
        client_id (str | Unset): Client ID obtained while registering an application in the Google Cloud console or
            Microsoft Identity platform.
        tenant_id (str | Unset): Tenant ID in Microsoft Entra ID.
        user_id (str | Unset): Authenticated user account ID. Veeam Explorer will send email messages on behalf of this
            user.
        mail_api_url (None | str | Unset): Microsoft Graph endpoint for sending emails.
        is_authenticated (bool | None | Unset): Defines a user account authentication status.
        field_links (RESTSharePointSmtpSettingsLinks | Unset):
        field_actions (RESTSharePointSmtpSettingsActions | Unset):
    """

    enable_notification: bool | Unset = UNSET
    server: str | Unset = UNSET
    port: int | Unset = UNSET
    from_: str | Unset = UNSET
    use_authentication: bool | Unset = UNSET
    use_ssl: bool | Unset = UNSET
    username: str | Unset = UNSET
    authentication_type: RESTAuthenticationType | Unset = UNSET
    client_id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    mail_api_url: None | str | Unset = UNSET
    is_authenticated: bool | None | Unset = UNSET
    field_links: RESTSharePointSmtpSettingsLinks | Unset = UNSET
    field_actions: RESTSharePointSmtpSettingsActions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_notification = self.enable_notification

        server = self.server

        port = self.port

        from_ = self.from_

        use_authentication = self.use_authentication

        use_ssl = self.use_ssl

        username = self.username

        authentication_type: str | Unset = UNSET
        if not isinstance(self.authentication_type, Unset):
            authentication_type = self.authentication_type.value

        client_id = self.client_id

        tenant_id = self.tenant_id

        user_id = self.user_id

        mail_api_url: None | str | Unset
        if isinstance(self.mail_api_url, Unset):
            mail_api_url = UNSET
        else:
            mail_api_url = self.mail_api_url

        is_authenticated: bool | None | Unset
        if isinstance(self.is_authenticated, Unset):
            is_authenticated = UNSET
        else:
            is_authenticated = self.is_authenticated

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_notification is not UNSET:
            field_dict["enableNotification"] = enable_notification
        if server is not UNSET:
            field_dict["server"] = server
        if port is not UNSET:
            field_dict["port"] = port
        if from_ is not UNSET:
            field_dict["from"] = from_
        if use_authentication is not UNSET:
            field_dict["useAuthentication"] = use_authentication
        if use_ssl is not UNSET:
            field_dict["useSSL"] = use_ssl
        if username is not UNSET:
            field_dict["username"] = username
        if authentication_type is not UNSET:
            field_dict["authenticationType"] = authentication_type
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if mail_api_url is not UNSET:
            field_dict["mailApiUrl"] = mail_api_url
        if is_authenticated is not UNSET:
            field_dict["isAuthenticated"] = is_authenticated
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_share_point_smtp_settings_actions import RESTSharePointSmtpSettingsActions
        from ..models.rest_share_point_smtp_settings_links import RESTSharePointSmtpSettingsLinks

        d = dict(src_dict)
        enable_notification = d.pop("enableNotification", UNSET)

        server = d.pop("server", UNSET)

        port = d.pop("port", UNSET)

        from_ = d.pop("from", UNSET)

        use_authentication = d.pop("useAuthentication", UNSET)

        use_ssl = d.pop("useSSL", UNSET)

        username = d.pop("username", UNSET)

        _authentication_type = d.pop("authenticationType", UNSET)
        authentication_type: RESTAuthenticationType | Unset
        if isinstance(_authentication_type, Unset):
            authentication_type = UNSET
        else:
            authentication_type = RESTAuthenticationType(_authentication_type)

        client_id = d.pop("clientId", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        user_id = d.pop("userId", UNSET)

        def _parse_mail_api_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mail_api_url = _parse_mail_api_url(d.pop("mailApiUrl", UNSET))

        def _parse_is_authenticated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_authenticated = _parse_is_authenticated(d.pop("isAuthenticated", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: RESTSharePointSmtpSettingsLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTSharePointSmtpSettingsLinks.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTSharePointSmtpSettingsActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTSharePointSmtpSettingsActions.from_dict(_field_actions)

        rest_share_point_smtp_settings = cls(
            enable_notification=enable_notification,
            server=server,
            port=port,
            from_=from_,
            use_authentication=use_authentication,
            use_ssl=use_ssl,
            username=username,
            authentication_type=authentication_type,
            client_id=client_id,
            tenant_id=tenant_id,
            user_id=user_id,
            mail_api_url=mail_api_url,
            is_authenticated=is_authenticated,
            field_links=field_links,
            field_actions=field_actions,
        )

        rest_share_point_smtp_settings.additional_properties = d
        return rest_share_point_smtp_settings

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
