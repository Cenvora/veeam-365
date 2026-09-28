from enum import Enum


class RESTOfficeLicenseDetectedSkuType(str, Enum):
    EDUCATION = "Education"
    OTHER = "Other"

    def __str__(self) -> str:
        return str(self.value)
