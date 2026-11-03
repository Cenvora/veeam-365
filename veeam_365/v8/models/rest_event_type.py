from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTEventType(str, Enum):
    JOBDELETE = "JobDelete"
    JOBEXCLUDEDITEMSCHANGE = "JobExcludedItemsChange"
    JOBSELECTEDITEMSCHANGE = "JobSelectedItemsChange"
    JOBSESSIONDELETE = "JobSessionDelete"
    JOBSESSIONUPDATE = "JobSessionUpdate"
    JOBUPDATE = "JobUpdate"
    M365BACKUPSTORAGEPOLICYDELETE = "M365BackupStoragePolicyDelete"
    M365BACKUPSTORAGEPOLICYSELECTEDITEMSCHANGE = "M365BackupStoragePolicySelectedItemsChange"
    M365BACKUPSTORAGEPOLICYUPDATE = "M365BackupStoragePolicyUpdate"
    ORGANIZATIONGROUPDELETE = "OrganizationGroupDelete"
    ORGANIZATIONGROUPUPDATE = "OrganizationGroupUpdate"
    ORGANIZATIONSITEDELETE = "OrganizationSiteDelete"
    ORGANIZATIONSITEUPDATE = "OrganizationSiteUpdate"
    ORGANIZATIONTEAMDELETE = "OrganizationTeamDelete"
    ORGANIZATIONTEAMUPDATE = "OrganizationTeamUpdate"
    ORGANIZATIONUSERDELETE = "OrganizationUserDelete"
    ORGANIZATIONUSERUPDATE = "OrganizationUserUpdate"
    PROTECTEDGROUPDELETE = "ProtectedGroupDelete"
    PROTECTEDGROUPUPDATE = "ProtectedGroupUpdate"
    PROTECTEDSITEDELETE = "ProtectedSiteDelete"
    PROTECTEDSITEUPDATE = "ProtectedSiteUpdate"
    PROTECTEDTEAMDELETE = "ProtectedTeamDelete"
    PROTECTEDTEAMUPDATE = "ProtectedTeamUpdate"
    PROTECTEDUSERDELETE = "ProtectedUserDelete"
    PROTECTEDUSERUPDATE = "ProtectedUserUpdate"
    RESTOREPOINTDELETE = "RestorePointDelete"
    RESTOREPOINTOBJECTSCHANGE = "RestorePointObjectsChange"
    RESTOREPOINTUPDATE = "RestorePointUpdate"
    RESTORESESSIONDELETE = "RestoreSessionDelete"
    RESTORESESSIONUPDATE = "RestoreSessionUpdate"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
