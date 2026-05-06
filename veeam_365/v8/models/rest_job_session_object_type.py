from enum import Enum

class RESTJobSessionObjectType(str, Enum):
    GROUP = "Group"
    SITE = "Site"
    TEAM = "Team"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
