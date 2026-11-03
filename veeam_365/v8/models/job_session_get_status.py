from enum import Enum

from ..._lenient_enum import keep_unknown_value


class JobSessionGetStatus(str, Enum):
    FAILED = "Failed"
    RUNNING = "Running"
    STOPPED = "Stopped"
    SUCCEEDED = "Succeeded"
    WARNING = "Warning"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
