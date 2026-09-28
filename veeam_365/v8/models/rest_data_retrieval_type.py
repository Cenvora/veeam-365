from enum import Enum


class RESTDataRetrievalType(str, Enum):
    EXCHANGE = "Exchange"
    ONEDRIVE = "OneDrive"
    SHAREPOINT = "SharePoint"
    TEAMS = "Teams"

    def __str__(self) -> str:
        return str(self.value)
