from enum import Enum

class RESTProxyFromClientInternetProxyType(str, Enum):
    CUSTOM = "Custom"
    FROMMANAGEMENTSERVER = "FromManagementServer"

    def __str__(self) -> str:
        return str(self.value)
