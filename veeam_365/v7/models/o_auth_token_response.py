from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="OAuthTokenResponse")


@_attrs_define
class OAuthTokenResponse:
    """
    Attributes:
        access_token (str): String that represents authorization issued to the user and that must be used in all
            requests during the current logon session.
        refresh_token (str): String that represents authorization granted to the user and that can be used to obtain a
            new access token if the current access token expires or becomes lost.
        token_type (str): Type of the user authorization.
        expires_in (int): Access token lifetime.
        user_name (str): Name of the authorized user.
        issued (datetime.datetime): Date and time when the tokens were issued.
        expires (datetime.datetime): Date and time when the access token expires.
    """

    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    user_name: str
    issued: datetime.datetime
    expires: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        refresh_token = self.refresh_token

        token_type = self.token_type

        expires_in = self.expires_in

        user_name = self.user_name

        issued = self.issued.isoformat()

        expires = self.expires.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": token_type,
                "expires_in": expires_in,
                "userName": user_name,
                ".issued": issued,
                ".expires": expires,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token")

        refresh_token = d.pop("refresh_token")

        token_type = d.pop("token_type")

        expires_in = d.pop("expires_in")

        user_name = d.pop("userName")

        issued = isoparse(d.pop(".issued"))

        expires = isoparse(d.pop(".expires"))

        o_auth_token_response = cls(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type=token_type,
            expires_in=expires_in,
            user_name=user_name,
            issued=issued,
            expires=expires,
        )

        o_auth_token_response.additional_properties = d
        return o_auth_token_response

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
