from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTOrganizationSyncPart(str, Enum):
    GROUPMEMBERS = "GroupMembers"
    GROUPS = "Groups"
    SITES = "Sites"
    USERS = "Users"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
