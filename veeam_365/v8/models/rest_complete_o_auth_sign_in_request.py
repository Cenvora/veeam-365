from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTCompleteOAuthSignInRequest")



@_attrs_define
class RESTCompleteOAuthSignInRequest:
    """ 
        Attributes:
            code (str | Unset): Specifies value that you get from the Google Authorization Server or Microsoft Identity
                platform in the redirect URL. Veeam Backup for Microsoft 365 and Veeam Explorers will use this value to obtain
                an access token.
            state (str | Unset): Specifies value that you get from the Google Authorization Server or Microsoft Identity
                platform in the redirect URL. Veeam Backup for Microsoft 365 and Veeam Explorers will use this value to check
                that the `code` property value matches the authentication request.
     """

    code: str | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        state = self.state


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        state = d.pop("state", UNSET)

        rest_complete_o_auth_sign_in_request = cls(
            code=code,
            state=state,
        )


        rest_complete_o_auth_sign_in_request.additional_properties = d
        return rest_complete_o_auth_sign_in_request

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
