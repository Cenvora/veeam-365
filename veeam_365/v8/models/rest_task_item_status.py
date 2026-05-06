from enum import Enum

class RESTTaskItemStatus(str, Enum):
    COMPLETED = "Completed"
    DEFERRED = "Deferred"
    INPROGRESS = "InProgress"
    NOTSTARTED = "NotStarted"
    WAITINGONSOMEONEELSE = "WaitingOnSomeoneElse"

    def __str__(self) -> str:
        return str(self.value)
