from enum import Enum

class RESTOrganizationCurrentSyncStateStatus(str, Enum):
    QUEUED = "Queued"
    RUNNING = "Running"

    def __str__(self) -> str:
        return str(self.value)
