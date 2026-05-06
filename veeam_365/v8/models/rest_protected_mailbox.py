from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="RESTProtectedMailbox")



@_attrs_define
class RESTProtectedMailbox:
    """ 
        Attributes:
            id (UUID | Unset): Mailbox ID. Example: 00000000-0000-0000-0000-000000000000.
            display_name (str | Unset): Display name of the mailbox.
            email (str | Unset): Mailbox email.
            is_archive (bool | Unset): Defines whether the mailbox is of the *Archive* type.
     """

    id: UUID | Unset = UNSET
    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    is_archive: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        display_name = self.display_name

        email = self.email

        is_archive = self.is_archive


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if is_archive is not UNSET:
            field_dict["isArchive"] = is_archive

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        display_name = d.pop("displayName", UNSET)

        email = d.pop("email", UNSET)

        is_archive = d.pop("isArchive", UNSET)

        rest_protected_mailbox = cls(
            id=id,
            display_name=display_name,
            email=email,
            is_archive=is_archive,
        )


        rest_protected_mailbox.additional_properties = d
        return rest_protected_mailbox

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
