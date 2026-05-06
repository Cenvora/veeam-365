from enum import Enum

class RESTJobSessionType(str, Enum):
    BACKUP = "Backup"
    COPY = "Copy"

    def __str__(self) -> str:
        return str(self.value)
