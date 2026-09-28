from enum import Enum


class RESTLicenseOverviewOptionsFormat(str, Enum):
    CSV = "CSV"
    PDF = "PDF"

    def __str__(self) -> str:
        return str(self.value)
