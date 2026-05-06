from enum import Enum

class RESTUserType(str, Enum):
    PUBLIC = "Public"
    SHARED = "Shared"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
