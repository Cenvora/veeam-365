from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_event_type import RESTEventType

T = TypeVar("T", bound="RESTOrganizationSiteUpdateEvent")


@_attrs_define
class RESTOrganizationSiteUpdateEvent:
    """
    Attributes:
        event_type (RESTEventType): Type of the event.
        id (str): Organization site ID.
        organization_id (UUID): Backed-up organization ID.
        e_tag (int): Version number that Veeam Backup for Microsoft 365 assigns if the organization site was modified.
    """

    event_type: RESTEventType
    id: str
    organization_id: UUID
    e_tag: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        id = self.id

        organization_id = str(self.organization_id)

        e_tag = self.e_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "id": id,
                "organizationId": organization_id,
                "eTag": e_tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = RESTEventType(d.pop("eventType"))

        id = d.pop("id")

        organization_id = UUID(d.pop("organizationId"))

        e_tag = d.pop("eTag")

        rest_organization_site_update_event = cls(
            event_type=event_type,
            id=id,
            organization_id=organization_id,
            e_tag=e_tag,
        )

        rest_organization_site_update_event.additional_properties = d
        return rest_organization_site_update_event

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
