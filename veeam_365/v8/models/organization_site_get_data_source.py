from enum import Enum

class OrganizationSiteGetDataSource(str, Enum):
    PREFERLOCAL = "PreferLocal"
    PREFERLOCALRESYNCED = "PreferLocalResynced"
    PRODUCTION = "Production"

    def __str__(self) -> str:
        return str(self.value)
