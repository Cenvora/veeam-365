from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTGroupMemberType(str, Enum):
    GROUP = "Group"
    UNKNOWN = "Unknown"
    USER = "User"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
