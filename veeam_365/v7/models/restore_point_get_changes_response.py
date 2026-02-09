from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
    from ..models.rest_restore_point import RESTRestorePoint


T = TypeVar("T", bound="RestorePointGetChangesResponse")


@_attrs_define
class RestorePointGetChangesResponse:
    """
    Attributes:
        next_change_token (str): Next change token.
        limit (int): Limits the maximum number of items that the server will return on a page. The maximum supported
            number of items per page is *10,000*. The default value is *30*.
        results (list[RESTRestorePoint]): Array of objects.
        set_id (UUID | Unset): ID of this request stored in cache. Using the ID in subsequent requests, you decrease the
            number of requests to the cloud.
        field_links (RESTLinkHALDictionary | Unset):
        total_count (int | None | Unset):
    """

    next_change_token: str
    limit: int
    results: list[RESTRestorePoint]
    set_id: UUID | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    total_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_change_token = self.next_change_token

        limit = self.limit

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        set_id: str | Unset = UNSET
        if not isinstance(self.set_id, Unset):
            set_id = str(self.set_id)

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        total_count: int | None | Unset
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        else:
            total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nextChangeToken": next_change_token,
                "limit": limit,
                "results": results,
            }
        )
        if set_id is not UNSET:
            field_dict["setId"] = set_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_restore_point import RESTRestorePoint

        d = dict(src_dict)
        next_change_token = d.pop("nextChangeToken")

        limit = d.pop("limit")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = RESTRestorePoint.from_dict(results_item_data)

            results.append(results_item)

        _set_id = d.pop("setId", UNSET)
        set_id: UUID | Unset
        if isinstance(_set_id, Unset):
            set_id = UNSET
        else:
            set_id = UUID(_set_id)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        def _parse_total_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_count = _parse_total_count(d.pop("totalCount", UNSET))

        restore_point_get_changes_response = cls(
            next_change_token=next_change_token,
            limit=limit,
            results=results,
            set_id=set_id,
            field_links=field_links,
            total_count=total_count,
        )

        restore_point_get_changes_response.additional_properties = d
        return restore_point_get_changes_response

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
