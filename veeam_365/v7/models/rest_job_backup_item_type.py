from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTJobBackupItemType(str, Enum):
    GROUP = "Group"
    ONEDRIVEFOLDERS = "OneDriveFolders"
    PARTIALORGANIZATION = "PartialOrganization"
    PERSONALSITES = "PersonalSites"
    SITE = "Site"
    TEAM = "Team"
    USER = "User"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
