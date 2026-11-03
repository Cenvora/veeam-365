from enum import Enum

from ..._lenient_enum import keep_unknown_value


class OrganizationSiteGetLocationFilter(str, Enum):
    ANY = "Any"
    CLOUD = "Cloud"
    ONPREMISES = "OnPremises"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
