from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_rbac_role_role_type import RESTRbacRoleRoleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_rbac_role_links import RESTRbacRoleLinks


T = TypeVar("T", bound="RESTRbacRole")


@_attrs_define
class RESTRbacRole:
    """
    Attributes:
        id (None | Unset | UUID): ID of the restore operator role.
        organization_id (UUID | Unset): Backed-up organization ID.
        name (str | Unset): Name of the restore operator role.
        description (str | Unset): Description of the restore operator role.
        role_type (RESTRbacRoleRoleType | Unset): Type of the restore operator role. <ul> <li>*EntireOrganization*.
            Restore operators are allowed to explore and restore backed-up data of all objects within the specified
            Microsoft 365 organization.</li> <li>*SpecificObjects*. Restore operators are allowed to explore and restore
            backed-up data of the specified objects.</li> </ul>
        field_links (RESTRbacRoleLinks | Unset):
    """

    id: None | Unset | UUID = UNSET
    organization_id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    role_type: RESTRbacRoleRoleType | Unset = UNSET
    field_links: RESTRbacRoleLinks | Unset = UNSET
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
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_rbac_role_links import RESTRbacRoleLinks

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
        role_type: RESTRbacRoleRoleType | Unset
        if isinstance(_role_type, Unset):
            role_type = UNSET
        else:
            role_type = RESTRbacRoleRoleType(_role_type)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTRbacRoleLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTRbacRoleLinks.from_dict(_field_links)

        rest_rbac_role = cls(
            id=id,
            organization_id=organization_id,
            name=name,
            description=description,
            role_type=role_type,
            field_links=field_links,
        )

        rest_rbac_role.additional_properties = d
        return rest_rbac_role

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
