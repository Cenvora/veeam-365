from enum import Enum


class RESTCopyJobSchedulePolicyType(str, Enum):
    DAILYATTIME = "DailyAtTime"
    IMMEDIATE = "Immediate"
    PERIODICALLY = "Periodically"

    def __str__(self) -> str:
        return str(self.value)
