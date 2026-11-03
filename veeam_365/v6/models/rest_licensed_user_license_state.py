from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTLicensedUserLicenseState(str, Enum):
    EXCEEDED = "Exceeded"
    LICENSED = "Licensed"
    NEW = "New"
    TEMPORARILYASSIGNED = "TemporarilyAssigned"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
