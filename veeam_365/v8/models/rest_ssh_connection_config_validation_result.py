from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_status import ConnectionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTSshConnectionConfigValidationResult")


@_attrs_define
class RESTSshConnectionConfigValidationResult:
    """
    Attributes:
        status (ConnectionStatus | Unset): Status of checking the SSH connection.
        fingerprint (str | Unset): SSH fingerprint.
        public_base_64_key (str | Unset): Public key file provided as a Base64 string.
    """

    status: ConnectionStatus | Unset = UNSET
    fingerprint: str | Unset = UNSET
    public_base_64_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        fingerprint = self.fingerprint

        public_base_64_key = self.public_base_64_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if public_base_64_key is not UNSET:
            field_dict["publicBase64Key"] = public_base_64_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ConnectionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ConnectionStatus(_status)

        fingerprint = d.pop("fingerprint", UNSET)

        public_base_64_key = d.pop("publicBase64Key", UNSET)

        rest_ssh_connection_config_validation_result = cls(
            status=status,
            fingerprint=fingerprint,
            public_base_64_key=public_base_64_key,
        )

        rest_ssh_connection_config_validation_result.additional_properties = d
        return rest_ssh_connection_config_validation_result

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
