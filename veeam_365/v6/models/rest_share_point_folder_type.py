from enum import Enum


class RESTSharePointFolderType(str, Enum):
    LIBRARYFOLDER = "LibraryFolder"
    LISTFOLDER = "ListFolder"

    def __str__(self) -> str:
        return str(self.value)
