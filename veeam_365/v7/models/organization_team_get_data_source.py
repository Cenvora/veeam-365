from enum import Enum

from ..._lenient_enum import keep_unknown_value


class OrganizationTeamGetDataSource(str, Enum):
    PREFERLOCAL = "PreferLocal"
    PREFERLOCALRESYNCED = "PreferLocalResynced"
    PRODUCTION = "Production"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
