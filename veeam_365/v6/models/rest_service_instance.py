from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTServiceInstance")


@_attrs_define
class RESTServiceInstance:
    """
    Attributes:
        installation_id (UUID | Unset):  Example: 00000000-0000-0000-0000-000000000000.
        version (str | Unset):
    """

    installation_id: UUID | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        installation_id: str | Unset = UNSET
        if not isinstance(self.installation_id, Unset):
            installation_id = str(self.installation_id)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if installation_id is not UNSET:
            field_dict["installationId"] = installation_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _installation_id = d.pop("installationId", UNSET)
        installation_id: UUID | Unset
        if isinstance(_installation_id, Unset):
            installation_id = UNSET
        else:
            installation_id = UUID(_installation_id)

        version = d.pop("version", UNSET)

        rest_service_instance = cls(
            installation_id=installation_id,
            version=version,
        )

        rest_service_instance.additional_properties = d
        return rest_service_instance

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
