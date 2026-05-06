from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_organization_type import RestOrganizationType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.rest_exchange_settings import RESTExchangeSettings
  from ..models.rest_on_premises_organization_actions import RestOnPremisesOrganizationActions
  from ..models.rest_on_premises_organization_links import RestOnPremisesOrganizationLinks
  from ..models.rest_sharepoint_settings import RESTSharepointSettings





T = TypeVar("T", bound="RestOnPremisesOrganization")



@_attrs_define
class RestOnPremisesOrganization:
    """ 
        Attributes:
            type_ (RestOrganizationType | Unset): Specifies the organization type.
            is_sharepoint (bool | None | Unset): Defines whether to add an on-premises SharePoint organization.
            sharepoint_settings (RESTSharepointSettings | Unset):
            is_exchange (bool | None | Unset): Defines whether to add an on-premises Exchange organization.
            exchange_settings (RESTExchangeSettings | Unset):
            id (None | Unset | UUID): Specifies the identification number of the Microsoft 365 organization added to Veeam
                Backup for Microsoft 365. Example: 00000000-0000-0000-0000-000000000000.
            name (str | Unset): Specifies the name of the on-premises organization.
            office_name (str | Unset): Specifies the Microsoft 365 Online name.
            description (None | str | Unset): Specifies the on-premises organization description.
            is_backedup (bool | None | Unset): Defines whether the organizations was backed up.
            first_backuptime (datetime.datetime | None | Unset): Specifies the date and time when the first backup was
                created for the organization.
            last_backuptime (datetime.datetime | None | Unset): Specifies the date and time when the last backup was created
                for the organization.
            backed_up_organization_id (None | str | Unset): Specifies the identification number of the backed-up
                organization in the backup.
            field_links (RestOnPremisesOrganizationLinks | Unset):
            field_actions (RestOnPremisesOrganizationActions | Unset):
     """

    type_: RestOrganizationType | Unset = UNSET
    is_sharepoint: bool | None | Unset = UNSET
    sharepoint_settings: RESTSharepointSettings | Unset = UNSET
    is_exchange: bool | None | Unset = UNSET
    exchange_settings: RESTExchangeSettings | Unset = UNSET
    id: None | Unset | UUID = UNSET
    name: str | Unset = UNSET
    office_name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_backedup: bool | None | Unset = UNSET
    first_backuptime: datetime.datetime | None | Unset = UNSET
    last_backuptime: datetime.datetime | None | Unset = UNSET
    backed_up_organization_id: None | str | Unset = UNSET
    field_links: RestOnPremisesOrganizationLinks | Unset = UNSET
    field_actions: RestOnPremisesOrganizationActions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_exchange_settings import RESTExchangeSettings
        from ..models.rest_on_premises_organization_actions import RestOnPremisesOrganizationActions
        from ..models.rest_on_premises_organization_links import RestOnPremisesOrganizationLinks
        from ..models.rest_sharepoint_settings import RESTSharepointSettings
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        is_sharepoint: bool | None | Unset
        if isinstance(self.is_sharepoint, Unset):
            is_sharepoint = UNSET
        else:
            is_sharepoint = self.is_sharepoint

        sharepoint_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sharepoint_settings, Unset):
            sharepoint_settings = self.sharepoint_settings.to_dict()

        is_exchange: bool | None | Unset
        if isinstance(self.is_exchange, Unset):
            is_exchange = UNSET
        else:
            is_exchange = self.is_exchange

        exchange_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exchange_settings, Unset):
            exchange_settings = self.exchange_settings.to_dict()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        name = self.name

        office_name = self.office_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        backed_up_organization_id: None | str | Unset
        if isinstance(self.backed_up_organization_id, Unset):
            backed_up_organization_id = UNSET
        else:
            backed_up_organization_id = self.backed_up_organization_id

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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_sharepoint is not UNSET:
            field_dict["isSharepoint"] = is_sharepoint
        if sharepoint_settings is not UNSET:
            field_dict["sharepointSettings"] = sharepoint_settings
        if is_exchange is not UNSET:
            field_dict["isExchange"] = is_exchange
        if exchange_settings is not UNSET:
            field_dict["exchangeSettings"] = exchange_settings
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if office_name is not UNSET:
            field_dict["officeName"] = office_name
        if description is not UNSET:
            field_dict["description"] = description
        if is_backedup is not UNSET:
            field_dict["isBackedup"] = is_backedup
        if first_backuptime is not UNSET:
            field_dict["firstBackuptime"] = first_backuptime
        if last_backuptime is not UNSET:
            field_dict["lastBackuptime"] = last_backuptime
        if backed_up_organization_id is not UNSET:
            field_dict["backedUpOrganizationId"] = backed_up_organization_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_exchange_settings import RESTExchangeSettings
        from ..models.rest_on_premises_organization_actions import RestOnPremisesOrganizationActions
        from ..models.rest_on_premises_organization_links import RestOnPremisesOrganizationLinks
        from ..models.rest_sharepoint_settings import RESTSharepointSettings
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RestOrganizationType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RestOrganizationType(_type_)




        def _parse_is_sharepoint(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_sharepoint = _parse_is_sharepoint(d.pop("isSharepoint", UNSET))


        _sharepoint_settings = d.pop("sharepointSettings", UNSET)
        sharepoint_settings: RESTSharepointSettings | Unset
        if isinstance(_sharepoint_settings,  Unset):
            sharepoint_settings = UNSET
        else:
            sharepoint_settings = RESTSharepointSettings.from_dict(_sharepoint_settings)




        def _parse_is_exchange(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_exchange = _parse_is_exchange(d.pop("isExchange", UNSET))


        _exchange_settings = d.pop("exchangeSettings", UNSET)
        exchange_settings: RESTExchangeSettings | Unset
        if isinstance(_exchange_settings,  Unset):
            exchange_settings = UNSET
        else:
            exchange_settings = RESTExchangeSettings.from_dict(_exchange_settings)




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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


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


        def _parse_backed_up_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backed_up_organization_id = _parse_backed_up_organization_id(d.pop("backedUpOrganizationId", UNSET))


        _field_links = d.pop("_links", UNSET)
        field_links: RestOnPremisesOrganizationLinks | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RestOnPremisesOrganizationLinks.from_dict(_field_links)




        _field_actions = d.pop("_actions", UNSET)
        field_actions: RestOnPremisesOrganizationActions | Unset
        if isinstance(_field_actions,  Unset):
            field_actions = UNSET
        else:
            field_actions = RestOnPremisesOrganizationActions.from_dict(_field_actions)




        rest_on_premises_organization = cls(
            type_=type_,
            is_sharepoint=is_sharepoint,
            sharepoint_settings=sharepoint_settings,
            is_exchange=is_exchange,
            exchange_settings=exchange_settings,
            id=id,
            name=name,
            office_name=office_name,
            description=description,
            is_backedup=is_backedup,
            first_backuptime=first_backuptime,
            last_backuptime=last_backuptime,
            backed_up_organization_id=backed_up_organization_id,
            field_links=field_links,
            field_actions=field_actions,
        )


        rest_on_premises_organization.additional_properties = d
        return rest_on_premises_organization

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
