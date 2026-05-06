from enum import Enum

class RESTProxyType(str, Enum):
    DOMAIN = "Domain"
    LOCAL = "Local"
    WORKGROUP = "Workgroup"

    def __str__(self) -> str:
        return str(self.value)
