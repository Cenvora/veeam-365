from enum import Enum

class RESTEditBackupJobBackupType(str, Enum):
    ENTIREORGANIZATION = "EntireOrganization"
    SELECTEDITEMS = "SelectedItems"

    def __str__(self) -> str:
        return str(self.value)
