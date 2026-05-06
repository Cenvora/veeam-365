from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_office_license_detected_sku_type import RESTOfficeLicenseDetectedSkuType
from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="RESTOfficeLicense")



@_attrs_define
class RESTOfficeLicense:
    """ 
        Attributes:
            sku_id (UUID | Unset): Unique ID of the service SKU. Example: 00000000-0000-0000-0000-000000000000.
            sku_part_number (str | Unset): Unique display name of the service SKU. Example:
                00000000-0000-0000-0000-000000000000.
            detected_sku_type (RESTOfficeLicenseDetectedSkuType | Unset): Type of the service SKU.
     """

    sku_id: UUID | Unset = UNSET
    sku_part_number: str | Unset = UNSET
    detected_sku_type: RESTOfficeLicenseDetectedSkuType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        sku_id: str | Unset = UNSET
        if not isinstance(self.sku_id, Unset):
            sku_id = str(self.sku_id)

        sku_part_number = self.sku_part_number

        detected_sku_type: str | Unset = UNSET
        if not isinstance(self.detected_sku_type, Unset):
            detected_sku_type = self.detected_sku_type.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sku_id is not UNSET:
            field_dict["skuId"] = sku_id
        if sku_part_number is not UNSET:
            field_dict["skuPartNumber"] = sku_part_number
        if detected_sku_type is not UNSET:
            field_dict["detectedSkuType"] = detected_sku_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _sku_id = d.pop("skuId", UNSET)
        sku_id: UUID | Unset
        if isinstance(_sku_id,  Unset):
            sku_id = UNSET
        else:
            sku_id = UUID(_sku_id)




        sku_part_number = d.pop("skuPartNumber", UNSET)

        _detected_sku_type = d.pop("detectedSkuType", UNSET)
        detected_sku_type: RESTOfficeLicenseDetectedSkuType | Unset
        if isinstance(_detected_sku_type,  Unset):
            detected_sku_type = UNSET
        else:
            detected_sku_type = RESTOfficeLicenseDetectedSkuType(_detected_sku_type)




        rest_office_license = cls(
            sku_id=sku_id,
            sku_part_number=sku_part_number,
            detected_sku_type=detected_sku_type,
        )


        rest_office_license.additional_properties = d
        return rest_office_license

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
