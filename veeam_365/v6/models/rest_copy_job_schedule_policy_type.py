from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTCopyJobSchedulePolicyType(str, Enum):
    DAILYATTIME = "DailyAtTime"
    IMMEDIATE = "Immediate"
    PERIODICALLY = "Periodically"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
