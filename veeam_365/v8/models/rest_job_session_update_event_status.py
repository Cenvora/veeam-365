from enum import Enum

class RESTJobSessionUpdateEventStatus(str, Enum):
    FAILED = "Failed"
    NOTCONFIGURED = "NotConfigured"
    RUNNING = "Running"
    STOPPED = "Stopped"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
