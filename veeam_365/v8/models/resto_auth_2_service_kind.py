from enum import Enum

class RESTOAuth2ServiceKind(str, Enum):
    GOOGLEGMAIL = "GoogleGmail"
    MICROSOFT365 = "Microsoft365"

    def __str__(self) -> str:
        return str(self.value)
