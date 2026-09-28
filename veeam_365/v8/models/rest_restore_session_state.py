from enum import Enum


class RESTRestoreSessionState(str, Enum):
    STOPPED = "Stopped"
    WORKING = "Working"

    def __str__(self) -> str:
        return str(self.value)
