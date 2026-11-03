from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTTaskItemStatus(str, Enum):
    COMPLETED = "Completed"
    DEFERRED = "Deferred"
    INPROGRESS = "InProgress"
    NOTSTARTED = "NotStarted"
    WAITINGONSOMEONEELSE = "WaitingOnSomeoneElse"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
