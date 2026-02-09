from enum import Enum


class RESTOrganizationSyncStateType(str, Enum):
    FULL = "Full"
    INCREMENTAL = "Incremental"

    def __str__(self) -> str:
        return str(self.value)
