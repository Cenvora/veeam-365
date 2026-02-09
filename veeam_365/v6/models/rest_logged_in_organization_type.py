from enum import Enum


class RESTLoggedInOrganizationType(str, Enum):
    HYBRID = "Hybrid"
    OFFICE365 = "Office365"
    ONPREMISES = "OnPremises"

    def __str__(self) -> str:
        return str(self.value)
