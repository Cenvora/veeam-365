from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_authentication_type import RESTAuthenticationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTAuditEmailSettingsRequest")


@_attrs_define
class RESTAuditEmailSettingsRequest:
    """
    Attributes:
        user_password (str | Unset): Specifies a password.
        enable_notification (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 will send audit
            notifications by email.
        smtp_server (str | Unset): Specifies the full DNS name or IP address of the SMTP server for sending audit email
            notifications.
        port (int | None | Unset): Specifies the port used for connection to the SMTP server.
        use_authentication (bool | None | Unset): Defines whether the SMTP server requires authentication.
        username (str | Unset): Specifies the user name of the account used for authentication to the SMTP server.
        use_ssl (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 will use a secure connection to
            transmit audit email notifications.
        from_ (str | Unset): Specifies email address of the notification sender.
        to (str | Unset): Specifies email address of the notification recipient. For listing multiple recipients, use
            semicolon as a separator.
        subject (str | Unset): Specifies the subject for audit email notifications. The subject of an email notification
            displays information according to the following variables: <ul> <li>*%OrganizationName%* - organization whose
            data was processed by a backup or backup copy job.</li> <li>*%DisplayName%* - display name of the backed-up item
            for which a user performed an operation.</li> <li>*%Action%* - name of the operation performed with the backed-
            up data.</li> <li>*%InitiatedByUserName%* - user name of the account used to perform an operation with the
            backed-up data.</li> <li>*%StartTime%* - date and time when a user performed an operation with the backed-up
            data.</li> </ul>
        authentication_type (RESTAuthenticationType | Unset): Specifies authentication method that Veeam Backup for
            Microsoft 365 uses to send email notifications.
        user_id (str | Unset): Specifies an authenticated user account ID. Veeam Backup for Microsoft 365 will send
            audit email notifications on behalf of this user.
        mail_api_url (None | str | Unset): Specifies the Microsoft Graph API URL of Azure AD application registered in
            the Microsoft Azure portal.
        request_id (None | str | Unset): Specifies an auhentication request ID.
    """

    user_password: str | Unset = UNSET
    enable_notification: bool | None | Unset = UNSET
    smtp_server: str | Unset = UNSET
    port: int | None | Unset = UNSET
    use_authentication: bool | None | Unset = UNSET
    username: str | Unset = UNSET
    use_ssl: bool | None | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    subject: str | Unset = UNSET
    authentication_type: RESTAuthenticationType | Unset = UNSET
    user_id: str | Unset = UNSET
    mail_api_url: None | str | Unset = UNSET
    request_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_password = self.user_password

        enable_notification: bool | None | Unset
        if isinstance(self.enable_notification, Unset):
            enable_notification = UNSET
        else:
            enable_notification = self.enable_notification

        smtp_server = self.smtp_server

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        use_authentication: bool | None | Unset
        if isinstance(self.use_authentication, Unset):
            use_authentication = UNSET
        else:
            use_authentication = self.use_authentication

        username = self.username

        use_ssl: bool | None | Unset
        if isinstance(self.use_ssl, Unset):
            use_ssl = UNSET
        else:
            use_ssl = self.use_ssl

        from_ = self.from_

        to = self.to

        subject = self.subject

        authentication_type: str | Unset = UNSET
        if not isinstance(self.authentication_type, Unset):
            authentication_type = self.authentication_type.value

        user_id = self.user_id

        mail_api_url: None | str | Unset
        if isinstance(self.mail_api_url, Unset):
            mail_api_url = UNSET
        else:
            mail_api_url = self.mail_api_url

        request_id: None | str | Unset
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_password is not UNSET:
            field_dict["userPassword"] = user_password
        if enable_notification is not UNSET:
            field_dict["enableNotification"] = enable_notification
        if smtp_server is not UNSET:
            field_dict["smtpServer"] = smtp_server
        if port is not UNSET:
            field_dict["port"] = port
        if use_authentication is not UNSET:
            field_dict["useAuthentication"] = use_authentication
        if username is not UNSET:
            field_dict["username"] = username
        if use_ssl is not UNSET:
            field_dict["useSSL"] = use_ssl
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if subject is not UNSET:
            field_dict["subject"] = subject
        if authentication_type is not UNSET:
            field_dict["authenticationType"] = authentication_type
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if mail_api_url is not UNSET:
            field_dict["mailApiUrl"] = mail_api_url
        if request_id is not UNSET:
            field_dict["requestId"] = request_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_password = d.pop("userPassword", UNSET)

        def _parse_enable_notification(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_notification = _parse_enable_notification(d.pop("enableNotification", UNSET))

        smtp_server = d.pop("smtpServer", UNSET)

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_use_authentication(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_authentication = _parse_use_authentication(d.pop("useAuthentication", UNSET))

        username = d.pop("username", UNSET)

        def _parse_use_ssl(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_ssl = _parse_use_ssl(d.pop("useSSL", UNSET))

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        subject = d.pop("subject", UNSET)

        _authentication_type = d.pop("authenticationType", UNSET)
        authentication_type: RESTAuthenticationType | Unset
        if isinstance(_authentication_type, Unset):
            authentication_type = UNSET
        else:
            authentication_type = RESTAuthenticationType(_authentication_type)

        user_id = d.pop("userId", UNSET)

        def _parse_mail_api_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mail_api_url = _parse_mail_api_url(d.pop("mailApiUrl", UNSET))

        def _parse_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_id = _parse_request_id(d.pop("requestId", UNSET))

        rest_audit_email_settings_request = cls(
            user_password=user_password,
            enable_notification=enable_notification,
            smtp_server=smtp_server,
            port=port,
            use_authentication=use_authentication,
            username=username,
            use_ssl=use_ssl,
            from_=from_,
            to=to,
            subject=subject,
            authentication_type=authentication_type,
            user_id=user_id,
            mail_api_url=mail_api_url,
            request_id=request_id,
        )

        rest_audit_email_settings_request.additional_properties = d
        return rest_audit_email_settings_request

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
