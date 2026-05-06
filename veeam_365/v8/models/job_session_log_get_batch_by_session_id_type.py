from enum import Enum

class JobSessionLogGetBatchBySessionIdType(str, Enum):
    ERROR = "Error"
    RUNNING = "Running"
    STOP = "Stop"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
