from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTJobLastStatus(str, Enum):
    DISCONNECTED = "Disconnected"
    FAILED = "Failed"
    NOTCONFIGURED = "NotConfigured"
    QUEUED = "Queued"
    RUNNING = "Running"
    STOPPED = "Stopped"
    SUCCESS = "Success"
    WARNING = "Warning"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
