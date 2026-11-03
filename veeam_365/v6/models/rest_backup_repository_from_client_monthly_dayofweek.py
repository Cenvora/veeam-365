from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTBackupRepositoryFromClientMonthlyDayofweek(str, Enum):
    FRIDAY = "Friday"
    MONDAY = "Monday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    THURSDAY = "Thursday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
