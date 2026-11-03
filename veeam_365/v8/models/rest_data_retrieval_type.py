from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTDataRetrievalType(str, Enum):
    EXCHANGE = "Exchange"
    ONEDRIVE = "OneDrive"
    SHAREPOINT = "SharePoint"
    TEAMS = "Teams"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
