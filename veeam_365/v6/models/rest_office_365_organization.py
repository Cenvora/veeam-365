from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_organization_region import RestOrganizationRegion
from ..models.rest_organization_type import RestOrganizationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_office_365_connection_settings_type_0 import RESTOffice365ConnectionSettingsType0
    from ..models.rest_office_365_organization_actions import RestOffice365OrganizationActions
    from ..models.rest_office_365_organization_links import RestOffice365OrganizationLinks


T = TypeVar("T", bound="RestOffice365Organization")


@_attrs_define
class RestOffice365Organization:
    """
    Attributes:
        is_teams_online (bool | None | Unset):
        is_teams_chats_online (bool | None | Unset):
        configure_application (bool | None | Unset):
        user_code (str | Unset):
        new_application_name (None | str | Unset):
        exchange_online_settings (None | RESTOffice365ConnectionSettingsType0 | Unset):
        share_point_online_settings (None | RESTOffice365ConnectionSettingsType0 | Unset):
        is_exchange_online (bool | None | Unset):
        is_share_point_online (bool | None | Unset):
        type_ (RestOrganizationType | Unset):
        region (RestOrganizationRegion | Unset):
        id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        name (str | Unset):
        office_name (str | Unset):
        is_backedup (bool | None | Unset):
        first_backuptime (datetime.datetime | None | Unset):
        last_backuptime (datetime.datetime | None | Unset):
        field_links (RestOffice365OrganizationLinks | Unset):
        field_actions (RestOffice365OrganizationActions | Unset):
    """

    is_teams_online: bool | None | Unset = UNSET
    is_teams_chats_online: bool | None | Unset = UNSET
    configure_application: bool | None | Unset = UNSET
    user_code: str | Unset = UNSET
    new_application_name: None | str | Unset = UNSET
    exchange_online_settings: None | RESTOffice365ConnectionSettingsType0 | Unset = UNSET
    share_point_online_settings: None | RESTOffice365ConnectionSettingsType0 | Unset = UNSET
    is_exchange_online: bool | None | Unset = UNSET
    is_share_point_online: bool | None | Unset = UNSET
    type_: RestOrganizationType | Unset = UNSET
    region: RestOrganizationRegion | Unset = UNSET
    id: None | Unset | UUID = UNSET
    name: str | Unset = UNSET
    office_name: str | Unset = UNSET
    is_backedup: bool | None | Unset = UNSET
    first_backuptime: datetime.datetime | None | Unset = UNSET
    last_backuptime: datetime.datetime | None | Unset = UNSET
    field_links: RestOffice365OrganizationLinks | Unset = UNSET
    field_actions: RestOffice365OrganizationActions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_office_365_connection_settings_type_0 import RESTOffice365ConnectionSettingsType0

        is_teams_online: bool | None | Unset
        if isinstance(self.is_teams_online, Unset):
            is_teams_online = UNSET
        else:
            is_teams_online = self.is_teams_online

        is_teams_chats_online: bool | None | Unset
        if isinstance(self.is_teams_chats_online, Unset):
            is_teams_chats_online = UNSET
        else:
            is_teams_chats_online = self.is_teams_chats_online

        configure_application: bool | None | Unset
        if isinstance(self.configure_application, Unset):
            configure_application = UNSET
        else:
            configure_application = self.configure_application

        user_code = self.user_code

        new_application_name: None | str | Unset
        if isinstance(self.new_application_name, Unset):
            new_application_name = UNSET
        else:
            new_application_name = self.new_application_name

        exchange_online_settings: dict[str, Any] | None | Unset
        if isinstance(self.exchange_online_settings, Unset):
            exchange_online_settings = UNSET
        elif isinstance(self.exchange_online_settings, RESTOffice365ConnectionSettingsType0):
            exchange_online_settings = self.exchange_online_settings.to_dict()
        else:
            exchange_online_settings = self.exchange_online_settings

        share_point_online_settings: dict[str, Any] | None | Unset
        if isinstance(self.share_point_online_settings, Unset):
            share_point_online_settings = UNSET
        elif isinstance(self.share_point_online_settings, RESTOffice365ConnectionSettingsType0):
            share_point_online_settings = self.share_point_online_settings.to_dict()
        else:
            share_point_online_settings = self.share_point_online_settings

        is_exchange_online: bool | None | Unset
        if isinstance(self.is_exchange_online, Unset):
            is_exchange_online = UNSET
        else:
            is_exchange_online = self.is_exchange_online

        is_share_point_online: bool | None | Unset
        if isinstance(self.is_share_point_online, Unset):
            is_share_point_online = UNSET
        else:
            is_share_point_online = self.is_share_point_online

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        region: str | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        name = self.name

        office_name = self.office_name

        is_backedup: bool | None | Unset
        if isinstance(self.is_backedup, Unset):
            is_backedup = UNSET
        else:
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

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_teams_online is not UNSET:
            field_dict["isTeamsOnline"] = is_teams_online
        if is_teams_chats_online is not UNSET:
            field_dict["isTeamsChatsOnline"] = is_teams_chats_online
        if configure_application is not UNSET:
            field_dict["configureApplication"] = configure_application
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if new_application_name is not UNSET:
            field_dict["newApplicationName"] = new_application_name
        if exchange_online_settings is not UNSET:
            field_dict["exchangeOnlineSettings"] = exchange_online_settings
        if share_point_online_settings is not UNSET:
            field_dict["sharePointOnlineSettings"] = share_point_online_settings
        if is_exchange_online is not UNSET:
            field_dict["isExchangeOnline"] = is_exchange_online
        if is_share_point_online is not UNSET:
            field_dict["isSharePointOnline"] = is_share_point_online
        if type_ is not UNSET:
            field_dict["type"] = type_
        if region is not UNSET:
            field_dict["region"] = region
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if office_name is not UNSET:
            field_dict["officeName"] = office_name
        if is_backedup is not UNSET:
            field_dict["isBackedup"] = is_backedup
        if first_backuptime is not UNSET:
            field_dict["firstBackuptime"] = first_backuptime
        if last_backuptime is not UNSET:
            field_dict["lastBackuptime"] = last_backuptime
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_office_365_connection_settings_type_0 import RESTOffice365ConnectionSettingsType0
        from ..models.rest_office_365_organization_actions import RestOffice365OrganizationActions
        from ..models.rest_office_365_organization_links import RestOffice365OrganizationLinks

        d = dict(src_dict)

        def _parse_is_teams_online(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_teams_online = _parse_is_teams_online(d.pop("isTeamsOnline", UNSET))

        def _parse_is_teams_chats_online(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_teams_chats_online = _parse_is_teams_chats_online(d.pop("isTeamsChatsOnline", UNSET))

        def _parse_configure_application(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        configure_application = _parse_configure_application(d.pop("configureApplication", UNSET))

        user_code = d.pop("userCode", UNSET)

        def _parse_new_application_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_application_name = _parse_new_application_name(d.pop("newApplicationName", UNSET))

        def _parse_exchange_online_settings(data: object) -> None | RESTOffice365ConnectionSettingsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_rest_office_365_connection_settings_type_0 = (
                    RESTOffice365ConnectionSettingsType0.from_dict(data)
                )

                return componentsschemas_rest_office_365_connection_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTOffice365ConnectionSettingsType0 | Unset, data)

        exchange_online_settings = _parse_exchange_online_settings(d.pop("exchangeOnlineSettings", UNSET))

        def _parse_share_point_online_settings(data: object) -> None | RESTOffice365ConnectionSettingsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_rest_office_365_connection_settings_type_0 = (
                    RESTOffice365ConnectionSettingsType0.from_dict(data)
                )

                return componentsschemas_rest_office_365_connection_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTOffice365ConnectionSettingsType0 | Unset, data)

        share_point_online_settings = _parse_share_point_online_settings(d.pop("sharePointOnlineSettings", UNSET))

        def _parse_is_exchange_online(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_exchange_online = _parse_is_exchange_online(d.pop("isExchangeOnline", UNSET))

        def _parse_is_share_point_online(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_share_point_online = _parse_is_share_point_online(d.pop("isSharePointOnline", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: RestOrganizationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestOrganizationType(_type_)

        _region = d.pop("region", UNSET)
        region: RestOrganizationRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = RestOrganizationRegion(_region)

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

        name = d.pop("name", UNSET)

        office_name = d.pop("officeName", UNSET)

        def _parse_is_backedup(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_backedup = _parse_is_backedup(d.pop("isBackedup", UNSET))

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

        _field_links = d.pop("_links", UNSET)
        field_links: RestOffice365OrganizationLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RestOffice365OrganizationLinks.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RestOffice365OrganizationActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RestOffice365OrganizationActions.from_dict(_field_actions)

        rest_office_365_organization = cls(
            is_teams_online=is_teams_online,
            is_teams_chats_online=is_teams_chats_online,
            configure_application=configure_application,
            user_code=user_code,
            new_application_name=new_application_name,
            exchange_online_settings=exchange_online_settings,
            share_point_online_settings=share_point_online_settings,
            is_exchange_online=is_exchange_online,
            is_share_point_online=is_share_point_online,
            type_=type_,
            region=region,
            id=id,
            name=name,
            office_name=office_name,
            is_backedup=is_backedup,
            first_backuptime=first_backuptime,
            last_backuptime=last_backuptime,
            field_links=field_links,
            field_actions=field_actions,
        )

        rest_office_365_organization.additional_properties = d
        return rest_office_365_organization

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
