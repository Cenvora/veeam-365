from enum import Enum

class RESTOperatorExploreOptionsType(str, Enum):
    VEOD = "Veod"
    VESP = "Vesp"
    VET = "Vet"
    VEX = "Vex"

    def __str__(self) -> str:
        return str(self.value)
