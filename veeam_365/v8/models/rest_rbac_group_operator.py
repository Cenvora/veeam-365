from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_rbac_operator_type import RESTRbacOperatorType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_rbac_group import RESTRbacGroup
    from ..models.rest_rbac_group_operator_links import RESTRbacGroupOperatorLinks


T = TypeVar("T", bound="RESTRbacGroupOperator")


@_attrs_define
class RESTRbacGroupOperator:
    """
    Attributes:
        type_ (RESTRbacOperatorType): Type of the object.
        group (RESTRbacGroup):
        id (str): ID of the restore operator.
        field_links (RESTRbacGroupOperatorLinks | Unset):
    """

    type_: RESTRbacOperatorType
    group: RESTRbacGroup
    id: str
    field_links: RESTRbacGroupOperatorLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        group = self.group.to_dict()

        id = self.id

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "group": group,
                "id": id,
            }
        )
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_rbac_group import RESTRbacGroup
        from ..models.rest_rbac_group_operator_links import RESTRbacGroupOperatorLinks

        d = dict(src_dict)
        type_ = RESTRbacOperatorType(d.pop("type"))

        group = RESTRbacGroup.from_dict(d.pop("group"))

        id = d.pop("id")

        _field_links = d.pop("_links", UNSET)
        field_links: RESTRbacGroupOperatorLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTRbacGroupOperatorLinks.from_dict(_field_links)

        rest_rbac_group_operator = cls(
            type_=type_,
            group=group,
            id=id,
            field_links=field_links,
        )

        rest_rbac_group_operator.additional_properties = d
        return rest_rbac_group_operator

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
