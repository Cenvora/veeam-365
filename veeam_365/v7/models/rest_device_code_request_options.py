from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_device_code_request_options_target_region import RESTDeviceCodeRequestOptionsTargetRegion
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTDeviceCodeRequestOptions")


@_attrs_define
class RESTDeviceCodeRequestOptions:
    """
    Attributes:
        target_application_id (None | Unset | UUID): Specifies the ID of the Azure AD application that you want to use
            for data restore. Example: 00000000-0000-0000-0000-000000000000.
        target_region (RESTDeviceCodeRequestOptionsTargetRegion | Unset): Specifies a region of the Microsoft 365
            organization that contains data you want to restore.

            **Note**: This property is only required when planning to restore to a custom location.
        target_organization_name (str | Unset): Specifies a name of the Microsoft 365 organization to which you want to
            restore data.

            **Note**: This property is only required when planning to restore to a custom location.
    """

    target_application_id: None | Unset | UUID = UNSET
    target_region: RESTDeviceCodeRequestOptionsTargetRegion | Unset = UNSET
    target_organization_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_application_id: None | str | Unset
        if isinstance(self.target_application_id, Unset):
            target_application_id = UNSET
        elif isinstance(self.target_application_id, UUID):
            target_application_id = str(self.target_application_id)
        else:
            target_application_id = self.target_application_id

        target_region: str | Unset = UNSET
        if not isinstance(self.target_region, Unset):
            target_region = self.target_region.value

        target_organization_name = self.target_organization_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_application_id is not UNSET:
            field_dict["targetApplicationId"] = target_application_id
        if target_region is not UNSET:
            field_dict["targetRegion"] = target_region
        if target_organization_name is not UNSET:
            field_dict["targetOrganizationName"] = target_organization_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_target_application_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_application_id_type_0 = UUID(data)

                return target_application_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        target_application_id = _parse_target_application_id(d.pop("targetApplicationId", UNSET))

        _target_region = d.pop("targetRegion", UNSET)
        target_region: RESTDeviceCodeRequestOptionsTargetRegion | Unset
        if isinstance(_target_region, Unset):
            target_region = UNSET
        else:
            target_region = RESTDeviceCodeRequestOptionsTargetRegion(_target_region)

        target_organization_name = d.pop("targetOrganizationName", UNSET)

        rest_device_code_request_options = cls(
            target_application_id=target_application_id,
            target_region=target_region,
            target_organization_name=target_organization_name,
        )

        rest_device_code_request_options.additional_properties = d
        return rest_device_code_request_options

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
