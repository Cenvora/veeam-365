from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTEncryptionKeyToSend")


@_attrs_define
class RESTEncryptionKeyToSend:
    """
    Attributes:
        password (str | Unset):
        new_password (str | Unset):
        old_password (str | Unset):
        id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        description (str | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    password: str | Unset = UNSET
    new_password: str | Unset = UNSET
    old_password: str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    description: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        new_password = self.new_password

        old_password = self.old_password

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        description = self.description

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if new_password is not UNSET:
            field_dict["newPassword"] = new_password
        if old_password is not UNSET:
            field_dict["oldPassword"] = old_password
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        password = d.pop("password", UNSET)

        new_password = d.pop("newPassword", UNSET)

        old_password = d.pop("oldPassword", UNSET)

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        description = d.pop("description", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_encryption_key_to_send = cls(
            password=password,
            new_password=new_password,
            old_password=old_password,
            id=id,
            description=description,
            field_links=field_links,
        )

        rest_encryption_key_to_send.additional_properties = d
        return rest_encryption_key_to_send

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
