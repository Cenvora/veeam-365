from enum import Enum

from ..._lenient_enum import keep_unknown_value


class OrganizationGroupGetLocationFilter(str, Enum):
    ANY = "Any"
    CLOUD = "Cloud"
    CLOUDORHYBRID = "CloudOrHybrid"
    HYBRID = "Hybrid"
    ONPREMISES = "OnPremises"
    ONPREMISESORHYBRID = "OnPremisesOrHybrid"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
