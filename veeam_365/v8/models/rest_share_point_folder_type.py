from enum import Enum


class RESTSharePointFolderType(str, Enum):
    LIBRARYFOLDER = "LibraryFolder"
    LIBRARYITEM = "LibraryItem"
    LISTFOLDER = "ListFolder"
    LISTITEM = "ListItem"

    def __str__(self) -> str:
        return str(self.value)
