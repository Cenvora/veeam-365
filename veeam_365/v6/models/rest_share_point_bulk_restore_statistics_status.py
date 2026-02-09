from enum import Enum


class RESTSharePointBulkRestoreStatisticsStatus(str, Enum):
    FAILED = "Failed"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
