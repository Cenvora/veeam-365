from enum import Enum


class RESTBulkMailboxRestoreStatisticsStatus(str, Enum):
    FAILED = "Failed"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
