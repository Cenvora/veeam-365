from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTExchangeItemImportance(str, Enum):
    HIGH = "High"
    LOW = "Low"
    NORMAL = "Normal"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
