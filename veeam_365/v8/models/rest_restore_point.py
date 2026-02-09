from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_restore_point_links import RESTRestorePointLinks


T = TypeVar("T", bound="RESTRestorePoint")


@_attrs_define
class RESTRestorePoint:
    """
    Attributes:
        id (str | Unset): ID of the restore point.
        is_deleted (bool | Unset): Defines whether the restore point contains data marked as deleted or soft deleted.
        repository_id (UUID | Unset): Backup repository ID. Example: 00000000-0000-0000-0000-000000000000.
        backup_time (datetime.datetime | Unset): Date and time when the restore point was created.
        job_id (UUID | Unset): ID of a backup job. Example: 00000000-0000-0000-0000-000000000000.
        retrieval_id (UUID | Unset): ID of a retrieval job. Example: 00000000-0000-0000-0000-000000000000.
        organization_id (UUID | Unset): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
        is_exchange (bool | Unset): Defines whether the restore point contains Microsoft Exchange data.
        is_share_point (bool | Unset): Defines whether the restore point contains Microsoft SharePoint data.
        is_one_drive (bool | Unset): Defines whether the restore point contains Microsoft OneDrive data.
        is_teams (bool | Unset): Defines whether the restore point contains Microsoft Teams data.
        is_long_term_copy (bool | Unset): Defines whether the restore point was created by a backup copy job in the
            following object storage repositories: Azure Blob Storage Archive access tier, Amazon S3 Glacier Instant
            Retrieval, Amazon S3 Glacier Flexible Retrieval or Amazon S3 Glacier Deep Archive storage classes.
        is_copy (bool | Unset): Defines whether the restore point was created by a backup copy job in any object storage
            repository.
        is_retrieved (bool | Unset): Defines whether the restore point was retrieved from object storage repository by a
            data retrieval job.
        e_tag (int | Unset): Version number that Veeam Backup for Microsoft 365 assigns if the restore point was
            modified.
        objects_etag (int | Unset): Version number that Veeam Backup for Microsoft 365 assigns if objects included to
            the restore point were modified.
        immutability_expires_on (datetime.datetime | None | Unset): Date and time until which the backed-up data in the
            restore point will be blocked for deletion or modification.
        field_links (RESTRestorePointLinks | Unset):
    """

    id: str | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    repository_id: UUID | Unset = UNSET
    backup_time: datetime.datetime | Unset = UNSET
    job_id: UUID | Unset = UNSET
    retrieval_id: UUID | Unset = UNSET
    organization_id: UUID | Unset = UNSET
    is_exchange: bool | Unset = UNSET
    is_share_point: bool | Unset = UNSET
    is_one_drive: bool | Unset = UNSET
    is_teams: bool | Unset = UNSET
    is_long_term_copy: bool | Unset = UNSET
    is_copy: bool | Unset = UNSET
    is_retrieved: bool | Unset = UNSET
    e_tag: int | Unset = UNSET
    objects_etag: int | Unset = UNSET
    immutability_expires_on: datetime.datetime | None | Unset = UNSET
    field_links: RESTRestorePointLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_deleted = self.is_deleted

        repository_id: str | Unset = UNSET
        if not isinstance(self.repository_id, Unset):
            repository_id = str(self.repository_id)

        backup_time: str | Unset = UNSET
        if not isinstance(self.backup_time, Unset):
            backup_time = self.backup_time.isoformat()

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

        retrieval_id: str | Unset = UNSET
        if not isinstance(self.retrieval_id, Unset):
            retrieval_id = str(self.retrieval_id)

        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        is_exchange = self.is_exchange

        is_share_point = self.is_share_point

        is_one_drive = self.is_one_drive

        is_teams = self.is_teams

        is_long_term_copy = self.is_long_term_copy

        is_copy = self.is_copy

        is_retrieved = self.is_retrieved

        e_tag = self.e_tag

        objects_etag = self.objects_etag

        immutability_expires_on: None | str | Unset
        if isinstance(self.immutability_expires_on, Unset):
            immutability_expires_on = UNSET
        elif isinstance(self.immutability_expires_on, datetime.datetime):
            immutability_expires_on = self.immutability_expires_on.isoformat()
        else:
            immutability_expires_on = self.immutability_expires_on

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if backup_time is not UNSET:
            field_dict["backupTime"] = backup_time
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if retrieval_id is not UNSET:
            field_dict["retrievalId"] = retrieval_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if is_exchange is not UNSET:
            field_dict["isExchange"] = is_exchange
        if is_share_point is not UNSET:
            field_dict["isSharePoint"] = is_share_point
        if is_one_drive is not UNSET:
            field_dict["isOneDrive"] = is_one_drive
        if is_teams is not UNSET:
            field_dict["isTeams"] = is_teams
        if is_long_term_copy is not UNSET:
            field_dict["isLongTermCopy"] = is_long_term_copy
        if is_copy is not UNSET:
            field_dict["isCopy"] = is_copy
        if is_retrieved is not UNSET:
            field_dict["isRetrieved"] = is_retrieved
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag
        if objects_etag is not UNSET:
            field_dict["objectsEtag"] = objects_etag
        if immutability_expires_on is not UNSET:
            field_dict["immutabilityExpiresOn"] = immutability_expires_on
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_restore_point_links import RESTRestorePointLinks

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        _repository_id = d.pop("repositoryId", UNSET)
        repository_id: UUID | Unset
        if isinstance(_repository_id, Unset):
            repository_id = UNSET
        else:
            repository_id = UUID(_repository_id)

        _backup_time = d.pop("backupTime", UNSET)
        backup_time: datetime.datetime | Unset
        if isinstance(_backup_time, Unset):
            backup_time = UNSET
        else:
            backup_time = isoparse(_backup_time)

        _job_id = d.pop("jobId", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id, Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)

        _retrieval_id = d.pop("retrievalId", UNSET)
        retrieval_id: UUID | Unset
        if isinstance(_retrieval_id, Unset):
            retrieval_id = UNSET
        else:
            retrieval_id = UUID(_retrieval_id)

        _organization_id = d.pop("organizationId", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        is_exchange = d.pop("isExchange", UNSET)

        is_share_point = d.pop("isSharePoint", UNSET)

        is_one_drive = d.pop("isOneDrive", UNSET)

        is_teams = d.pop("isTeams", UNSET)

        is_long_term_copy = d.pop("isLongTermCopy", UNSET)

        is_copy = d.pop("isCopy", UNSET)

        is_retrieved = d.pop("isRetrieved", UNSET)

        e_tag = d.pop("eTag", UNSET)

        objects_etag = d.pop("objectsEtag", UNSET)

        def _parse_immutability_expires_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                immutability_expires_on_type_0 = isoparse(data)

                return immutability_expires_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        immutability_expires_on = _parse_immutability_expires_on(d.pop("immutabilityExpiresOn", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: RESTRestorePointLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTRestorePointLinks.from_dict(_field_links)

        rest_restore_point = cls(
            id=id,
            is_deleted=is_deleted,
            repository_id=repository_id,
            backup_time=backup_time,
            job_id=job_id,
            retrieval_id=retrieval_id,
            organization_id=organization_id,
            is_exchange=is_exchange,
            is_share_point=is_share_point,
            is_one_drive=is_one_drive,
            is_teams=is_teams,
            is_long_term_copy=is_long_term_copy,
            is_copy=is_copy,
            is_retrieved=is_retrieved,
            e_tag=e_tag,
            objects_etag=objects_etag,
            immutability_expires_on=immutability_expires_on,
            field_links=field_links,
        )

        rest_restore_point.additional_properties = d
        return rest_restore_point

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
