from enum import Enum


class RESTBackupRepositoryFromClientRetentionFrequencyType(str, Enum):
    DAILY = "Daily"
    MONTHLY = "Monthly"

    def __str__(self) -> str:
        return str(self.value)
