from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.token_data_body_grant_type import TokenDataBodyGrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenDataBody")


@_attrs_define
class TokenDataBody:
    r"""
    Attributes:
        grant_type (TokenDataBodyGrantType): Specifies a grant type that will be used to authenticate a user. Default:
            TokenDataBodyGrantType.PASSWORD.
        username (str | Unset): \[Required if the `grant_type` property value is *password*\] Specifies a user name.
        password (str | Unset): \[Required if the `grant_type` property value is *password*\] Specifies a user password.
        refresh_token (str | Unset): \[Required if the `grant_type` property value is *refresh_token*\] Specifies a
            refresh token.
        client_id (str | Unset): \[Required if the `grant_type` property value is *urn:ietf:params:oauth:grant-type:jwt-
            bearer* or *operator*\] Specifies either an application ID or combination of a user ID and tenant ID in the
            following format: *userId.tenantId*.
        assertion (str | Unset): \[Required if the `grant_type` property value is *urn:ietf:params:oauth:grant-type:jwt-
            bearer* or *operator*\] Specifies an assertion.
        integration_token (str | Unset): \[Required if the `grant_type` property value is *integration*\] Specifies an
            integration token.
        disable_antiforgery_token (bool | None | Unset): Defines whether an antiforgery token is not required for Veeam
            Backup for Microsoft 365 REST API authorization process. The antiforgery token is stored in web browser cookies
            and protects an access and refresh tokens during a web browser REST API session.
    """

    grant_type: TokenDataBodyGrantType = TokenDataBodyGrantType.PASSWORD
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    refresh_token: str | Unset = UNSET
    client_id: str | Unset = UNSET
    assertion: str | Unset = UNSET
    integration_token: str | Unset = UNSET
    disable_antiforgery_token: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type.value

        username = self.username

        password = self.password

        refresh_token = self.refresh_token

        client_id = self.client_id

        assertion = self.assertion

        integration_token = self.integration_token

        disable_antiforgery_token: bool | None | Unset
        if isinstance(self.disable_antiforgery_token, Unset):
            disable_antiforgery_token = UNSET
        else:
            disable_antiforgery_token = self.disable_antiforgery_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if assertion is not UNSET:
            field_dict["assertion"] = assertion
        if integration_token is not UNSET:
            field_dict["integration_token"] = integration_token
        if disable_antiforgery_token is not UNSET:
            field_dict["disable_antiforgery_token"] = disable_antiforgery_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = TokenDataBodyGrantType(d.pop("grant_type"))

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        client_id = d.pop("client_id", UNSET)

        assertion = d.pop("assertion", UNSET)

        integration_token = d.pop("integration_token", UNSET)

        def _parse_disable_antiforgery_token(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disable_antiforgery_token = _parse_disable_antiforgery_token(d.pop("disable_antiforgery_token", UNSET))

        token_data_body = cls(
            grant_type=grant_type,
            username=username,
            password=password,
            refresh_token=refresh_token,
            client_id=client_id,
            assertion=assertion,
            integration_token=integration_token,
            disable_antiforgery_token=disable_antiforgery_token,
        )

        token_data_body.additional_properties = d
        return token_data_body

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
