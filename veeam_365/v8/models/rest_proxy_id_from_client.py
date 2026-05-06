from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="RESTProxyIdFromClient")



@_attrs_define
class RESTProxyIdFromClient:
    """ 
        Attributes:
            proxy_id (UUID | Unset): Specifies IDs of the backup proxy servers that you want to add to the backup proxy pool
                or remove from the backup proxy pool. For more information on how to get such IDs, see [Get Backup Proxy
                Servers](#/Proxy/Proxy_GetProxies). Example: 00000000-0000-0000-0000-000000000000.
     """

    proxy_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        proxy_id: str | Unset = UNSET
        if not isinstance(self.proxy_id, Unset):
            proxy_id = str(self.proxy_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if proxy_id is not UNSET:
            field_dict["proxyId"] = proxy_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _proxy_id = d.pop("proxyId", UNSET)
        proxy_id: UUID | Unset
        if isinstance(_proxy_id,  Unset):
            proxy_id = UNSET
        else:
            proxy_id = UUID(_proxy_id)




        rest_proxy_id_from_client = cls(
            proxy_id=proxy_id,
        )


        rest_proxy_id_from_client.additional_properties = d
        return rest_proxy_id_from_client

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
