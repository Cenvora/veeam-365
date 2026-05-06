from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_rbac_operator_type import RESTRbacOperatorType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_rbac_user import RESTRbacUser
  from ..models.rest_rbac_user_operator_links import RESTRbacUserOperatorLinks





T = TypeVar("T", bound="RESTRbacUserOperator")



@_attrs_define
class RESTRbacUserOperator:
    """ 
        Attributes:
            type_ (RESTRbacOperatorType): Type of the object.
            user (RESTRbacUser):
            id (str): ID of the restore operator.
            field_links (RESTRbacUserOperatorLinks | Unset):
     """

    type_: RESTRbacOperatorType
    user: RESTRbacUser
    id: str
    field_links: RESTRbacUserOperatorLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_rbac_user import RESTRbacUser
        from ..models.rest_rbac_user_operator_links import RESTRbacUserOperatorLinks
        type_ = self.type_.value

        user = self.user.to_dict()

        id = self.id

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "user": user,
            "id": id,
        })
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_rbac_user import RESTRbacUser
        from ..models.rest_rbac_user_operator_links import RESTRbacUserOperatorLinks
        d = dict(src_dict)
        type_ = RESTRbacOperatorType(d.pop("type"))




        user = RESTRbacUser.from_dict(d.pop("user"))




        id = d.pop("id")

        _field_links = d.pop("_links", UNSET)
        field_links: RESTRbacUserOperatorLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTRbacUserOperatorLinks.from_dict(_field_links)




        rest_rbac_user_operator = cls(
            type_=type_,
            user=user,
            id=id,
            field_links=field_links,
        )


        rest_rbac_user_operator.additional_properties = d
        return rest_rbac_user_operator

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
