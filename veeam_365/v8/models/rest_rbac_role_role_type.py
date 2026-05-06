from enum import Enum

class RESTRbacRoleRoleType(str, Enum):
    ENTIREORGANIZATION = "EntireOrganization"
    SPECIFICOBJECTS = "SpecificObjects"

    def __str__(self) -> str:
        return str(self.value)
