from enum import Enum


class RESTRbacItemType(str, Enum):
    GROUP = "Group"
    SITE = "Site"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
