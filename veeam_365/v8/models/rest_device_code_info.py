from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="RESTDeviceCodeInfo")



@_attrs_define
class RESTDeviceCodeInfo:
    """ 
        Attributes:
            user_code (str | Unset): Code that you must copy and then specify on Microsoft Identity platform.
            verification_uri (str | Unset): Verification URL that you must open to sign in to Microsoft Identity platform.
            expires_on_utc (datetime.datetime | Unset): Date and time when the code expires.
            message (str | Unset): Help message.
     """

    user_code: str | Unset = UNSET
    verification_uri: str | Unset = UNSET
    expires_on_utc: datetime.datetime | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_code = self.user_code

        verification_uri = self.verification_uri

        expires_on_utc: str | Unset = UNSET
        if not isinstance(self.expires_on_utc, Unset):
            expires_on_utc = self.expires_on_utc.isoformat()

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if verification_uri is not UNSET:
            field_dict["verificationUri"] = verification_uri
        if expires_on_utc is not UNSET:
            field_dict["expiresOnUtc"] = expires_on_utc
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_code = d.pop("userCode", UNSET)

        verification_uri = d.pop("verificationUri", UNSET)

        _expires_on_utc = d.pop("expiresOnUtc", UNSET)
        expires_on_utc: datetime.datetime | Unset
        if isinstance(_expires_on_utc,  Unset):
            expires_on_utc = UNSET
        else:
            expires_on_utc = isoparse(_expires_on_utc)




        message = d.pop("message", UNSET)

        rest_device_code_info = cls(
            user_code=user_code,
            verification_uri=verification_uri,
            expires_on_utc=expires_on_utc,
            message=message,
        )


        rest_device_code_info.additional_properties = d
        return rest_device_code_info

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
