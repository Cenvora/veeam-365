from enum import Enum


class SharePointListSearchListByOptionsItemType(str, Enum):
    ALL = "All"
    FOLDERS = "Folders"
    ITEMS = "Items"

    def __str__(self) -> str:
        return str(self.value)
