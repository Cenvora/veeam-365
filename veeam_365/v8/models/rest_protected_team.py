from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTProtectedTeam")


@_attrs_define
class RESTProtectedTeam:
    """
    Attributes:
        id (UUID | Unset): Team ID. Example: 00000000-0000-0000-0000-000000000000.
        msid (UUID | Unset): ID of the protected team assigned by Microsoft. Example:
            00000000-0000-0000-0000-000000000000.
        display_name (str | Unset): Display name of the team.
        description (str | Unset): Description of the team.
        organization_id (None | Unset | UUID): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
        backed_up_organization_id (str | Unset): ID of the backed-up organization in the backup.
        e_tag (int | Unset): Version number that Veeam Backup for Microsoft 365 assigns if the protected team was
            modified.
    """

    id: UUID | Unset = UNSET
    msid: UUID | Unset = UNSET
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    backed_up_organization_id: str | Unset = UNSET
    e_tag: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        msid: str | Unset = UNSET
        if not isinstance(self.msid, Unset):
            msid = str(self.msid)

        display_name = self.display_name

        description = self.description

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        backed_up_organization_id = self.backed_up_organization_id

        e_tag = self.e_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if msid is not UNSET:
            field_dict["msid"] = msid
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if backed_up_organization_id is not UNSET:
            field_dict["backedUpOrganizationId"] = backed_up_organization_id
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _msid = d.pop("msid", UNSET)
        msid: UUID | Unset
        if isinstance(_msid, Unset):
            msid = UNSET
        else:
            msid = UUID(_msid)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organizationId", UNSET))

        backed_up_organization_id = d.pop("backedUpOrganizationId", UNSET)

        e_tag = d.pop("eTag", UNSET)

        rest_protected_team = cls(
            id=id,
            msid=msid,
            display_name=display_name,
            description=description,
            organization_id=organization_id,
            backed_up_organization_id=backed_up_organization_id,
            e_tag=e_tag,
        )

        rest_protected_team.additional_properties = d
        return rest_protected_team

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
