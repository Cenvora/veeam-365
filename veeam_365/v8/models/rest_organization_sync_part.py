from enum import Enum


class RESTOrganizationSyncPart(str, Enum):
    GROUPMEMBERS = "GroupMembers"
    GROUPS = "Groups"
    SITES = "Sites"
    USERS = "Users"

    def __str__(self) -> str:
        return str(self.value)
