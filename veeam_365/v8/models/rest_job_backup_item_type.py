from enum import Enum

class RESTJobBackupItemType(str, Enum):
    GROUP = "Group"
    ONEDRIVEFOLDERS = "OneDriveFolders"
    PARTIALORGANIZATION = "PartialOrganization"
    PERSONALSITES = "PersonalSites"
    SITE = "Site"
    TEAM = "Team"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
