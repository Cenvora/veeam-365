from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="RESTApplication")



@_attrs_define
class RESTApplication:
    """ 
        Attributes:
            application_id (UUID | Unset): Microsoft Entra application ID. Example: 00000000-0000-0000-0000-000000000000.
            display_name (str | Unset): Name of Microsoft Entra application.
            tags (list[str] | Unset): Tags for the application (if any).
     """

    application_id: UUID | Unset = UNSET
    display_name: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        application_id: str | Unset = UNSET
        if not isinstance(self.application_id, Unset):
            application_id = str(self.application_id)

        display_name = self.display_name

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _application_id = d.pop("applicationId", UNSET)
        application_id: UUID | Unset
        if isinstance(_application_id,  Unset):
            application_id = UNSET
        else:
            application_id = UUID(_application_id)




        display_name = d.pop("displayName", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        rest_application = cls(
            application_id=application_id,
            display_name=display_name,
            tags=tags,
        )


        rest_application.additional_properties = d
        return rest_application

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
