from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTRestoreObjectType(str, Enum):
    ITEM = "Item"
    LIST = "List"
    SITE = "Site"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
