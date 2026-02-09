from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_object_storage_type import RESTObjectStorageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_amazon_bucket_s3_compatible import RESTAmazonBucketS3Compatible
    from ..models.rest_amazon_s3_compatible_object_storage_repository_links import (
        RESTAmazonS3CompatibleObjectStorageRepositoryLinks,
    )


T = TypeVar("T", bound="RESTAmazonS3CompatibleObjectStorageRepository")


@_attrs_define
class RESTAmazonS3CompatibleObjectStorageRepository:
    """
    Attributes:
        amazon_bucket_s3_compatible (RESTAmazonBucketS3Compatible | Unset):
        s_3_folder (str | Unset):
        id (UUID | Unset):  Example: 00000000-0000-0000-0000-000000000000.
        name (str | Unset):
        description (str | Unset):
        account_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        size_limit_enabled (bool | None | Unset):
        size_limit_gb (int | None | Unset):
        used_space_bytes (int | None | Unset):
        free_space_bytes (int | None | Unset):
        type_ (RESTObjectStorageType | Unset):
        field_links (RESTAmazonS3CompatibleObjectStorageRepositoryLinks | Unset):
    """

    amazon_bucket_s3_compatible: RESTAmazonBucketS3Compatible | Unset = UNSET
    s_3_folder: str | Unset = UNSET
    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    account_id: None | Unset | UUID = UNSET
    size_limit_enabled: bool | None | Unset = UNSET
    size_limit_gb: int | None | Unset = UNSET
    used_space_bytes: int | None | Unset = UNSET
    free_space_bytes: int | None | Unset = UNSET
    type_: RESTObjectStorageType | Unset = UNSET
    field_links: RESTAmazonS3CompatibleObjectStorageRepositoryLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amazon_bucket_s3_compatible: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amazon_bucket_s3_compatible, Unset):
            amazon_bucket_s3_compatible = self.amazon_bucket_s3_compatible.to_dict()

        s_3_folder = self.s_3_folder

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

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon_bucket_s3_compatible is not UNSET:
            field_dict["amazonBucketS3Compatible"] = amazon_bucket_s3_compatible
        if s_3_folder is not UNSET:
            field_dict["s3Folder"] = s_3_folder
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
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_amazon_bucket_s3_compatible import RESTAmazonBucketS3Compatible
        from ..models.rest_amazon_s3_compatible_object_storage_repository_links import (
            RESTAmazonS3CompatibleObjectStorageRepositoryLinks,
        )

        d = dict(src_dict)
        _amazon_bucket_s3_compatible = d.pop("amazonBucketS3Compatible", UNSET)
        amazon_bucket_s3_compatible: RESTAmazonBucketS3Compatible | Unset
        if isinstance(_amazon_bucket_s3_compatible, Unset):
            amazon_bucket_s3_compatible = UNSET
        else:
            amazon_bucket_s3_compatible = RESTAmazonBucketS3Compatible.from_dict(_amazon_bucket_s3_compatible)

        s_3_folder = d.pop("s3Folder", UNSET)

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

        _field_links = d.pop("_links", UNSET)
        field_links: RESTAmazonS3CompatibleObjectStorageRepositoryLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTAmazonS3CompatibleObjectStorageRepositoryLinks.from_dict(_field_links)

        rest_amazon_s3_compatible_object_storage_repository = cls(
            amazon_bucket_s3_compatible=amazon_bucket_s3_compatible,
            s_3_folder=s_3_folder,
            id=id,
            name=name,
            description=description,
            account_id=account_id,
            size_limit_enabled=size_limit_enabled,
            size_limit_gb=size_limit_gb,
            used_space_bytes=used_space_bytes,
            free_space_bytes=free_space_bytes,
            type_=type_,
            field_links=field_links,
        )

        rest_amazon_s3_compatible_object_storage_repository.additional_properties = d
        return rest_amazon_s3_compatible_object_storage_repository

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
