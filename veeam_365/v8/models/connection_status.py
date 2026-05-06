from enum import Enum

class ConnectionStatus(str, Enum):
    FAILED = "Failed"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
