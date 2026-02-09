from enum import Enum


class RESTOrganizationSyncStateStatus(str, Enum):
    ERROR = "Error"
    NONE = "None"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
