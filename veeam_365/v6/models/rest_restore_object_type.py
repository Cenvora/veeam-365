from enum import Enum


class RESTRestoreObjectType(str, Enum):
    ITEM = "Item"
    LIST = "List"
    SITE = "Site"

    def __str__(self) -> str:
        return str(self.value)
