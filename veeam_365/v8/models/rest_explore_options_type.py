from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTExploreOptionsType(str, Enum):
    VEOD = "Veod"
    VESP = "Vesp"
    VET = "Vet"
    VEX = "Vex"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
