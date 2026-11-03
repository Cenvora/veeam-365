from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTTeamsChannelPreviewType(str, Enum):
    PRIVATE = "Private"
    SHARED = "Shared"
    STANDARD = "Standard"
    UNKNOWNFUTUREVALUE = "UnknownFutureValue"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
