from enum import Enum

class RESTVersionBackupOptionsFromClientSharePointBackupMode(str, Enum):
    ALL = "All"
    LATEST = "Latest"

    def __str__(self) -> str:
        return str(self.value)
