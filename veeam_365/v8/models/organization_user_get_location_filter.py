from enum import Enum

class OrganizationUserGetLocationFilter(str, Enum):
    ANY = "Any"
    CLOUD = "Cloud"
    CLOUDORHYBRID = "CloudOrHybrid"
    HYBRID = "Hybrid"
    ONPREMISES = "OnPremises"
    ONPREMISESORHYBRID = "OnPremisesOrHybrid"

    def __str__(self) -> str:
        return str(self.value)
