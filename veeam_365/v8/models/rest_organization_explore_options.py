from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_organization_explore_options_type import RESTOrganizationExploreOptionsType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="RESTOrganizationExploreOptions")



@_attrs_define
class RESTOrganizationExploreOptions:
    """ 
        Attributes:
            date_time (datetime.datetime | None | Unset): Specifies the date and time.
            type_ (RESTOrganizationExploreOptionsType | Unset): Specifies a type of the restore session to start.
            show_deleted (bool | None | Unset): Defines whether the restore session will show items that have been removed
                by the user before the specified date.
            show_all_versions (bool | None | Unset): Defines whether the restore session will show all versions of items
                that have been modified by the user before the specified date.
            repository_id (None | Unset | UUID): Specifies the identification number of the backup repository. For more
                information on how to get this parameter, see [Get Backup
                Repositories](#/BackupRepository/BackupRepository_GetRepositories).
     """

    date_time: datetime.datetime | None | Unset = UNSET
    type_: RESTOrganizationExploreOptionsType | Unset = UNSET
    show_deleted: bool | None | Unset = UNSET
    show_all_versions: bool | None | Unset = UNSET
    repository_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        date_time: None | str | Unset
        if isinstance(self.date_time, Unset):
            date_time = UNSET
        elif isinstance(self.date_time, datetime.datetime):
            date_time = self.date_time.isoformat()
        else:
            date_time = self.date_time

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        show_deleted: bool | None | Unset
        if isinstance(self.show_deleted, Unset):
            show_deleted = UNSET
        else:
            show_deleted = self.show_deleted

        show_all_versions: bool | None | Unset
        if isinstance(self.show_all_versions, Unset):
            show_all_versions = UNSET
        else:
            show_all_versions = self.show_all_versions

        repository_id: None | str | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        elif isinstance(self.repository_id, UUID):
            repository_id = str(self.repository_id)
        else:
            repository_id = self.repository_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if type_ is not UNSET:
            field_dict["type"] = type_
        if show_deleted is not UNSET:
            field_dict["showDeleted"] = show_deleted
        if show_all_versions is not UNSET:
            field_dict["showAllVersions"] = show_all_versions
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_date_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_time_type_0 = isoparse(data)



                return date_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_time = _parse_date_time(d.pop("dateTime", UNSET))


        _type_ = d.pop("type", UNSET)
        type_: RESTOrganizationExploreOptionsType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RESTOrganizationExploreOptionsType(_type_)




        def _parse_show_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_deleted = _parse_show_deleted(d.pop("showDeleted", UNSET))


        def _parse_show_all_versions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_all_versions = _parse_show_all_versions(d.pop("showAllVersions", UNSET))


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


        rest_organization_explore_options = cls(
            date_time=date_time,
            type_=type_,
            show_deleted=show_deleted,
            show_all_versions=show_all_versions,
            repository_id=repository_id,
        )


        rest_organization_explore_options.additional_properties = d
        return rest_organization_explore_options

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
