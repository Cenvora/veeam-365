from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTSharePointFolderType(str, Enum):
    LIBRARYFOLDER = "LibraryFolder"
    LIBRARYITEM = "LibraryItem"
    LISTFOLDER = "ListFolder"
    LISTITEM = "ListItem"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
