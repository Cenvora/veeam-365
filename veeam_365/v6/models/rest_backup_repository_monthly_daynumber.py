from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTBackupRepositoryMonthlyDaynumber(str, Enum):
    FIRST = "First"
    FOURTH = "Fourth"
    LAST = "Last"
    SECOND = "Second"
    THIRD = "Third"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
