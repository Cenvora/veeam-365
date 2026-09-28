from enum import Enum


class OneDriveSearchOneDriveByOptionsItemType(str, Enum):
    ALL = "All"
    DOCUMENTS = "Documents"
    FOLDERS = "Folders"

    def __str__(self) -> str:
        return str(self.value)
