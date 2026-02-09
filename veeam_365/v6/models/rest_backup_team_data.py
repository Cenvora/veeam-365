from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTBackupTeamData")


@_attrs_define
class RESTBackupTeamData:
    """
    Attributes:
        id (str):
        organization_id (str):
        display_name (str | Unset):
        backed_up_time (datetime.datetime | None | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: str
    organization_id: str
    display_name: str | Unset = UNSET
    backed_up_time: datetime.datetime | None | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization_id = self.organization_id

        display_name = self.display_name

        backed_up_time: None | str | Unset
        if isinstance(self.backed_up_time, Unset):
            backed_up_time = UNSET
        elif isinstance(self.backed_up_time, datetime.datetime):
            backed_up_time = self.backed_up_time.isoformat()
        else:
            backed_up_time = self.backed_up_time

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organizationId": organization_id,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if backed_up_time is not UNSET:
            field_dict["backedUpTime"] = backed_up_time
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        id = d.pop("id")

        organization_id = d.pop("organizationId")

        display_name = d.pop("displayName", UNSET)

        def _parse_backed_up_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backed_up_time_type_0 = isoparse(data)

                return backed_up_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        backed_up_time = _parse_backed_up_time(d.pop("backedUpTime", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_backup_team_data = cls(
            id=id,
            organization_id=organization_id,
            display_name=display_name,
            backed_up_time=backed_up_time,
            field_links=field_links,
        )

        rest_backup_team_data.additional_properties = d
        return rest_backup_team_data

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
