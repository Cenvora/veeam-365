from enum import Enum

class RESTJobSchedulePolicyType(str, Enum):
    DAILY = "Daily"
    MANUALONLY = "ManualOnly"
    PERIODICALLY = "Periodically"

    def __str__(self) -> str:
        return str(self.value)
