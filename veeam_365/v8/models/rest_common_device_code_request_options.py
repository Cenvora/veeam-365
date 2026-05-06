from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_common_device_code_request_options_target_region import RESTCommonDeviceCodeRequestOptionsTargetRegion
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="RESTCommonDeviceCodeRequestOptions")



@_attrs_define
class RESTCommonDeviceCodeRequestOptions:
    """ 
        Attributes:
            target_region (RESTCommonDeviceCodeRequestOptionsTargetRegion | Unset): Specifies the region of the Microsoft
                365 organization that you plan to add.
            login_graph_app_organization_id (None | Unset | UUID): Specifies the identification number of the Microsoft 365
                organization in which Microsoft Graph API application you want to log in using the device code. For more
                information on how to get this parameter, see [Get Organizations](#/Organization/Organization_Get).
     """

    target_region: RESTCommonDeviceCodeRequestOptionsTargetRegion | Unset = UNSET
    login_graph_app_organization_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        target_region: str | Unset = UNSET
        if not isinstance(self.target_region, Unset):
            target_region = self.target_region.value


        login_graph_app_organization_id: None | str | Unset
        if isinstance(self.login_graph_app_organization_id, Unset):
            login_graph_app_organization_id = UNSET
        elif isinstance(self.login_graph_app_organization_id, UUID):
            login_graph_app_organization_id = str(self.login_graph_app_organization_id)
        else:
            login_graph_app_organization_id = self.login_graph_app_organization_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if target_region is not UNSET:
            field_dict["targetRegion"] = target_region
        if login_graph_app_organization_id is not UNSET:
            field_dict["loginGraphAppOrganizationId"] = login_graph_app_organization_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _target_region = d.pop("targetRegion", UNSET)
        target_region: RESTCommonDeviceCodeRequestOptionsTargetRegion | Unset
        if isinstance(_target_region,  Unset):
            target_region = UNSET
        else:
            target_region = RESTCommonDeviceCodeRequestOptionsTargetRegion(_target_region)




        def _parse_login_graph_app_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                login_graph_app_organization_id_type_0 = UUID(data)



                return login_graph_app_organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        login_graph_app_organization_id = _parse_login_graph_app_organization_id(d.pop("loginGraphAppOrganizationId", UNSET))


        rest_common_device_code_request_options = cls(
            target_region=target_region,
            login_graph_app_organization_id=login_graph_app_organization_id,
        )


        rest_common_device_code_request_options.additional_properties = d
        return rest_common_device_code_request_options

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
