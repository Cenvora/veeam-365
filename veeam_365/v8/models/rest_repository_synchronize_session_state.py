from enum import Enum

class RESTRepositorySynchronizeSessionState(str, Enum):
    FAILED = "Failed"
    NONE = "None"
    SYNCHRONIZING = "Synchronizing"

    def __str__(self) -> str:
        return str(self.value)
