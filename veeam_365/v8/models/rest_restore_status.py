from enum import Enum


class RESTRestoreStatus(str, Enum):
    FAILED = "Failed"
    SKIPPED = "Skipped"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
