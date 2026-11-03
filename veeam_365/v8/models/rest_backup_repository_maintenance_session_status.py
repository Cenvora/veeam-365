from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTBackupRepositoryMaintenanceSessionStatus(str, Enum):
    CANCELED = "Canceled"
    CANCELING = "Canceling"
    FAILED = "Failed"
    FAILING = "Failing"
    FINISHED = "Finished"
    FINISHING = "Finishing"
    INITIALIZED = "Initialized"
    PREPARING = "Preparing"
    RUNNING = "Running"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
