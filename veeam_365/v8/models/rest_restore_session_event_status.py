from enum import Enum


class RESTRestoreSessionEventStatus(str, Enum):
    CANCELLED = "Cancelled"
    FAILED = "Failed"
    RUNNING = "Running"
    SKIPPED = "Skipped"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
