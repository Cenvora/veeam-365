from enum import Enum

class RESTGroupType(str, Enum):
    DISTRIBUTION = "Distribution"
    DYNAMICDISTRIBUTION = "DynamicDistribution"
    OFFICE365 = "Office365"
    SECURITY = "Security"

    def __str__(self) -> str:
        return str(self.value)
