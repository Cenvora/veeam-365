from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
    from ..models.rest_organization_current_sync_state import RESTOrganizationCurrentSyncState
    from ..models.rest_organization_last_sync_state import RESTOrganizationLastSyncState


T = TypeVar("T", bound="RESTOrganizationSyncState")


@_attrs_define
class RESTOrganizationSyncState:
    """
    Attributes:
        organization_id (UUID | Unset): ID of the Microsoft 365 organization. Example:
            00000000-0000-0000-0000-000000000000.
        last_sync_state (None | RESTOrganizationLastSyncState | Unset): Details of the latest synchronization.
        current_sync_state (RESTOrganizationCurrentSyncState | Unset):
        field_links (RESTLinkHALDictionary | Unset): Related resources.
    """

    organization_id: UUID | Unset = UNSET
    last_sync_state: None | RESTOrganizationLastSyncState | Unset = UNSET
    current_sync_state: RESTOrganizationCurrentSyncState | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_organization_last_sync_state import RESTOrganizationLastSyncState

        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        last_sync_state: dict[str, Any] | None | Unset
        if isinstance(self.last_sync_state, Unset):
            last_sync_state = UNSET
        elif isinstance(self.last_sync_state, RESTOrganizationLastSyncState):
            last_sync_state = self.last_sync_state.to_dict()
        else:
            last_sync_state = self.last_sync_state

        current_sync_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_sync_state, Unset):
            current_sync_state = self.current_sync_state.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if last_sync_state is not UNSET:
            field_dict["lastSyncState"] = last_sync_state
        if current_sync_state is not UNSET:
            field_dict["currentSyncState"] = current_sync_state
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_organization_current_sync_state import RESTOrganizationCurrentSyncState
        from ..models.rest_organization_last_sync_state import RESTOrganizationLastSyncState

        d = dict(src_dict)
        _organization_id = d.pop("organizationId", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        def _parse_last_sync_state(data: object) -> None | RESTOrganizationLastSyncState | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_sync_state_type_1 = RESTOrganizationLastSyncState.from_dict(data)

                return last_sync_state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTOrganizationLastSyncState | Unset, data)

        last_sync_state = _parse_last_sync_state(d.pop("lastSyncState", UNSET))

        _current_sync_state = d.pop("currentSyncState", UNSET)
        current_sync_state: RESTOrganizationCurrentSyncState | Unset
        if isinstance(_current_sync_state, Unset):
            current_sync_state = UNSET
        else:
            current_sync_state = RESTOrganizationCurrentSyncState.from_dict(_current_sync_state)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_organization_sync_state = cls(
            organization_id=organization_id,
            last_sync_state=last_sync_state,
            current_sync_state=current_sync_state,
            field_links=field_links,
        )

        rest_organization_sync_state.additional_properties = d
        return rest_organization_sync_state

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
