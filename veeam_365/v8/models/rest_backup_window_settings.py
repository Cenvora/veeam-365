from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RESTBackupWindowSettings")



@_attrs_define
class RESTBackupWindowSettings:
    """ 
        Attributes:
            backup_window (list[bool] | Unset): Defines an hourly scheme for the backup window. The scheduling scheme
                consists of 168 boolean elements. These elements can be logically divided into 7 groups by 24. Each group
                represents a day of the week starting from Sunday. Each element represents a backup hour: <ul> <li>*true* - the
                allowed backup hour</li> <li>*false* - the prohibited backup hour</li> </ul>
            minute_offset (int | None | Unset): Current minute offset from the UTC time.
     """

    backup_window: list[bool] | Unset = UNSET
    minute_offset: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        backup_window: list[bool] | Unset = UNSET
        if not isinstance(self.backup_window, Unset):
            backup_window = self.backup_window



        minute_offset: int | None | Unset
        if isinstance(self.minute_offset, Unset):
            minute_offset = UNSET
        else:
            minute_offset = self.minute_offset


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if backup_window is not UNSET:
            field_dict["backupWindow"] = backup_window
        if minute_offset is not UNSET:
            field_dict["minuteOffset"] = minute_offset

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_window = cast(list[bool], d.pop("backupWindow", UNSET))


        def _parse_minute_offset(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        minute_offset = _parse_minute_offset(d.pop("minuteOffset", UNSET))


        rest_backup_window_settings = cls(
            backup_window=backup_window,
            minute_offset=minute_offset,
        )


        rest_backup_window_settings.additional_properties = d
        return rest_backup_window_settings

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
