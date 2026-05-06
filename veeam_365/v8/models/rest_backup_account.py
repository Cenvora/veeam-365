from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_group_member import RESTGroupMember





T = TypeVar("T", bound="RESTBackupAccount")



@_attrs_define
class RESTBackupAccount:
    """ 
        Attributes:
            group_member (RESTGroupMember | Unset):
            password (str | Unset): Specifies a password.
     """

    group_member: RESTGroupMember | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_group_member import RESTGroupMember
        group_member: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_member, Unset):
            group_member = self.group_member.to_dict()

        password = self.password


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if group_member is not UNSET:
            field_dict["groupMember"] = group_member
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_group_member import RESTGroupMember
        d = dict(src_dict)
        _group_member = d.pop("groupMember", UNSET)
        group_member: RESTGroupMember | Unset
        if isinstance(_group_member,  Unset):
            group_member = UNSET
        else:
            group_member = RESTGroupMember.from_dict(_group_member)




        password = d.pop("password", UNSET)

        rest_backup_account = cls(
            group_member=group_member,
            password=password,
        )


        rest_backup_account.additional_properties = d
        return rest_backup_account

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
