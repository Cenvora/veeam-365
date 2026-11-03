from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTAuthenticationType(str, Enum):
    CUSTOMSMTP = "CustomSmtp"
    GOOGLEGMAIL = "GoogleGmail"
    MICROSOFT365 = "Microsoft365"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
