from enum import Enum

class RESTDataRetrievalSessionType(str, Enum):
    RETRIEVALCHANGEAVAILABILITYPERIODDAYS = "RetrievalChangeAvailabilityPeriodDays"
    RETRIEVALREMOVING = "RetrievalRemoving"
    RETRIEVE = "Retrieve"

    def __str__(self) -> str:
        return str(self.value)
