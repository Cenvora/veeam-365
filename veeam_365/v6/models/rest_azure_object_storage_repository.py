from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_object_storage_type import RESTObjectStorageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_azure_archiver_appliance import RESTAzureArchiverAppliance
    from ..models.rest_azure_container import RESTAzureContainer
    from ..models.rest_azure_object_storage_repository_links import RESTAzureObjectStorageRepositoryLinks
    from ..models.rest_azure_subscription import RESTAzureSubscription
    from ..models.rest_service_account_info import RESTServiceAccountInfo


T = TypeVar("T", bound="RESTAzureObjectStorageRepository")


@_attrs_define
class RESTAzureObjectStorageRepository:
    """
    Attributes:
        azure_container (RESTAzureContainer | Unset):
        azure_folder (str | Unset):
        id (UUID | Unset):  Example: 00000000-0000-0000-0000-000000000000.
        name (str | Unset):
        description (str | Unset):
        account_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        size_limit_enabled (bool | None | Unset):
        size_limit_gb (int | None | Unset):
        used_space_bytes (int | None | Unset):
        free_space_bytes (int | None | Unset):
        type_ (RESTObjectStorageType | Unset):
        use_archiver_appliance (bool | None | Unset):
        azure_service_account (RESTServiceAccountInfo | Unset):
        azure_subscription (RESTAzureSubscription | Unset):
        azure_archiver_appliance (RESTAzureArchiverAppliance | Unset):
        field_links (RESTAzureObjectStorageRepositoryLinks | Unset):
    """

    azure_container: RESTAzureContainer | Unset = UNSET
    azure_folder: str | Unset = UNSET
    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    account_id: None | Unset | UUID = UNSET
    size_limit_enabled: bool | None | Unset = UNSET
    size_limit_gb: int | None | Unset = UNSET
    used_space_bytes: int | None | Unset = UNSET
    free_space_bytes: int | None | Unset = UNSET
    type_: RESTObjectStorageType | Unset = UNSET
    use_archiver_appliance: bool | None | Unset = UNSET
    azure_service_account: RESTServiceAccountInfo | Unset = UNSET
    azure_subscription: RESTAzureSubscription | Unset = UNSET
    azure_archiver_appliance: RESTAzureArchiverAppliance | Unset = UNSET
    field_links: RESTAzureObjectStorageRepositoryLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        azure_container: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_container, Unset):
            azure_container = self.azure_container.to_dict()

        azure_folder = self.azure_folder

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        description = self.description

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        elif isinstance(self.account_id, UUID):
            account_id = str(self.account_id)
        else:
            account_id = self.account_id

        size_limit_enabled: bool | None | Unset
        if isinstance(self.size_limit_enabled, Unset):
            size_limit_enabled = UNSET
        else:
            size_limit_enabled = self.size_limit_enabled

        size_limit_gb: int | None | Unset
        if isinstance(self.size_limit_gb, Unset):
            size_limit_gb = UNSET
        else:
            size_limit_gb = self.size_limit_gb

        used_space_bytes: int | None | Unset
        if isinstance(self.used_space_bytes, Unset):
            used_space_bytes = UNSET
        else:
            used_space_bytes = self.used_space_bytes

        free_space_bytes: int | None | Unset
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        use_archiver_appliance: bool | None | Unset
        if isinstance(self.use_archiver_appliance, Unset):
            use_archiver_appliance = UNSET
        else:
            use_archiver_appliance = self.use_archiver_appliance

        azure_service_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_service_account, Unset):
            azure_service_account = self.azure_service_account.to_dict()

        azure_subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_subscription, Unset):
            azure_subscription = self.azure_subscription.to_dict()

        azure_archiver_appliance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_archiver_appliance, Unset):
            azure_archiver_appliance = self.azure_archiver_appliance.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if azure_container is not UNSET:
            field_dict["azureContainer"] = azure_container
        if azure_folder is not UNSET:
            field_dict["azureFolder"] = azure_folder
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if size_limit_enabled is not UNSET:
            field_dict["sizeLimitEnabled"] = size_limit_enabled
        if size_limit_gb is not UNSET:
            field_dict["sizeLimitGB"] = size_limit_gb
        if used_space_bytes is not UNSET:
            field_dict["usedSpaceBytes"] = used_space_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if type_ is not UNSET:
            field_dict["type"] = type_
        if use_archiver_appliance is not UNSET:
            field_dict["useArchiverAppliance"] = use_archiver_appliance
        if azure_service_account is not UNSET:
            field_dict["azureServiceAccount"] = azure_service_account
        if azure_subscription is not UNSET:
            field_dict["azureSubscription"] = azure_subscription
        if azure_archiver_appliance is not UNSET:
            field_dict["azureArchiverAppliance"] = azure_archiver_appliance
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_azure_archiver_appliance import RESTAzureArchiverAppliance
        from ..models.rest_azure_container import RESTAzureContainer
        from ..models.rest_azure_object_storage_repository_links import RESTAzureObjectStorageRepositoryLinks
        from ..models.rest_azure_subscription import RESTAzureSubscription
        from ..models.rest_service_account_info import RESTServiceAccountInfo

        d = dict(src_dict)
        _azure_container = d.pop("azureContainer", UNSET)
        azure_container: RESTAzureContainer | Unset
        if isinstance(_azure_container, Unset):
            azure_container = UNSET
        else:
            azure_container = RESTAzureContainer.from_dict(_azure_container)

        azure_folder = d.pop("azureFolder", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                account_id_type_0 = UUID(data)

                return account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))

        def _parse_size_limit_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        size_limit_enabled = _parse_size_limit_enabled(d.pop("sizeLimitEnabled", UNSET))

        def _parse_size_limit_gb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_limit_gb = _parse_size_limit_gb(d.pop("sizeLimitGB", UNSET))

        def _parse_used_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used_space_bytes = _parse_used_space_bytes(d.pop("usedSpaceBytes", UNSET))

        def _parse_free_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: RESTObjectStorageType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTObjectStorageType(_type_)

        def _parse_use_archiver_appliance(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_archiver_appliance = _parse_use_archiver_appliance(d.pop("useArchiverAppliance", UNSET))

        _azure_service_account = d.pop("azureServiceAccount", UNSET)
        azure_service_account: RESTServiceAccountInfo | Unset
        if isinstance(_azure_service_account, Unset):
            azure_service_account = UNSET
        else:
            azure_service_account = RESTServiceAccountInfo.from_dict(_azure_service_account)

        _azure_subscription = d.pop("azureSubscription", UNSET)
        azure_subscription: RESTAzureSubscription | Unset
        if isinstance(_azure_subscription, Unset):
            azure_subscription = UNSET
        else:
            azure_subscription = RESTAzureSubscription.from_dict(_azure_subscription)

        _azure_archiver_appliance = d.pop("azureArchiverAppliance", UNSET)
        azure_archiver_appliance: RESTAzureArchiverAppliance | Unset
        if isinstance(_azure_archiver_appliance, Unset):
            azure_archiver_appliance = UNSET
        else:
            azure_archiver_appliance = RESTAzureArchiverAppliance.from_dict(_azure_archiver_appliance)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTAzureObjectStorageRepositoryLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTAzureObjectStorageRepositoryLinks.from_dict(_field_links)

        rest_azure_object_storage_repository = cls(
            azure_container=azure_container,
            azure_folder=azure_folder,
            id=id,
            name=name,
            description=description,
            account_id=account_id,
            size_limit_enabled=size_limit_enabled,
            size_limit_gb=size_limit_gb,
            used_space_bytes=used_space_bytes,
            free_space_bytes=free_space_bytes,
            type_=type_,
            use_archiver_appliance=use_archiver_appliance,
            azure_service_account=azure_service_account,
            azure_subscription=azure_subscription,
            azure_archiver_appliance=azure_archiver_appliance,
            field_links=field_links,
        )

        rest_azure_object_storage_repository.additional_properties = d
        return rest_azure_object_storage_repository

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
