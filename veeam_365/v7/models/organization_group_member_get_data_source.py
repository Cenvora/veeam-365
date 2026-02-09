from enum import Enum


class OrganizationGroupMemberGetDataSource(str, Enum):
    PREFERLOCAL = "PreferLocal"
    PREFERLOCALRESYNCED = "PreferLocalResynced"
    PRODUCTION = "Production"

    def __str__(self) -> str:
        return str(self.value)
