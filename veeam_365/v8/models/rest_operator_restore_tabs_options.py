from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_teams_tab import RestTeamsTab


T = TypeVar("T", bound="RESTOperatorRestoreTabsOptions")


@_attrs_define
class RESTOperatorRestoreTabsOptions:
    """
    Attributes:
        restore_changed_tabs (bool): Defines whether to restore tabs that have been modified in the original location
            since the time when the backup was created.
        restore_missing_tabs (bool): Defines whether to restore tabs that are missed in the original location.
        tabs (list[RestTeamsTab] | Unset): Specifies IDs of the channel tabs that you want to restore. For more
            information on how to get such IDs, see [Get Tabs](TeamsTab#operation/TeamsTab_Get).

            **Note**: If you omit this property, all backed-up tabs of the specified channel will be restored.
        reason (str | Unset): Specifies a reason for the restore operation.
    """

    restore_changed_tabs: bool
    restore_missing_tabs: bool
    tabs: list[RestTeamsTab] | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_changed_tabs = self.restore_changed_tabs

        restore_missing_tabs = self.restore_missing_tabs

        tabs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tabs, Unset):
            tabs = []
            for tabs_item_data in self.tabs:
                tabs_item = tabs_item_data.to_dict()
                tabs.append(tabs_item)

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restoreChangedTabs": restore_changed_tabs,
                "restoreMissingTabs": restore_missing_tabs,
            }
        )
        if tabs is not UNSET:
            field_dict["tabs"] = tabs
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_tab import RestTeamsTab

        d = dict(src_dict)
        restore_changed_tabs = d.pop("restoreChangedTabs")

        restore_missing_tabs = d.pop("restoreMissingTabs")

        _tabs = d.pop("tabs", UNSET)
        tabs: list[RestTeamsTab] | Unset = UNSET
        if _tabs is not UNSET:
            tabs = []
            for tabs_item_data in _tabs:
                tabs_item = RestTeamsTab.from_dict(tabs_item_data)

                tabs.append(tabs_item)

        reason = d.pop("reason", UNSET)

        rest_operator_restore_tabs_options = cls(
            restore_changed_tabs=restore_changed_tabs,
            restore_missing_tabs=restore_missing_tabs,
            tabs=tabs,
            reason=reason,
        )

        rest_operator_restore_tabs_options.additional_properties = d
        return rest_operator_restore_tabs_options

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
