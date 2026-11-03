from enum import Enum

from ..._lenient_enum import keep_unknown_value


class AzureStorageEndpointNullable(str, Enum):
    CHINA = "China"
    GERMANY = "Germany"
    GLOBAL = "Global"
    GOVERNMENT = "Government"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
