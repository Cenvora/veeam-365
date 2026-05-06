from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_restore_session_event_status import RESTRestoreSessionEventStatus
from ..models.rest_restore_session_event_type import RESTRestoreSessionEventType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary





T = TypeVar("T", bound="RESTRestoreSessionEvent")



@_attrs_define
class RESTRestoreSessionEvent:
    """ 
        Attributes:
            id (UUID): ID of the restore session event. Example: 00000000-0000-0000-0000-000000000000.
            status (RESTRestoreSessionEventStatus): Status of the restore session.
            start_time (datetime.datetime): Date and time when the restore session event was started.
            message (str): Message of the restore session event.
            order (int): Order number of the restore session event.
            item_name (str | Unset): Name of the restored item.
            item_type (str | Unset): Type of the restored item.
            item_size_bytes (int | Unset): Size of the restored item in *Bytes*.
            source (str | Unset): Source path of the restored item.
            target (str | Unset): Target path to the restored item.
            type_ (RESTRestoreSessionEventType | Unset): Type of the restore session event.
            end_time (datetime.datetime | None | Unset): Date and time when the restore session event ended.
            duration (str | Unset): Duration of the restore session.
            title (str | Unset): Title of the restore session event.
            organization_id (None | Unset | UUID): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
            backed_up_organization_id (None | str | Unset): ID of the backed-up organization in the backup.
            user_id (None | str | Unset): ID of the backed-up organization user.
            group_id (None | str | Unset): ID of the backed-up organization group.
            site_id (None | str | Unset): ID of the backed-up organization site.
            team_id (None | Unset | UUID): ID of the backed-up team. Example: 00000000-0000-0000-0000-000000000000.
            field_links (RESTLinkHALDictionary | Unset): Related resources.
     """

    id: UUID
    status: RESTRestoreSessionEventStatus
    start_time: datetime.datetime
    message: str
    order: int
    item_name: str | Unset = UNSET
    item_type: str | Unset = UNSET
    item_size_bytes: int | Unset = UNSET
    source: str | Unset = UNSET
    target: str | Unset = UNSET
    type_: RESTRestoreSessionEventType | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    duration: str | Unset = UNSET
    title: str | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    backed_up_organization_id: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    group_id: None | str | Unset = UNSET
    site_id: None | str | Unset = UNSET
    team_id: None | Unset | UUID = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        id = str(self.id)

        status = self.status.value

        start_time = self.start_time.isoformat()

        message = self.message

        order = self.order

        item_name = self.item_name

        item_type = self.item_type

        item_size_bytes = self.item_size_bytes

        source = self.source

        target = self.target

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        duration = self.duration

        title = self.title

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        backed_up_organization_id: None | str | Unset
        if isinstance(self.backed_up_organization_id, Unset):
            backed_up_organization_id = UNSET
        else:
            backed_up_organization_id = self.backed_up_organization_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        site_id: None | str | Unset
        if isinstance(self.site_id, Unset):
            site_id = UNSET
        else:
            site_id = self.site_id

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        elif isinstance(self.team_id, UUID):
            team_id = str(self.team_id)
        else:
            team_id = self.team_id

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "status": status,
            "startTime": start_time,
            "message": message,
            "order": order,
        })
        if item_name is not UNSET:
            field_dict["itemName"] = item_name
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if item_size_bytes is not UNSET:
            field_dict["itemSizeBytes"] = item_size_bytes
        if source is not UNSET:
            field_dict["source"] = source
        if target is not UNSET:
            field_dict["target"] = target
        if type_ is not UNSET:
            field_dict["type"] = type_
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if title is not UNSET:
            field_dict["title"] = title
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if backed_up_organization_id is not UNSET:
            field_dict["backedUpOrganizationId"] = backed_up_organization_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        status = RESTRestoreSessionEventStatus(d.pop("status"))




        start_time = isoparse(d.pop("startTime"))




        message = d.pop("message")

        order = d.pop("order")

        item_name = d.pop("itemName", UNSET)

        item_type = d.pop("itemType", UNSET)

        item_size_bytes = d.pop("itemSizeBytes", UNSET)

        source = d.pop("source", UNSET)

        target = d.pop("target", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTRestoreSessionEventType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RESTRestoreSessionEventType(_type_)




        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)



                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))


        duration = d.pop("duration", UNSET)

        title = d.pop("title", UNSET)

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)



                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organizationId", UNSET))


        def _parse_backed_up_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backed_up_organization_id = _parse_backed_up_organization_id(d.pop("backedUpOrganizationId", UNSET))


        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))


        def _parse_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))


        def _parse_site_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_id = _parse_site_id(d.pop("siteId", UNSET))


        def _parse_team_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                team_id_type_0 = UUID(data)



                return team_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        team_id = _parse_team_id(d.pop("teamId", UNSET))


        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links,  Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)




        rest_restore_session_event = cls(
            id=id,
            status=status,
            start_time=start_time,
            message=message,
            order=order,
            item_name=item_name,
            item_type=item_type,
            item_size_bytes=item_size_bytes,
            source=source,
            target=target,
            type_=type_,
            end_time=end_time,
            duration=duration,
            title=title,
            organization_id=organization_id,
            backed_up_organization_id=backed_up_organization_id,
            user_id=user_id,
            group_id=group_id,
            site_id=site_id,
            team_id=team_id,
            field_links=field_links,
        )


        rest_restore_session_event.additional_properties = d
        return rest_restore_session_event

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
