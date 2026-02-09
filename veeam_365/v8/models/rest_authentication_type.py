from enum import Enum


class RESTAuthenticationType(str, Enum):
    CUSTOMSMTP = "CustomSmtp"
    GOOGLEGMAIL = "GoogleGmail"
    MICROSOFT365 = "Microsoft365"

    def __str__(self) -> str:
        return str(self.value)
