from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTJobSchedulePolicyType(str, Enum):
    DAILY = "Daily"
    MANUALONLY = "ManualOnly"
    PERIODICALLY = "Periodically"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
