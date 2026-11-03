from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTCopyJobSchedulePolicyPeriodicallyEvery(str, Enum):
    HOURS1 = "Hours1"
    HOURS2 = "Hours2"
    HOURS4 = "Hours4"
    HOURS8 = "Hours8"
    MINUTES10 = "Minutes10"
    MINUTES15 = "Minutes15"
    MINUTES30 = "Minutes30"
    MINUTES5 = "Minutes5"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
