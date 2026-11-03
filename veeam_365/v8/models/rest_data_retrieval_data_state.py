from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTDataRetrievalDataState(str, Enum):
    CHANGINGAVAILABILITYPERIOD = "ChangingAvailabilityPeriod"
    REMOVING = "Removing"
    RETRIEVED = "Retrieved"
    RETRIEVING = "Retrieving"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
