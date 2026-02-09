from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_repository_synchronize_session_state import RESTRepositorySynchronizeSessionState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTRepositorySynchronizeSession")


@_attrs_define
class RESTRepositorySynchronizeSession:
    """
    Attributes:
        id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        repository_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        state (RESTRepositorySynchronizeSessionState | Unset):
        progress_percent (int | None | Unset):
        error (str | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: None | Unset | UUID = UNSET
    repository_id: None | Unset | UUID = UNSET
    state: RESTRepositorySynchronizeSessionState | Unset = UNSET
    progress_percent: int | None | Unset = UNSET
    error: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        repository_id: None | str | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        elif isinstance(self.repository_id, UUID):
            repository_id = str(self.repository_id)
        else:
            repository_id = self.repository_id

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        progress_percent: int | None | Unset
        if isinstance(self.progress_percent, Unset):
            progress_percent = UNSET
        else:
            progress_percent = self.progress_percent

        error = self.error

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if state is not UNSET:
            field_dict["state"] = state
        if progress_percent is not UNSET:
            field_dict["progressPercent"] = progress_percent
        if error is not UNSET:
            field_dict["error"] = error
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

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

        def _parse_repository_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_id_type_0 = UUID(data)

                return repository_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        repository_id = _parse_repository_id(d.pop("repositoryId", UNSET))

        _state = d.pop("state", UNSET)
        state: RESTRepositorySynchronizeSessionState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RESTRepositorySynchronizeSessionState(_state)

        def _parse_progress_percent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        progress_percent = _parse_progress_percent(d.pop("progressPercent", UNSET))

        error = d.pop("error", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_repository_synchronize_session = cls(
            id=id,
            repository_id=repository_id,
            state=state,
            progress_percent=progress_percent,
            error=error,
            field_links=field_links,
        )

        rest_repository_synchronize_session.additional_properties = d
        return rest_repository_synchronize_session

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
