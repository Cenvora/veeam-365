from enum import Enum

class RESTDataRetrievalDataState(str, Enum):
    CHANGINGAVAILABILITYPERIOD = "ChangingAvailabilityPeriod"
    REMOVING = "Removing"
    RETRIEVED = "Retrieved"
    RETRIEVING = "Retrieving"

    def __str__(self) -> str:
        return str(self.value)
