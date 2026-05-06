from enum import Enum

class RESTUserLocationType(str, Enum):
    CLOUD = "Cloud"
    HYBRID = "Hybrid"
    ONPREMISES = "OnPremises"

    def __str__(self) -> str:
        return str(self.value)
