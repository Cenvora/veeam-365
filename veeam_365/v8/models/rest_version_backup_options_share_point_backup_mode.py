from enum import Enum

class RESTVersionBackupOptionsSharePointBackupMode(str, Enum):
    ALL = "All"
    LATEST = "Latest"

    def __str__(self) -> str:
        return str(self.value)
