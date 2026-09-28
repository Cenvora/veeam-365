from enum import Enum


class SharePointSiteSearchSiteByOptionsContainerType(str, Enum):
    LIBRARY = "Library"
    LIST = "List"

    def __str__(self) -> str:
        return str(self.value)
