from enum import Enum


class RESTBackupRepositoryFromClientRetentionPeriodType(str, Enum):
    DAILY = "Daily"
    MONTHLY = "Monthly"
    YEARLY = "Yearly"

    def __str__(self) -> str:
        return str(self.value)
