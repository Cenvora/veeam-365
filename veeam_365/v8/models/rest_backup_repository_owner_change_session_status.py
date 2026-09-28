from enum import Enum


class RESTBackupRepositoryOwnerChangeSessionStatus(str, Enum):
    FAILED = "Failed"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    WAITING = "Waiting"

    def __str__(self) -> str:
        return str(self.value)
