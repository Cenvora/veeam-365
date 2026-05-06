from enum import Enum

class OrganizationSiteGetLocationFilter(str, Enum):
    ANY = "Any"
    CLOUD = "Cloud"
    ONPREMISES = "OnPremises"

    def __str__(self) -> str:
        return str(self.value)
