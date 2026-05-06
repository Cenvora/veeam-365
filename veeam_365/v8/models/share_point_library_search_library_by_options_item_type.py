from enum import Enum

class SharePointLibrarySearchLibraryByOptionsItemType(str, Enum):
    ALL = "All"
    FOLDERS = "Folders"
    ITEMS = "Items"

    def __str__(self) -> str:
        return str(self.value)
