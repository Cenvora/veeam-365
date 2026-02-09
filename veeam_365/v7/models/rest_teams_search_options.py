from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_teams_search_options_type import RESTTeamsSearchOptionsType

T = TypeVar("T", bound="RESTTeamsSearchOptions")


@_attrs_define
class RESTTeamsSearchOptions:
    """
    Attributes:
        type_ (RESTTeamsSearchOptionsType): Specifies the type of Microsoft Teams items that you want to find.
        query (str): Specifies query parameters used to search for Microsoft Teams items. For the complete list of
            supported query parameters, see the Veeam Backup for Microsoft 365 REST API Reference Overview, section
            [Appendix A. Item Search Parameters](https://helpcenter.veeam.com/docs/vbo365/rest/appendix_search.html?ver=70).
    """

    type_: RESTTeamsSearchOptionsType
    query: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        query = self.query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "query": query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = RESTTeamsSearchOptionsType(d.pop("type"))

        query = d.pop("query")

        rest_teams_search_options = cls(
            type_=type_,
            query=query,
        )

        rest_teams_search_options.additional_properties = d
        return rest_teams_search_options

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
