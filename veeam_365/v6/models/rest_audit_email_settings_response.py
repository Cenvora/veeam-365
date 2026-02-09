from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_audit_email_settings_response_actions import RESTAuditEmailSettingsResponseActions
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTAuditEmailSettingsResponse")


@_attrs_define
class RESTAuditEmailSettingsResponse:
    """
    Attributes:
        field_links (RESTLinkHALDictionary | Unset):
        field_actions (RESTAuditEmailSettingsResponseActions | Unset):
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

    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTAuditEmailSettingsResponseActions | Unset = UNSET
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
        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

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
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
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
        from ..models.rest_audit_email_settings_response_actions import RESTAuditEmailSettingsResponseActions
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTAuditEmailSettingsResponseActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTAuditEmailSettingsResponseActions.from_dict(_field_actions)

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

        rest_audit_email_settings_response = cls(
            field_links=field_links,
            field_actions=field_actions,
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

        rest_audit_email_settings_response.additional_properties = d
        return rest_audit_email_settings_response

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
