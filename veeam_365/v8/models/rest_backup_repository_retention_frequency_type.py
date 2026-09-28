from enum import Enum


class RESTBackupRepositoryRetentionFrequencyType(str, Enum):
    DAILY = "Daily"
    MONTHLY = "Monthly"

    def __str__(self) -> str:
        return str(self.value)
