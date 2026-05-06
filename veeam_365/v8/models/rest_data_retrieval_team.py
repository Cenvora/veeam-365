from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.rest_data_retrieval_team_links import RESTDataRetrievalTeamLinks





T = TypeVar("T", bound="RESTDataRetrievalTeam")



@_attrs_define
class RESTDataRetrievalTeam:
    """ 
        Attributes:
            id (UUID | Unset): Team ID. Example: 00000000-0000-0000-0000-000000000000.
            display_name (str | Unset): Display name of the team.
            description (str | Unset): Description of the team.
            field_links (RESTDataRetrievalTeamLinks | Unset):
     """

    id: UUID | Unset = UNSET
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    field_links: RESTDataRetrievalTeamLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_data_retrieval_team_links import RESTDataRetrievalTeamLinks
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        display_name = self.display_name

        description = self.description

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        from ..models.rest_data_retrieval_team_links import RESTDataRetrievalTeamLinks
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTDataRetrievalTeamLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTDataRetrievalTeamLinks.from_dict(_field_links)




        rest_data_retrieval_team = cls(
            id=id,
            display_name=display_name,
            description=description,
            field_links=field_links,
        )


        rest_data_retrieval_team.additional_properties = d
        return rest_data_retrieval_team

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
