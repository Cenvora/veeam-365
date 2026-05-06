from enum import Enum

class RESTRbacOperatorType(str, Enum):
    GROUP = "Group"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
