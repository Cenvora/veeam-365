from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTTeam")


@_attrs_define
class RESTTeam:
    """
    Attributes:
        id (UUID): Team ID. Example: 00000000-0000-0000-0000-000000000000.
        display_name (str): Display name of the team.
        mail (str): Email address of the team.
        e_tag (int | None | Unset): Version number that Veeam Backup for Microsoft 365 assigns if the team was modified.
        description (str | Unset): Description of the team.
        msid (None | Unset | UUID): ID of the team assigned by Microsoft.
        field_links (RESTLinkHALDictionary | Unset): Related resources.
    """

    id: UUID
    display_name: str
    mail: str
    e_tag: int | None | Unset = UNSET
    description: str | Unset = UNSET
    msid: None | Unset | UUID = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        display_name = self.display_name

        mail = self.mail

        e_tag: int | None | Unset
        if isinstance(self.e_tag, Unset):
            e_tag = UNSET
        else:
            e_tag = self.e_tag

        description = self.description

        msid: None | str | Unset
        if isinstance(self.msid, Unset):
            msid = UNSET
        elif isinstance(self.msid, UUID):
            msid = str(self.msid)
        else:
            msid = self.msid

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
                "mail": mail,
            }
        )
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag
        if description is not UNSET:
            field_dict["description"] = description
        if msid is not UNSET:
            field_dict["msid"] = msid
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        display_name = d.pop("displayName")

        mail = d.pop("mail")

        def _parse_e_tag(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        e_tag = _parse_e_tag(d.pop("eTag", UNSET))

        description = d.pop("description", UNSET)

        def _parse_msid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                msid_type_0 = UUID(data)

                return msid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        msid = _parse_msid(d.pop("msid", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_team = cls(
            id=id,
            display_name=display_name,
            mail=mail,
            e_tag=e_tag,
            description=description,
            msid=msid,
            field_links=field_links,
        )

        rest_team.additional_properties = d
        return rest_team

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
