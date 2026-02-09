from enum import Enum


class JobSessionGetStatus(str, Enum):
    FAILED = "Failed"
    RUNNING = "Running"
    STOPPED = "Stopped"
    SUCCEEDED = "Succeeded"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
