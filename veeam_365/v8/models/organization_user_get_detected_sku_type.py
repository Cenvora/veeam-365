from enum import Enum


class OrganizationUserGetDetectedSkuType(str, Enum):
    EDUCATION = "Education"
    OTHER = "Other"

    def __str__(self) -> str:
        return str(self.value)
