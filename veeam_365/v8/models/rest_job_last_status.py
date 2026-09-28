from enum import Enum


class RESTJobLastStatus(str, Enum):
    DISCONNECTED = "Disconnected"
    FAILED = "Failed"
    NOTCONFIGURED = "NotConfigured"
    QUEUED = "Queued"
    RUNNING = "Running"
    STOPPED = "Stopped"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
