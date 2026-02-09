from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_amazon_s3_glacier_retrieval_policy import RESTAmazonS3GlacierRetrievalPolicy
from ..models.rest_azure_archive_retrieval_policy import RESTAzureArchiveRetrievalPolicy
from ..models.rest_data_retrieval_data_state import RESTDataRetrievalDataState
from ..models.rest_data_retrieval_session_status import RESTDataRetrievalSessionStatus
from ..models.rest_data_retrieval_storage_type import RESTDataRetrievalStorageType
from ..models.rest_data_retrieval_type import RESTDataRetrievalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_data_retrieval_composed_actions import RESTDataRetrievalComposedActions
    from ..models.rest_data_retrieval_composed_links import RESTDataRetrievalComposedLinks


T = TypeVar("T", bound="RESTDataRetrievalComposed")


@_attrs_define
class RESTDataRetrievalComposed:
    """
    Attributes:
        name (str | Unset): Name of the retrieval job.
        description (None | str | Unset): Description of the retrieval job.
        storage_type (RESTDataRetrievalStorageType | Unset): Type of the object storage repository.
        amazon_s3_glacier_retrieval_policy (RESTAmazonS3GlacierRetrievalPolicy | Unset): Retrieval policy that is
            selected for Amazon S3 Glacier Flexible Retrieval and Amazon S3 Glacier Deep Archive repository.
        id (UUID | Unset): Retrieval job ID. Example: 00000000-0000-0000-0000-000000000000.
        point_in_time (datetime.datetime | Unset): Point in time that you want to retrieve from one the following object
            storage repositories: Azure Blob Storage Archive access tier, Amazon S3 Glacier Flexible Retrieval or Amazon S3
            Glacier Deep Archive storage classes.
        retrieved_restore_point_id (str | Unset): ID of the retrieved restore point.
        organization_id (None | Unset | UUID): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
        organization_unique_id (str | Unset): Backed-up organization unique ID.
        repository_id (UUID | Unset): ID of one of the following object storage repositories: Azure Blob Storage Archive
            access tier, Amazon S3 Glacier Flexible Retrieval or Amazon S3 Glacier Deep Archive storage classes.
             Example: 00000000-0000-0000-0000-000000000000.
        data_state (RESTDataRetrievalDataState | Unset): Status of the backed-up data.
        last_status (RESTDataRetrievalSessionStatus | Unset): Latest status of the retrieval job.
        start_time (datetime.datetime | Unset): Date and time when the retrieval job started.
        expiration_time (datetime.datetime | None | Unset): Date and time when the retrieved data becomes unavailable.
        enable_expiration_notification (bool | Unset): Defines whether Veeam Backup for Microsoft 365 will send a
            notification by email before the retrieved data expires.
        expiration_hours_threshold (int | Unset): Number of hours that should remain before to send a notification by
            email about expiration of the retrieved data. Use this property only with the `enableExpirationNotification`
            property.
        type_ (RESTDataRetrievalType | Unset): Type of the retrieval job.
        show_deleted (bool | Unset): Defines whether the data retrieval session will show items that have been removed
            by the user before the specified point in time.
        show_all_versions (bool | Unset): Defines whether the data retrieval session will show all versions of items
            that have been modified by the user before the specified point in time.
        field_links (RESTDataRetrievalComposedLinks | Unset):
        field_actions (RESTDataRetrievalComposedActions | Unset):
        azure_archive_retrieval_policy (RESTAzureArchiveRetrievalPolicy | Unset): Retrieval policy that is selected for
            Azure Blob Storage Archive.
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    storage_type: RESTDataRetrievalStorageType | Unset = UNSET
    amazon_s3_glacier_retrieval_policy: RESTAmazonS3GlacierRetrievalPolicy | Unset = UNSET
    id: UUID | Unset = UNSET
    point_in_time: datetime.datetime | Unset = UNSET
    retrieved_restore_point_id: str | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    organization_unique_id: str | Unset = UNSET
    repository_id: UUID | Unset = UNSET
    data_state: RESTDataRetrievalDataState | Unset = UNSET
    last_status: RESTDataRetrievalSessionStatus | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    expiration_time: datetime.datetime | None | Unset = UNSET
    enable_expiration_notification: bool | Unset = UNSET
    expiration_hours_threshold: int | Unset = UNSET
    type_: RESTDataRetrievalType | Unset = UNSET
    show_deleted: bool | Unset = UNSET
    show_all_versions: bool | Unset = UNSET
    field_links: RESTDataRetrievalComposedLinks | Unset = UNSET
    field_actions: RESTDataRetrievalComposedActions | Unset = UNSET
    azure_archive_retrieval_policy: RESTAzureArchiveRetrievalPolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        storage_type: str | Unset = UNSET
        if not isinstance(self.storage_type, Unset):
            storage_type = self.storage_type.value

        amazon_s3_glacier_retrieval_policy: str | Unset = UNSET
        if not isinstance(self.amazon_s3_glacier_retrieval_policy, Unset):
            amazon_s3_glacier_retrieval_policy = self.amazon_s3_glacier_retrieval_policy.value

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        point_in_time: str | Unset = UNSET
        if not isinstance(self.point_in_time, Unset):
            point_in_time = self.point_in_time.isoformat()

        retrieved_restore_point_id = self.retrieved_restore_point_id

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        organization_unique_id = self.organization_unique_id

        repository_id: str | Unset = UNSET
        if not isinstance(self.repository_id, Unset):
            repository_id = str(self.repository_id)

        data_state: str | Unset = UNSET
        if not isinstance(self.data_state, Unset):
            data_state = self.data_state.value

        last_status: str | Unset = UNSET
        if not isinstance(self.last_status, Unset):
            last_status = self.last_status.value

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        expiration_time: None | str | Unset
        if isinstance(self.expiration_time, Unset):
            expiration_time = UNSET
        elif isinstance(self.expiration_time, datetime.datetime):
            expiration_time = self.expiration_time.isoformat()
        else:
            expiration_time = self.expiration_time

        enable_expiration_notification = self.enable_expiration_notification

        expiration_hours_threshold = self.expiration_hours_threshold

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        show_deleted = self.show_deleted

        show_all_versions = self.show_all_versions

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        azure_archive_retrieval_policy: str | Unset = UNSET
        if not isinstance(self.azure_archive_retrieval_policy, Unset):
            azure_archive_retrieval_policy = self.azure_archive_retrieval_policy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if storage_type is not UNSET:
            field_dict["storageType"] = storage_type
        if amazon_s3_glacier_retrieval_policy is not UNSET:
            field_dict["amazonS3GlacierRetrievalPolicy"] = amazon_s3_glacier_retrieval_policy
        if id is not UNSET:
            field_dict["id"] = id
        if point_in_time is not UNSET:
            field_dict["pointInTime"] = point_in_time
        if retrieved_restore_point_id is not UNSET:
            field_dict["retrievedRestorePointId"] = retrieved_restore_point_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization_unique_id is not UNSET:
            field_dict["organizationUniqueId"] = organization_unique_id
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if data_state is not UNSET:
            field_dict["dataState"] = data_state
        if last_status is not UNSET:
            field_dict["lastStatus"] = last_status
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if enable_expiration_notification is not UNSET:
            field_dict["enableExpirationNotification"] = enable_expiration_notification
        if expiration_hours_threshold is not UNSET:
            field_dict["expirationHoursThreshold"] = expiration_hours_threshold
        if type_ is not UNSET:
            field_dict["type"] = type_
        if show_deleted is not UNSET:
            field_dict["showDeleted"] = show_deleted
        if show_all_versions is not UNSET:
            field_dict["showAllVersions"] = show_all_versions
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
        if azure_archive_retrieval_policy is not UNSET:
            field_dict["azureArchiveRetrievalPolicy"] = azure_archive_retrieval_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_data_retrieval_composed_actions import RESTDataRetrievalComposedActions
        from ..models.rest_data_retrieval_composed_links import RESTDataRetrievalComposedLinks

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _storage_type = d.pop("storageType", UNSET)
        storage_type: RESTDataRetrievalStorageType | Unset
        if isinstance(_storage_type, Unset):
            storage_type = UNSET
        else:
            storage_type = RESTDataRetrievalStorageType(_storage_type)

        _amazon_s3_glacier_retrieval_policy = d.pop("amazonS3GlacierRetrievalPolicy", UNSET)
        amazon_s3_glacier_retrieval_policy: RESTAmazonS3GlacierRetrievalPolicy | Unset
        if isinstance(_amazon_s3_glacier_retrieval_policy, Unset):
            amazon_s3_glacier_retrieval_policy = UNSET
        else:
            amazon_s3_glacier_retrieval_policy = RESTAmazonS3GlacierRetrievalPolicy(_amazon_s3_glacier_retrieval_policy)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _point_in_time = d.pop("pointInTime", UNSET)
        point_in_time: datetime.datetime | Unset
        if isinstance(_point_in_time, Unset):
            point_in_time = UNSET
        else:
            point_in_time = isoparse(_point_in_time)

        retrieved_restore_point_id = d.pop("retrievedRestorePointId", UNSET)

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organizationId", UNSET))

        organization_unique_id = d.pop("organizationUniqueId", UNSET)

        _repository_id = d.pop("repositoryId", UNSET)
        repository_id: UUID | Unset
        if isinstance(_repository_id, Unset):
            repository_id = UNSET
        else:
            repository_id = UUID(_repository_id)

        _data_state = d.pop("dataState", UNSET)
        data_state: RESTDataRetrievalDataState | Unset
        if isinstance(_data_state, Unset):
            data_state = UNSET
        else:
            data_state = RESTDataRetrievalDataState(_data_state)

        _last_status = d.pop("lastStatus", UNSET)
        last_status: RESTDataRetrievalSessionStatus | Unset
        if isinstance(_last_status, Unset):
            last_status = UNSET
        else:
            last_status = RESTDataRetrievalSessionStatus(_last_status)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        def _parse_expiration_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_time_type_0 = isoparse(data)

                return expiration_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_time = _parse_expiration_time(d.pop("expirationTime", UNSET))

        enable_expiration_notification = d.pop("enableExpirationNotification", UNSET)

        expiration_hours_threshold = d.pop("expirationHoursThreshold", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RESTDataRetrievalType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTDataRetrievalType(_type_)

        show_deleted = d.pop("showDeleted", UNSET)

        show_all_versions = d.pop("showAllVersions", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTDataRetrievalComposedLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTDataRetrievalComposedLinks.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTDataRetrievalComposedActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTDataRetrievalComposedActions.from_dict(_field_actions)

        _azure_archive_retrieval_policy = d.pop("azureArchiveRetrievalPolicy", UNSET)
        azure_archive_retrieval_policy: RESTAzureArchiveRetrievalPolicy | Unset
        if isinstance(_azure_archive_retrieval_policy, Unset):
            azure_archive_retrieval_policy = UNSET
        else:
            azure_archive_retrieval_policy = RESTAzureArchiveRetrievalPolicy(_azure_archive_retrieval_policy)

        rest_data_retrieval_composed = cls(
            name=name,
            description=description,
            storage_type=storage_type,
            amazon_s3_glacier_retrieval_policy=amazon_s3_glacier_retrieval_policy,
            id=id,
            point_in_time=point_in_time,
            retrieved_restore_point_id=retrieved_restore_point_id,
            organization_id=organization_id,
            organization_unique_id=organization_unique_id,
            repository_id=repository_id,
            data_state=data_state,
            last_status=last_status,
            start_time=start_time,
            expiration_time=expiration_time,
            enable_expiration_notification=enable_expiration_notification,
            expiration_hours_threshold=expiration_hours_threshold,
            type_=type_,
            show_deleted=show_deleted,
            show_all_versions=show_all_versions,
            field_links=field_links,
            field_actions=field_actions,
            azure_archive_retrieval_policy=azure_archive_retrieval_policy,
        )

        rest_data_retrieval_composed.additional_properties = d
        return rest_data_retrieval_composed

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
