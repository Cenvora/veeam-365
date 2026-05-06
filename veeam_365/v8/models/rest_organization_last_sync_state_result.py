from enum import Enum

class RESTOrganizationLastSyncStateResult(str, Enum):
    ERROR = "Error"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
