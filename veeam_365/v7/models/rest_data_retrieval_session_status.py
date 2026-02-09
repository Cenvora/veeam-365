from enum import Enum


class RESTDataRetrievalSessionStatus(str, Enum):
    FAILED = "Failed"
    NOTCONFIGURED = "NotConfigured"
    RUNNING = "Running"
    STOPPED = "Stopped"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
