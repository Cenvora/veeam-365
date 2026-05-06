from enum import Enum

class RESTCloudServiceAccountType(str, Enum):
    AWS = "AWS"
    AZURE = "Azure"

    def __str__(self) -> str:
        return str(self.value)
