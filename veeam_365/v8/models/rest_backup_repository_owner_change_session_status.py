from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTBackupRepositoryOwnerChangeSessionStatus(str, Enum):
    FAILED = "Failed"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    WAITING = "Waiting"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
