from enum import Enum


class RESTLicenseStatus(str, Enum):
    EXPIRED = "Expired"
    VALID = "Valid"

    def __str__(self) -> str:
        return str(self.value)
