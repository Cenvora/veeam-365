from enum import Enum

class RESTGroupLocationType(str, Enum):
    CLOUD = "Cloud"
    HYBRID = "Hybrid"
    ONPREMISES = "OnPremises"

    def __str__(self) -> str:
        return str(self.value)
