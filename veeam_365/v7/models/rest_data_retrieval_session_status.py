from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTDataRetrievalSessionStatus(str, Enum):
    FAILED = "Failed"
    NOTCONFIGURED = "NotConfigured"
    RUNNING = "Running"
    STOPPED = "Stopped"
    SUCCESS = "Success"
    WARNING = "Warning"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
