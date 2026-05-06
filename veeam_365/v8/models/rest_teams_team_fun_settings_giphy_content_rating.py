from enum import Enum

class RESTTeamsTeamFunSettingsGiphyContentRating(str, Enum):
    MODERATE = "Moderate"
    STRICT = "Strict"
    UNKNOWNFUTUREVALUE = "UnknownFutureValue"

    def __str__(self) -> str:
        return str(self.value)
