from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_data_retrieval_from_client_amazon_s3_glacier_retrieval_policy import RESTDataRetrievalFromClientAmazonS3GlacierRetrievalPolicy
from ..models.rest_data_retrieval_from_client_azure_archive_retrieval_policy import RESTDataRetrievalFromClientAzureArchiveRetrievalPolicy
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.rest_backup_mailbox_data import RESTBackupMailboxData
  from ..models.rest_backup_one_drive_data import RESTBackupOneDriveData
  from ..models.rest_backup_site_data import RESTBackupSiteData
  from ..models.rest_backup_team_data import RESTBackupTeamData





T = TypeVar("T", bound="RESTDataRetrievalFromClient")



@_attrs_define
class RESTDataRetrievalFromClient:
    """ 
        Attributes:
            name (None | str | Unset): Specifies a name of the retrieval job.
            description (None | str | Unset): Specifies a description of the retrieval job.
            organization_id (str | Unset): Specifies the backed-up organization unique ID.
            repository_id (None | Unset | UUID): Specifies the ID of one of the following object storage repositories: Azure
                Blob Storage Archive access tier, Amazon S3 Glacier Flexible Retrieval or Amazon S3 Glacier Deep Archive storage
                classes.
                 Example: 00000000-0000-0000-0000-000000000000.
            point_in_time (datetime.datetime | None | Unset): Specifies point in time that you want to retrieve from one of
                the following object storage repositories: Azure Blob Storage Archive access tier, Amazon S3 Glacier Flexible
                Retrieval or Amazon S3 Glacier Deep Archive storage classes.
            show_deleted (bool | None | Unset): Defines whether the data retrieval session will show items that have been
                removed by the user before the specified point in time.
            show_all_versions (bool | None | Unset): Defines whether the data retrieval session will show all versions of
                items that have been modified by the user before the specified point in time.
            availability_period_days (int | Unset): Specifies how many days you will be able to explore and restore the
                retrieved data using Veeam Explorers.
            enable_expiration_notification (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 will send a
                notification by email before the retrieved data expires.
            expiration_hours_threshold (int | None | Unset): Specifies how many hours should remain before the retrieved
                data expires to send a notification by email.  Use this property only with the `enableExpirationNotification`
                property.
            mailboxes (list[RESTBackupMailboxData] | Unset): Specifies IDs of the mailboxes whose backed-up data you want to
                retrieve from object storage repository. For more information on how to get such IDs, see [Get Mailbox Data by
                Repository ID](#/BackupMailboxData/BackupMailboxData_GetMailboxesData).
            one_drives (list[RESTBackupOneDriveData] | Unset): Specifies IDs of OneDrives whose backed-up data you want to
                retrieve from object storage repository. For more information on how to get such IDs, see [Get OneDrive Data by
                Repository ID](#/BackupOneDriveData/BackupOneDriveData_GetOneDrivesData).
            sites (list[RESTBackupSiteData] | Unset): Specifies IDs of the SharePoint sites whose backed-up data you want to
                retrieve from object storage repository. For more information on how to get such IDs, see [Get SharePoint Data
                by Repository ID](#/BackupSiteData/BackupSiteData_GetSitesData).
            teams (list[RESTBackupTeamData] | Unset): Specifies IDs of the teams whose backed-up data you want to retrieve
                from object storage repository. For more information on how to get such IDs, see [Get Teams Data by Repository
                ID](#/BackupTeamData/BackupTeamData_GetTeamsData).
            amazon_s3_glacier_retrieval_policy (RESTDataRetrievalFromClientAmazonS3GlacierRetrievalPolicy | Unset):
                Specifies the retrieval policy for Amazon S3 Glacier Flexible Retrieval and Amazon S3 Glacier Deep Archive
                object storage repositories.
            azure_archive_retrieval_policy (RESTDataRetrievalFromClientAzureArchiveRetrievalPolicy | Unset): Specifies the
                retrieval policy for Azure Blob Storage Archive.
     """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    organization_id: str | Unset = UNSET
    repository_id: None | Unset | UUID = UNSET
    point_in_time: datetime.datetime | None | Unset = UNSET
    show_deleted: bool | None | Unset = UNSET
    show_all_versions: bool | None | Unset = UNSET
    availability_period_days: int | Unset = UNSET
    enable_expiration_notification: bool | None | Unset = UNSET
    expiration_hours_threshold: int | None | Unset = UNSET
    mailboxes: list[RESTBackupMailboxData] | Unset = UNSET
    one_drives: list[RESTBackupOneDriveData] | Unset = UNSET
    sites: list[RESTBackupSiteData] | Unset = UNSET
    teams: list[RESTBackupTeamData] | Unset = UNSET
    amazon_s3_glacier_retrieval_policy: RESTDataRetrievalFromClientAmazonS3GlacierRetrievalPolicy | Unset = UNSET
    azure_archive_retrieval_policy: RESTDataRetrievalFromClientAzureArchiveRetrievalPolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_backup_mailbox_data import RESTBackupMailboxData
        from ..models.rest_backup_one_drive_data import RESTBackupOneDriveData
        from ..models.rest_backup_site_data import RESTBackupSiteData
        from ..models.rest_backup_team_data import RESTBackupTeamData
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        organization_id = self.organization_id

        repository_id: None | str | Unset
        if isinstance(self.repository_id, Unset):
            repository_id = UNSET
        elif isinstance(self.repository_id, UUID):
            repository_id = str(self.repository_id)
        else:
            repository_id = self.repository_id

        point_in_time: None | str | Unset
        if isinstance(self.point_in_time, Unset):
            point_in_time = UNSET
        elif isinstance(self.point_in_time, datetime.datetime):
            point_in_time = self.point_in_time.isoformat()
        else:
            point_in_time = self.point_in_time

        show_deleted: bool | None | Unset
        if isinstance(self.show_deleted, Unset):
            show_deleted = UNSET
        else:
            show_deleted = self.show_deleted

        show_all_versions: bool | None | Unset
        if isinstance(self.show_all_versions, Unset):
            show_all_versions = UNSET
        else:
            show_all_versions = self.show_all_versions

        availability_period_days = self.availability_period_days

        enable_expiration_notification: bool | None | Unset
        if isinstance(self.enable_expiration_notification, Unset):
            enable_expiration_notification = UNSET
        else:
            enable_expiration_notification = self.enable_expiration_notification

        expiration_hours_threshold: int | None | Unset
        if isinstance(self.expiration_hours_threshold, Unset):
            expiration_hours_threshold = UNSET
        else:
            expiration_hours_threshold = self.expiration_hours_threshold

        mailboxes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mailboxes, Unset):
            mailboxes = []
            for mailboxes_item_data in self.mailboxes:
                mailboxes_item = mailboxes_item_data.to_dict()
                mailboxes.append(mailboxes_item)



        one_drives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.one_drives, Unset):
            one_drives = []
            for one_drives_item_data in self.one_drives:
                one_drives_item = one_drives_item_data.to_dict()
                one_drives.append(one_drives_item)



        sites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)



        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)



        amazon_s3_glacier_retrieval_policy: str | Unset = UNSET
        if not isinstance(self.amazon_s3_glacier_retrieval_policy, Unset):
            amazon_s3_glacier_retrieval_policy = self.amazon_s3_glacier_retrieval_policy.value


        azure_archive_retrieval_policy: str | Unset = UNSET
        if not isinstance(self.azure_archive_retrieval_policy, Unset):
            azure_archive_retrieval_policy = self.azure_archive_retrieval_policy.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if point_in_time is not UNSET:
            field_dict["pointInTime"] = point_in_time
        if show_deleted is not UNSET:
            field_dict["showDeleted"] = show_deleted
        if show_all_versions is not UNSET:
            field_dict["showAllVersions"] = show_all_versions
        if availability_period_days is not UNSET:
            field_dict["availabilityPeriodDays"] = availability_period_days
        if enable_expiration_notification is not UNSET:
            field_dict["enableExpirationNotification"] = enable_expiration_notification
        if expiration_hours_threshold is not UNSET:
            field_dict["expirationHoursThreshold"] = expiration_hours_threshold
        if mailboxes is not UNSET:
            field_dict["mailboxes"] = mailboxes
        if one_drives is not UNSET:
            field_dict["oneDrives"] = one_drives
        if sites is not UNSET:
            field_dict["sites"] = sites
        if teams is not UNSET:
            field_dict["teams"] = teams
        if amazon_s3_glacier_retrieval_policy is not UNSET:
            field_dict["amazonS3GlacierRetrievalPolicy"] = amazon_s3_glacier_retrieval_policy
        if azure_archive_retrieval_policy is not UNSET:
            field_dict["azureArchiveRetrievalPolicy"] = azure_archive_retrieval_policy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_backup_mailbox_data import RESTBackupMailboxData
        from ..models.rest_backup_one_drive_data import RESTBackupOneDriveData
        from ..models.rest_backup_site_data import RESTBackupSiteData
        from ..models.rest_backup_team_data import RESTBackupTeamData
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        organization_id = d.pop("organizationId", UNSET)

        def _parse_repository_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_id_type_0 = UUID(data)



                return repository_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        repository_id = _parse_repository_id(d.pop("repositoryId", UNSET))


        def _parse_point_in_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                point_in_time_type_0 = isoparse(data)



                return point_in_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        point_in_time = _parse_point_in_time(d.pop("pointInTime", UNSET))


        def _parse_show_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_deleted = _parse_show_deleted(d.pop("showDeleted", UNSET))


        def _parse_show_all_versions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_all_versions = _parse_show_all_versions(d.pop("showAllVersions", UNSET))


        availability_period_days = d.pop("availabilityPeriodDays", UNSET)

        def _parse_enable_expiration_notification(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_expiration_notification = _parse_enable_expiration_notification(d.pop("enableExpirationNotification", UNSET))


        def _parse_expiration_hours_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expiration_hours_threshold = _parse_expiration_hours_threshold(d.pop("expirationHoursThreshold", UNSET))


        _mailboxes = d.pop("mailboxes", UNSET)
        mailboxes: list[RESTBackupMailboxData] | Unset = UNSET
        if _mailboxes is not UNSET:
            mailboxes = []
            for mailboxes_item_data in _mailboxes:
                mailboxes_item = RESTBackupMailboxData.from_dict(mailboxes_item_data)



                mailboxes.append(mailboxes_item)


        _one_drives = d.pop("oneDrives", UNSET)
        one_drives: list[RESTBackupOneDriveData] | Unset = UNSET
        if _one_drives is not UNSET:
            one_drives = []
            for one_drives_item_data in _one_drives:
                one_drives_item = RESTBackupOneDriveData.from_dict(one_drives_item_data)



                one_drives.append(one_drives_item)


        _sites = d.pop("sites", UNSET)
        sites: list[RESTBackupSiteData] | Unset = UNSET
        if _sites is not UNSET:
            sites = []
            for sites_item_data in _sites:
                sites_item = RESTBackupSiteData.from_dict(sites_item_data)



                sites.append(sites_item)


        _teams = d.pop("teams", UNSET)
        teams: list[RESTBackupTeamData] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = RESTBackupTeamData.from_dict(teams_item_data)



                teams.append(teams_item)


        _amazon_s3_glacier_retrieval_policy = d.pop("amazonS3GlacierRetrievalPolicy", UNSET)
        amazon_s3_glacier_retrieval_policy: RESTDataRetrievalFromClientAmazonS3GlacierRetrievalPolicy | Unset
        if isinstance(_amazon_s3_glacier_retrieval_policy,  Unset):
            amazon_s3_glacier_retrieval_policy = UNSET
        else:
            amazon_s3_glacier_retrieval_policy = RESTDataRetrievalFromClientAmazonS3GlacierRetrievalPolicy(_amazon_s3_glacier_retrieval_policy)




        _azure_archive_retrieval_policy = d.pop("azureArchiveRetrievalPolicy", UNSET)
        azure_archive_retrieval_policy: RESTDataRetrievalFromClientAzureArchiveRetrievalPolicy | Unset
        if isinstance(_azure_archive_retrieval_policy,  Unset):
            azure_archive_retrieval_policy = UNSET
        else:
            azure_archive_retrieval_policy = RESTDataRetrievalFromClientAzureArchiveRetrievalPolicy(_azure_archive_retrieval_policy)




        rest_data_retrieval_from_client = cls(
            name=name,
            description=description,
            organization_id=organization_id,
            repository_id=repository_id,
            point_in_time=point_in_time,
            show_deleted=show_deleted,
            show_all_versions=show_all_versions,
            availability_period_days=availability_period_days,
            enable_expiration_notification=enable_expiration_notification,
            expiration_hours_threshold=expiration_hours_threshold,
            mailboxes=mailboxes,
            one_drives=one_drives,
            sites=sites,
            teams=teams,
            amazon_s3_glacier_retrieval_policy=amazon_s3_glacier_retrieval_policy,
            azure_archive_retrieval_policy=azure_archive_retrieval_policy,
        )


        rest_data_retrieval_from_client.additional_properties = d
        return rest_data_retrieval_from_client

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
