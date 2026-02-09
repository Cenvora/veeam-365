from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_rbac_role_create_model_role_type import RESTRbacRoleCreateModelRoleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_rbac_item_composed import RESTRbacItemComposed
    from ..models.rest_rbac_role_create_model_links import RESTRbacRoleCreateModelLinks


T = TypeVar("T", bound="RESTRbacRoleCreateModel")


@_attrs_define
class RESTRbacRoleCreateModel:
    """
    Attributes:
        id (None | Unset | UUID):
        organization_id (UUID | Unset):
        name (str | Unset):
        description (str | Unset):
        role_type (RESTRbacRoleCreateModelRoleType | Unset):
        operators (list[RESTRbacItemComposed] | Unset):
        selected_items (list[RESTRbacItemComposed] | Unset):
        excluded_items (list[RESTRbacItemComposed] | Unset):
        field_links (RESTRbacRoleCreateModelLinks | Unset):
    """

    id: None | Unset | UUID = UNSET
    organization_id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    role_type: RESTRbacRoleCreateModelRoleType | Unset = UNSET
    operators: list[RESTRbacItemComposed] | Unset = UNSET
    selected_items: list[RESTRbacItemComposed] | Unset = UNSET
    excluded_items: list[RESTRbacItemComposed] | Unset = UNSET
    field_links: RESTRbacRoleCreateModelLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        name = self.name

        description = self.description

        role_type: str | Unset = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.value

        operators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.operators, Unset):
            operators = []
            for operators_item_data in self.operators:
                operators_item = operators_item_data.to_dict()
                operators.append(operators_item)

        selected_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.selected_items, Unset):
            selected_items = []
            for selected_items_item_data in self.selected_items:
                selected_items_item = selected_items_item_data.to_dict()
                selected_items.append(selected_items_item)

        excluded_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.excluded_items, Unset):
            excluded_items = []
            for excluded_items_item_data in self.excluded_items:
                excluded_items_item = excluded_items_item_data.to_dict()
                excluded_items.append(excluded_items_item)

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if role_type is not UNSET:
            field_dict["roleType"] = role_type
        if operators is not UNSET:
            field_dict["operators"] = operators
        if selected_items is not UNSET:
            field_dict["selectedItems"] = selected_items
        if excluded_items is not UNSET:
            field_dict["excludedItems"] = excluded_items
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_rbac_item_composed import RESTRbacItemComposed
        from ..models.rest_rbac_role_create_model_links import RESTRbacRoleCreateModelLinks

        d = dict(src_dict)

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

        _organization_id = d.pop("organizationId", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _role_type = d.pop("roleType", UNSET)
        role_type: RESTRbacRoleCreateModelRoleType | Unset
        if isinstance(_role_type, Unset):
            role_type = UNSET
        else:
            role_type = RESTRbacRoleCreateModelRoleType(_role_type)

        _operators = d.pop("operators", UNSET)
        operators: list[RESTRbacItemComposed] | Unset = UNSET
        if _operators is not UNSET:
            operators = []
            for operators_item_data in _operators:
                operators_item = RESTRbacItemComposed.from_dict(operators_item_data)

                operators.append(operators_item)

        _selected_items = d.pop("selectedItems", UNSET)
        selected_items: list[RESTRbacItemComposed] | Unset = UNSET
        if _selected_items is not UNSET:
            selected_items = []
            for selected_items_item_data in _selected_items:
                selected_items_item = RESTRbacItemComposed.from_dict(selected_items_item_data)

                selected_items.append(selected_items_item)

        _excluded_items = d.pop("excludedItems", UNSET)
        excluded_items: list[RESTRbacItemComposed] | Unset = UNSET
        if _excluded_items is not UNSET:
            excluded_items = []
            for excluded_items_item_data in _excluded_items:
                excluded_items_item = RESTRbacItemComposed.from_dict(excluded_items_item_data)

                excluded_items.append(excluded_items_item)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTRbacRoleCreateModelLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTRbacRoleCreateModelLinks.from_dict(_field_links)

        rest_rbac_role_create_model = cls(
            id=id,
            organization_id=organization_id,
            name=name,
            description=description,
            role_type=role_type,
            operators=operators,
            selected_items=selected_items,
            excluded_items=excluded_items,
            field_links=field_links,
        )

        rest_rbac_role_create_model.additional_properties = d
        return rest_rbac_role_create_model

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
