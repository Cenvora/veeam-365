from enum import Enum

class RESTGroupMemberType(str, Enum):
    GROUP = "Group"
    UNKNOWN = "Unknown"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
