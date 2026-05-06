from enum import Enum

class OrganizationTeamGetByIdDataSource(str, Enum):
    PREFERLOCAL = "PreferLocal"
    PREFERLOCALRESYNCED = "PreferLocalResynced"
    PRODUCTION = "Production"

    def __str__(self) -> str:
        return str(self.value)
