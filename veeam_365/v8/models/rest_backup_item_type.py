from enum import Enum


class RESTBackupItemType(str, Enum):
    GROUP = "Group"
    MAILBOX = "Mailbox"
    ONEDRIVE = "OneDrive"
    SITE = "Site"
    TEAM = "Team"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
