from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTNotificationEmailSettingsRequest")


@_attrs_define
class RESTNotificationEmailSettingsRequest:
    """
    Attributes:
        user_password (str | Unset):
        notify_on_success (bool | None | Unset):
        notify_on_warning (bool | None | Unset):
        notify_on_failure (bool | None | Unset):
        supress_until_last_retry (bool | None | Unset):
        attach_detailed_report (bool | None | Unset):
        enable_notification (bool | None | Unset):
        smtp_server (str | Unset):
        port (int | None | Unset):
        use_authentication (bool | None | Unset):
        username (str | Unset):
        use_ssl (bool | None | Unset):
        from_ (str | Unset):
        to (str | Unset):
        subject (str | Unset):
    """

    user_password: str | Unset = UNSET
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_password = self.user_password

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_password is not UNSET:
            field_dict["userPassword"] = user_password
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_password = d.pop("userPassword", UNSET)

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

        rest_notification_email_settings_request = cls(
            user_password=user_password,
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
        )

        rest_notification_email_settings_request.additional_properties = d
        return rest_notification_email_settings_request

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
