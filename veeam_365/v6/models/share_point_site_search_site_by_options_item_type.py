from enum import Enum

from ..._lenient_enum import keep_unknown_value


class SharePointSiteSearchSiteByOptionsItemType(str, Enum):
    ALL = "All"
    FOLDERS = "Folders"
    ITEMS = "Items"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
