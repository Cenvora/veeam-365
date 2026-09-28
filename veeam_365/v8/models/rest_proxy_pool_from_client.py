from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.rest_proxy_id_from_client import RESTProxyIdFromClient


T = TypeVar("T", bound="RESTProxyPoolFromClient")


@_attrs_define
class RESTProxyPoolFromClient:
    """
    Attributes:
        name (str): Specifies the backup proxy pool name.
        description (str): Specifies the backup proxy pool description.
        proxy_ids (list[RESTProxyIdFromClient]): Specifies IDs of the backup proxy servers to add to the new backup
            proxy pool. For more information on how to get such IDs, see [Get Backup Proxy
            Servers](Proxy#operation/Proxy_GetProxies).
    """

    name: str
    description: str
    proxy_ids: list[RESTProxyIdFromClient]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        proxy_ids = []
        for proxy_ids_item_data in self.proxy_ids:
            proxy_ids_item = proxy_ids_item_data.to_dict()
            proxy_ids.append(proxy_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "proxyIds": proxy_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_proxy_id_from_client import RESTProxyIdFromClient

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        proxy_ids = []
        _proxy_ids = d.pop("proxyIds")
        for proxy_ids_item_data in _proxy_ids:
            proxy_ids_item = RESTProxyIdFromClient.from_dict(proxy_ids_item_data)

            proxy_ids.append(proxy_ids_item)

        rest_proxy_pool_from_client = cls(
            name=name,
            description=description,
            proxy_ids=proxy_ids,
        )

        rest_proxy_pool_from_client.additional_properties = d
        return rest_proxy_pool_from_client

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
