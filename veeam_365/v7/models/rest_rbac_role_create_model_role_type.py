from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTRbacRoleCreateModelRoleType(str, Enum):
    ENTIREORGANIZATION = "EntireOrganization"
    SPECIFICOBJECTS = "SpecificObjects"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
