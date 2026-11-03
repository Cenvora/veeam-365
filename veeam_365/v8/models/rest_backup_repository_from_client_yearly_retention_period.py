from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTBackupRepositoryFromClientYearlyRetentionPeriod(str, Enum):
    KEEP = "Keep"
    YEAR1 = "Year1"
    YEARS10 = "Years10"
    YEARS2 = "Years2"
    YEARS25 = "Years25"
    YEARS3 = "Years3"
    YEARS5 = "Years5"
    YEARS7 = "Years7"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
