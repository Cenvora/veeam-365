from enum import Enum


class SharePointSiteSearchSitesByOptionsContainerType(str, Enum):
    LIBRARY = "Library"
    LIST = "List"

    def __str__(self) -> str:
        return str(self.value)
