from enum import Enum

class RESTTeamsChannelPreviewType(str, Enum):
    PRIVATE = "Private"
    SHARED = "Shared"
    STANDARD = "Standard"
    UNKNOWNFUTUREVALUE = "UnknownFutureValue"

    def __str__(self) -> str:
        return str(self.value)
