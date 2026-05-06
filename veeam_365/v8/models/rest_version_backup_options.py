from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_version_backup_options_share_point_backup_mode import RESTVersionBackupOptionsSharePointBackupMode
from ..types import UNSET, Unset






T = TypeVar("T", bound="RESTVersionBackupOptions")



@_attrs_define
class RESTVersionBackupOptions:
    """ 
        Attributes:
            share_point_backup_mode (RESTVersionBackupOptionsSharePointBackupMode | Unset): Version backup mode used for the
                SharePoint backup.
     """

    share_point_backup_mode: RESTVersionBackupOptionsSharePointBackupMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        share_point_backup_mode: str | Unset = UNSET
        if not isinstance(self.share_point_backup_mode, Unset):
            share_point_backup_mode = self.share_point_backup_mode.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if share_point_backup_mode is not UNSET:
            field_dict["sharePointBackupMode"] = share_point_backup_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _share_point_backup_mode = d.pop("sharePointBackupMode", UNSET)
        share_point_backup_mode: RESTVersionBackupOptionsSharePointBackupMode | Unset
        if isinstance(_share_point_backup_mode,  Unset):
            share_point_backup_mode = UNSET
        else:
            share_point_backup_mode = RESTVersionBackupOptionsSharePointBackupMode(_share_point_backup_mode)




        rest_version_backup_options = cls(
            share_point_backup_mode=share_point_backup_mode,
        )


        rest_version_backup_options.additional_properties = d
        return rest_version_backup_options

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
