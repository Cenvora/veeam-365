from enum import Enum

class RESTLicensedUserLicenseState(str, Enum):
    EXCEEDED = "Exceeded"
    LICENSED = "Licensed"
    NEW = "New"
    TEMPORARILYASSIGNED = "TemporarilyAssigned"

    def __str__(self) -> str:
        return str(self.value)
