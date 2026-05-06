from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_authentication_type import RESTAuthenticationType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
  from ..models.rest_smtp_settings_actions import RESTSmtpSettingsActions





T = TypeVar("T", bound="RESTSmtpSettings")



@_attrs_define
class RESTSmtpSettings:
    """ 
        Attributes:
            username (str | Unset): User name of the account used for authentication to the SMTP server.
            enable_notification (bool | None | Unset): Defines whether Veeam Explorer is enabled to send email messages.
            server (str | Unset): DNS name or IP address of the SMTP server for sending email messages.
            port (int | None | Unset): Port used for connection to the SMTP server.
            from_ (str | Unset): Email address of the notification sender.
            use_authentication (bool | None | Unset): Defines whether the SMTP server requires authentication.
            use_ssl (bool | None | Unset): Defines whether Veeam Explorer uses a secure connection to send email messages.
            authentication_type (RESTAuthenticationType | Unset): Specifies authentication method that Veeam Backup for
                Microsoft 365 and Veeam Explorers use to send emails.
            client_id (str | Unset): Client ID obtained while registering an application in the Google Cloud console or
                Microsoft Identity platform.
            tenant_id (str | Unset): Tenant ID in Microsoft Entra ID.
            user_id (None | str | Unset): Authenticated user account ID. Veeam Explorer will send email messages on behalf
                of this user.
            mail_api_url (None | str | Unset): Specifies the Microsoft Graph endpoint for sending emails.
            is_authenticated (bool | None | Unset): Defines a user account authentication status.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
            field_actions (RESTSmtpSettingsActions | Unset):
     """

    username: str | Unset = UNSET
    enable_notification: bool | None | Unset = UNSET
    server: str | Unset = UNSET
    port: int | None | Unset = UNSET
    from_: str | Unset = UNSET
    use_authentication: bool | None | Unset = UNSET
    use_ssl: bool | None | Unset = UNSET
    authentication_type: RESTAuthenticationType | Unset = UNSET
    client_id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    mail_api_url: None | str | Unset = UNSET
    is_authenticated: bool | None | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTSmtpSettingsActions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_smtp_settings_actions import RESTSmtpSettingsActions
        username = self.username

        enable_notification: bool | None | Unset
        if isinstance(self.enable_notification, Unset):
            enable_notification = UNSET
        else:
            enable_notification = self.enable_notification

        server = self.server

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        from_ = self.from_

        use_authentication: bool | None | Unset
        if isinstance(self.use_authentication, Unset):
            use_authentication = UNSET
        else:
            use_authentication = self.use_authentication

        use_ssl: bool | None | Unset
        if isinstance(self.use_ssl, Unset):
            use_ssl = UNSET
        else:
            use_ssl = self.use_ssl

        authentication_type: str | Unset = UNSET
        if not isinstance(self.authentication_type, Unset):
            authentication_type = self.authentication_type.value


        client_id = self.client_id

        tenant_id = self.tenant_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
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
        field_dict.update({
        })
        if username is not UNSET:
            field_dict["username"] = username
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
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_smtp_settings_actions import RESTSmtpSettingsActions
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        def _parse_enable_notification(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_notification = _parse_enable_notification(d.pop("enableNotification", UNSET))


        server = d.pop("server", UNSET)

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))


        from_ = d.pop("from", UNSET)

        def _parse_use_authentication(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_authentication = _parse_use_authentication(d.pop("useAuthentication", UNSET))


        def _parse_use_ssl(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_ssl = _parse_use_ssl(d.pop("useSSL", UNSET))


        _authentication_type = d.pop("authenticationType", UNSET)
        authentication_type: RESTAuthenticationType | Unset
        if isinstance(_authentication_type,  Unset):
            authentication_type = UNSET
        else:
            authentication_type = RESTAuthenticationType(_authentication_type)




        client_id = d.pop("clientId", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))


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
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTSmtpSettingsActions | Unset
        if isinstance(_field_actions,  Unset):
            field_actions = UNSET
        else:
            field_actions = RESTSmtpSettingsActions.from_dict(_field_actions)




        rest_smtp_settings = cls(
            username=username,
            enable_notification=enable_notification,
            server=server,
            port=port,
            from_=from_,
            use_authentication=use_authentication,
            use_ssl=use_ssl,
            authentication_type=authentication_type,
            client_id=client_id,
            tenant_id=tenant_id,
            user_id=user_id,
            mail_api_url=mail_api_url,
            is_authenticated=is_authenticated,
            field_links=field_links,
            field_actions=field_actions,
        )


        rest_smtp_settings.additional_properties = d
        return rest_smtp_settings

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
