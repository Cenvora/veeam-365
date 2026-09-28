from enum import Enum


class RESTBackupRepositoryMaintenanceMode(str, Enum):
    NONE = "None"
    REPOSITORYDISABLED = "RepositoryDisabled"
    SESSIONSDISABLED = "SessionsDisabled"

    def __str__(self) -> str:
        return str(self.value)
