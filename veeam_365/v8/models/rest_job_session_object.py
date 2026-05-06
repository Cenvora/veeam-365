from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_job_session_object_status import RESTJobSessionObjectStatus
from ..models.rest_job_session_object_type import RESTJobSessionObjectType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary





T = TypeVar("T", bound="RESTJobSessionObject")



@_attrs_define
class RESTJobSessionObject:
    """ 
        Attributes:
            id (str | Unset): ID of an object processed by the job session.
            type_ (RESTJobSessionObjectType | Unset): Processed object type.
            status (RESTJobSessionObjectStatus | Unset): Status of object processing during the job session.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
     """

    id: str | Unset = UNSET
    type_: RESTJobSessionObjectType | Unset = UNSET
    status: RESTJobSessionObjectStatus | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTJobSessionObjectType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RESTJobSessionObjectType(_type_)




        _status = d.pop("status", UNSET)
        status: RESTJobSessionObjectStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = RESTJobSessionObjectStatus(_status)




        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        rest_job_session_object = cls(
            id=id,
            type_=type_,
            status=status,
            field_links=field_links,
        )


        rest_job_session_object.additional_properties = d
        return rest_job_session_object

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
