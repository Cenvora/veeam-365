from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_automatic_update_settings import RESTAutomaticUpdateSettings





T = TypeVar("T", bound="RESTUpdateProductConfig")



@_attrs_define
class RESTUpdateProductConfig:
    """ 
        Attributes:
            enable_check_for_updates (bool): Defines whether to check and notify on available updates automatically.
            update_settings (RESTAutomaticUpdateSettings | Unset):
     """

    enable_check_for_updates: bool
    update_settings: RESTAutomaticUpdateSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_automatic_update_settings import RESTAutomaticUpdateSettings
        enable_check_for_updates = self.enable_check_for_updates

        update_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_settings, Unset):
            update_settings = self.update_settings.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "enableCheckForUpdates": enable_check_for_updates,
        })
        if update_settings is not UNSET:
            field_dict["updateSettings"] = update_settings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_automatic_update_settings import RESTAutomaticUpdateSettings
        d = dict(src_dict)
        enable_check_for_updates = d.pop("enableCheckForUpdates")

        _update_settings = d.pop("updateSettings", UNSET)
        update_settings: RESTAutomaticUpdateSettings | Unset
        if isinstance(_update_settings,  Unset):
            update_settings = UNSET
        else:
            update_settings = RESTAutomaticUpdateSettings.from_dict(_update_settings)




        rest_update_product_config = cls(
            enable_check_for_updates=enable_check_for_updates,
            update_settings=update_settings,
        )


        rest_update_product_config.additional_properties = d
        return rest_update_product_config

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
