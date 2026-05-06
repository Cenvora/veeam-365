from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_history_settings_actions import RESTHistorySettingsActions
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary





T = TypeVar("T", bound="RESTHistorySettings")



@_attrs_define
class RESTHistorySettings:
    """ 
        Attributes:
            keep_allsessions (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 will keep backup and
                backup copy job sessions forever. Otherwise, the job sessions will be kept during 53 weeks by default.
            keeponly_last (int | None | Unset): Number of weeks during which backup and backup copy job sessions will be
                kept.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
            field_actions (RESTHistorySettingsActions | Unset):
     """

    keep_allsessions: bool | None | Unset = UNSET
    keeponly_last: int | None | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTHistorySettingsActions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_history_settings_actions import RESTHistorySettingsActions
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        keep_allsessions: bool | None | Unset
        if isinstance(self.keep_allsessions, Unset):
            keep_allsessions = UNSET
        else:
            keep_allsessions = self.keep_allsessions

        keeponly_last: int | None | Unset
        if isinstance(self.keeponly_last, Unset):
            keeponly_last = UNSET
        else:
            keeponly_last = self.keeponly_last

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if keep_allsessions is not UNSET:
            field_dict["keepAllsessions"] = keep_allsessions
        if keeponly_last is not UNSET:
            field_dict["keeponlyLast"] = keeponly_last
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_history_settings_actions import RESTHistorySettingsActions
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        d = dict(src_dict)
        def _parse_keep_allsessions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        keep_allsessions = _parse_keep_allsessions(d.pop("keepAllsessions", UNSET))


        def _parse_keeponly_last(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        keeponly_last = _parse_keeponly_last(d.pop("keeponlyLast", UNSET))


        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTHistorySettingsActions | Unset
        if isinstance(_field_actions,  Unset):
            field_actions = UNSET
        else:
            field_actions = RESTHistorySettingsActions.from_dict(_field_actions)




        rest_history_settings = cls(
            keep_allsessions=keep_allsessions,
            keeponly_last=keeponly_last,
            field_links=field_links,
            field_actions=field_actions,
        )


        rest_history_settings.additional_properties = d
        return rest_history_settings

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
