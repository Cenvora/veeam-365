from enum import Enum


class RESTRbacUserType(str, Enum):
    PUBLICMAILBOX = "PublicMailbox"
    SHAREDMAILBOX = "SharedMailbox"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
