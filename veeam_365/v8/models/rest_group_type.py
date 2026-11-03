from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTGroupType(str, Enum):
    DISTRIBUTION = "Distribution"
    DYNAMICDISTRIBUTION = "DynamicDistribution"
    OFFICE365 = "Office365"
    SECURITY = "Security"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
