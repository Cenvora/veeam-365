from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
    from ..models.rest_management_mode_actions import RESTManagementModeActions


T = TypeVar("T", bound="RESTManagementMode")


@_attrs_define
class RESTManagementMode:
    """
    Attributes:
        is_managed (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 is managed by Veeam Service
            Provider Console or Veeam One.
        manager_id (None | Unset | UUID): ID of the Veeam Service Provider Console server that manages Veeam Backup for
            Microsoft 365. Example: 00000000-0000-0000-0000-000000000000.
        company_name (str | Unset): Name of the company that manages Veeam Backup for Microsoft 365.
        field_links (RESTLinkHALDictionary | Unset): Related resources.
        field_actions (RESTManagementModeActions | Unset):
    """

    is_managed: bool | None | Unset = UNSET
    manager_id: None | Unset | UUID = UNSET
    company_name: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTManagementModeActions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_managed: bool | None | Unset
        if isinstance(self.is_managed, Unset):
            is_managed = UNSET
        else:
            is_managed = self.is_managed

        manager_id: None | str | Unset
        if isinstance(self.manager_id, Unset):
            manager_id = UNSET
        elif isinstance(self.manager_id, UUID):
            manager_id = str(self.manager_id)
        else:
            manager_id = self.manager_id

        company_name = self.company_name

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_managed is not UNSET:
            field_dict["isManaged"] = is_managed
        if manager_id is not UNSET:
            field_dict["managerId"] = manager_id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_management_mode_actions import RESTManagementModeActions

        d = dict(src_dict)

        def _parse_is_managed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_managed = _parse_is_managed(d.pop("isManaged", UNSET))

        def _parse_manager_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                manager_id_type_0 = UUID(data)

                return manager_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        manager_id = _parse_manager_id(d.pop("managerId", UNSET))

        company_name = d.pop("companyName", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTManagementModeActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTManagementModeActions.from_dict(_field_actions)

        rest_management_mode = cls(
            is_managed=is_managed,
            manager_id=manager_id,
            company_name=company_name,
            field_links=field_links,
            field_actions=field_actions,
        )

        rest_management_mode.additional_properties = d
        return rest_management_mode

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
