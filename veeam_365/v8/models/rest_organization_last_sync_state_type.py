from enum import Enum

class RESTOrganizationLastSyncStateType(str, Enum):
    FULL = "Full"
    INCREMENTAL = "Incremental"

    def __str__(self) -> str:
        return str(self.value)
