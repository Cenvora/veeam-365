from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_restore_point_team_links import RESTRestorePointTeamLinks


T = TypeVar("T", bound="RESTRestorePointTeam")


@_attrs_define
class RESTRestorePointTeam:
    """
    Attributes:
        id (None | Unset | UUID): Team ID. Example: 00000000-0000-0000-0000-000000000000.
        display_name (str | Unset): Display name of the team.
        description (str | Unset): Description of the team.
        field_links (RESTRestorePointTeamLinks | Unset):
    """

    id: None | Unset | UUID = UNSET
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    field_links: RESTRestorePointTeamLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        display_name = self.display_name

        description = self.description

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_restore_point_team_links import RESTRestorePointTeamLinks

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

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTRestorePointTeamLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTRestorePointTeamLinks.from_dict(_field_links)

        rest_restore_point_team = cls(
            id=id,
            display_name=display_name,
            description=description,
            field_links=field_links,
        )

        rest_restore_point_team.additional_properties = d
        return rest_restore_point_team

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
