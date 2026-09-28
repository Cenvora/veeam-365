from enum import Enum


class RESTTeamsTeamPrivacy(str, Enum):
    HIDDENMEMBERSHIP = "HiddenMembership"
    PRIVATE = "Private"
    PUBLIC = "Public"

    def __str__(self) -> str:
        return str(self.value)
