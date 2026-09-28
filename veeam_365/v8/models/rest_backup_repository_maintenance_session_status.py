from enum import Enum


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

    def __str__(self) -> str:
        return str(self.value)
