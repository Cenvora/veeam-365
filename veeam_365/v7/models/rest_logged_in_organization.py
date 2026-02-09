from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_logged_in_organization_type import RESTLoggedInOrganizationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_logged_in_organization_actions import RESTLoggedInOrganizationActions


T = TypeVar("T", bound="RESTLoggedInOrganization")


@_attrs_define
class RESTLoggedInOrganization:
    """
    Attributes:
        id (str | Unset): ID of the organization added to Veeam Backup for Microsoft 365.
        name (str | Unset): Name of the Microsoft organization.
        description (None | str | Unset): Description of the Microsoft organization.
        type_ (RESTLoggedInOrganizationType | Unset): Type of the organization.
        is_backedup (bool | Unset): Defines whether the organizations was backed up.
        first_backuptime (datetime.datetime | None | Unset): Date and time when the first backup was created for the
            organization.
        last_backuptime (datetime.datetime | None | Unset): Date and time when the last backup was created for the
            organization.
        field_actions (RESTLoggedInOrganizationActions | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    type_: RESTLoggedInOrganizationType | Unset = UNSET
    is_backedup: bool | Unset = UNSET
    first_backuptime: datetime.datetime | None | Unset = UNSET
    last_backuptime: datetime.datetime | None | Unset = UNSET
    field_actions: RESTLoggedInOrganizationActions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        is_backedup = self.is_backedup

        first_backuptime: None | str | Unset
        if isinstance(self.first_backuptime, Unset):
            first_backuptime = UNSET
        elif isinstance(self.first_backuptime, datetime.datetime):
            first_backuptime = self.first_backuptime.isoformat()
        else:
            first_backuptime = self.first_backuptime

        last_backuptime: None | str | Unset
        if isinstance(self.last_backuptime, Unset):
            last_backuptime = UNSET
        elif isinstance(self.last_backuptime, datetime.datetime):
            last_backuptime = self.last_backuptime.isoformat()
        else:
            last_backuptime = self.last_backuptime

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_backedup is not UNSET:
            field_dict["isBackedup"] = is_backedup
        if first_backuptime is not UNSET:
            field_dict["firstBackuptime"] = first_backuptime
        if last_backuptime is not UNSET:
            field_dict["lastBackuptime"] = last_backuptime
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_logged_in_organization_actions import RESTLoggedInOrganizationActions

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: RESTLoggedInOrganizationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTLoggedInOrganizationType(_type_)

        is_backedup = d.pop("isBackedup", UNSET)

        def _parse_first_backuptime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_backuptime_type_0 = isoparse(data)

                return first_backuptime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_backuptime = _parse_first_backuptime(d.pop("firstBackuptime", UNSET))

        def _parse_last_backuptime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backuptime_type_0 = isoparse(data)

                return last_backuptime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_backuptime = _parse_last_backuptime(d.pop("lastBackuptime", UNSET))

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTLoggedInOrganizationActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTLoggedInOrganizationActions.from_dict(_field_actions)

        rest_logged_in_organization = cls(
            id=id,
            name=name,
            description=description,
            type_=type_,
            is_backedup=is_backedup,
            first_backuptime=first_backuptime,
            last_backuptime=last_backuptime,
            field_actions=field_actions,
        )

        rest_logged_in_organization.additional_properties = d
        return rest_logged_in_organization

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
