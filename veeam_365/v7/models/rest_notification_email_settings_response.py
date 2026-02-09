from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_authentication_type import RESTAuthenticationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
    from ..models.rest_notification_email_settings_response_actions import RESTNotificationEmailSettingsResponseActions


T = TypeVar("T", bound="RESTNotificationEmailSettingsResponse")


@_attrs_define
class RESTNotificationEmailSettingsResponse:
    """
    Attributes:
        field_links (RESTLinkHALDictionary | Unset):
        field_actions (RESTNotificationEmailSettingsResponseActions | Unset):
        notify_on_success (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 sends email
            notifications if a backup or backup copy job completes successfully without any warnings or errors.
        notify_on_warning (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 sends email
            notifications if a backup or backup copy job completes with warnings.
        notify_on_failure (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 sends email
            notifications if a backup or backup copy job completes with errors.
        supress_until_last_retry (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 sends email
            notifications only after the last attempt of a backup or backup copy job.
        attach_detailed_report (bool | None | Unset): Defines whether a detailed report about the job results is
            included as an email attachment.
        enable_notification (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 is set to send email
            notifications.
        smtp_server (str | Unset): DNS name or IP address of the SMTP server for sending email notifications.
        port (int | None | Unset): Port used for connection to the SMTP server.
        use_authentication (bool | None | Unset): Defines whether the SMTP server requires authentication.
        username (str | Unset): User name of the account used for authentication to the SMTP server.
        use_ssl (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 uses a secure connection to
            transmit email notifications.
        from_ (str | Unset): Email address of the notification sender.
        to (str | Unset): Email address of the notification recipient. For listing multiple recipients, use semicolon as
            a separator.
        subject (str | Unset): Subject for email notifications. The subject of an email notification displays
            information according to the following variables: <ul> <li>*%JobName%* - name of a backup or backup copy
            job.</li> <li>*%JobResult%* - a job result.</li> <li>*%OrgName%* - organization whose data was processed by a
            backup or backup copy job.</li> <li>*%MailboxCount%* - total number of processed objects.</li> <li>*%Issues%* -
            number of objects that were processed with the *Failed* or *Warning* status.</li> <li>*%Time%* - date and time
            of a job completion.</li> </ul>
        authentication_type (RESTAuthenticationType | Unset): Specifies authentication method that Veeam Backup for
            Microsoft 365 uses to send email notifications.
        client_id (str | Unset): Client ID obtained while registering an application in the Google Cloud console or
            Microsoft Azure portal.
        tenant_id (str | Unset): Tenant ID in Azure Active Directory.
        user_id (str | Unset): Authenticated user account ID. Veeam Backup for Microsoft 365 sends email notifications
            on behalf of this user.
        mail_api_url (None | str | Unset): Microsoft Graph API URL of Azure AD application registered in the Microsoft
            Azure portal.
        is_authenticated (bool | None | Unset): Defines a user account authentication status.
    """

    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTNotificationEmailSettingsResponseActions | Unset = UNSET
    notify_on_success: bool | None | Unset = UNSET
    notify_on_warning: bool | None | Unset = UNSET
    notify_on_failure: bool | None | Unset = UNSET
    supress_until_last_retry: bool | None | Unset = UNSET
    attach_detailed_report: bool | None | Unset = UNSET
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
    client_id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    mail_api_url: None | str | Unset = UNSET
    is_authenticated: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        notify_on_success: bool | None | Unset
        if isinstance(self.notify_on_success, Unset):
            notify_on_success = UNSET
        else:
            notify_on_success = self.notify_on_success

        notify_on_warning: bool | None | Unset
        if isinstance(self.notify_on_warning, Unset):
            notify_on_warning = UNSET
        else:
            notify_on_warning = self.notify_on_warning

        notify_on_failure: bool | None | Unset
        if isinstance(self.notify_on_failure, Unset):
            notify_on_failure = UNSET
        else:
            notify_on_failure = self.notify_on_failure

        supress_until_last_retry: bool | None | Unset
        if isinstance(self.supress_until_last_retry, Unset):
            supress_until_last_retry = UNSET
        else:
            supress_until_last_retry = self.supress_until_last_retry

        attach_detailed_report: bool | None | Unset
        if isinstance(self.attach_detailed_report, Unset):
            attach_detailed_report = UNSET
        else:
            attach_detailed_report = self.attach_detailed_report

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
        if notify_on_success is not UNSET:
            field_dict["notifyOnSuccess"] = notify_on_success
        if notify_on_warning is not UNSET:
            field_dict["notifyOnWarning"] = notify_on_warning
        if notify_on_failure is not UNSET:
            field_dict["notifyOnFailure"] = notify_on_failure
        if supress_until_last_retry is not UNSET:
            field_dict["supressUntilLastRetry"] = supress_until_last_retry
        if attach_detailed_report is not UNSET:
            field_dict["attachDetailedReport"] = attach_detailed_report
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_notification_email_settings_response_actions import (
            RESTNotificationEmailSettingsResponseActions,
        )

        d = dict(src_dict)
        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTNotificationEmailSettingsResponseActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTNotificationEmailSettingsResponseActions.from_dict(_field_actions)

        def _parse_notify_on_success(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_on_success = _parse_notify_on_success(d.pop("notifyOnSuccess", UNSET))

        def _parse_notify_on_warning(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_on_warning = _parse_notify_on_warning(d.pop("notifyOnWarning", UNSET))

        def _parse_notify_on_failure(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_on_failure = _parse_notify_on_failure(d.pop("notifyOnFailure", UNSET))

        def _parse_supress_until_last_retry(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supress_until_last_retry = _parse_supress_until_last_retry(d.pop("supressUntilLastRetry", UNSET))

        def _parse_attach_detailed_report(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        attach_detailed_report = _parse_attach_detailed_report(d.pop("attachDetailedReport", UNSET))

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

        rest_notification_email_settings_response = cls(
            field_links=field_links,
            field_actions=field_actions,
            notify_on_success=notify_on_success,
            notify_on_warning=notify_on_warning,
            notify_on_failure=notify_on_failure,
            supress_until_last_retry=supress_until_last_retry,
            attach_detailed_report=attach_detailed_report,
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
            client_id=client_id,
            tenant_id=tenant_id,
            user_id=user_id,
            mail_api_url=mail_api_url,
            is_authenticated=is_authenticated,
        )

        rest_notification_email_settings_response.additional_properties = d
        return rest_notification_email_settings_response

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
